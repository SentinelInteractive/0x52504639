# `zsmam` (type code `0x6e`)

Written 2026-11-26. Decode limit stated first: only the container is decoded on all 5 slots; the field profile is measured but no count, record boundary, stride or inner magic is decoded (`artifact: docs/formats/zsmam.md:78-86`; `artifact: final_tail_report.md:63-70`). Grade **C** (container only), matching the published Classified status (`artifact: docs/coverage.md:160`). Write status W0 (`artifact: docs/formats/zsmam.md:88-90`).


Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x6e`; the executable's callback type-name table resolves it to `zsmam` (string `0x14677fc48`), measured by string xref (`artifact: docs/formats/zsmam.md:5-7`). The store registration uses `SecMotionAssetMapStore` at `0x145bac0fc`, `mov r8d,0x6e`, call `0x1419ca0b0` (`artifact: docs/formats/zsmam.md:9`). Structural identity is the container only: a pointer at `+0x08`, a constant `0x50000060` at `+0x18` and an integer pair at `+0x10/+0x14` in all five slots, with nothing else repeating (`artifact: docs/formats/zsmam.md:11`). A secondary-motion asset map reading is inferred from the class name alone (`artifact: docs/formats/zsmam.md:11`).

## Counts

| Measure | Value | Source |
|---|---:|---|
| Slots | 5 | `artifact: docs_complete_work/type_counts.tsv` row `0000006e`; `artifact: docs/coverage.md:160` |
| Stored bytes | 370,720 | same two sources |
| Logical bytes | 792,464 | same two sources |
| Denominator | 1,255,039 slots | `artifact: docs/coverage.md:7,40` |

Three slots are in `packs.rpf`, one in a shared minigame root and one in a shared rest-of-world root; each slot sits in a different archive header and all five name hashes are unresolved and distinct (`artifact: docs/formats/zsmam.md:19-28`). The five logical sizes are 1,360; 1,584; 288,976; 496,896; 3,648 bytes, and the two large slots hold 99.3 percent of stored bytes (`artifact: docs/formats/zsmam.md:30-38`). Byte sums overlap with nested containers (`artifact: docs/coverage.md:10`).

## Container

Verified on all 5 slots: sixteen stored zero bytes, `78 da` at `+0x10`; one stream in three slots and two in the two large slots, with gaps 0, 5 and 7 bytes; `logical == sum(inflated)` on 5 of 5, zero inflate errors and an empty exception list (`artifact: docs/formats/zsmam.md:40-48`). First-stream lengths are 1,360; 1,584; 3,648; 262,144; 458,752, so there is no fixed header stream (`artifact: docs/formats/zsmam.md:49`). One 1,648-stored/3,648-logical slot accounts byte-exactly as `16 + 0 + 1,617 + 15` stored and 3,648 inflated with four trailing zero bytes (`artifact: docs/formats/zsmam.md:50`).

## Fields

Offsets are relative to the inflated payload; integers are little-endian (`artifact: docs/formats/zsmam.md:52-54`).

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| `+0x08` | 4 | `0x50000000`-relative pointer, target in range in 5/5 | measured | `artifact: docs/formats/zsmam.md:58` |
| `+0x10` | 4 | Small integer in all five: 2, 2, 256, 512, 4; part of the only repeating pair | measured | `artifact: docs/formats/zsmam.md:59,30-36` |
| `+0x14` | 4 | Small integer in all five: 6, 11, 2,896, 6,569, 41; part of the pair | measured | `artifact: docs/formats/zsmam.md:60,30-36` |
| `+0x18` | 4 | `0x50000060` in all five | measured | `artifact: docs/formats/zsmam.md:61` |
| `+0x2c..+0x3c`, `+0x4c`, `+0x5c`, `+0x78..+0x84`, `+0x98..+0xa4` | 4 each | Zero | measured | `artifact: docs/formats/zsmam.md:62` |
| `+0x60..+0x74` | 4 each | Hash-like words, five distinct values per offset; meaning unknown | measured | `artifact: docs/formats/zsmam.md:63` |
| pair as count/offset | — | Refuted on 5/5: `+0x14` lands in the header for small slots and opaque body for large ones; 60 target-word comparisons false; stream 2 opens with 9 and 3 bytes | unknown | `artifact: docs/formats/zsmam.md:65-67`; `artifact: final_tail_report.md:65-68` |
| secondary-motion map semantics | — | Inferred from store class only | inferred | `artifact: docs/formats/zsmam.md:11` |

The exhaustive `size = stride*count + c` search over offsets `0..0xff` and strides 2/4/8/12/16/24/32/40/48 found zero fits (`artifact: docs/formats/zsmam.md:65`). All 35 stride-by-slot fits are vacuous at this population size (`artifact: final_tail_report.md:68`).

## Decode status

Container: measured on 5 of 5 slots (`artifact: docs/formats/zsmam.md:80`). Header: field profile only; three cells repeat and no field identifies a count, table or record (`artifact: docs/formats/zsmam.md:81`). Record layer and element semantics: not decoded, with a clean negative (`artifact: docs/formats/zsmam.md:82-83`). Companion join found zero name-hash partners and no embedded own hash, stored size or logical size (`artifact: docs/formats/zsmam.md:84`). Grade C. No encoder or game-load test (`artifact: docs/formats/zsmam.md:90`).

## Verification

The retained census-count artifact records these reproduction commands; this documentation pass did not rerun them:

```
rustc -O artifact: docs_complete_work/count_inventory.rs -o artifact: docs_complete_work/count_inventory.exe
& artifact: docs_complete_work/count_inventory.exe artifact: type_census.csv artifact: docs_complete_work
```

Observed: `data_rows: 1255039`, `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, `malformed_or_unparsable_rows: 0` (`artifact: docs_complete_work/inventory_log.txt`); row `0000006e` in `artifact: docs_complete_work/type_counts.tsv` is 5 / 370,720 / 792,464. Source-side checks quoted, not re-run: `type_probe inventory artifact: type_census.csv 0000006e out zsmam_slots.tsv` selected 5 rows in 0.14 s; the `tail3` container pass ran in 0.004 s; final Rust `zsmam_final` processed all 5 slots at 2,442.7 slots/s; an independent one-shot re-derivation reproduced the pointer, constant and all five integer pairs (`artifact: docs/formats/zsmam.md:92-99`). The PE was read as data only (`artifact: docs/formats/zsmam.md:100`).

## Unknowns

What the `(+0x10, +0x14)` pair measures, since a row/column or count/stride reading is unsupported (`artifact: docs/formats/zsmam.md:104`); why one slot sits per archive header across three roots (`artifact: docs/formats/zsmam.md:105`); the hash-like words at `+0x60..+0x74` (`artifact: docs/formats/zsmam.md:106`); the store reader (`artifact: docs/formats/zsmam.md:107`).

## Changelog

- 2026-11-26: created this page. No earlier `artifact: docs_complete/zsmam.md` existed at the time of writing. Sources: `artifact: docs/formats/zsmam.md`, `artifact: final_tail_report.md:63-70`, `artifact: docs/coverage.md:160`, `artifact: docs_complete_work/format_evidence.md:402-403`. No archive scan, decoder run, asset copy, key or publication was performed. Other final documents and source files were not modified.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zsmam.md`. No count was selected by modification time.

