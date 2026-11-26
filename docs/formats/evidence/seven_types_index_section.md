
<!-- BEGIN seven-resource-types-2026-11-26 -->

## Identity

This retained document is supporting material; it introduces no independently decoded resource type. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/seven_types_index_section.md`.

## Counts

No additional population count is asserted in this section. Any recorded counts retain their original evidence in Verification. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/seven_types_index_section.md`.

## Container

No additional storage-layer claim is introduced by this section. Original placement or container observations, if any, remain in Verification. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/seven_types_index_section.md`.

## Fields

This support section asserts no additional binary field layout.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| not applicable | not applicable | No additional binary field is asserted | unknown | `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/seven_types_index_section.md` |

## Decode status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/seven_types_index_section.md`.

## Verification

### Seven resource types: zdd, zsm, zascd, zldbmt, zmt, znv, zsp

These seven type codes account for **235,446 slots**, **18,437,133,488 stored bytes**, and **69,980,587,296 logical bytes**. The census denominator is **1,255,039 data rows**, comprising **1,153,560 Resource** and **101,479 Binary** rows; its header is excluded. Each row below sums only its own type's slot population. Source: [parent-verified Rust census](evidence/seven_types_census.parent_verified.txt), sections `[DENOMINATOR]`, `[TOTALS]`, `[PER_TARGET]`, and `[PER_TARGET_ROOT]`; input `artifact: type_census.csv` (312,661,753 bytes).

| Type code | Documentation | Slots | Stored bytes | Logical bytes | Grade and bounded decode reach |
|---|---|---:|---:|---:|---|
| `0x04` | [zdd](zdd.md) | 48,584 | 6,309,542,464 | 14,577,057,200 | Partial: root header, name region, pointer tables; referenced object payloads unresolved; historical probe unavailable in the current tree. |
| `0x58` | [zsm](zsm.md) | 40,019 | 659,721,600 | 1,531,499,328 | Partial: header, descriptors, one bounding-box variant on 8,741 slots; array-element meanings unresolved; historical probe unavailable in the current tree. |
| `0x6c` | [zascd](zascd.md) | 32,878 | 554,083,984 | 5,935,045,424 | Partial: shared wrapper, descriptor layout and family-level text-blob interpretation; no verified type-specific payload decoder or attributed text yield. |
| `0x6f` | [zldbmt](zldbmt.md) | 30,511 | 217,945,568 | 680,928,064 | Partial: shared wrapper, descriptor layout and family-level text-blob interpretation; no verified type-specific payload decoder or attributed text yield. |
| `0x0b` | [zmt](zmt.md) | 28,328 | 4,920,841,360 | 29,509,517,168 | Partial: shared wrapper, descriptor layout and family-level text-blob interpretation; other blob and payload meanings unresolved. |
| `0x4f` | [znv](znv.md) | 27,644 | 5,398,485,440 | 15,420,757,856 | Partial: tile header, node hierarchy and mesh arrays on 138/200 historically sampled slots; 62/200 walker failures remain. |
| `0x64` | [zsp](zsp.md) | 27,482 | 376,513,072 | 2,325,782,256 | Partial: container, bucket/hash structure, token fields and flags; token, flag and key semantics unresolved. |

The grade is a summary of documented structural reach, not a claim that all slots are semantically decoded. Each linked document separates historical measurements from commands available today and uses `measured`, `inferred`, `external`, or `unknown` for field confidence. Source: the linked documents' Decode status, Fields, and Verification sections.

Scope corrections: the supplied census gives **235,446**, rather than an estimated 245,000, slots for these codes. It recognizes `0DRPz` / `0DRPz@16` for exactly three of these codes (`0x6c`, `0x6f`, `0x0b`); the other four have `family=Unknown` and `magic=<null>`. That signature classification does not establish the absence of every possible nested wrapper. Source: [census distributions](evidence/seven_types_census.parent_verified.txt), `[DISTRIBUTIONS]`. The old coverage table's Classified rows are reconciled with later per-type evidence inside the linked documents.

Reproduce the census with Rust, without an archive scan:

```powershell
Set-Location artifact: docs_complete/evidence
rustc -O seven_types_census.rs -o seven_types_census.exe
.\seven_types_census.exe artifact: type_census.csv artifact: docs_complete/evidence/seven_types_census.parent_verified.txt
```

Run `artifact: docs_complete/evidence/verify_seven_docs.ps1` to check the eight required headings and the exact field-confidence vocabulary. Documentation revision: 2026-11-26. Five fast-worker leaves supplied four document scans and one independent Rust census pass; the supervising worker reran the counter and reviewed the outputs. The section fragment is retained as [merge evidence](evidence/seven_types_index_section.md).
<!-- END seven-resource-types-2026-11-26 -->

## Unknowns

This heading does not resolve any unknown field or decoding limit. Consult the retained evidence and its source limitations. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/seven_types_index_section.md`.

## Changelog

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/evidence/seven_types_index_section.md`. No count was selected by modification time.

