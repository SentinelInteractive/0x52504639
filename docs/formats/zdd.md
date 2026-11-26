# `zdd` (type code `0x04`)

Written 2026-11-26. Local sources only; no public URLs were consulted and no external claim is used as measurement. **Beyond-container decode is available only in a bounded form: the 16-byte prefix, the zlib chain, the 0x40-byte root header and the name region are decoded; the payload behind the `+0x30` pointer array is not decoded, and there is no full-object decoder or encoder.** The 16-zero prefix plus `78DA` observation is container framing, not a content decode. Sources: `artifact: docs/formats/zdd.md` (2026-11-24), `workspace: CONTEXT_HANDOFF.md` (2026-11-24), `workspace: coverage_audit/out/tables.md`, `artifact: type_census.csv` (per-slot dump), `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt` (parent-verified Rust census).


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The resource descriptor type word is `0x04`. The executable's variant-0 name for that index is `zdd`; variant strings are `idd` and `#dd` (`artifact: docs/formats/zdd.md:1,7`; `CONTEXT_HANDOFF.md:169`).

- Structural identity, measured: a small fixed root header, a name region, a hash/object region and a pointer array, followed by a payload. Entries carry a lower-snake-case identifier ending in a dot plus a two-character type tag (`zdd.md:9-10`).
- Semantic identity, inferred: a container for named sub-resources; the two-character tag is the same tag the executable uses for a resource type. The object layout behind the pointer array is not decoded, so material identity is unproven (`zdd.md:10-12`). The word "dictionary" is consistent with the measured structure but no class name is claimed (`zdd.md:12`).
- Executable-side, local-only evidence (not for the public copy): name-table VA `0x1462fcd50` (variant 0) points to the string `zdd` at `0x146784b8c`; variant-1 table `0x1462fcde8` points to `idd` at `0x146784b90`; exactly one pointer to the `zdd` string exists in the image (`zdd.md:85-86`). No `.?AVzdd` RTTI, constructor or factory xref was located; handler identity is unknown (`zdd.md:87-88`).

No competitor project or external implementation is cited in this document.

## Counts

Per-root counts, measured, from `artifact: docs/formats/zdd.md:16-25`; every root row is reproduced by the parent-verified Rust census at `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt:49-55`:

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 24,423 | 2,683,898,560 | 5,874,261,856 |
| `levels.rpf` | 22,379 | 3,444,182,880 | 8,405,092,080 |
| `pack/story000/story000.rpf` | 890 | 152,789,600 | 233,949,472 |
| `pack/core_restofworld/core_restofworld.rpf` | 796 | 20,692,976 | 46,425,216 |
| `pack/shared_minigame000/shared_minigame000.rpf` | 81 | 6,435,856 | 14,019,056 |
| `data.rpf` | 14 | 1,496,032 | 3,242,432 |
| `pack/story000_restofworld/story000_restofworld.rpf` | 1 | 46,560 | 67,088 |
| **Total** | **48,584** | **6,309,542,464** | **14,577,057,200** |

- Census denominator, parent-verified: **1,255,039** all census slot rows, split **1,153,560 Resource + 101,479 Binary**, malformed rows **0** (`artifact: docs_complete/evidence/seven_types_census.parent_verified.txt:20-27`). Binary rows are the null-word slots (`coverage_audit/out/tables.md:8`). `zdd` occupies 48,584 of all slot rows; the quantities in the table above are denominated within the `zdd` type population of 48,584, not across all slot rows. `artifact: type_census.csv` is a per-slot dump of 1,255,039 records, not an aggregate table.
- Census family for `zdd` is `Unknown`, magic `<null>`, kind `Resource` in all 48,584 rows; it is **not** a `0DRPz` wrapper (`seven_types_census.parent_verified.txt:77-83`). Of the seven target types in that report, only `zascd` (`0x6c`), `zldbmt` (`0x6f`) and `zmt` (`0x0b`) carry family `0DRPz` (`:91-111`).
- Units: **stored bytes** are on-disk compressed extents including the 16-byte prefix, inter-stream padding and trailing zero run; **logical bytes** are the sum of inflated stream lengths, with the 16-byte prefix excluded for this type (`CONTEXT_HANDOFF.md:100`; `zdd.md:34,42`). `stored = 16 + sum(compressed extents) + sum(padding) + trailing` (`zdd.md:42`).
- Header generations are not uniform: generation 4 in 23,788 slots, 5 in 19,185, 8 in 5,611; root generation 4 in all 48,584; every slot is a `Resource` entry (`zdd.md:27`).
- Name origin: 41,520 unresolved hashes (5,541,043,136 stored / 12,882,950,704 logical) and 7,064 dictionary matches (768,499,328 / 1,694,106,496) (`zdd.md:28`).
- Logical size, measured: min 1,808 B, p25 32,640, median 65,120, p75 264,944, p90 652,624, p99 4,342,352, max 30,143,664 B; mean 300,036 B. Two slots exceed 16 MiB, nine exceed 8 MiB (`zdd.md:29-30`).

## Container

Measured on all 48,584 slots (`artifact: docs/formats/zdd.md:32-42`):

- 16 zero bytes at stored offset 0 and `0x78DA` at stored `+0x10`: 48,584 of 48,584. No other CMF/FLG pair observed.
- Chain of up to six zlib streams. `logical == sum(inflated stream lengths)` in 48,582 of 48,584; stream histogram 2 -> 33,222, 3 -> 13,887, 4 -> 1,464, 5 -> 9, 6 -> 2; 114,018 streams total. Zero unaligned stream starts.
- Inter-stream padding 0 to 15 bytes to the next 16-byte boundary. Of 65,434 boundaries, 3,942 have no padding and 61,492 carry 1-15 bytes. Padding is not part of `logical`.
- 45,361 slots end with a zero run between the last stream and the stored-range end.
- Two exceptions are short by exactly 48 bytes each (4,109,392 declared vs 4,109,344 inflated; 362,304 vs 362,256), both generation 8, both ending with a clean `StreamEnd` and a short non-zlib tail. Cause not established.
- Not a nested archive in general: literal scan of inflated payloads found `0DRPz` in 0 slots, `RPF9` in 2, the 8-byte inner schema pair in 0 (`zdd.md:109`). The two `RPF9` hits are special cases, not representative.

## Fields

Offsets are relative to the first inflated byte of the slot. Column labels are offsets unless a meaning is sourced. Observations are separated from semantic inference inside the Meaning column; a row with an inferred role is marked `inferred` even when its numeric observation is measured. Confidence vocabulary is exactly `measured`, `inferred`, `external`, `unknown`. Root header verified on all 48,584 slots; table targets on full chains of the stratified sample (`zdd.md:46`).

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00` | u64 | zero in 48,584/48,584 | measured |
| `+0x08` | u32 | relative pointer `0x50000000 + offset`, in range 48,584/48,584; target begins the name region (role inferred) | inferred |
| `+0x0c` | u32 | zero in all | measured |
| `+0x10` | u64 | zero in all | measured |
| `+0x18` | u64 | 1 in 48,584/48,584 | measured |
| `+0x20` | u32 | relative pointer, in range 48,584/48,584; target begins with 64-bit values and floats (role inferred) | inferred |
| `+0x28` | u32 | two equal u16 halves in 48,584/48,584; 108 distinct values (`0x0001/0x0001` 29,141; `0x0004/0x0004` 12,876; `0x0002/0x0002` 1,986; `0x0010/0x0010` 898; `0x0003/0x0003` 650); read as count/capacity (inferred) | inferred |
| `+0x2c` | u32 | zero in all | measured |
| `+0x30` | u32 | relative pointer, in range 48,584/48,584; target is an array of relative pointers | measured |
| `+0x34` | u32 | zero in all | measured |
| `+0x38` | u32 | identical to `+0x28` in 48,584/48,584 | measured |
| `+0x3c` | u32 | zero in all | measured |
| `+0x40` | variable | payload start; no stable field schema found | unknown |

Name region, from the `+0x08` target (`zdd.md:64-69`): `+0x00` u64 zero, then a pair of equal u16 halves at `+0x08` and zeros to `+0x20`; one to four inline NUL-terminated strings, 19-30 printable characters, lower snake case with digits and a final dot plus a two-character tag. In the sample with eight entries the strings are replaced by an array of relative pointers, so names can be indirect. The two-character tag matches the executable's variant-2 label for the drawable type in the sample inspected. 48,576 of 48,584 slots contain a printable run of eight or more characters; 28,133 contain a run of 32 or more.

Object side, from the `+0x30` target (`zdd.md:71,75-81`): array of u64 relative pointers with high word zero. Pointer count does not equal the header pair in samples tested (4 pointers for count 1 or 4, 3 for count 3, 16 for count 8); population relationship not established. One independently rechecked 3,472-byte inflated sample follows `+0x30` to `0xa90` and four pointer-shaped qwords to `0x4a0`, `0x8c0`, `0x900`, `0x790`; a second target at `0x8c0` has pointer-shaped qwords at object-relative `+0x08`, `+0x10`, `+0x20` and zeros at `+0x18`, `+0x28`, `+0x30`. At the `+0x20` target, four pairs of u32 words have second words 4, 8, 12, 16; first words and pair semantics unknown. This is a partial prefix in one sample, not a decoder. An earlier reading of paired u32s near `+0x40` as a hash/offset table was rejected: of 32,945 slots with at least two such pairs, only 202 show a monotone second word and 62,423 distinct first words appear.

## Decode status

**Source chronology discrepancy, stated explicitly.** `CONTEXT_HANDOFF.md:169` (written 2026-11-24) and the per-type note `artifact: docs/formats/zdd.md:98` (2026-11-24) both list `zdd` as **Partial**: header, name region and pointer tables decoded, wrapped objects undecoded. `workspace: coverage_audit/out/tables.md:12` lists the same type as **Classified** with note "Dictionary container; one member was located in a control, but no dictionary decoder exists." That audit row also labels `zscript` "none published" and `zbn` "Classified", contrary to the handoff (`CONTEXT_HANDOFF.md:144-152`), so it is treated as the older/stale aggregate snapshot. The reconciliation uses the newest per-type note plus the handoff coverage table; the audit row is retained here only as a documented conflict, not as the decode verdict.

Precise bounded capability (`zdd.md:90-98`): verified on 48,584 of 48,584 slots are the container (prefix, zlib header, chain, alignment, padding rule, exact logical size except two 48-byte shortfalls), the `0x40`-byte root header field by field including three in-range relative pointers and matched u16 pairs, and the name region on nine fully inflated stratified samples. Explanation stops at byte `0x40`, the payload start, and at the object layout behind the `+0x30` pointer array. The 16-zero prefix plus `78DA` is wrapper observation only and is not a full decode. No encoder; write status W0 (`zdd.md:100-102`). Handler identity unknown (`zdd.md:88`).

## Verification

- Whole-census reconciliation in Rust, as recorded in the 2026-11-24 per-type note: 1,255,039 rows; per-type totals reproduce 48,584 / 6,309,542,464 / 14,577,057,200 (`zdd.md:106`).
- Population chain walk, Rust, all 48,584 slots: `sum(inflated) == logical` on 48,582; stream histogram as above; 114,018 streams; 0 unaligned stream starts; 45,361 zero-tail slots (`zdd.md:107`).
- Population verifier, Rust, for this type: prefix, `0x78DA`, `u64@0 == 0`, `+0x08` pointer in range - 48,584/48,584 on every assertion (`zdd.md:108`).
- Literal scan and stratified samples as listed in `zdd.md:109-110`; hypotheses rejected at `zdd.md:111`.
- **Census cross-check, parent-verified.** `artifact: type_census.csv` is a per-slot dump of 1,255,039 records, not an aggregate table. The common Rust verifier was run by the parent; its current evidence is `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt`. Reproduction command, from the evidence directory: `.\seven_types_census.exe artifact: type_census.csv artifact: docs_complete/evidence/seven_types_census.parent_verified.txt`. The report gives denominator 1,255,039 with malformed rows 0 and kind split 1,153,560 Resource + 101,479 Binary (`:20-27`), combined seven-target totals 235,446 slots / 18,437,133,488 stored / 69,980,587,296 logical (`:29-37`), and for `0x04` exactly 48,584 / 6,309,542,464 / 14,577,057,200 with zero unparsable and zero zero-valued rows (`:40`). All per-root rows in the Counts table reproduce the `PER_TARGET_ROOT` rows at `:49-55`. All totals match the 2026-11-24 per-type note; no cross-check remains open.
- **Decoder-current-capability command: none exists.** The current CLI exposes no zdd decoder. Evidence inspection commands, not decode commands:

```powershell
& 'workspace: sentinel-rpf9-core/target/release/srpf9.exe' --help
Get-ChildItem 'workspace: sentinel-rpf9-core/src/bin' -Filter *.rs | Select-Object -ExpandProperty Name
Get-ChildItem 'workspace: sentinel-rpf9-core/target/release' -Filter *.exe | Select-Object -ExpandProperty Name
```

  `srpf9.exe --help` returns only `info, scan, toc, carve, mhiu, tpfd, model, material, psin, awc, bench`; there is no zdd/zsm command. No zdd/zsm source file appears in `src/bin/` and no zdd/zsm executable appears in `target/release/`. The historical probe `zdd_objprobe` on `strat_data.bin` is mentioned at `zdd.md:79` but is not present in the current tree and cannot be re-run or verified. No fake decode command is supplied.
- **Restore/build requirement, two distinct things.** (a) Engine-label extractor: `cargo build --release --offline --features private-exe-toc --bin srpf9` rebuilds only the `srpf9` CLI (`info, scan, toc, carve, mhiu, tpfd, model, material, psin, awc, bench`); it does **not** build any per-type probe and does not restore a zdd decoder (`CONTEXT_HANDOFF.md:315-318`; `srpf9.exe --help`). (b) Per-type probe: reproducing the historical `zdd_objprobe` run requires restoring its source into `sentinel-rpf9-core/src/bin/` and building that specific target, e.g. `cargo build --release --offline --bin <probe_name>` with the actual probe name. The note names the probe `zdd_objprobe` (`zdd.md:79`), but no matching source file exists in `src/bin/`, so the exact source and Cargo target remain **unknown**. No restored probe or rebuilt zdd decoder exists at writing time. The data input is `workspace: game_scarlett_master.exe`, read as data and never executed (`zdd.md:3`).
- No public/external source was used.

## Unknowns

1. Layout of the objects behind the `+0x30` pointer array; does the two-character tag identify their type (`zdd.md:115`)? **To settle:** follow one `+0x30` pointer in a small slot and compare the target header with the known drawable and bound headers (`zdd.md:115`).
2. Rule setting the pointer count (`zdd.md:116`). **To settle:** population histogram of pointer count against the header pair, a small addition to the existing scanner (`zdd.md:116`).
3. The 48-byte shortfall in the two generation-8 exceptions (`zdd.md:40,117`). **To settle:** locate those two slots, compare declared logical size with inflated length, and inspect the trailing non-zlib bytes after `StreamEnd` (`zdd.md:40`).
4. Exact proportion of slots with a structurally valid name table, as opposed to printable bytes somewhere (`zdd.md:118`). **To settle:** validate all 48,584 inflated name regions for u64 zero at `+0x00`, equal-u16 pair at `+0x08`, zeros to `+0x20`, then a NUL-terminated tagged string (`zdd.md:64-69`).
5. Any handler or vtable on the executable side (`zdd.md:119`). **To settle:** the static xref search is a closed negative (`zdd.md:85-88`; `CONTEXT_HANDOFF.md:282`); only a runtime consumer trace or a new static entry point could decide it.
6. Semantics of the `+0x28`/`+0x38` equal-u16 pair beyond the inferred count/capacity reading (`zdd.md:56`). **To settle:** cross-tabulate the pair value against resolved object-pointer count across the stratified samples; a one-to-one relation would confirm the reading (`zdd.md:56,71,75`).

## Changelog

- 2026-11-26: document created. Reconciled the stale `coverage_audit/out/tables.md` Classified row against the 2026-11-24 per-type note and handoff Partial verdict. Corrected confidence labels to the exact vocabulary `measured`/`inferred`/`external`/`unknown`, separating observations from inferred roles. Removed rounded percentages and timings; only exact counts, exact ratios and integers are given. Reclassified `type_census.csv` as a per-slot dump of 1,255,039 records. Replaced the local scanning count with the parent-verified common Rust census evidence at `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt` (denominator 1,255,039 = 1,153,560 Resource + 101,479 Binary, malformed 0; combined seven-target totals 235,446 / 18,437,133,488 / 69,980,587,296); removed the earlier gap notes and all timings. Recorded that `zdd` is census family `Unknown` with `<null>` magic, not `0DRPz`. Distinguished the `srpf9` engine-label rebuild from per-type probe restore, whose exact source and Cargo target remain unknown. Paired every Unknowns item with a settling test. No public/URL sources; no invented semantics.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zdd.md`. No count was selected by modification time.

