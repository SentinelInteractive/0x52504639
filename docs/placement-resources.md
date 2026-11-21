# Placement resources

World placement is stored in `0DRPz` resources inside the `levels` archive, not in a separate placement file. A resource is a zlib stream with a block map, and the block map addresses the entity, prop and grass tables inside it. The tables are plaintext once the resource is inflated, so placement is readable without the table key.

The numbers below are from a full-file census of the `levels` archive, 183,992 resources in total.

## What the census finds

| Record type | Resources | Blocks | Records | Stride |
| --- | ---: | ---: | ---: | ---: |
| Map data root | 162,374 | 162,374 | 1 per map | 0x460 fixed |
| Entity | 28,516 | 28,518 | 2,244,675 | 0x90 |
| Prop batch | 96,816 | 96,816 | 708,007 | 0x170 |
| Prop instance | 96,816 | 96,816 | 24,886,645 | 0x40, physical page |
| Grass batch | 55,809 | 55,809 | 202,144 | 0x1A0 |
| Grass instance | 55,809 | 55,809 | 219,484,361 | 0x10, physical page |
| Archetype definition | 5,826 | 5,826 | 1,339,293 | 0xB8 |
| MLO instance | 2,590 | 2,590 | not counted | 0x250 |

Block hashes are taken from each resource's own embedded schema and name a struct type, not a file type. The map-data root hash appears once per map, which is why its resource count is the map count.

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

Physical chunks follow the virtual ones as further zlib streams. A reader that only follows virtual pointers sees the entity table and misses props and grass entirely, because instance arrays live in physical pages.

## Entity records

Entity records have a stride of 0x90 and are the main placement primitive.

| Offset | Type | Field |
| --- | --- | --- |
| `+0x08` | u64 | name or definition hash |
| `+0x10` | f32 x4 | rotation quaternion, stored as the inverse |
| `+0x20` | u64 | guid |
| `+0x38` | f32 x3 | position in metres |
| `+0x44` | u32 | archetype hash |
| `+0x48` | u32 | flags |
| `+0x54` | f32 | scale xy |
| `+0x58` | f32 | scale z |

Coordinates are plain IEEE-754 floats in RAGE Z-up metres, little-endian. Rotation is stored as the inverse, so the world rotation is the conjugate with x, y and z negated and w kept.

Three flag values dominate the entity table, `0x180090`, `0x180094` and `0x1800B0`. Their meaning is not decoded.

## Prop instances

Prop instances have a stride of 0x40 and live in physical pages.

`+0x00`, `+0x10` and `+0x20` hold three rows of a 3 by 4 row-major matrix. The first three columns are orthonormal, and the fourth column is the translation. `+0x30` is a float scale, `+0x34` a u32 archetype, `+0x38` another float, and `+0x3C` packed flags.

Batch records hold the batch origin at `+0x38`, `+0x3C` and `+0x40`, and instance translations are relative to it. This is why an instance matrix read without its batch origin lands in the wrong place.

## Grass instances

Grass instances have a stride of 0x10 and live in physical pages. The first 6 bytes read as three signed 16-bit values give plausible tile-local offsets, and bytes 8 to 12 carry a word that matches the batch archetype in some blocks.

The quantisation scale and the last 4 bytes are unverified. Grass is the one record type where the layout is not confirmed.

## A block map with zero physical pages

The block map declares a virtual chunk count and a physical chunk count, and zero is a legal value for the second. A resource that keeps its payload in virtual pages alone reports zero physical pages and still carries complete entity blocks. Such a map is neither truncated nor damaged.

48,320 of the 183,992 resources declare zero physical chunks and still carry entity blocks. Of the 28,516 entity-bearing resources, 22,628 declare zero physical pages, and those resources hold 2,183,724 entities, which is 97.3 percent of the total.

The two ways of counting therefore diverge sharply. A pass that requires at least one physical page keeps 135,672 of the 183,992 resources and reaches 60,851 entities. A pass that accepts zero as a legal count reaches 2,244,675. The split does not sum exactly to that total, because 100 entities are counted in the total but fall in neither group as measured.

Prop and grass instances, 24,886,645 and 219,484,361 of them, are the opposite case: they live in physical pages and need the physical dereference.

## What is not placement

Four hashes in the `levels` archive look like placement candidates and are not: `0xfb42c06a`, `0xba51bd1e`, `0x6c4d9553` and `0xe33df1c6`. They form a disjoint family of 6,552 resources that never co-occurs with an entity or map-data block.

They hold node and indirection tables rather than geometry. One is 65,536-byte pages of sparse 16-byte nodes that are 97 percent zero; another is a sparse count, count, index table; another starts with a u32 count followed by the same node pattern. No stride fits, and no field decodes as a position. They are part of the gen9 drawable and indirection set.

## Open items

- The 0x48 entity flags are not decoded.
- The grass quantisation scale is unverified.
- The relationship between the map-data root and its entity blocks is structural only; no schema for the root is published here.
- Placement is readable, but assembling a continuous world still needs tile origins and the 8 by 8 cell order solved per tile.
