# Type census — exact slot/byte counts

Source: `artifact: type_census.csv` (312,661,753 bytes). Header verified against all 21 declared columns.
Each CSV data row is one archive slot, so `slots` = row count for that type.

Reproduce:

```
rustc -O artifact: docs_complete/evidence/census_counts.rs -o artifact: docs_complete/evidence/census_counts.exe
artifact: docs_complete/evidence/census_counts.exe
```

Method: standalone Rust std-only CSV reader (quoted fields, doubled quotes, embedded newlines, CRLF), full-file scan, u64/u128 integer sums. No Python or PowerShell batch processing. `rustc 1.95.0`, `rustc -O`; 966 ms, ~1,299,212 rows/s.

| label | type_hash | slots | stored_bytes | logical_bytes | family (measured) | distinct roots |
|---|---|---:|---:|---:|---|---:|
| zbdr | 0000000f | 250,434 | 7,335,183,152 | 124,157,781,744 | Unknown (250,434) | 2 |
| zdr | 00000002 | 167,897 | 46,719,905,568 | 100,362,894,768 | Unknown (167,897) | 5 |
| zmap | 00000049 | 166,072 | 4,770,055,552 | 8,063,899,008 | 0DRPz (166,072) | 3 |
| zbn | 00000006 | 92,199 | 11,093,949,168 | 17,156,781,648 | Unknown (92,199) | 3 |
| zcd | 00000043 | 62,384 | 6,794,403,072 | 11,262,899,120 | Unknown (62,384) | 7 |
| zft | 00000003 | 55,488 | 5,915,592,480 | 14,211,185,152 | Unknown (55,488) | 5 |
| **combined** | six ids | **794,474** | **82,629,088,992** | **275,215,441,440** | — | — |
| all CSV rows | 37 hashes | 1,255,039 | — | — | — | — |

Checks: total rows = 1,255,039 (expected denominator, exact match); header ok; 0 schema mismatches; 0 integer-parse errors in the five checked numeric columns; 0 UTF-8 errors in the checked family/type-hash fields; sum of per-family counts = sum of per-type_hash counts = 1,255,039; each target count agrees with the general type-hash histogram; combined equals the sum of the six. These are internal consistency checks, not independent implementations of the counter. Machine-readable detail is in `census_counts.json`; TSV in `census_counts.tsv`.

Grouping: the `family` column is magic-derived, not a type id. Measured distribution: `Unknown` 867,780, `0DRPz` 290,294, `ADAT` 71,676, `PSIN` 18,640, `9FPR` 4,351, `RBF0` 1,278, `KB2` 797, `XML` 221, `SGD5` 2 (9 families, 37 type hashes). Five of the six requested hashes have family `Unknown` exclusively, so grouping by family would merge five different types into one bucket; `00000049` is `0DRPz` exclusively. Group by `type_hash` only.

Ambiguities: the resource-type labels are caller-supplied names keyed to the supplied hex ids; the CSV has no resource-type-label column, so that mapping is not independently verifiable from this source. `stored_bytes` and `logical_bytes` are summed as given; no decompression or adjustment was applied. Summed stored lengths are slot accounting, not a deduplicated measure of physical disk extents.

Artifacts: `census_counts.rs`, `census_counts.exe`, `census_counts.json`, `census_counts.tsv`, `census_evidence.md` in `artifact: docs_complete/evidence/`.

Supervising-worker verification on 2026-11-26: read the Rust source, recompiled with `rustc -O`, reran the complete counter and checked the JSON validation flags. Fresh output: `rows=1255039 elapsed_ms=925 rows_per_sec=1356798.9 schema_mismatch=0 int_err=0 header_ok=true denom_ok=true`; all six byte totals and the combined totals exactly match the table above. Language: Rust; full-file scan, 312,661,753 input bytes. This repeats the implementation and confirms reproducibility; it is not an independent parser.

## Identity

This retained document is supporting material; it introduces no independently decoded resource type. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md`.

## Counts

No additional population count is asserted in this section. Any recorded counts retain their original evidence in Verification. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md`.

## Container

No additional storage-layer claim is introduced by this section. Original placement or container observations, if any, remain in Verification. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md`.

## Fields

This support section asserts no additional binary field layout.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| not applicable | not applicable | No additional binary field is asserted | unknown | `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md` |

## Decode status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md`.

## Verification

The source text was retained during heading reconciliation. Snapshot: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md`. No new payload decode was performed by that edit.

## Unknowns

This heading does not resolve any unknown field or decoding limit. Consult the retained evidence and its source limitations. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md`.

## Changelog

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/census_evidence.md`. No count was selected by modification time.

