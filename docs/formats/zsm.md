# `zsm` (type code `0x58`)

Written 2026-11-26. Local sources only; no public URLs were consulted and no external claim is used as measurement. **Beyond-container decode is available only in a bounded form: the 16-byte prefix, the one- or two-stream zlib chain, the header fields through `+0x10c`, the bounding box in one header variant and the array descriptors are decoded; the elements behind the descriptors are not decoded, and there is no full-payload decoder or encoder.** The 16-zero prefix plus `78DA` observation is container framing, not a content decode. Semantic meaning of most fields is explicitly unknown. Sources: `artifact: docs/formats/zsm.md` (2026-11-24), `workspace: CONTEXT_HANDOFF.md` (2026-11-24), `workspace: coverage_audit/out/tables.md`, `artifact: type_census.csv` (per-slot dump), `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt` (parent-verified Rust census).


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The resource descriptor type word is `0x58`. The executable's variant-0 name is `zsm`; variant strings are `ism` and `#sm` (`artifact: docs/formats/zsm.md:1,7`; `CONTEXT_HANDOFF.md:170`).

- Structural identity, measured: a compact numeric record - a short header, a local bounding box in one header variant, and a set of arrays described by repeated `{pointer, 0, count, capacity}` descriptors (`zsm.md:9`).
- Semantic identity, unknown with a leading inferred hypothesis: an auxiliary per-object shape or simulation record belonging to a drawable-class asset. The reading is inferred from the asset class of the few matched names, local-scale coordinates and the array graph; the specific class is not established and the payload cannot be interpreted without the element layout (`zsm.md:10-12`). This is the weakest identification of the five types in that study and is reported as such; `zsm` is a tag, not a description (`zsm.md:12`).
- Executable-side, local-only evidence (not for the public copy): name-table entry at VA `0x14618daa0` points to `0x14677f9b4`, which begins the three strings `zsm`, `ism`, `#sm`; verified by direct read (`zsm.md:75`). The following string-pool entry begins `HAL::Drawable...` but is a pool neighbour, not a reference, and is a lead only (`zsm.md:76`). No RTTI, constructor or factory reference found; handler identity unknown (`zsm.md:77`).

No competitor project or external implementation is cited in this document.

## Counts

Per-root counts, measured, from `artifact: docs/formats/zsm.md:16-21`; every root row is reproduced by the parent-verified Rust census at `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt:64-66`:

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 39,947 | 659,442,176 | 1,530,627,024 |
| `pack/core_restofworld/core_restofworld.rpf` | 36 | 140,272 | 246,320 |
| `pack/shared_minigame000/shared_minigame000.rpf` | 36 | 139,152 | 625,984 |
| **Total** | **40,019** | **659,721,600** | **1,531,499,328** |

- Census denominator, parent-verified: **1,255,039** all census slot rows, split **1,153,560 Resource + 101,479 Binary**, malformed rows **0** (`artifact: docs_complete/evidence/seven_types_census.parent_verified.txt:20-27`). Binary rows are the null-word slots (`coverage_audit/out/tables.md:8`). `zsm` occupies 40,019 of all slot rows; the quantities in the table above are denominated within the `zsm` type population of 40,019, not across all slot rows. `artifact: type_census.csv` is a per-slot dump of 1,255,039 records, not an aggregate table.
- Census family for `zsm` is `Unknown`, magic `<null>`, kind `Resource` in all 40,019 rows; it is **not** a `0DRPz` wrapper (`seven_types_census.parent_verified.txt:84-90`). Of the seven target types in that report, only `zascd` (`0x6c`), `zldbmt` (`0x6f`) and `zmt` (`0x0b`) carry family `0DRPz` (`:91-111`).
- Units: **stored bytes** are on-disk compressed extents including the 16-byte prefix, inter-stream padding and trailing zero run; **logical bytes** are the sum of inflated stream lengths. For this type the prefix is excluded from `logical` and `logical == sum(inflated)` with no exceptions (`CONTEXT_HANDOFF.md:100`; `zsm.md:30-33`).
- Header generation 4 and root generation 4 in all 40,019 slots; every slot is a `Resource` entry (`zsm.md:23`).
- Name origin: 40,008 unresolved hashes (659,590,576 stored / 1,531,177,280 logical) and 11 dictionary matches (131,024 / 322,048). Eleven distinct matched names, one slot each; not reproduced. All 11 resolve to drawable-class assets (apparel, a weapon attachment, a prop, a vehicle-side record) (`zsm.md:24`).
- Logical size, measured: min 112 B, p25 8,704, median 23,584, p75 41,552, p90 131,568, p99 204,880, max 1,245,824 B; mean 38,269 B (`zsm.md:25`).
- The population is bimodal in stream count, correlating with size: one-stream slots run 112 B to a few KiB; two-stream slots carry the bulk above that (`zsm.md:26`).

## Container

Measured on all 40,019 slots (`artifact: docs/formats/zsm.md:28-39`):

- 16 zero bytes at stored offset 0 and `0x78DA` at stored `+0x10`: 40,019 of 40,019.
- `logical == sum(inflated stream lengths)`: 40,019 of 40,019, no exceptions. Zero unterminated streams.
- Stream count: one stream in 18,888 slots, two in 21,131, none with three; 61,150 streams total. All stream starts are 16-byte aligned.
- Of 21,131 stream-to-stream boundaries, 1,363 carry no padding and 19,768 carry 1-15 bytes to the next 16-byte boundary. Padding is not part of `logical`.
- 37,542 slots have a zero run between the last stream and the stored-range end.
- In the largest reported two-stream sample, the first stream inflates to 640 bytes and the second to 1,245,184 bytes. The first carries the header; both streams are needed for the full payload (`artifact: docs/formats/zsm.md:39`).

## Fields

Offsets are relative to the first inflated byte. Values are population histograms from the first inflated stream of all 40,019 slots, plus a full-payload field scan of 40,000 slots with at least `0x110` first-stream bytes (`zsm.md:41-43`). Column labels are offsets unless a meaning is sourced. Observations are separated from semantic inference inside the Meaning column; a row with an inferred role is marked `inferred` even when its numeric observation is measured. Confidence vocabulary is exactly `measured`, `inferred`, `external`, `unknown`. Variant qualifiers are stated in Meaning, not in Confidence.

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00` | u64 | zero in 40,019/40,019 | measured |
| `+0x08` | u32 | relative pointer `0x50000000 + offset`, in range 39,217/40,000 scanned; 2,403 distinct targets, most common 0x140 (5,530), 0x1d0 (2,392), 0x200 (2,390) | measured |
| `+0x0c` | u32 | zero in all | measured |
| `+0x10` | u32 | zero in 38,432 slots; nonzero values mostly pointer-shaped; read as header-variant discriminator (inferred) | inferred |
| `+0x18` | u32 | 311 distinct; `0x00020000` 8,402, `0x00030000` 7,280, `0x00038000` 5,630 | unknown |
| `+0x1c` | u32 | `0x7d8f3db3` in 26,662, zero in 13,198 | measured |
| `+0x20` | u32 | 251 distinct; `0x7fffffbf` 6,841, `0x005f9000` 4,898, `0x00090340` 4,854 | unknown |
| `+0x24` | u32 | small integers: 6 (3,579), 20 (3,389), 22 (3,314), 4 (2,761) | unknown |
| `+0x30`, `+0x34`, `+0x38` | 3 x f32 | min corner of a bounding box in the 8,741-slot variant carrying bbox initialisers; `min <= max` on all three axes in 8,741/8,741 (variant-local) | measured |
| `+0x40`, `+0x44`, `+0x48` | 3 x f32 | max corner of the same box in that variant | measured |
| `+0x50`-`+0x5c` | 4 x f32 | exactly `0x7f7fffff` (+FLT_MAX) in the same 8,741 slots | measured |
| `+0x60`-`+0x6c` | 4 x f32 | exactly `0xff7fffff` (-FLT_MAX) in the same 8,741 slots | measured |
| `+0x70` | u32 | relative pointer in 23,641/40,000; most common target 0x140 | measured |
| `+0x90`/`+0x94` | u32 | zero in 40,003/40,005 | measured |
| `+0x98`/`+0x9c` | 2 x u32 | count/capacity pair, equal in every observed slot: (0,0) 19,579, (1,1) 3,964, (9,9) 871, (22,22) 746, (20,20) 695 | measured |
| `+0xa0`, `+0xb0` | u32 | relative pointers in 20,046/40,005 | measured |
| `+0xa8`/`+0xac` | 2 x u32 | second count pair; `+0xa8` = 1 in 18,972, `+0xac` = 1 in 19,048 | measured |
| `+0xb8`-`+0xcc` | 6 x u32 | hash-like 64-bit words; none matched any name hash (6 searches, 0 hits); "hash" reading inferred | inferred |
| `+0xd8` | u32 | zero in 40,005/40,005 | measured |
| `+0xe4` | u32 | `0x00030000` in 20,046/40,005 | measured |
| `+0xec`, `+0xf0`, `+0xf4` | 3 x f32 | 1e-6 in 13,575, 1e6 in 13,575, 1.0 in 13,579; quantisation/epsilon reading inferred | inferred |

Array descriptors are a repeated 16-byte `{u32 relative pointer, u32 zero, u32 count, u32 capacity}` with `count == capacity` in every observed case; one sample exposes seven of them. The elements behind the pointers are not decoded, so their meaning is unknown (`zsm.md:69`).

The bounding-box reading is variant-local, not population-wide: unconditioned, `min <= max` holds on only 36,299/40,000 slots on the first axis and 20,093 on the second, because other header variants reuse `+0x30` and `+0x40` for pointers. Conditioned on the 8,741 slots carrying the +FLT_MAX/-FLT_MAX initialiser pair, the box is exact on all three axes (`zsm.md:71`, `zsm.md:98`). The smallest slot, 112 logical bytes, is accounted for byte for byte (zero words, one relative pointer at `+0x08` to `+0x50`, one counted field, one value at `+0x58`); the semantics of `+0x18`, `+0x1c`, `+0x20` remain unknown even there (`zsm.md:85`).

## Decode status

**Source chronology discrepancy, stated explicitly.** `CONTEXT_HANDOFF.md:170` (written 2026-11-24) and the per-type note `artifact: docs/formats/zsm.md:87` (2026-11-24) both list `zsm` as **Partial**: header, descriptors and one bounding-box variant decoded. `workspace: coverage_audit/out/tables.md:13` lists the same type as **Classified** with note "Name and count verified; no payload decoder." That audit row also labels `zscript` "none published" and `zbn` "Classified", contrary to the handoff (`CONTEXT_HANDOFF.md:144-152`), so it is treated as the older/stale aggregate snapshot. The reconciliation uses the newest per-type note plus the handoff coverage table; the audit row is retained here only as a documented conflict, not as the decode verdict.

Precise bounded capability (`zsm.md:79-87`): container verified on 40,019/40,019 including the exact logical rule; header fields through `+0x10c` with the bounding box fully explained in the 8,741-slot variant and the array descriptors decoded but not their elements; the 112-byte slot accounted for byte for byte. Explanation stops at the first pointed-to array, at a variable offset (0x50 in the 112-byte slot, 0x140-0x250 in a 16 KiB slot). This is header plus descriptors, not a semantic payload decode. The 16-zero prefix plus `78DA` is wrapper observation only and is not a full decode. No encoder; write status W0 (`zsm.md:89-91`). Handler identity unknown (`zsm.md:77`). A caveat kept honest: 8,321/40,019 slots contain a printable run of 32 bytes or more, so "no strings anywhere" is not proven (`zsm.md:102`).

## Verification

- Whole-census reconciliation in Rust, as recorded in the 2026-11-24 per-type note, reproduces 40,019 / 659,721,600 / 1,531,499,328 exactly (`zsm.md:95`).
- Population chain walk, Rust, for this type: prefix and `0x78DA` 40,019/40,019; `sum(inflated) == logical` 40,019/40,019; 0 unterminated streams; stream histogram 1 -> 18,888, 2 -> 21,131 (`zsm.md:96`).
- Independent population verifier, Rust: re-inflates every slot and asserts prefix, `0x78DA`, `u64@0 == 0` and `+0x08` pointer range - 40,019/40,019 on each (`zsm.md:97`).
- Bounding-box test: +FLT_MAX group 8,741 slots; -FLT_MAX group 8,741; same slots; `min <= max` on all axes 8,741/8,741 within the group (`zsm.md:98`).
- Stratified samples: 112 B, 656 B, 8,704 B, 16,416 B, 23,584 B, 41,552 B, 1,245,824 B; all inflated to exactly `logical` (`zsm.md:99`). A prepared sample was truncated by a tool cap and a wrong stored size; both artefacts identified and conclusions rest on complete slots only (`zsm.md:100`). Hypotheses rejected at `zsm.md:101`.
- **Census cross-check, parent-verified.** `artifact: type_census.csv` is a per-slot dump of 1,255,039 records, not an aggregate table. The common Rust verifier was run by the parent; its current evidence is `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt`. Reproduction command, from the evidence directory: `.\seven_types_census.exe artifact: type_census.csv artifact: docs_complete/evidence/seven_types_census.parent_verified.txt`. The report gives denominator 1,255,039 with malformed rows 0 and kind split 1,153,560 Resource + 101,479 Binary (`:20-27`), combined seven-target totals 235,446 slots / 18,437,133,488 stored / 69,980,587,296 logical (`:29-37`), and for `0x58` exactly 40,019 / 659,721,600 / 1,531,499,328 with zero unparsable and zero zero-valued rows (`:41`). All per-root rows in the Counts table reproduce the `PER_TARGET_ROOT` rows at `:64-66`. All totals match the 2026-11-24 per-type note; no cross-check remains open.
- **Decoder-current-capability command: none exists.** The current CLI exposes no zsm decoder. Evidence inspection commands, not decode commands:

```powershell
& 'workspace: sentinel-rpf9-core/target/release/srpf9.exe' --help
Get-ChildItem 'workspace: sentinel-rpf9-core/src/bin' -Filter *.rs | Select-Object -ExpandProperty Name
Get-ChildItem 'workspace: sentinel-rpf9-core/target/release' -Filter *.exe | Select-Object -ExpandProperty Name
```

  `srpf9.exe --help` returns only `info, scan, toc, carve, mhiu, tpfd, model, material, psin, awc, bench`; there is no zdd/zsm command. No zdd/zsm source file appears in `src/bin/` and no zdd/zsm executable appears in `target/release/`. No historical zsm probe binary is present in the current tree. No fake decode command is supplied.
- **Restore/build requirement, two distinct things.** (a) Engine-label extractor: `cargo build --release --offline --features private-exe-toc --bin srpf9` rebuilds only the `srpf9` CLI (`info, scan, toc, carve, mhiu, tpfd, model, material, psin, awc, bench`); it does **not** build any per-type probe and does not restore a zsm decoder (`CONTEXT_HANDOFF.md:315-318`; `srpf9.exe --help`). (b) Per-type probe: reproducing the historical population chain walk and independent verifier requires restoring each probe source into `sentinel-rpf9-core/src/bin/` and building that specific target with `cargo build --release --offline --bin <probe_name>`. `zsm.md:95-97` names no probe binary, and no matching source file exists in `src/bin/`, so the exact source and Cargo target remain **unknown**. No restored probe or rebuilt zsm decoder exists at writing time. The data input is `workspace: game_scarlett_master.exe`, read as data and never executed (`zsm.md:3`).
- Local path note: `artifact: _bucket2_probe/` was inspected as an assigned input. It contains terrain-blend / placement control-block work (`0x50000000..0x58000000` is its VIRT pointer range, not a type word) and holds **no zdd or zsm decode evidence**. Its `0x58` matches are address constants and scale offsets, not the `0x58` resource type word.
- No public/external source was used.

## Unknowns

1. Element layout behind the array descriptors (`zsm.md:106`). **To settle:** dump the pointed-to region for a 112-byte slot and a 16 KiB slot and match `count × element size` against the pointer span (`zsm.md:106`).
2. Meaning of `+0x18`, `+0x1c`, `+0x20` and the `+0xd0`/`+0xe4`/`+0xf0` constants (`zsm.md:107`). **To settle:** extend the 40,000-slot full-payload field scan (`zsm.md:43`) to cross-tabulate each constant against the descriptor pairs and the bbox variant; a one-to-one relation would identify the field.
3. Whether the hash-like words at `+0xb8` are name hashes from a table not present locally (`zsm.md:108`). **To settle:** search a fuller name-hash registry beyond the local index; the six local searches returned 0 hits (`zsm.md:64`).
4. The printable region in 8,321 of 40,019 slots (`zsm.md:102,109`). **To settle:** dump and classify those printable runs as names, text blobs or binary noise by whole-payload run counting (`zsm.md:102`).
5. Any handler, vtable or RTTI name for the type (`zsm.md:110`). **To settle:** xref search around name-table VA `0x14618daa0` and the string-pool entry for the three variant strings; the completed search found none (`zsm.md:75-77`), so a runtime trace would be required for more.
6. Semantic identification beyond the inferred "drawable-class auxiliary record" hypothesis (`zsm.md:10`). **To settle:** decode the array elements (item 1) and match the local-scale vectors against a known drawable-class record.

## Changelog

- 2026-11-26: document created. Reconciled the stale `coverage_audit/out/tables.md` Classified row against the 2026-11-24 per-type note and handoff Partial verdict. Corrected confidence labels to the exact vocabulary `measured`/`inferred`/`external`/`unknown`, separating observations from inferred roles and keeping variant qualifiers out of the Confidence column. Removed rounded percentages and timings; only exact counts, exact ratios and integers are given. Reclassified `type_census.csv` as a per-slot dump of 1,255,039 records; replaced the local scanning count with the parent-verified common Rust census evidence at `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt` (denominator 1,255,039 = 1,153,560 Resource + 101,479 Binary, malformed 0; combined seven-target totals 235,446 / 18,437,133,488 / 69,980,587,296); removed the earlier gap notes. Recorded that `zsm` is census family `Unknown` with `<null>` magic, not `0DRPz`. Distinguished the `srpf9` engine-label rebuild from per-type probe restore, whose exact source and Cargo target remain unknown. Paired every Unknowns item with a settling test and replaced the rounded printable-run share with the exact ratio 8,321 of 40,019. Noted `_bucket2_probe` holds no zdd/zsm evidence. No public/URL sources; no invented semantics.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zsm.md`. No count was selected by modification time.

