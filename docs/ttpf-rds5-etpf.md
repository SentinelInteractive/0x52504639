# TTPF: RDS5 and ETPF

A `.ttpf` file is a texture database. It is not an RPF archive and it is not enciphered. The file is an RDS5 header, an 8-byte chunk table, an ETPF descriptor block, and then the chunk payloads. Because the descriptor block is plaintext, the whole texture layout of the game is readable without a key.

The counts below cover 57 database files on disk and 46 distinct databases once duplicates are removed.

## RDS5 header

```text
0x00  RDS5
0x04  u32  chunk table entry count
0x08  u32  flags
0x0C  u32  flags
0x10  u32  header page count
0x18  entries * 8  chunk table
....  zero padding to 0x100
ETPF  descriptor block
....  chunk payloads
```

The word at `0x10` is a header page count, not a texture count. The ETPF block starts at `header pages * 0x100`, and the descriptor count is a separate field inside ETPF. Reading `0x10` as a texture count was an early error and it undercounted by an order of magnitude.

## Chunk table

Each 8-byte entry stores the end of one chunk and the codec of the next chunk. Chunk `i` spans from the end of chunk `i-1` to its own end, and chunk 0 starts at the 0x100-aligned end of the table.

```text
next codec  = (lo >> 26) & 0xF      0 RAW, 1..7 BCPack BC1..BC7, 8 ZLIB
file end    = (lo & 0x03FFFFFF) * 0x100
virtual end = (hi & 0x000FFFFF) * 0x4000 + ((lo >> 30) & 3) * 0x1000
```

The codec field belongs to the next chunk, not the current one. Reading it as the current chunk's codec shifts every type by one entry, which is enough to mislabel an entire database.

Chunk 0 is the ETPF block and is never zlib.

## ETPF block

```text
0x00  ETPF
0x04  u32 A  constant 634
0x08  u32 B  descriptor record count
0x0C  u32 C  unexplained
0x10  B * 16 descriptors
```

`A` is 634 in every database examined. `B` is the descriptor count and is the number that matches the texture total. `C` is unexplained; it is 0x4290 for the graphics database and does not track `B` or the chunk count.

Each descriptor is 16 bytes:

```text
u0 bits  0..13  width - 1
u0 bits 14..27  height - 1
u1 bits  0..2   format byte
u1 bits  3..9   DXGI_FORMAT
u1 bits 24..31  mip count
u2 bits  0..19  virtual page index; page * 0x1000
u3              nonzero on 5 records; unclassified
```

Width and height are stored minus one, so the decoded surface is one pixel larger than the field value in each axis. The virtual page index is an address, not an ordinal; multiplying it by 0x1000 gives the offset in the virtual texture space.

## Counts

| Scope | Databases | Descriptors | Chunks | Virtual size |
| --- | ---: | ---: | ---: | ---: |
| All 57 files | 57 | 357,115 | 1,026,947 | 151.59 GB |
| Distinct | 46 | 352,461 | 1,014,545 | 149.24 GB |

The 11 duplicate files are byte-identical copies, so the distinct column is the number to quote for content.

Of the texel bytes, 88.91 percent are reachable in software. BC7 and BC6H account for 22.08 percent and decode with an established software decoder. BCPack accounts for 10.96 percent. Its entropy layer is identified and its container framing is partly recovered, but no BCPack surface has been decoded end to end and no decoder is distributed. The measurements are in `docs/bcpack-entropy.md`.

BC7 carries 77,838 descriptors and BC6H carries 1,025. Together they hold 43.7 GB at mip 0 and 45.9 GB once the mip chains are included, which is 35.76 percent of all chain bytes. Nearly all of the software-reachable texel volume therefore sits in two codecs, and the BCPack share is not reachable in software yet.

## Codec distribution

Codecs are recorded per chunk, so a database can be almost entirely one type. The graphics database is the worked example: 1,550 table entries, `A=634`, `B=912`, `C=17040`, 912 descriptors and 1,550 chunks, with 1,402 zlib, 100 BC5, 27 BC7, 18 BC1, 1 BC3 and 1 raw.

That mix is normal. Most chunk payloads are zlib-compressed copies of a surface, and the BCn codecs appear where a surface was stored compressed rather than deflated.

## Deswizzle

Surfaces are stored in Morton order at 4 KiB or 64 KiB granularity, depending on the block size of the format. The tile shift is `12 - log2(bytes per element)`, which reproduces the observed 4 KiB and 64 KiB splits and matches the inverse swizzle bit for bit.

Export to PNG and DDS is exact for the formats we decode, with two known residuals: plus or minus one in the alpha channel, and the Z channel of BC5 normals, where the stored two-channel value is reconstructed rather than read.

## What remains open

- ETPF `C` is stored but unexplained.
- The mip rule is not derived. Mip levels are stored and counted, but the chain is not rebuilt deterministically.
- The 5 records with a nonzero `u3` are unclassified.
- BCPack is not decoded. The entropy layer is identified, the framing is partly recovered, and 10.96 percent of texel bytes wait on a complete framing solution.
