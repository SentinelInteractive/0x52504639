# `zmmd` (type code `0x66`)

Written 2026-11-26. Decode limit stated first: only the container and a 16-word header pattern are measured on all 142 slots; no count, stride, record boundary or second-stream role is decoded (`artifact: docs/formats/zmmd.md:80-88`; `artifact: final_tail_report.md:49-61`). Grade **C** (container only), matching the published Classified status (`artifact: docs/coverage.md:156`). Write status W0 (`artifact: docs/formats/zmmd.md:90-92`).


Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x66`; the executable's callback type-name table resolves it to `zmmd` (string `0x1467844aa`), measured by string xref (`artifact: docs/formats/zmmd.md:5-7`). The store registration uses `MotionMatcherStore` at `0x145b40dfc`, `mov r8d,0x66`, call `0x1419ca0b0` (`artifact: docs/formats/zmmd.md:9`). Structural identity is the shared container plus an exact bimodal size split: 129 slots at or below 131,072 logical bytes and 13 at or above 237,536 with nothing between (`artifact: docs/formats/zmmd.md:11-13,31`). The first 64 inflated bytes follow one 16-word pattern in 139 of 142 slots (`artifact: docs/formats/zmmd.md:14`). A motion-matcher reading is inferred from the class name and float statistics; no field maps to a motion, match or pose (`artifact: docs/formats/zmmd.md:16`).

## Counts

| Measure | Value | Source |
|---|---:|---|
| Slots | 142 | `artifact: docs_complete_work/type_counts.tsv` row `00000066`; `artifact: docs/coverage.md:156` |
| Stored bytes | 7,096,224 | same two sources |
| Logical bytes | 10,378,208 | same two sources |
| Denominator | 1,255,039 slots | `artifact: docs/coverage.md:7,40` |

All 142 slots are in `anim.rpf`, spread across 13 archive headers (largest 65 slots), with one dictionary name and 141 unresolved hashes; all 64-bit name hashes are distinct (`artifact: docs/formats/zmmd.md:20-29`). The 13 large slots hold 85.4 percent of stored bytes on 9.2 percent of slots (`artifact: docs/formats/zmmd.md:32`). Logical sizes take 96 distinct values, but the 129/13 split is exact (`artifact: docs/formats/zmmd.md:31`). Byte sums overlap with nested containers (`artifact: docs/coverage.md:10`).

## Container

Verified on all 142 slots: sixteen stored zero bytes, `78 da` at `+0x10`, gaps 0..15 bytes, `logical == sum(inflated)` on 142 of 142, zero inflate errors and an empty exception list (`artifact: docs/formats/zmmd.md:34-42`). Stream counts are one in 129 slots and two in 13, but the two-stream set is **not** the large set: the overlap is 10 of 13, with indices 11, 14 and 16 two-stream but small, and 6, 12 and 18 large but single-stream (`artifact: docs/formats/zmmd.md:38-39`; `artifact: final_tail_report.md:53-56`). This corrects an earlier coincidence claim; the bimodal size split itself stands (`artifact: docs/formats/zmmd.md:39`).

## Fields

Offsets are relative to the inflated payload; integers are little-endian (`artifact: docs/formats/zmmd.md:45-47`).

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| first 16 u32 words | 4 each | Pattern `Z Z P Z Z Z Z Z Z Z Z Z Z Z P Z` in 139/142 slots; two variants at the last positions | measured | `artifact: docs/formats/zmmd.md:49-55` |
| `+0x08` | 4 | `0x50000000`-relative pointer, target inside payload in 142/142 | measured | `artifact: docs/formats/zmmd.md:59` |
| `+0x0c..+0x34` | 4 each | Zero in all slots | measured | `artifact: docs/formats/zmmd.md:61` |
| `+0x38` | 4 | Second pointer in 140 slots, small integer in 2 | measured | `artifact: docs/formats/zmmd.md:60` |
| `+0x40` | 4 | Pair of u16 (44/46 in the smallest slot); meaning unknown | measured | `artifact: docs/formats/zmmd.md:62` |
| `+0x44` | 4 | `1` | measured | `artifact: docs/formats/zmmd.md:62` |
| `+0x50` | 4 | Small integer, 4 distinct values in 4 slots, zero elsewhere | measured | `artifact: docs/formats/zmmd.md:63` |
| `+0x5c` | 4 | `0x01000000` | measured | `artifact: docs/formats/zmmd.md:64` |
| `+0x68` | 4 | Distinct hash-like word per slot; not the name hash (0/142) | measured | `artifact: docs/formats/zmmd.md:65` |
| body words | 4 | 2,594,552 words, 14.50 percent zero, 96.15 percent parse as `abs(f) <= 1`; element meaning unknown | measured | `artifact: docs/formats/zmmd.md:69` |
| header extent / fixed block | — | No `size = stride*count + c` fit and 96 distinct smallest pointer targets; earlier 224-byte header claim withdrawn | unknown | `artifact: docs/formats/zmmd.md:67` |
| semantic identity | — | Motion-matcher reading inferred from class name only | inferred | `artifact: docs/formats/zmmd.md:16` |

## Decode status

Container: measured on 142 of 142 slots (`artifact: docs/formats/zmmd.md:82`). Header: shape measured, roles not decoded; no count (`artifact: docs/formats/zmmd.md:83`). Record layer: not decoded; no stride, count or fixed-extent block table (`artifact: docs/formats/zmmd.md:84`). The second stream in the 13 two-stream slots has no shared header: 0 of 64 constant byte offsets, 0 of 13 count fits at offsets 0, 4 and 8, and differing prefix kinds (`artifact: docs/formats/zmmd.md:86`; `artifact: final_tail_report.md:57-58`). The parent re-check confirmed the 10/13 overlap from all 142 slots (`artifact: docs/formats/zmmd.md:102`). Grade C: the correction to the inherited claim is not a decoded layer. No encoder or game-load test (`artifact: docs/formats/zmmd.md:92`).

## Verification

The retained census-count artifact records these reproduction commands; this documentation pass did not rerun them:

```
rustc -O artifact: docs_complete_work/count_inventory.rs -o artifact: docs_complete_work/count_inventory.exe
& artifact: docs_complete_work/count_inventory.exe artifact: type_census.csv artifact: docs_complete_work
```

Observed: `data_rows: 1255039`, `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, `malformed_or_unparsable_rows: 0` (`artifact: docs_complete_work/inventory_log.txt`); row `00000066` in `artifact: docs_complete_work/type_counts.tsv` is 142 / 7,096,224 / 10,378,208. Source-side checks quoted, not re-run: `type_probe inventory artifact: type_census.csv 00000066 out zmmd_slots.tsv` selected 142 rows in 0.14 s; final Rust `zmmd_final` re-inflated all 142 slots in 0.037 s (3,883 slots/s) and found no shared second-stream header; the parent re-check script `artifact: type_reports/final_zmmd/verify_by_parent.py` confirmed overlap 10 of 13 (`artifact: docs/formats/zmmd.md:94-103`). The PE was read as data only (`artifact: docs/formats/zmmd.md:105`).

## Unknowns

The same-hash companion evidence is contradictory: this type's source reports zero cross-type companions, whereas the zpmd report records a zmmd twin. No shared-layout conclusion is adopted, and the join needs reconciliation. Sources: `artifact: docs/formats/zmmd.md`, Verification; `artifact: docs/formats/zpmd.md`, Decode.

What distinguishes the three large single-stream slots and what the second stream carries (`artifact: docs/formats/zmmd.md:109`); the `(u16, u16)` pair at `+0x40` and the `1` at `+0x44` (`artifact: docs/formats/zmmd.md:110`); whether `+0x68` keys a record (`artifact: docs/formats/zmmd.md:111`); the float body's element structure (`artifact: docs/formats/zmmd.md:112`); the loader, whose vtable is generic store bookkeeping (`artifact: docs/formats/zmmd.md:103,113`).

## Changelog

- 2026-11-26: created this page. No earlier `artifact: docs_complete/zmmd.md` existed at the time of writing. Sources: `artifact: docs/formats/zmmd.md`, `artifact: final_tail_report.md:49-61`, `artifact: docs/coverage.md:156`, `artifact: docs_complete_work/format_evidence.md:414-415`. No archive scan, decoder run, asset copy, key or publication was performed. Other final documents and source files were not modified.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zmmd.md`. No count was selected by modification time.

