# The RPF9 container

RPF9 is the archive format used by the game. An archive is a 64-byte header, two tables of 16-byte records, a payload region and a trailer. The header is the only plaintext structure in the file; both tables are enciphered, and the payload behind them is ordinary zlib.

All figures on this page were measured across 4,330 headers, unless a smaller sample is named.

## Header

The header is 64 bytes. The payload begins at the offset stored at `0x04`, and everything after it is either a payload stream or the trailer.

| Offset | Size | Field | Notes |
| --- | --- | --- | --- |
| `0x00` | 4 | Magic | `0x52504639`, which reads `9FPR` on disk in little-endian |
| `0x04` | 4 | Header length | Payload starts here |
| `0x08` | 4 | Split offset | End of table 1, start of table 2 |
| `0x0C` | 4 | Trailer size | |
| `0x10` | 8 | Archive id | |
| `0x18` | 4 | Generation word | `(gen << 16) \| 0x7A00`, with gen from 4 to 8 |
| `0x1C` | 4 | Constant | `0x150` in every header |
| `0x20` | 4 | Version pair | Two 16-bit values, high 1 to 8 and low 3 to 13 |
| `0x24` | 4 | Declared entry count | Directories included |
| `0x28` | 4 | Profile or key-slot id | Four values across the corpus |
| `0x2C` | 4 | Flags | `0x90F01` or `0x90F02` |
| `0x30` | 4 | Constant | `0x10` |
| `0x34` | 12 | Zero | |

Both table lengths are multiples of 16 in all 4,330 headers, and the trailer length is a multiple of 16 as well. Every header sits on a 4 KiB boundary.

## The `0x40` region

The 32 bytes from `0x40` to `0x60` were treated as one value in early passes. They are two fields with different behaviour, and the distinction matters because a 32-byte value was tried as a key or initialisation vector.

`0x40..0x50` is byte-identical in all 4,330 headers. It is a fixed sentinel:

```text
5f 08 da ab ec bd d4 02 58 c3 51 68 07 02 4c 24
```

`0x50..0x60` is a format tag that follows the generation and version tuple. The full corpus holds four values, distributed 2,863, 1,398, 67 and 2. Cross-tabulating the generation word against this block gives 27 groups with no mixed group, so each `(gen, version high, version low)` tuple maps to exactly one tag. The tag follows the version, not the `0x28` field.

Two readings remain open. Either the tag is plaintext and encipherment starts at `0x60`, or it is the ciphertext of a constant descriptor. Neither reading makes it a key, an initialisation vector or a cipher selector, and the earlier assumption that it was a 32-byte constant did not survive the full corpus.

## Table geometry

Table 1 runs from `0x40` to the split offset. Table 2 runs from the split to the header length. Both hold 16-byte records.

Table 2 carries one record per declared entry in most archives; the median ratio of declared count to table-2 records is 1.000. Top-level archives sit near 1.6, because the declared count includes directories while table 2 holds files only.

Table 1 varies with the path or name payload. It is 512 bytes in the smallest archive and grows with the entry count, reaching 950 KB in the largest. There are no repeated 16-byte slots and no all-zero slots in table 2, so it is not a plaintext hash table with empty buckets.

Because table 1 is a function of the name payload, its length is the only structural signal about the names it stores.

## Payload

The payload is plaintext zlib. Streams start with `78 01`, `78 5E`, `78 9C` or `78 DA`. They are 16-byte aligned and not necessarily 4 KiB aligned.

Some resources begin with 16 zero bytes and place a zlib stream at `+0x10`. Those are virtual resources.

Large resources are split across consecutive 64 KiB pages, and each page is its own zlib stream. A reader stitches the pages before parsing, which is how multi-page geometry and metadata are read.

## Nested archives

Nested RPF9 archives start on 4 KiB boundaries inside a payload stream. A census by container gives 438 nested archives in `levels`, 122 in `anim`, 34 in `packs`, 26 in `audio`, 16 in `navmeshes`, 15 in `data`, 5 in `textures` and 3 in `script`, with one each in `common`, `movies`, `shaders` and `appdata0`.

The total is 4,330 headers, of which 2,536 are inside the 12 top-level archives and 1,794 are inside the `pack` containers.

## Trailer

The trailer occupies the last `trailerSize` bytes and is a multiple of 16 in every header. It is not random in the sense that was first reported, and it is not locked to the entry count.

Across 663 trailers there are 490 distinct first blocks, and 14 archives carry an all-zero 16-byte block. An earlier claim that the first block is a function of the declared count came from a subset, and it does not hold over the full corpus. The trailer cannot be used as a key oracle.

Its meaning remains unknown. So do the exact entry layouts of both tables.

## How it differs from RPF7

RPF7 packs its directory as a plaintext structure with a per-entry name hash, so a reader can walk the tree without a key. RPF9 replaces that directory with two enciphered tables of fixed 16-byte records. The payload handling is close to RPF7: zlib streams, page-aligned resources and a trailer.

The practical consequence is that the container can be parsed and the content can be read, but filenames, extents and the tree cannot. Extents come from carving rather than from records, which is why the stream index is the working substitute for the directory.
