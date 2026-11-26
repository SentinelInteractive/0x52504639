# `znv` (type code `0x4f`)

Written 2026-11-26. Local sources only; no public URL or competitor material was consulted and no external claim is used as measurement. **Beyond-container decode is available only in a bounded form: the full-population zlib chain, the root header through `+0x10c`, the 0x60-byte node array and the footer-declared mesh arrays are decoded; the mesh walk succeeds on a 200-slot stratified sample (138 of 200), not on the whole population. Vertex-element semantics, node-field semantics, the footer mask words and the walker's 62 failures are not decoded.** There is no encoder; write status W0. Sources: `artifact: docs/formats/znv.md`, `artifact: t5/findings_znv.md`, `workspace: coverage_audit/out/tables.md`, `artifact: type_census.csv`, `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt`, `workspace: CONTEXT_HANDOFF.md`.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The +16 resource type word is `0x4f`. The executable's variant-0 name is `znv`; the other two variant strings are `inv` and `#nv` (`docs/formats/znv.md:7,75`; `artifact: enum_variant_discriminant_report.md:66`). It sits in the callback table at `0x14618d9e0`, unlike the static-enum types (`0drpz.md:76`; `enum_variant_discriminant_report.md:66`). The neighbouring codes `0x50..0x55` are `znvs`, `zpl`, `znd`, `zvr`, `zwr`, `znh`, a navigation-name block in the executable's own table (`znv.md:7,76`; `findings_znv.md:112`).

- Structural identity, measured: a tile record with an identity 3×4 transform, a tile scale pair, a node hierarchy of 0x60-byte nodes carrying box corners in whole metres, and a footer declaring a 12-byte vertex array and a `u16` index array (`znv.md:9`).
- Semantic identity, inferred: a navigation-mesh tile. Node corner pairs are integer metre magnitudes 256 m apart with a constant height term, and the index array maximum equals the vertex count minus one, a closed mesh (`znv.md:10`). The note declines to expand the tag and claims the mesh structure instead (`znv.md:12`).

Executable-side naming (`znv.md:75-77`): name-table VA `0x14618da58` (variant 0) points to `znv` at `0x1467795a2`, variant 1 `inv` at `0x1467795a6`; external, verified as given. No handler, constructor or RTTI record was located in a bounded search.

## Counts

Per-root breakdown from `PER_TARGET_ROOT` of the parent-verified census (`evidence/seven_types_census.parent_verified.txt`), which confirms a single root:

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `navmeshes.rpf` | **27,644** | **5,398,485,440** | **15,420,757,856** |
| **Total** | **27,644** | **5,398,485,440** | **15,420,757,856** |

Sources: `evidence/seven_types_census.parent_verified.txt` `[PER_TARGET]` row `0000004f` and `[PER_TARGET_ROOT]`; `docs/formats/znv.md:16-23`, `t5/findings_znv.md:8` (rechecked from `4f_znv_slots.tsv` and `type_census.csv`), `coverage_audit/out/tables.md:17`, `CONTEXT_HANDOFF.md:174`, all in agreement.

- Denominator: **1,255,039** data rows in `artifact: type_census.csv`, every row counted regardless of kind: **1,153,560 Resource + 101,479 Binary**, with `malformed_rows: 0` (`evidence/seven_types_census.parent_verified.txt`, `[DENOMINATOR]` and `[ALL_ROWS_KIND_DISTRIBUTION]`). This is not a Resource-only denominator. All 27,644 `znv` rows are `Resource`, family `Unknown`, magic `<null>` (`[DISTRIBUTIONS]`).
- Source file size: `source_file_size_bytes: 312,661,753`, exact from the census evidence header.
- Units: **stored bytes** include the 16-byte prefix, inter-stream padding and trailing zero run; **logical bytes** equal the sum of inflated stream lengths with that 16-byte prefix excluded, measured 27,644/27,644 (`znv.md:31-32`).
- Header generation 4 in 27,644/27,644 and root generation 4 in 27,644/27,644; every slot is a `Resource` entry (`znv.md:21`; `findings_znv.md:9`).
- Name origin: 27,585 unresolved hashes (5,398,226,352 stored / 15,419,915,360 logical) and 59 dictionary matches (259,088 / 842,496), with 59 distinct matched names, none reproduced (`znv.md:22`; `findings_znv.md:10`).
- Logical size, measured (`znv.md:23`): min 1,136 B, p25 132,912, median 132,912, p75 720,896, p90 1,769,472, p99 3,485,456, max 7,733,248 B; mean 557,834 B. A second local note gives p99 3,486,960 and mean 557,833.81 (`findings_znv.md:13`); the tail quantiles differ by rounding or sample convention and no population claim rests on those two digits.
- Twelve distinct archive headers hold the slots: ten with 2,448 each, one with 3,002 and one with 162; 10×2,448 + 3,002 + 162 = 27,644 (`znv.md:25`; `findings_znv.md:12`).

## Container

Measured on all 27,644 slots (`docs/formats/znv.md:29-37`; `t5/findings_znv.md:14`):

| Item | State | Confidence |
|---|---|---|
| Prefix | 16 zero bytes at stored `+0x00` and `0x78DA` at stored `+0x10`: 27,644/27,644 | measured |
| Compression | zlib; each chain starts with a `78 da` header at `+0x10` | measured |
| Pages | One stream in 4,598 slots, two in 23,046; 50,690 streams total | measured |
| Alignment | Every stream start is 16-byte aligned; 1,512 of 23,046 inter-stream boundaries have no padding and 21,534 carry 1-15 bytes | measured |
| Chain | `logical == sum(inflated stream lengths)` in 27,644/27,644; the 16 stored zero bytes are outside `logical` | measured |
| Tail | 26,907 slots have a zero run between the last stream and the stored-range end | measured |

Stream count does not track size: the largest slot (7,733,248 B) is a single stream, while a 132,912 B modal slot has two. In two-stream slots the first stream ends on a 64 KiB multiple of output (131,072, 1,441,792, 3,932,160 observed), so the split follows virtual page boundaries rather than a fixed byte budget (`znv.md:36`). An earlier chain tool capped output at `logical − 16` and produced a spurious "inflates to logical minus 16" reading; that tool was fixed and the claim withdrawn (`znv.md:37`; `findings_znv.md:35`).

## Fields

Offsets are relative to the first inflated byte. Column labels are offsets unless a meaning is sourced. Confidence vocabulary: measured / inferred / external / unknown. Population histograms cover the first inflated stream of all 27,644 slots; full-payload values come from a 200-slot stratified sample (`znv.md:41`; `findings_znv.md:45`).

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00` | u64 | zero in 27,644/27,644 | measured |
| `+0x08` | u32 | relative pointer `0x50000000+offset`; 143/27,644 resolve inside the first-stream cap, 200/200 inside full payloads | inferred |
| `+0x10` | u32 | discriminator counts: 9 in 18,791 slots, 11 in 5,507, 3 in 3,149, 7 in 161, 1 in 35. These sum to 27,643; one of the 27,644 slots is not represented, so this is not an exhaustive distribution | unknown |
| `+0x14` | u32 | `0x00010015` (65,557) in 27,644/27,644 | unknown |
| `+0x18` | u64 | zero in all | measured |
| `+0x20`–`+0x4c` | 12 × f32 | identity 3×4 matrix; the `1.0` word in 27,644/27,644, remaining words zero | inferred |
| `+0x60`, `+0x64` | 2 × f32 | 128.0 in 27,482 slots; the 162 smallest-header slots carry other values (13.875, 11.0, 3.25 …) | inferred |
| `+0x68` | f32/u32 | zero in 136/200 sampled slots, otherwise small floats or integers | unknown |
| `+0x6c` | u32 | zero in all | measured |
| `+0x70` | u32 | relative pointer to the footer descriptor table, in range in 200/200 full payloads | inferred |
| `+0x80`, `+0x88`, `+0x98` | u32 | further descriptor pointers, in range in 200/200 | inferred |
| `+0x90` | u32 | array count, modal 4,352 in 15,461 of 27,644 slots | inferred |
| `+0xa0` | u32 | pointer to a 0x60-byte-stride node array | inferred |
| `+0xa8`, `+0xb0`, `+0xb8` | u32 | zero or a valid pointer in sampled full payloads; exact frequency unavailable | unknown |
| `+0xc0`, `+0xc4` | 2 × u32 | counts, modal 1,089 and 1,152 in the same 15,461-slot family | inferred |
| `+0xc8`, `+0xcc` | 2 × u32 | counts/sizes, modal 148,128 and 118,150 in the same family | unknown |
| `+0xe8` | u32 | `0x09090516` in 24,474 of 27,644 | unknown |
| `+0xf8`, `+0x104` | u32 | 16 in 138/200 sampled slots | measured |
| other words | u32 | `+0x04`, `+0x0c`, `+0x1c`, `+0x24`–`+0x5c`, `+0x74`–`+0x7c`, `+0x84`–`+0x8c` zero in all sampled full payloads | measured |

Declared structure from a modal-size slot with footer at `0x206c0` (`znv.md:65-71`; `findings_znv.md:82-86`):

- Footer declares two 16-byte-stride entries: a vertex array at `0x1a2c0` with 1,089 elements of 12 bytes and an index array at `0x180c0` with 4,352 `u16` values.
- The index array maximum is 1,088 with 1,089 unique values, exactly the vertex count range; 1,089 = 33 × 33. The pair closes as a mesh.
- Each 12-byte vertex element has a strong 12-byte periodicity and six 16-bit slots including `0xffff` sentinels; it is not a float triple.
- Node records at the `+0xa0` target are 0x60 bytes: two float pairs plus a constant 0.35, with corner pairs such as (−12,288, 4,224) and (−12,032, 4,352), integer metre magnitudes 256 apart.
- Footer mask words 1,365 / 2,730 / 4,095 follow the array descriptors in modal slots; no meaning is claimed.

## Decode status

The verdict is **Partial**, settled by measurement: the container, tile header, node hierarchy and mesh arrays are located and walked (`docs/formats/znv.md:81-89`; `findings_znv.md:101-107`). `CONTEXT_HANDOFF.md:174`, `artifact: docs/coverage.md:139`, `artifact: repo-publisher/docs/type_registry.md:50` and `artifact: deep_layers.md:12` agree. The older `coverage_audit/out/tables.md:17` Classified row is superseded by those measurements and is not an open question. The unresolved counts are kept below: 138/200 mesh walks succeed and 62/200 fail.

Precise bounded capability (`znv.md:81-89`; `findings_znv.md:101-107`):

- Full population: container on 27,644/27,644 slots; chain rule and stream histogram on 27,644/27,644.
- Full population with a 32 KiB first-stream cap: field histograms on all 27,644 slots; full chains are required for deeper fields because 19,237/27,644 slots hit that cap (`findings_znv.md:118`).
- 200-slot rank-stratified sample: root header through `+0x10c`, footer pointer, discriminator, identity matrix, 128.0 pair and five descriptor pointers byte-checked on 200/200 fully inflated payloads.
- 200-slot sample mesh walk: 138/200 succeed. A pair is accepted when the vertex span `ptrA + nA*12` and index span `ptrB + nB*2` fit the buffer and every `u16` index is below `nA`.
- Explanation stops at the footer mask words, inside the 0x60-byte node records from `+0x18` onward, and at the six 16-bit vertex fields. The 62 walk failures concentrate in larger slots whose footers expose fewer aligned `(pointer, count)` pairs; that is a walker gap, not a format finding. No encoder; W0 (`znv.md:91-93`).

**Current decoder command exists and was re-run on 2026-11-26.** The binary `artifact: t5/znv_probe/target/release/znv_probe.exe` is present (412,672 bytes). Its `--help` usage string lists `inventory | container N | fields N | one off stored logical out`, but `walk` and `meshfile` are also implemented and were used in the source evidence; a bounded recheck `znv_probe.exe walk 5` returned `walk tried=5 ok=3 in 0.1s`. No bulk decode was run for this document. Commands from `t5/findings_znv.md:107`:

```powershell
cd artifact: t5/znv_probe
cargo build --release --offline
.\target\release\znv_probe.exe container 200
.\target\release\znv_probe.exe fields 200
.\target\release\znv_probe.exe walk 200
.\target\release\znv_probe.exe meshfile out\one110.bin
```

`slot.exe <root> <abs_offset> <stored> <logical> <out.bin>` (`artifact: t5/slot/target/release/slot.exe`) is a single-slot inflator, but its `exact` flag caps output at `logical−16`; it must not define the logical-size rule (`findings_znv.md:29,35`).

## Verification

Short inline paths resolve as follows: `znv.md` = `artifact: docs/formats/znv.md`; `findings_znv.md` = `artifact: t5/findings_znv.md`; `tables.md` = `workspace: coverage_audit/out/tables.md`; `CONTEXT_HANDOFF.md` = `workspace: CONTEXT_HANDOFF.md`; `evidence/...` = `artifact: docs_complete/evidence/...`.

- Parent-verified common census, fresh citation. Reproduction, run from the evidence directory:

```powershell
cd artifact: docs_complete/evidence
rustc -O seven_types_census.rs -o seven_types_census.exe
.\seven_types_census.exe artifact: type_census.csv artifact: docs_complete/evidence/seven_types_census.parent_verified.txt
```

  Exact output used here: `source_file_size_bytes: 312661753`; `total_data_rows_denominator: 1255039`; `Resource 1153560`, `Binary 101479`, `all_rows_kind_sum: 1255039`; `malformed_rows: 0`; `0000004f` row `27644 / 5398485440 / 15420757856`, zero stored, zero logical, zero unparsable. Its `[PER_TARGET_ROOT]` has the single root `navmeshes.rpf` with the same triple, reproduced in Counts. Timing in the evidence: `total_seconds: 0.660435`, `rows_per_sec_total: 1900322.33`, `bytes_per_sec_total: 473418046.72`, `MiB_per_sec_total: 451.49`. All figures are read from the cited file; no new scan was run for this document. Language of the census tool: Rust (`rustc -O`).
- Whole-census reconciliation in Rust reproduces 27,644 / 5,398,485,440 / 15,420,757,856 (`znv.md:97`).
- Population chain walk, Rust, 32.1 s for 5.4 GB stored / 15.4 GB inflated: `sum(inflated) == logical` 27,644/27,644, stream histogram 1→4,598 and 2→23,046, 0 unterminated streams, 0 unaligned starts, 26,907 zero-tail slots (`znv.md:98`).
- Independent population verifier, Rust, 3.1 s: prefix, `0x78DA`, `u64@0 == 0` and `+0x08` pointer range, 27,644/27,644 on each (`znv.md:99`).
- Field population histograms over 27,644 slots: `+0x14` constant 65,557; `+0x20` = `1.0f` in all; `+0x10` five distinct values; `+0x60`/`+0x64` = 128.0 in 27,482 (`znv.md:100`).
- Stratified samples: 1,136 B, 132,912 B (median/modal), 720,896 B and 7,733,248 B; all inflate to exactly `logical` (`znv.md:101`). Sample timings, Rust: `container 200` 0.44 s, `fields 200` 0.41 s, `walk 200` 0.40 s, `inventory` 0.83 s (`findings_znv.md:139-147`). Fresh bounded recheck 2026-11-26: `znv_probe.exe walk 5` → `walk tried=5 ok=3 in 0.1s`.
- Hypotheses rejected (`znv.md:102`; `findings_znv.md:119-124`): `0x4f` is not `0x64` at another LOD (different header shape, zero shared header offsets, different size and array distributions); the 1,089-element array is not f32 triples; "index count is a multiple of four" was withdrawn, since the modal count 4,352 is divisible by four; the initial "distinct matched paths = 1" came from reading the wrong TSV column and is invalid.
- Language: Rust for all archived probes and for the census tool; the only new checks here were bounded CLI calls. No Python pipeline was used. Pending gap: a population-wide mesh walk.

## Unknowns

Each item is an open question with a proposed test. A "To settle" line is a proposal, not a measurement already performed.

1. Semantics of the six 16-bit fields per 12-byte vertex element and the quantisation scale to metres (`znv.md:106`). To settle (proposal): decode vertex elements in one tile and compare them with the 0x60-byte node box corners, reporting residual in metres under candidate scales.
2. Footer mask words 1,365 / 2,730 / 4,095 and the 1–15 trailing stored bytes are unassigned (`znv.md:107`). To settle (proposal): histogram mask words across the 200-slot sample against vertex and index counts, and align trailing stored bytes to the next stream start; report any exact relation found.
3. Fields from `+0x18` onward in each 0x60-byte node and the four child pointers are unresolved (`znv.md:108`). To settle (proposal): walk parent to child inside one tile, map node fields to tile coordinates and report which fields track the 256 m grid.
4. Footer layout for large slots; the walker fails on 62 of 200 stratified samples (`znv.md:109`). To settle (proposal): inspect the 62 failed payloads for aligned `(relptr, count)` pairs under explicitly stated relaxed constraints and report recovered counts; the acceptance rule must not be changed post hoc.
5. Any handler, constructor or vtable on the executable side is unknown (`znv.md:110`). To settle (proposal): run a bounded executable xref from the callback-table slot for `0x4f` and report any RTTI or vtable pointer with a verified string xref, or record a clean negative.
6. Meaning of the `+0x10` discriminator values is unknown, and the measured counts sum to 27,643, leaving one of 27,644 slots unrepresented. To settle (proposal): re-run the histogram over all 27,644 full payloads, identify the missing slot and report its value.
7. Exact frequency of zero versus pointer in `+0xa8`/`+0xb0`/`+0xb8` is unavailable. To settle (proposal): histogram the three words over all 27,644 full payloads and report exact zero and in-range counts.

## Changelog

- 2026-11-26: document created. Reconciled the stale `coverage_audit/out/tables.md:17` Classified row against the 2026-11-24 per-type note and handoff Partial verdict, with the 138/200 sample explicitly bounded. Records 27,644 / 5,398,485,440 / 15,420,757,856 against the 1,255,039 all-row denominator (1,153,560 Resource + 101,479 Binary), with the navmeshes-only root split from the parent-verified census. Verifies the current `znv_probe` decoder and re-runs a bounded `walk 5` check. Confidence cells normalized to measured/inferred/external/unknown; rounded percentages and derived speeds removed; the single-slot shortfall in the variant distribution is flagged. No public URL, no competitor names, no invented semantic fields, no bulk decode.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/znv.md`. No count was selected by modification time. Reconciliation decisions: rejected the nonexistent drive-D audit-table citation in favor of the existing workspace artifact.

