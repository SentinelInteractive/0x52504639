# `zmt` (type code `0x0b`)

**Grade: C — container/wrapper only.** No type-specific beyond-container decoder is verified for `zmt`: there is no verified `zmt`-specific semantic decoder, no per-type decode audit and no cited payload field map or record stride. A generic `0DRPz` family extractor does exist and is cited in Decode status; it is not a `zmt` semantic decoder. Family-level `0DRPz` wrapper, descriptor-table and text/localisation support exists, but it is family evidence, not a type-wide decode of `0x0b`, and the family sweep was never split by type word, so no decode count below is attributable to code `0x0b` alone. Written 2026-11-26 from local artifacts cited inline; no archive scan or new census aggregation was run for this page. One external URL is cited as a historically recorded check only and was not re-fetched here. Short-path aliases are resolved at the start of Verification. Counts are index slots; byte sums of nested containers overlap and are not unique physical bytes (`artifact: type_census.md`:7; `workspace: CONTEXT_HANDOFF.md`:section 4).


Additional citation aliases: `type_inventory.md` = `artifact: docs_complete_work/type_inventory.md`; `rpf9-container.md` = `artifact: repo-publisher/docs/rpf9-container.md`.

Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The +16 resource type word is `0x0b`. The executable's variant-0 name-table entry at `0x1462fcd30` reads `zmt`; the other two variant strings are `imt` and `#mt` (`artifact: enum_variant_discriminant_report.md`:34,53). The type word lies in the static enum block `0x00..0x12`, not the callback table. This is a local executable-byte reading.

The family note `0drpz.md`:11-22 lists eight codes carrying the `0DRPz` signature. The parent-verified census classifies the `0DRPz` family among the seven audited types as exactly three: `zascd` `0x6c`, `zldbmt` `0x6f` and `zmt` `0x0b` (`evidence/seven_types_census.parent_verified.txt`, `[DISTRIBUTIONS]`). These are different scopes, a signature-family claim and a census classification, and are not merged.

- Structural identity, measured at family scope: a page resource with a 0x50-byte `0DRPz` root struct, a blob descriptor table whose listed fields (`u32 id`, `u32 len`, `u64 virtual ptr`) sum to 16 bytes, and typed blobs addressed by relative virtual pointers (`0drpz.md`:36-53; `drpz-localisation.md`:3,9-31). The localisation page calls the record 12-byte; that label conflicts with its own field widths and is treated as a known discrepancy, not as a stride.
- Semantic identity, unknown at type scope. The four-blob combination `0x10`, `0x101`, `0xA8478889`, `0x99331089` is a localisation table (`drpz-localisation.md`:47-56), but no source in this workspace assigns a `zmt`-specific meaning to code `0x0b`. No semantic field is invented here.
- Status is Partial in the current table (`artifact: docs/coverage.md`:138); the older `tables.md` status column is not imported.

## Counts

Per-root breakdown from `PER_TARGET_ROOT` of the parent-verified census (`evidence/seven_types_census.parent_verified.txt`), which resolves the earlier root-split gap:

| Root | Slots | Stored bytes | Logical bytes | Evidence |
|---|---:|---:|---:|---|
| `data.rpf` | 1,286 | 9,926,544 | 23,327,376 | `seven_types_census.parent_verified.txt`, `[PER_TARGET_ROOT] [0000000b]` |
| `levels.rpf` | 19,950 | 4,259,670,768 | 28,161,239,552 | same |
| `navmeshes.rpf` | 1,188 | 7,073,280 | 28,633,456 | same |
| `pack/shared_minigame000/shared_minigame000.rpf` | 1 | 2,208 | 4,896 | same |
| `pack/story000/story000.rpf` | 3,916 | 583,839,296 | 1,136,030,480 | same |
| `pack/story000_restofworld/story000_restofworld.rpf` | 26 | 7,089,024 | 15,879,392 | same |
| `packs.rpf` | 1,961 | 53,240,240 | 144,402,016 | same |
| **Total** | **28,328** | **4,920,841,360** | **29,509,517,168** | `seven_types_census.parent_verified.txt`, `[PER_TARGET] [0000000b]` |

The total triple is independently corroborated by `artifact: docs_complete_work/type_inventory.md` section 3, `artifact: docs/coverage.md`:138 and `workspace: CONTEXT_HANDOFF.md`:173.

- Denominator: **1,255,039** data rows in `artifact: type_census.csv`, every row counted regardless of kind: **1,153,560 Resource + 101,479 Binary**, with `malformed_rows: 0` (`evidence/seven_types_census.parent_verified.txt`, `[DENOMINATOR]` and `[ALL_ROWS_KIND_DISTRIBUTION]`). This is not a Resource-only denominator. All 28,328 `zmt` rows are `Resource` with family `0DRPz` and magic `0DRPz@16` (`[DISTRIBUTIONS]`).
- Source file size: `source_file_size_bytes: 312,661,753`, exact from the census evidence header.
- The `0DRPz` family triple, a different and broader scope, is 290,294 slots / 12,137,708,928 stored / 51,368,850,240 logical (`0drpz.md`:26-27; `tables.md`:49). The ratio between the type and family counts is 28,328 / 290,294 and is not a decode count.
- Units: **stored bytes** are on-disk compressed extents including the 16-byte prefix, inter-stream padding and any trailing run; **logical bytes** are the declared resource size. For the family the 16-byte prefix sits outside the compressed and encrypted stream (`0drpz.md`:72). Whether the declared logical size for code `0x0b` includes that prefix was not separately measured; see Container and Unknowns.

## Container

Family-level prefix, compression and wrapper framing are measured across all 290,294 `0DRPz` slots (`0drpz.md`:36-72,100); the per-`0x0b` stream histogram is not.

| Item | State | Confidence | Evidence |
|---|---|---|---|
| Prefix | 16 zero bytes at stored `+0x00`; signature `0DRPz` at inflated `+0x10`, measured 290,294/290,294 family slots | measured | `0drpz.md`:36-41,100 |
| Compression | zlib stream beginning at stored `+0x10` | measured | `0drpz.md`:39-41,72 |
| Pages | Family resources are page resources; a known localisation page drops 1,908 strings to a second page | measured | `drpz-localisation.md`:117 |
| Alignment | Unknown. The 16-byte prefix is a measured field but does not imply page or stream alignment; no per-`0x0b` stream-start histogram was measured | unknown | `0drpz.md`:39; per-code histogram absent |
| Chain | One or more zlib streams; continuation pages occur. Per-`0x0b` stream-count histogram, padding distribution and the `logical == sum(inflated)` identity are not separately measured | unknown | `0drpz.md`:109-110; `drpz-localisation.md`:117 |

Inflated resource prefix, from `0drpz.md`:41-53 and `drpz-localisation.md`:13-35:

```
+0x00  u64 zero
+0x08  u64 reference pointer, virtual
+0x10  root struct, 0x50 bytes
         +0x00  "0DRPz"
         +0x10  u32 variant word
         +0x18  u64 pointer
         +0x28  u64 pointer to blob descriptor table
         +0x30  u64 pointer
         +0x38  u32 (count reading disputed; see Fields)
         +0x3C  u32 low u16 = descriptor count, high u16 = other bits, semantics not established
blob table: count * { u32 id, u32 len, u64 virtual ptr }   -- fields sum to 16 bytes
```

A virtual pointer minus the resource's own base gives an offset inside that resource. Observed bases include `0x50000000`, `0x60000000`, `0x40000000` and zero; the base is per resource, not global (`0drpz.md`:54-55; `drpz-localisation.md`:33).

## Fields

Offsets are relative to the first inflated byte. Confidence is exactly measured / inferred / external / unknown. Observations in this table are family-level (`0drpz.md`, `drpz-localisation.md`) and are not a `zmt`-specific population histogram.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| `+0x00` | u64 | zero | measured | `0drpz.md`:42 |
| `+0x08` | u64 | Reference pointer, virtual; target meaning not established | unknown | `0drpz.md`:43 |
| `+0x10` | 0x50 bytes | `0DRPz` root struct; magic at root `+0x00` | measured | `0drpz.md`:44-45 |
| root `+0x10` | u32 | Variant word; meaning not established | unknown | `0drpz.md`:46 |
| root `+0x18` | u64 | Pointer | measured | `0drpz.md`:47 |
| root `+0x28` | u64 | Pointer to the blob descriptor table | inferred | `0drpz.md`:48 |
| root `+0x30` | u64 | Pointer | measured | `0drpz.md`:49 |
| root `+0x38` | u32 | Count reading disputed: `drpz-localisation.md`:28-29 calls it a descriptor count, `0drpz.md`:64 says reading it as a count is wrong | unknown | `drpz-localisation.md`:28-29; `0drpz.md`:64 |
| root `+0x3C` | u32 | Low u16 = descriptor count; high u16 = other bits, meaning not established | inferred | `0drpz.md`:51,64 |
| descriptor `+0x00` | u32 | Blob id | measured | `0drpz.md`:52; `drpz-localisation.md`:41-43 |
| descriptor `+0x04` | u32 | Blob byte length | measured | `drpz-localisation.md`:44 |
| descriptor `+0x08` | u64 | Virtual pointer to blob data | measured | `drpz-localisation.md`:45 |
| blob `0x10` | variable | NUL-separated UTF-8 string pool | inferred | `0drpz.md`:59; `drpz-localisation.md`:51 |
| blob `0x101` | 16-byte records | `{u32 hash, u32 0, u32 (n<<16) &#124; 1, u32 0}`; meaning of the hash not established | unknown | `0drpz.md`:60,90 |
| blob `0xA8478889` | variable | Per-string offsets | inferred | `0drpz.md`:61 |
| blob `0x99331089` | variable | Pool/schema descriptor | inferred | `0drpz.md`:62 |

Both source contradictions are retained, not silently reconciled: `drpz-localisation.md`:39 calls the descriptor a 12-byte record while its own listed fields (`u32 id`, `u32 len`, `u64 ptr`, `drpz-localisation.md`:41-45) total 16 bytes, as in `0drpz.md`:52; and the descriptor count is read from the low u16 of `root+0x3C` (`0drpz.md`:64), not from `root+0x38` as `drpz-localisation.md`:28-29 also states. The four blob ids together are the localisation combination; the `0x10` pool alone also occurs in name-bearing resources, so a pool alone does not make a text table (`drpz-localisation.md`:56). No `zmt`-specific blob-id distribution was measured.

## Decode status

**Source chronology, stated explicitly.** `workspace: coverage_audit/out/tables.md`:16 is an older snapshot that lists `zmt` as Partial; the current `artifact: docs/coverage.md`:138 and `CONTEXT_HANDOFF.md`:173 give the same verdict. There is no status conflict for this type. The limitation is scope: the localisation run covered four archives and the `0DRPz` family, giving 68,412 `0DRPz` resources, 25,834 tables and 7,289,933 strings (`drpz-localisation.md`:83-97); those are family counts and are not attributed to `zmt`.

Precise bounded capability: wrapper, root fields, descriptor table and the four text blob ids decode at family level; the classifier accepts a pool with at least 10 strings, mean length at least 8 and at least 0.90 valid UTF-8 strings (`0drpz.md`:66-70; `drpz-localisation.md`:60-79). Explanation stops at non-text blob ids, continuation pages, the external key-name hash behind `0x101`, and the disputed `root+0x38` word. No encoder; write status W0 (`0drpz.md`:92-96). No `zmt`-specific semantic decoder exists; the generic family extractor is described next.

**Current family extractor exists; no `zmt`-specific semantic decoder exists.** The binary `workspace: drpz/target/release/drpz.exe` is present in the project tree, with source `workspace: drpz/src/main.rs`:871-924 (`parse_args`). The parent ran `drpz.exe --help` with exit 0 and saved the output at `artifact: docs_complete/evidence/drpz_help.txt`. Accepted switches are `--store`, `--out`, `--archive NAME[,NAME]|all`, `--limit`, `--mode stats|redact|text`, `--redact`, `--text`, `--min-strings`, `--min-mean`, `--names`, `--no-spans` and `--help`/`-h`. Default mode is `stats`: structure and counts only, no strings written; `--text` is the only mode that writes strings. This extractor decodes the `0DRPz` wrapper, descriptor table and text pools for the family. It is not a `zmt` semantic decoder: it does not resolve non-text blob ids, the disputed `root+0x38` word or key names behind blob `0x101`. An earlier statement that the binary and source were absent was scoped only to `artifact: `; that search never covered the project tree under `workspace: `, so the absence claim is withdrawn. No extraction was run for this document. `srpf9.exe --help` (bounded check, 2026-11-26) lists only `info, scan, toc, carve, mhiu, tpfd, model, material, psin, awc, bench`, so there is no `zmt` command there. Inspection commands, using binaries confirmed present by prior bounded checks on 2026-11-26:

```powershell
# enumerate code 0x0b slots from the census (type_probe usage: inventory|walk|samples|hex|join)
& 'artifact: type_reports/probe/target/release/type_probe.exe' inventory 'artifact: type_census.csv' 0000000b 'artifact: _zmt_inspect'

# inflate one slot selected from that inventory: slot.exe <root> <abs_offset> <stored> <logical> <out.bin>
& 'artifact: t5/slot/target/release/slot.exe' <root> <abs_offset> <stored> <logical> <out.bin>
```

## Verification

Short inline paths resolve as follows: `0drpz.md` = `artifact: docs/formats/0drpz.md`; `drpz-localisation.md` = `artifact: repo-publisher/docs/drpz-localisation.md`; `tables.md` = `workspace: coverage_audit/out/tables.md` (workspace path, older snapshot); `CONTEXT_HANDOFF.md` = `workspace: CONTEXT_HANDOFF.md`; `evidence/...` = `artifact: docs_complete/evidence/...`.

- Parent-verified common census, fresh citation. Reproduction, run from the evidence directory:

```powershell
cd artifact: docs_complete/evidence
rustc -O seven_types_census.rs -o seven_types_census.exe
.\seven_types_census.exe artifact: type_census.csv artifact: docs_complete/evidence/seven_types_census.parent_verified.txt
```

  Exact output used here: `source_file_size_bytes: 312661753`; `total_data_rows_denominator: 1255039`; `Resource 1153560`, `Binary 101479`, `all_rows_kind_sum: 1255039`; `malformed_rows: 0`; `0000000b` row `28328 / 4920841360 / 29509517168`, zero stored, zero logical, zero unparsable. Its seven `PER_TARGET_ROOT` rows for `0000000b` sum to the same triple and are reproduced in Counts. Timing in the evidence: `total_seconds: 0.660435`, `rows_per_sec_total: 1900322.33`, `bytes_per_sec_total: 473418046.72`, `MiB_per_sec_total: 451.49`. All figures are read from the cited file; no new scan was run for this document. Language of the census tool: Rust (`rustc -O`).
- Family signature at inflated `+0x10`: 290,294 / 290,294; type-word join delta zero for all eight codes (`0drpz.md`:100-101).
- Family sweep: 287,361 streams, 24,234,233,148 raw bytes, 2,072.1 MB/s and 25,764 streams/s (`drpz-localisation.md`:95-96; `0drpz.md`:102). These are **family-level** Rust throughput figures, not a `zmt` measurement.
- Determinism: byte-identical `tables.csv` SHA-1 across two runs (`drpz-localisation.md`:108). String pool sample: 0 invalid UTF-8, 0 control characters (`0drpz.md`:104).
- External attribution, not a current local measurement: a prior process recorded a historical check on 2026-11-26 of `https://raw.githubusercontent.com/SentinelInteractive/0x52504639/main/docs/drpz-localisation.md`. That URL was not re-fetched for this page, so no current external verification is asserted. It labels the blob descriptor a 12-byte record, but its listed fields sum to 16 bytes; the 12-byte stride is not imported. The same discrepancy is verifiable locally at `drpz-localisation.md`:39,41-45.
- Current family extractor, run by the parent and not re-run here: `& 'workspace: drpz/target/release/drpz.exe' --help` exited 0; output saved at `artifact: docs_complete/evidence/drpz_help.txt` (8 lines). The switches match `workspace: drpz/src/main.rs`:871-924, with the `--help` branch at `:906-916`. No extraction, no text output and no archive scan were run for this document.
- No new batch decode was run for this document. No Python pipeline was used. Pending gap: a per-`0x0b` stream/byte histogram.

## Unknowns

Each item is an open question with a proposed test. A "To settle" line is a proposal, not a measurement already performed.

1. A `zmt`-specific decode audit and per-type stream-count, padding and logical-sum histograms are unavailable. To settle (proposal): restrict the family chain walker to type `0000000b` and report stream-count, inter-stream padding and inflated-sum histograms against declared logical size, each with its slot-level denominator.
2. Whether the declared logical size for these slots includes the 16-byte prefix is not measured. To settle (proposal): on a stratified set of `zmt` slots, inflate the full uncapped chain and compare `sum(inflated)` with `logical` and with `logical − 16`; a zero-exception result against one form settles the question.
3. Which blob ids other than the localisation four are present in `zmt` resources is unenumerated at type scope. To settle (proposal): histogram every descriptor id over the 28,328 rows with type `0000000b` and publish per-id counts.
4. The `root+0x38` descriptor-count conflict between `drpz-localisation.md`:28-29 and `0drpz.md`:64, and the high 16 bits of `root+0x3C`, are unresolved. To settle (proposal): on fully inflated `zmt` roots compare `root+0x38` and the low u16 of `root+0x3C` against the number of parsed descriptor records in a stratified sample and report exceptions, without asserting either reading in advance.
5. The external key name behind blob `0x101` is not stored in the payload; its hash is not a hash of the stored text (`0drpz.md`:90). To settle (proposal): test a candidate key-name corpus against the hash records and report exact match counts; a hit settles it, no hit leaves it open.
6. Continuation pages that overrun a stream are dropped, not guessed (`drpz-localisation.md`:117). To settle (proposal): join consecutive page resources by descriptor continuity and report how many dropped strings are recovered with byte-exact continuation; no guessed offsets count.
7. The 12-byte descriptor label versus the 16-byte field total is retained, not resolved in favour of the prose. To settle (proposal): walk descriptor tables on fully inflated `zmt` roots and report the observed stride from successive record starts; the external prose label is not used as evidence.
8. Alignment for `0x0b` is unknown; the 16-byte prefix does not establish page or stream alignment. To settle (proposal): emit compressed-side stream-start offsets for all 28,328 `zmt` slots and report modulo-16 residuals; no alignment claim is made before that histogram exists.
9. No `zmt`-specific semantic decoder exists; the current `drpz.exe` family extractor does not supply one. To settle (proposal): document any type-scoped decoder entry point with a byte-verified field map and record stride for `0000000b`, or record a bounded clean negative; a generic family sweep is not sufficient.

## Changelog

- 2026-11-26, initial draft: stated that beyond-container decode is unavailable at `zmt` type scope; recorded 28,328 / 4,920,841,360 / 29,509,517,168 against the 1,255,039 all-row denominator with the seven-root split from the parent-verified census; verified no current `zmt` decoder and supplied inspection commands only.
- 2026-11-26, repair: set Grade C explicitly; corrected the invalid coverage-audit path alias to the actual workspace path `workspace: coverage_audit/out/tables.md`; removed the derived page-framing claim and left alignment unknown; converted the Fields and Container state tables to the required five-column evidence format with the per-row source in its own column; retained both source contradictions; cited the current `artifact: docs/coverage.md`:138 for status instead of the older snapshot's status column; and reattributed the external URL check as historical rather than asserting current verification. No competitor names, keys, assets or publication claims were added.
- 2026-11-26, decoder-proof correction: withdrew the earlier claim that `drpz.exe` and its source were absent. The binary is present at `workspace: drpz/target/release/drpz.exe`, the source at `workspace: drpz/src/main.rs`:871-924, and the parent's exit-0 `--help` output is saved at `artifact: docs_complete/evidence/drpz_help.txt`. It is a current generic `0DRPz` family extractor with `stats|redact|text` modes, not a `zmt` semantic decoder; no extraction was run here. All Unknowns items now carry a proposed, explicitly non-measured "To settle" test.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zmt.md`. No count was selected by modification time. Reconciliation decisions: rejected the measured-flags interpretation of the high u16 at root+0x3C; its meaning is unknown (`artifact: docs/formats/0drpz.md:112`).

