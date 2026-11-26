# `zjd` (type code `0x4d`)

Written 2026-11-26. Decode limit stated first: the container and one type-specific layer, an N-entry `u64` pointer array sized by a duplicated `(N, N)` pair, are measured on all 3 slots, but the records behind those pointers and the float block are **not decoded** (`artifact: docs/formats/zjd.md:73-81`; `artifact: final_tail_report.md:23-30`). Grade **B** (partial payload structure), matching the published Partial status (`artifact: docs/coverage.md:162`), not the older Classified audit row. Write status W0 (`artifact: docs/formats/zjd.md:83-85`).


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x4d`; the executable's callback type-name table resolves it to `zjd` (string `0x146784583`), measured by string xref (`artifact: docs/formats/zjd.md:5-7`). The store registration uses `JointLimitDictStore` at `0x145ca786c`, `mov r8d,0x4d`, call `0x1419ca0b0` (`artifact: docs/formats/zjd.md:9`). Structural identity is the container plus three pointer cells, a `1`, a duplicated `(N, N)` u16 pair at `+0x28/+0x38`, and an N-entry pointer array; the joint-limit reading is inferred from the class name alone (`artifact: docs/formats/zjd.md:11-13`). The type moved from Classified to Partial on the strength of the measured pointer array only (`artifact: final_tail_report.md:7,23-27`).

## Counts

| Measure | Value | Source |
|---|---:|---|
| Slots | 3 | `artifact: docs_complete_work/type_counts.tsv` row `0000004d`; `artifact: docs/coverage.md:162` |
| Stored bytes | 2,880 | same two sources |
| Logical bytes | 28,240 | same two sources |
| Denominator | 1,255,039 slots | `artifact: docs/coverage.md:7,40` |

All three slots are in `anim.rpf` and in one archive header; all name hashes are unresolved and distinct (`artifact: docs/formats/zjd.md:19-25`). The three rows are 352 stored / 3,968 logical with pair `(1,1)`, 640 / 5,104 with `(3,3)`, and 1,888 / 19,168 with `(10,10)` (`artifact: docs/formats/zjd.md:27-33`). Byte sums overlap with nested containers (`artifact: docs/coverage.md:10`).

## Container

Verified on all 3 slots: sixteen stored zero bytes, `78 da` at `+0x10`, exactly one zlib stream with gap 0, `logical == sum(inflated)` on 3 of 3, zero inflate errors and an empty exception list (`artifact: docs/formats/zjd.md:35-42`).

## Fields

Offsets are relative to the inflated payload; integers are little-endian (`artifact: docs/formats/zjd.md:44-46`).

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| `+0x08`, `+0x20`, `+0x30` | 4 each | `0x50000000`-relative pointers; all targets in range | measured | `artifact: docs/formats/zjd.md:50` |
| `+0x18` | 4 | `1` | measured | `artifact: docs/formats/zjd.md:51` |
| `+0x28` | 4 | Two equal u16 halves: `0x00010001`, `0x00030003`, `0x000A000A` (N = 1, 3, 10) | measured | `artifact: docs/formats/zjd.md:52` |
| `+0x30` target | 8 each | Array of exactly N `u64` pointers, `N*8` bytes, ending at the `+0x20` target; sizes 8 / 24 / 80; every target in range in 3/3 | measured | `artifact: docs/formats/zjd.md:53,58`; `artifact: final_tail_report.md:25-27` |
| `+0x38` | 4 | Equal to `+0x28` in all three slots; duplicate copy of N | measured | `artifact: docs/formats/zjd.md:54` |
| `+0x4c` | 4 | `1.0f` in all three slots | measured | `artifact: docs/formats/zjd.md:55` |
| `+0x50` onward | 4 each | Float words including a symmetric `-π`/`+π` pair and a symmetric `±0.0873` pair | measured | `artifact: docs/formats/zjd.md:56` |
| payload-wide stride | — | No `size = stride*count + c` fit over offsets `0..0xff` with strides 2/4/8/12/16/24/32/40/48 | unknown | `artifact: docs/formats/zjd.md:60` |
| angular-limit semantics | — | The `±π` pair is consistent with joint limits but unverified at N = 3 | inferred | `artifact: docs/formats/zjd.md:62` |

The pair does not size the whole payload: `(1,1)` goes with 3,968 bytes and `(10,10)` with 19,168, a 4.8-fold span with no proportionality (`artifact: docs/formats/zjd.md:60`).

## Decode status

Container: measured on 3 of 3 slots (`artifact: docs/formats/zjd.md:75`). Header: partly decoded; pointer cells, the pair and the N-entry array are measured (`artifact: docs/formats/zjd.md:76`). Record layer and element semantics: not decoded; the N pointed-to records, the float block and which pair copy is canonical are open (`artifact: docs/formats/zjd.md:77-81`; `artifact: final_tail_report.md:30`). Companion join found no name-hash partner and no embedded own hash, stored size or logical size (`artifact: docs/formats/zjd.md:79`). Grade B: one real type-specific layer verified on the whole population, not a payload decode. No encoder or game-load test (`artifact: docs/formats/zjd.md:85`).

## Verification

The retained census-count artifact records these reproduction commands; this documentation pass did not rerun them:

```
rustc -O artifact: docs_complete_work/count_inventory.rs -o artifact: docs_complete_work/count_inventory.exe
& artifact: docs_complete_work/count_inventory.exe artifact: type_census.csv artifact: docs_complete_work
```

Observed: `data_rows: 1255039`, `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, `malformed_or_unparsable_rows: 0` (`artifact: docs_complete_work/inventory_log.txt`); row `0000004d` in `artifact: docs_complete_work/type_counts.tsv` is 3 / 2,880 / 28,240. Source-side checks quoted, not re-run: `type_probe inventory artifact: type_census.csv 0000004d out zjd_slots.tsv` selected 3 rows in 0.13 s; final Rust `zjd_final` analysed the three slots in 0.001 s (5,499.5 slots/s); the independent parent script `artifact: type_reports/final_zjd/verify_by_parent.py` returned `ALL_SLOTS_OK=True` with 10/10, 3/3 and 1/1 valid pointer words (`artifact: docs/formats/zjd.md:87-94`). The PE was read as data only (`artifact: docs/formats/zjd.md:96`).

## Unknowns

Which copy of the duplicated pair is canonical and why it appears twice (`artifact: docs/formats/zjd.md:100`); the record layout behind the N pointers and whether floats are angular limits (`artifact: docs/formats/zjd.md:101`); layouts for N greater than 10, which the population lacks (`artifact: docs/formats/zjd.md:102`); the store reader, whose registration initialiser contains no parser (`artifact: docs/formats/zjd.md:103`).

## Changelog

- 2026-11-26: created this page. No earlier `artifact: docs_complete/zjd.md` existed at the time of writing. Sources: `artifact: docs/formats/zjd.md`, `artifact: final_tail_report.md:23-30`, `artifact: docs/coverage.md:162`, `artifact: docs_complete_work/format_evidence.md:390-392`. No archive scan, decoder run, asset copy, key or publication was performed. Other final documents and source files were not modified.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zjd.md`. No count was selected by modification time.

