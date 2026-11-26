# `zvert` (type code `0x12`)

Written 2026-11-26. Decode limit stated first: only the container is decoded on all 611 slots; the first stream and body are **not decoded beyond measured field and pointer profiles** (`artifact: docs/formats/zvert.md:108-115`; `artifact: final_tail_report.md:32-47`). Grade **C** (container only), matching the published Classified status (`artifact: docs/coverage.md:152`), not the older audit row. Write status W0 (`artifact: docs/formats/zvert.md:121-123`).


Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x12`; the executable's static enum table resolves it to `zvert` (string `0x146779d5c`), and the resolver geometry is verified as a 19-code static row with stride `0x98` (`artifact: docs/formats/zvert.md:7-11`). A store registration does exist under the class string `StreamVertex` at `0x14597878c`, `mov r8d,0x12`, `r9d=1`, call `0x1419ca0b0`; the earlier absence claim was a filter artifact (`artifact: docs/formats/zvert.md:13`; `artifact: final_tail_report.md:32-39`). The descriptor object and both its vtables were read; the derived overrides are bookkeeping (hash lookup, destructors, clears, accessors) and no payload parser is on either vtable (`artifact: docs/formats/zvert.md:13,95-106`). A thin structural identity is verified: two or three zlib streams behind the shared prefix, with two 64-bit pointers resolving into the first stream and never into the body (`artifact: docs/formats/zvert.md:15,76`).

## Counts

| Measure | Value | Source |
|---|---:|---|
| Slots | 611 | `artifact: docs_complete_work/type_counts.tsv` row `00000012`; `artifact: docs/coverage.md:152` |
| Stored bytes | 25,514,416 | same two sources |
| Logical bytes | 70,874,224 | same two sources |
| Denominator | 1,255,039 slots | `artifact: docs/coverage.md:7,40` |

All 611 slots sit in `levels.rpf`, in exactly two archive headers carrying 572 and 39 slots, and every containing header is generation 5 (`artifact: docs/formats/zvert.md:21-27`). All name hashes are distinct and none resolves to a name (`artifact: docs/formats/zvert.md:28`). Stored sizes run 1,616 to 123,440 bytes and logical sizes 3,184 to 266,192 bytes (`artifact: docs/formats/zvert.md:29-43`). Byte sums overlap with nested containers (`artifact: docs/coverage.md:10`).

## Container

Verified on all 611 slots: sixteen stored zero bytes, `78 da` at `+0x10`, and two streams in 316 slots or three in 295 (1,517 streams total); no slot has one or four (`artifact: docs/formats/zvert.md:45-50`). Later streams start at the next 16-byte-aligned stored offset with gaps 0..15 bytes; `logical == sum(inflated)` holds on 611 of 611, with zero inflate errors and an empty exception list (`artifact: docs/formats/zvert.md:51-53`). First-stream lengths take 27 distinct values from 528 to 8,464 bytes; the final stream is 131,072 bytes in 163 slots and 196,608 in 38 (`artifact: docs/formats/zvert.md:55`).

## Fields

Offsets are relative to the inflated first stream; integers are little-endian (`artifact: docs/formats/zvert.md:57-61`).

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| `+0x00` | 8 | Zero in all slots | measured | `artifact: docs/formats/zvert.md:65` |
| `+0x08` | 8 | Pointer-shaped, in range and 16-aligned on 611/611; 28 distinct targets, all inside the first stream | measured | `artifact: docs/formats/zvert.md:66,76` |
| `+0x10` | 8 | Pointer-shaped, in range on 611/611; 22 distinct targets, also inside the first stream | measured | `artifact: docs/formats/zvert.md:67,76` |
| `+0x18` | 8 | Two equal u16 halves in 611/611; values include `0x0001` (107 slots), `0x0009` (93), `0x0008` (76) | measured | `artifact: docs/formats/zvert.md:68` |
| `+0x20`, `+0x28` | 8 each | Zero in all slots | measured | `artifact: docs/formats/zvert.md:69` |
| `+0x30`, `+0x38`, `+0x48`, `+0x58..+0x88`, `+0xb0..+0xf8` | 8 each | Constant `0x00000080_00000080` fill in all slots; not a pointer | measured | `artifact: docs/formats/zvert.md:70` |
| `+0x40`, `+0x50`, `+0x90`, `+0xa0` | 8 each | Varying, second word always `0x80`; 460/209/493/518 distinct values | measured | `artifact: docs/formats/zvert.md:71-73` |
| header lattice | 8 | In 446/611 slots, pointer words step by `0x50`; 3,633 secondary words all inside the first stream, not a body stride | measured | `artifact: docs/formats/zvert.md:82` |
| first body u32 | 4 | `0x00004042` in 611/611 slots; role unknown | measured | `artifact: docs/formats/zvert.md:91` |
| body record layout | — | No count or valid stride; best stride test 16/611 and `%80` fits only 93/611 | unknown | `artifact: docs/formats/zvert.md:84,88-92` |
| vertex semantics | — | Reading the float-dominant body as vertex data is inferred from the label only | inferred | `artifact: docs/formats/zvert.md:93` |

## Decode status

Container: measured on 611 of 611 slots (`artifact: docs/formats/zvert.md:112`). Header stream: not decoded; the universal prefix is only 8 bytes, 27 length variants exist, and no field order or count was recovered (`artifact: docs/formats/zvert.md:78,113`). Body: measured but not decoded; no header word counts its records (best 38 of 611) and no fixed stride survives the population test (`artifact: docs/formats/zvert.md:88-92,114`). A raw-bit parse-back of one slot reproduced all 131,600 bytes with 0 mismatches but regenerated 0 bytes semantically, so no structural reconstruction is claimed (`artifact: docs/formats/zvert.md:117`). Grade C: container only. No encoder or game-load test (`artifact: docs/formats/zvert.md:123`).

## Verification

The retained census-count artifact records these reproduction commands; this documentation pass did not rerun them:

```
rustc -O artifact: docs_complete_work/count_inventory.rs -o artifact: docs_complete_work/count_inventory.exe
& artifact: docs_complete_work/count_inventory.exe artifact: type_census.csv artifact: docs_complete_work
```

Observed: `data_rows: 1255039`, `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, `malformed_or_unparsable_rows: 0` (`artifact: docs_complete_work/inventory_log.txt`); row `00000012` in `artifact: docs_complete_work/type_counts.tsv` is 611 / 25,514,416 / 70,874,224. Source-side checks quoted, not re-run: `zvert2.exe` over 611 slots loaded in 0.208 s (2,936.5 slots/s); final Rust `zvert_final` pass loaded in 0.208 s (2,938.3 slots/s) and produced pointer windows, stride/count grid and body-head constant; `type_probe inventory artifact: type_census.csv 00000012 out zvert_slots.tsv` selected 611 slots (`artifact: docs/formats/zvert.md:125-135`). The PE was read as data only (`artifact: docs/formats/zvert.md:3`).

## Unknowns

No recoverable count, stride, index array or record layout from the first stream (`artifact: docs/formats/zvert.md:141`); meaning of the 27 header-stream lengths and the class-constant pointers (`artifact: docs/formats/zvert.md:142-143`); the duplicated u16 pair and the body-head constant (`artifact: docs/formats/zvert.md:144`); why all 611 slots sit in header generation 5 (`artifact: docs/formats/zvert.md:145`); the consumer behind the store registration (`artifact: docs/formats/zvert.md:146`).

## Changelog

- 2026-11-26: created this page. No earlier `artifact: docs_complete/zvert.md` existed at the time of writing. Sources: `artifact: docs/formats/zvert.md`, `artifact: final_tail_report.md:32-47`, `artifact: docs/coverage.md:152`, `artifact: docs_complete_work/format_evidence.md:411-413`. No archive scan, decoder run, asset copy, key or publication was performed. Other final documents and source files were not modified.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zvert.md`. No count was selected by modification time.

