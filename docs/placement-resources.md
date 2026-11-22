# Placement resources

World placement is stored in `0DRPz` resources inside RPF9 archives, chiefly the `levels` archive, not in a separate placement file. A resource is a zlib stream with a block map, and the block map addresses the entity, prop and grass tables inside it. The tables are plaintext once the resource is inflated, so placement is readable without the table key.

This census scanned every one of the 22 archives in full, on a 16-byte grid. 290,294 resources and 4,316 RPF9 headers were found. Entity blocks occur in three of the archives. The two pack archives supply the increase over the earlier levels-only census. The 46 RDS5 databases that sit outside the archives were scanned as a coverage check and hold no `0DRPz` resource.

> Revision: this document previously stood behind 2,250,729 entity records from a levels-only census. That figure was a raw sum over every entity block and included 132 byte-identical duplicates. The figure this document stands behind is now 2,281,720, the de-duplicated total over all 22 archives. The label `guid` on entity `+0x20` is retracted. Both changes are recorded under Revision history. The prop `+0x34` retraction from an earlier revision is unchanged.

## What the census finds

Entity blocks occur in three archives. The per-archive result is:

| archive | headers | resources | entity resources | entity blocks | entity records |
| --- | ---: | ---: | ---: | ---: | ---: |
| levels.rpf | 2,030 | 188,449 | 30,792 | 30,794 | 2,250,729 |
| pack/story000/story000.rpf | 434 | 48,084 | 247 | 247 | 10,784 |
| pack/shared_minigame000/shared_minigame000.rpf | 49 | 787 | 102 | 103 | 20,339 |
| **total** | **4,316** | **290,294** | **31,141** | **31,144** | **2,281,852** |

The header and resource totals cover all 22 archives, including those with no placement resources. The entity figures come only from the three archives listed.

Two entity totals are worth stating plainly. The raw sum over every entity block is 2,281,852 records. Removing 132 byte-identical duplicate records leaves 2,281,720. This document stands behind 2,281,720 de-duplicated records.

The record types below are from the `levels` archive and are de-duplicated where a duplicate exists. The two pack archives also carry prop and grass blocks, 1,635 and 1,700 resources in story000 and 382 and 142 in shared_minigame000, so the prop and grass record totals below remain levels-only and are not install totals. Only the entity row has been counted across every archive.

| Record type | Resources | Blocks | Records | Stride |
| --- | ---: | ---: | ---: | ---: |
| Map data root | 162,374 | 162,374 | 1 per map | 0x460 fixed |
| Entity | 30,792 | 30,794 | 2,250,597 | 0x90 |
| Prop batch | 96,816 | 96,816 | 708,007 | 0x170 |
| Prop instance | 96,816 | 96,818 | 24,886,645 | 0x40, physical page |
| Grass batch | 55,809 | 55,809 | 202,144 | 0x1A0 |
| Grass instance | 55,809 | 202,144 | 219,484,361 | 0x10, physical page |
| Archetype definition | 5,945 | 5,945 | 1,339,478 | 0xB8 |
| MLO instance | 2,590 | 2,590 | not counted | 0x250 |

Block hashes are taken from each resource's own embedded schema and name a struct type, not a file type. The map-data root hash appears once per map, which is why its resource count is the map count.

Every stride above is confirmed over all blocks of that type, not estimated: 100 percent of prop instance blocks are a multiple of 0x40, of entity blocks a multiple of 0x90, of prop batch blocks a multiple of 0x170, of grass batch blocks a multiple of 0x1A0, and of grass instance blocks a multiple of 0x10 while only 48.93 percent are a multiple of 0x20.

### Probe grid

An 8-byte grid produces a byte-identical CSV to the 16-byte grid over the full levels archive, which is 76.16 GB. The CSV hash is SHA-256 037062b597423a15667c455d7cfefc8c75a9c2c7bb522ad3a74655672778ad73. The same holds on a 1.28 GB slice of levels and a 1.6 GB slice of story000. The grid is no longer the limiting factor.

## Resource structure

A resource is one zlib stream at a file offset, plus continuation streams where the resource is large. Once inflated, the virtual buffer `v` holds a small header that points at the block map.

| Offset | Type | Meaning |
| --- | --- | --- |
| `+0x00` | u64 | vft, must be zero for a resource root |
| `+0x08` | u64 | virtual pointer to the block map |
| `+0x10` | char[5] | magic `0DRPz` |
| `+0x38` | u64 | virtual pointer to the block table |
| `+0x4C` | u16 | block count |
| `+0x60` | u64 | `0x1601` marks a mid-resource geometry chunk |

The block map holds a virtual chunk count and a physical chunk count. The block table then holds one 16-byte entry per block: a hash, a size and a pointer. The pointer's tag selects the address space.

```text
0x5000_0000 | off   offset inside the virtual buffer
0x6000_0000 | off   offset inside the concatenated physical chunks
```

Physical chunks follow the virtual ones as further streams. A reader that only follows virtual pointers sees the entity table and misses props and grass entirely, because instance arrays live in physical pages.

### Locating the physical chunk

The physical chunk begins at the first 16-byte boundary at or after the end of the last virtual chunk, and it is stored in one of two ways:

- as its own zlib stream, or
- as raw uncompressed bytes.

Both forms occur in the same archive, sometimes within a few resources of each other, so a search that only accepts a zlib header steps over the raw case and silently lands on the next resource. Test the bytes at that offset for a zlib header first and inflate if present, otherwise take the raw bytes.

Two further rules matter:

- Consume **all** virtual chunks the block map declares, not just enough of them to see the block map. The block map is usually visible in the first chunk, so stopping there computes the physical offset from the wrong stream and truncates large resources.
- The physical chunk is not always exactly the size of the block it holds. A 0x40 prop instance block can sit in a 0x50 byte chunk, so allow a small tail rather than requiring an exact match.

## Entity records

Entity records have a stride of 0x90 and are the main placement primitive.

| Offset | Type | Field |
| --- | --- | --- |
| `+0x08` | u64 | name or definition hash |
| `+0x10` | f32 x4 | rotation quaternion, stored as the inverse |
| `+0x20` | u64 | repeated word, not a `guid`, see retraction |
| `+0x38` | f32 x3 | position in metres |
| `+0x44` | u32 | archetype hash |
| `+0x48` | u32 | flags |
| `+0x54` | f32 | scale xy |
| `+0x58` | f32 | scale z |

> **Retraction.** `+0x20` was previously published as `guid`. It holds 259,378 distinct values over 2,250,729 records, about 8.7 records per value. A unique identifier cannot repeat like this, so the label is withdrawn.

Coordinates are plain IEEE-754 floats in Z-up metres, little-endian. Rotation is stored as the inverse, so the world rotation is the conjugate with x, y and z negated and w kept.

`+0x44` reads as a genuine 32-bit hash: over 35,928 sampled records each of its four bytes is near-uniform across all 256 values. The same is true of `+0x08`. Any u32 field in this family that instead concentrates a single byte at zero or 0xFF is not a hash.

Three flag values dominate the entity table, `0x180090`, `0x180094` and `0x1800B0`. Their meaning is not decoded.

### De-duplication

A duplicate is a byte-identical entity block, the whole record including position, rotation, scale, archetype and the word at `+0x20`, that appears in two different resources. The probe removed 132 duplicate records in 43 blocks. All 43 duplicated blocks are inside the levels archive. No block is duplicated across archives. 22 of the 43 hold a single record. The rest hold 2 to 25 records.

Three resources carry two entity blocks each, and both blocks are counted, one in the levels archive with 9,389 records and 7,760 in a second, and one in shared_minigame000 with 8,183. Counting every block a resource declares rather than only the last one is worth 25,332 records. Zero entity blocks were lost because the virtual buffer was short.

### Validation over the population

These checks cover all 2,250,729 records in the levels archive. The quaternion norm at `+0x10` lies between 0.999 and 1.001 in 2,250,729 of 2,250,729 records, and no record has zero length. The archetype at `+0x44` is non-zero in 2,250,729 of 2,250,729 records. The name hash at `+0x08` is non-zero in 2,250,729 of 2,250,729 records. The position at `+0x38` is finite in 2,250,729 of 2,250,729 records.

Inside the raster bounds, 99.9998 percent of records are within x, 100.0000 percent within y, and 99.0225 percent within z. All three axes hold for 2,228,723 records, or 99.0223 percent. The 22,006 records outside the bounds are inside the raster in x and y and outside its -50 to 500 metre height band, which is where underground and below-sea-level placement sits.

## Prop instances

Prop instances have a stride of 0x40 and live in physical pages.

`+0x00`, `+0x10` and `+0x20` hold three rows of a 3 by 4 row-major matrix. The first three columns are orthonormal, and the fourth column is the translation at `+0x0C`, `+0x1C` and `+0x2C`. `+0x30` is a float scale, `+0x34` is a tint, `+0x38` is another float, and `+0x3C` is packed flags.

> **Retraction.** `+0x34` was previously published as a u32 archetype. It is a tint RGBA in memory order R, G, B, A. It is not a hash and not an index.

The evidence, over 57,970 structurally validated instances:

- 1,383 distinct values in total, which is a palette, not an identifier space.
- Byte 3 behaves as alpha: 0xFF in 44.5 percent of records and 0x00 in 38.1 percent. A 32-bit hash would put 0xFF there in about 0.39 percent of records, which is what entity `+0x44` actually does.
- The two most common values account for 70.6 percent of all instances: `0x00000000` (38.1 percent, no tint) and one constant `0xff165b44` (32.5 percent, an opaque dark olive). No archetype reference can be null in more than a third of all props and one constant in another third.
- The value varies per placement, not per model: of 1,518 sampled prop resources, 452 carry more than one distinct tint within the same batch model.

A minority of about 11.8 percent of instances carry a small integer (`0x00000001` to `0x00000007`, or `0x00000011`) at `+0x34` instead of a colour, and in every sampled case the colour word moves to `+0x3C`, where it is the same dark-olive family with an opaque alpha. Those records keep the two `1.0f` landmarks at `+0x30` and `+0x38`, so they are not misaligned. A colour field is therefore present in every instance; the sub-variant is unresolved.

Batch records hold the batch origin at `+0x38`, `+0x3C` and `+0x40`, and instance translations are relative to it. This is why an instance matrix read without its batch origin lands in the wrong place.

## Grass instances

Grass instances have a stride of 0x10 and live in physical pages.

| Offset | Type | Field |
| --- | --- | --- |
| `+0x00` | i16 x3 | tile-local offset |
| `+0x06` | u16 | packed pair of ~zero i8, likely tilt or normal |
| `+0x08` | RGBA8 | tint, same palette as the prop tint |
| `+0x0C` | u16 | quantisation value, low byte zero |
| `+0x0E` | u16 | zero |

The 0x10 stride is confirmed over all 202,144 blocks. The tint is the same colour space as the prop tint: the dominant 3-byte prefix is the RGB half of the prop field's dominant value, and the fourth byte is a density or alpha that concentrates at 0x00 and 0xFF. Bytes `+0x0C` and `+0x0E` are zero in 92.6 percent of sampled records, which is what fixes the record end.

This replaces the earlier text, which listed the first 6 bytes as plausible tile-local offsets, guessed that bytes 8 to 12 carried a word matching the batch archetype, and left the quantisation scale and last 4 bytes unverified. The word at `+0x08` is a tint rather than an archetype, and the quantisation scale is the `+0x0C` fixed-point field.

## A block map with zero physical pages

The block map declares a virtual chunk count and a physical chunk count, and zero is a legal value for the second. A resource that keeps its payload in virtual pages alone reports zero physical pages and still carries complete entity blocks. Such a map is neither truncated nor damaged.

Carve diagnostics over all 290,294 resources are now measured. 263,695 resources decoded fully. Zero had no block map. Zero had no block table. In 1,430 the chunk chain ended before the declared virtual chunk count was reached. In 25,169 a physical chunk was needed and was not accepted by the size test. The entity path does not depend on the physical chunk, and no entity block was lost to any of these.

## What is not placement

Four hashes in the `levels` archive look like placement candidates and are not: `0xfb42c06a`, `0xba51bd1e`, `0x6c4d9553` and `0xe33df1c6`. They form a disjoint family that never co-occurs with an entity or map-data block.

They hold node and indirection tables rather than geometry. One is 65,536-byte pages of sparse 16-byte nodes that are 97 percent zero; another is a sparse count, count, index table; another starts with a u32 count followed by the same node pattern. No stride fits, and no field decodes as a position. They are part of the gen9 drawable and indirection set.

## Revision history

| Item | Previously published | Corrected |
| --- | --- | --- |
| Census scope | `levels` archive only | all 22 archives |
| Resources | 188,449, levels only | 290,294, all archives |
| Entity records | 2,250,729, levels raw sum | 2,281,720, de-duplicated, all archives |
| Entity resources / blocks | 30,792 / 30,794 | 31,141 / 31,144 |
| Entity `+0x20` | `guid` | retracted, repeated word, 259,378 distinct values |

The earlier 2,250,729 was a raw sum over every entity block in the levels archive. 132 of those records are byte-identical duplicates of records in another resource, so levels alone is 2,250,597 de-duplicated. The two pack archives add 31,123 records: 10,784 from pack/story000/story000.rpf and 20,339 from pack/shared_minigame000/shared_minigame000.rpf. The net is 2,281,720. Added 31,123, lost 0.

## Open items

- The 0x48 entity flags are not decoded.
- The prop instance sub-variant that moves the tint to `+0x3C` is unresolved.
- The prop and grass record totals in the pack archives are not counted yet, only their resource and block counts.
- The relationship between the map-data root and its entity blocks is structural only; no schema for the root is published here.
- Placement is readable, but assembling a continuous world still needs tile origins and the 8 by 8 cell order solved per tile.
