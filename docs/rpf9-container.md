# The RPF9 container

RPF9 is the archive format used by the game. An archive is a 64-byte header, two directory tables, a payload region and a trailer. The header is the only plaintext structure in the file; both tables are enciphered, and the payload behind them is ordinary zlib.

Table 2 does not use fixed 16-byte records. Its record width is 9 or 10 bytes, selected by the flags field, and its length is `ceil(stride * count / 16) * 16`. An earlier version of this page called both tables "16-byte records"; that reading came from the table length being a multiple of 16 and did not survive measurement. The details are under [Table geometry](#table-geometry).

All figures on this page were measured across 4,373 headers, unless a smaller sample is named.

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
| `0x1C` | 4 | Generation constant | `0x150` in all 2,616 generation-4 headers and in no other generation. Not constant across the corpus, see below |
| `0x20` | 4 | Version pair | Two 16-bit values, high 1 to 8 and low 3 to 13. The high value selects the table-2 layout |
| `0x24` | 4 | Declared entry count | Describes table 2 only when the `0x20` high value is 1 |
| `0x28` | 4 | Profile or key-slot id | Four values across the corpus |
| `0x2C` | 4 | Flags | `0x90F01` or `0x90F02`. The low byte selects the table-2 record width: 1 gives 9 bytes, 2 gives 10 |
| `0x30` | 4 | Generation constant | `0x10` in all 2,616 generation-4 headers and in no other generation |
| `0x34` | 12 | Zero | |

Both table lengths are multiples of 16 in all 4,373 headers, and the trailer length is a multiple of 16 as well. Every header sits on a 4 KiB boundary.

### Generation invariants

`0x1C` and `0x30` were described in an earlier version as constants of the format. They are constants of generation 4 only. Per generation, `0x1C` takes these values: `0x150` in 2,616 headers, `0x2C0` in 257, `0x170` in 61, `0x1B0` in 39 and `0x2B0` in 35, with a further 1,322 headers spread over more than 400 distinct values, most of them carried by one or two headers each.

Every one of the 2,616 generation-4 headers has `0x150`, and no header of generation 5, 6, 7 or 8 does. `0x30` behaves the same way: `0x10` in those same 2,616 headers, with `0x180` (265), `0x2F0` (67), `0x30` (61) and `0x70` (39) among the others.

So both fields identify the generation rather than the format. A reader should test the generation word rather than assume either constant.

## The `0x40` region

The 32 bytes from `0x40` to `0x60` were treated as one value in early passes. They are two fields with different behaviour, and the distinction matters because a 32-byte value was tried as a key or initialisation vector.

`0x40..0x50` is byte-identical in all 4,373 headers. It is a fixed sentinel:

```text
5f 08 da ab ec bd d4 02 58 c3 51 68 07 02 4c 24
```

`0x50..0x60` is a format tag that follows the generation and version tuple. The full corpus holds four values, distributed 2,863, 1,398, 67 and 2. Cross-tabulating the generation word against this block gives 27 groups with no mixed group, so each `(gen, version high, version low)` tuple maps to exactly one tag. The tag follows the version, not the `0x28` field.

Two readings remain open. Either the tag is plaintext and encipherment starts at `0x60`, or it is the ciphertext of a constant descriptor. Neither reading makes it a key, an initialisation vector or a cipher selector, and the earlier assumption that it was a 32-byte constant did not survive the full corpus.

## Table geometry

Table 1 runs from `0x40` to the split offset. Table 2 runs from the split to the header length.

### Table 2 record width

The record width is not 16 bytes. It is `8 + low_byte(0x2C)`, which takes two values:

- `0x90F01`, low byte 1, stride 9 bytes
- `0x90F02`, low byte 2, stride 10 bytes

Across the corpus `0x90F01` accounts for 3,597 headers and `0x90F02` for 733. The table length is the stride times the record count, rounded up to a multiple of 16:

```text
table2_length = ceil(stride * count / 16) * 16
```

This holds without exception when the high 16-bit value of `0x20` is 1: 2,382 of 2,382 such headers, and 12 of 12 top-level archives.

The flag records a choice that the count already forces. Across all 4,373 headers there is no counterexample to this rule: counts from 1 to 254 carry `0x90F01` and a 9-byte record, counts from 257 upward carry `0x90F02` and a 10-byte record. No header declares 255 or 256 entries. A 9-byte record is one byte longer than the 8-byte prefix and a 10-byte record two, so the reading is that an index or count field inside the record needs one byte or two, and the writer picks the form that fits. That is an inference from the boundary, not a decode of the record.

`0x28` and the `0x20` version pair occur with either stride, so neither of them selects the width.

It does not hold for the generation-4 headers whose `0x20` high value is 2. There are 234 of them. Their table 2 is always a multiple of 16 long, but it is not a function of the declared count: as a fraction of the count it runs from 0.63 to 10.0, so the count field does not describe their record count. One of the 234 fits the formula by coincidence. Taken together, the formula describes 2,383 of the 2,616 generation-4 headers, 91.1 percent, and describes every top-level archive we hold.

The exceptions are worth stating plainly rather than averaging away. For those 234 headers the record count is not derivable from the header, which means their record width is unknown rather than 16 bytes.

An earlier version of this page reported that table 2 carries one record per declared entry, with the median ratio 1.000 and top-level archives near 1.6. The 1.6 figure was an artefact of dividing a 9 or 10-byte table by 16, not evidence about directory entries. The order-of-magnitude claim stands only where the formula above holds, and there the record count equals the declared count exactly.

### Table 1

Table 1 has no fixed record width. It is a multiple of 16 in all 4,373 headers, but its cost per declared entry ranges from 38 bytes to 11,424 bytes, with a median of 63 in generation 4, and a log-log correlation of 0.96 with the declared count. No stride of 9, 10 or 16 reproduces its length: all three rules fail on every header in the corpus.

That is consistent with the earlier reading that table 1 is a function of the path or name payload rather than of the entry count. It is 512 bytes in the smallest archive and reaches 1.4 MB in the largest, and because it is a function of the name payload its length is the only structural signal about the names it stores.

An earlier note said table 2 has no repeated 16-byte slots and no all-zero slots, and used that to argue it is not a plaintext hash table with empty buckets. That observation was made by slicing the table at 16-byte boundaries, which the stride measurement above shows is the wrong slice. It is withdrawn rather than kept, and the hash-table question for table 2 is open.

## Payload

The payload is plaintext zlib. Streams start with `78 01`, `78 5E`, `78 9C` or `78 DA`. They are 16-byte aligned and not necessarily 4 KiB aligned.

Some resources begin with 16 zero bytes and place a zlib stream at `+0x10`. Those are virtual resources.

Large resources are split across consecutive 64 KiB pages, and each page is its own zlib stream. A reader stitches the pages before parsing, which is how multi-page geometry and metadata are read.

## Nested archives

Nested RPF9 archives start on 4 KiB boundaries inside a payload stream. A census by container gives 438 nested archives in `levels`, 122 in `anim`, 34 in `packs`, 26 in `audio`, 16 in `navmeshes`, 15 in `data`, 5 in `textures` and 3 in `script`, with one each in `common`, `movies`, `shaders` and `appdata0`.

The total is 4,373 headers: 22 standalone root archives and 4,351 nested containers.

## Trailer

The trailer occupies the last `trailerSize` bytes and is a multiple of 16 in every header. It is not random in the sense that was first reported, and it is not locked to the entry count.

Across 663 trailers there are 490 distinct first blocks, and 14 archives carry an all-zero 16-byte block. An earlier claim that the first block is a function of the declared count came from a subset, and it does not hold over the full corpus. The trailer cannot be used as a key oracle.

Its meaning remains unknown. So do the exact entry layouts of both tables.

## How it differs from RPF7

RPF7 packs its directory as a plaintext structure with a per-entry name hash, so a reader can walk the tree without a key. RPF9 replaces that directory with two enciphered tables: a name table of unknown layout and a record table of 9 or 10 bytes per entry.

The practical consequence is that the container can be parsed and the content can be read, but filenames, extents and the tree cannot. Extents come from carving rather than from records, which is why the stream index is the working substitute for the directory.
