# `zpmd` (type code `0x45`)

Written 2026-11-26. Decode limit stated first: only the container and a header field profile with a measured extent are available for the single slot; record layout is not testable at N = 1 and element semantics are **not decoded** (`artifact: docs/formats/zpmd.md:65-75`; `artifact: final_tail_report.md:72-80`). Grade **C** (container only), matching the published Classified status (`artifact: docs/coverage.md:163`). Write status W0 (`artifact: docs/formats/zpmd.md:77-79`).


Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x45`; the executable's callback type-name table resolves it to `zpmd` (string `0x14678448c`), measured by string xref (`artifact: docs/formats/zpmd.md:5-7`). The store registration uses `PoseMatcherStore` at `0x145b92b0c`, `mov r8d,0x45`, call `0x1419ca0b0` (`artifact: docs/formats/zpmd.md:9`). Structural identity is the container only: one stream whose payload opens with two pointer cells, a `u16` pair `(20, 19)`, a `1` and `0x01000000`, with no count that sizes the payload (`artifact: docs/formats/zpmd.md:11`). A pose-data reading is inferred from the store class alone (`artifact: docs/formats/zpmd.md:13`). This is the smallest type in the package and remains Classified (`artifact: docs/formats/zpmd.md:15`).

## Counts

| Measure | Value | Source |
|---|---:|---|
| Slots | 1 | `artifact: docs_complete_work/type_counts.tsv` row `00000045`; `artifact: docs/coverage.md:163` |
| Stored bytes | 7,008 | same two sources |
| Logical bytes | 20,704 | same two sources |
| Denominator | 1,255,039 slots | `artifact: docs/coverage.md:7,40` |

The lone slot is in `anim.rpf`, with root and header generation 4 and an unresolved name hash (`artifact: docs/formats/zpmd.md:17-27`). Its stored-to-logical ratio is 2.954 (`artifact: docs/formats/zpmd.md:27`). Byte sums overlap with nested containers (`artifact: docs/coverage.md:10`).

## Container

Verified exhaustively on the one slot: sixteen stored zero bytes, `78 da` at `+0x10`, one stream with gap 0, `logical == sum(inflated)`, zero inflate errors and stored bytes accounted as `16 + compressed + trailing` (`artifact: docs/formats/zpmd.md:29-36`).

## Fields

Offsets are relative to the inflated payload; integers are little-endian (`artifact: docs/formats/zpmd.md:38-40`).

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| `+0x08`, `+0x38`, `+0x48` | 4 each | `0x50000000`-relative pointers, targets in range | measured | `artifact: docs/formats/zpmd.md:44` |
| `+0xb0` | 4 | Fourth pointer-like word; target `0x50c1` is inside the body, role unknown | measured | `artifact: docs/formats/zpmd.md:45,52` |
| `+0x40` | 4 | `0x00140013`, two u16 values 20 and 19; meaning unknown | measured | `artifact: docs/formats/zpmd.md:46` |
| `+0x44` | 4 | `1` | measured | `artifact: docs/formats/zpmd.md:47` |
| `+0x58` | 4 | `0x0000000b` (11) | measured | `artifact: docs/formats/zpmd.md:48` |
| `+0x5c` | 4 | `0x01000000` | measured | `artifact: docs/formats/zpmd.md:49` |
| `+0x00`, `+0x04`, `+0x0c..+0x34`, `+0x3c` | 4 each | Zero | measured | `artifact: docs/formats/zpmd.md:50` |
| header extent | — | Smallest pointer target `0x4b00` = 19,200 bytes; body is the remaining 1,504 bytes | measured | `artifact: docs/formats/zpmd.md:52`; `artifact: final_tail_report.md:74-75` |
| `(20,19)` pair arithmetic | — | `20*19*4 = 1,520`, 16 bytes more than the body; logical is not divisible by 20 or 19 (remainders 4 and 13) | measured | `artifact: docs/formats/zpmd.md:54`; `artifact: final_tail_report.md:76` |
| pair semantics | — | Shape, version or two counts; no owner of the 16-byte shortfall | unknown | `artifact: docs/formats/zpmd.md:54,94` |
| pose-data semantics | — | Inferred from store class only | inferred | `artifact: docs/formats/zpmd.md:13` |

The slot shares its name hash with one `zmmd` slot, but re-inflation found no shared 16-byte prefix and no size relation (`artifact: docs/formats/zpmd.md:71`). A comparison against the four `zrd` slots found 35 of 64 u32 offsets equal in at least one slot, 29 in none, and 35 equal in all four, mostly zeros; the `(20,19)` pair is the same field class as `zrd`'s `(16,17)` but no record magic or count is shared (`artifact: docs/formats/zpmd.md:72`; `artifact: final_tail_report.md:77-78`).

## Decode status

Container: measured on the one slot (`artifact: docs/formats/zpmd.md:67`). Header: field profile plus measured extent; the pair is 16 bytes short of `20*19*4` and does not size the payload (`artifact: docs/formats/zpmd.md:68-69`). Record layer: not testable at N = 1, so no stride fit is claimed (`artifact: docs/formats/zpmd.md:69`; `artifact: final_tail_report.md:80`). Element semantics: not decoded (`artifact: docs/formats/zpmd.md:70`). Grade C. No encoder or game-load test (`artifact: docs/formats/zpmd.md:79`).

## Verification

The retained census-count artifact records these reproduction commands; this documentation pass did not rerun them:

```
rustc -O artifact: docs_complete_work/count_inventory.rs -o artifact: docs_complete_work/count_inventory.exe
& artifact: docs_complete_work/count_inventory.exe artifact: type_census.csv artifact: docs_complete_work
```

Observed: `data_rows: 1255039`, `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, `malformed_or_unparsable_rows: 0` (`artifact: docs_complete_work/inventory_log.txt`); row `00000045` in `artifact: docs_complete_work/type_counts.tsv` is 1 / 7,008 / 20,704. Source-side checks quoted, not re-run: `type_probe inventory artifact: type_census.csv 00000045 out zpmd_slots.tsv` selected 1 row in 0.14 s; final Rust `zpmd_final` re-inflated 6 payloads in 0.038-0.041 s (about 147 slots/s) and produced the pointer extent, pair arithmetic and per-offset comparison; an independent one-shot re-derivation reproduced the pointer cells, pair and constants (`artifact: docs/formats/zpmd.md:81-87`). The PE was read as data only (`artifact: docs/formats/zpmd.md:89`).

## Unknowns

Raw-byte clarification: the reported u32 0x00140013 contains little-endian u16 halves 19 then 20; the source's pair notation (20,19) is not a verified dimension order. Sources: `artifact: docs/formats/zpmd.md`, Fields.

The companion/run evidence is contradictory: the zpmd report records a zmmd twin and no shared 16-byte prefix; the zmmd report says zero cross-type companions, and the final summary uses different shared-run wording. These statements establish no reconciled shared layout. Sources: `artifact: docs/formats/zpmd.md`, Decode; `artifact: docs/formats/zmmd.md`, Verification; `artifact: final_tail_report.md`, zpmd.

Everything below the container: record layout and element semantics (`artifact: docs/formats/zpmd.md:93`); whether the `(20,19)` pair is a shape, version or two counts and what owns the 16-byte shortfall (`artifact: docs/formats/zpmd.md:94`); the body reference at `+0xb0` (`artifact: docs/formats/zpmd.md:95`); the relation to the one `zmmd` name twin (`artifact: docs/formats/zpmd.md:96`); the store reader, whose initialiser has no payload parser (`artifact: docs/formats/zpmd.md:97`).

## Changelog

- 2026-11-26: created this page. No earlier `artifact: docs_complete/zpmd.md` existed at the time of writing. Sources: `artifact: docs/formats/zpmd.md`, `artifact: final_tail_report.md:72-80`, `artifact: docs/coverage.md:163`, `artifact: docs_complete_work/format_evidence.md:416-418`. No archive scan, decoder run, asset copy, key or publication was performed. Other final documents and source files were not modified.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zpmd.md`. No count was selected by modification time.

