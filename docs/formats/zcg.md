# `zcg` resources (type code `0x5f`)

Compiled 2026-11-26 from local artifacts. Decode scope: the shared zlib container plus the header/pointer structure measured below; payload element semantics are not decoded. This is not a container-only result. Grade **Partial**, scoped to that structure and not to semantics. Write status **W0**: no writer, no encoder, no pack-back and no game-load test in any source. Sources: `artifact: docs/formats/zcg.md`; `workspace: coverage_audit/out/tables.md` (counts derived from `artifact: type_census.csv`); `workspace: CONTEXT_HANDOFF.md`. All population scans were Rust release binaries, offline; the executable was read as a PE file and never executed.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x5f`. It resolves to the label `zcg` through the executable callback type-name table by string xref, not by a file extension (PE read as data; `artifact: docs/formats/zcg.md`, Exe path table; full VAs are withheld from this compiled copy). The word is registered with store class `ComputeGraphStore` at the shared store-register call site (same source, Exe path table). The registration is a measured PE-read claim; the semantic reading "compute graph" is **inferred** from the class name, since no node, edge, constant or dispatch was decoded (`artifact: docs/formats/zcg.md`, Identity).

Structural identity, **measured** on the whole population by `tail1` and the Python one-shot re-derivation recorded in `artifact: docs/formats/zcg.md` (Verification): one zlib stream behind the 16-zero prefix with `logical == sum(inflated)` in 518 of 518 slots; two self-relative words resolving to the payload end at `+0x08` and the `+0x10`/`+0x14` pair; and an 8-byte identifier at `+0x48` equal to the `zcgc` (`0x72`) twin's `+0x20` for the same 64-bit name hash in 518 of 518 pairs. The pairing is name/identifier equality, not a numeric reference: no `zcgc` size, offset or hash occurs in a `zcg` payload (0 of 518). The reader for the store was not located.

## Counts

Exact counts from `workspace: coverage_audit/out/tables.md` (`0x5f` row; derived census `artifact: type_census.csv`): **518 slots, 685,024 stored bytes, 5,228,768 logical bytes**. These agree across the census, the verified type-word join and the slot index (`type_probe inventory/join`; `artifact: docs/formats/zcg.md`, Verification).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 518 | 685,024 | 5,228,768 |
| **Total** | **518** | **685,024** | **5,228,768** |

Distribution facts from `artifact: docs/formats/zcg.md` (Counts; `tail1` passes): every slot is a resource entry, generation 4 at root and containing header; 2 archive headers carry 421 and 97 slots; 18 dictionary matches and 500 unresolved hashes, all 518 name hashes distinct; stored 96/1,536/1,568/1,584/1,616/5,424 (min/p25/median/p75/p95/max), logical 160/12,160/12,160/12,160/12,160/51,136. Logical size takes ten values, 12,160 in 419 slots.

## Container

Verified on 518 of 518 slots by `type_probe walk out\zcg_slots.tsv <archive-root> out\zcg_walk.txt` (518 slots, 0.07 s; 7,931 slots/s, 10.5 stored MB/s, 80.1 logical MB/s; `artifact: docs/formats/zcg.md`, Verification). Stored `+0x00..+0x0F` are sixteen zero bytes in 518 of 518 and `78 da` sits at `+0x10` in 518 of 518. One stream in all 518 slots, gap 0, no second stream. `logical == sum(inflated)` in 518 of 518; the `+16` convention never occurs; zero inflate errors; exception list empty.

## Fields

Offsets relative to the inflated payload, little-endian. Source for every row: `artifact: docs/formats/zcg.md` (Fields table), produced by the `tail1` `fields` pass over 518 slots and re-derived by a Python one-shot (Verification). Confidence vocabulary is limited to measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence |
|---|---:|---|---|
| `+0x00`, `+0x04`, `+0x0c`, `+0x1c..+0x44` | 4 | Zero in 518 of 518 (`tail1` fields; zcg.md Fields) | measured |
| `+0x08` | 4 | `0x50000000 + (logical - 32)`; target is the payload end less 32 bytes, 518 of 518 (`tail1` fields; Python one-shot) | measured |
| `+0x10` | 4 | `0x50000000 + (logical - d)`, d = 132 in 496, 128 in 16, 140 in 6 (`tail1` fields) | measured |
| `+0x14` | 4 | Equals `+0x10` in 518 of 518; duplicate word (`tail1` fields; Python one-shot) | measured |
| `+0x18` | 4 | Constant `0x50000060` in 518 of 518 (`tail1` fields) | measured |
| `+0x48` | 8 | Identifier-shaped 8-byte value, 465 distinct; equals `zcgc +0x20` for the same name hash in 518 of 518 pairs (`tail1` `ids`/`pairid`; Python one-shot). Meaning unknown | unknown |
| `+0x60` | 4 | Varies over 518 slots; meaning unknown (zcg.md Fields) | unknown |

No field name beyond an offset is asserted for cells without a measured role. Float metrics are reported in `artifact: docs/formats/zcg.md` (Decode), not recomputed here: 1,307,192 32-bit words, 56.65 percent exact zero and 99.88 percent parse as `|f| <= 1`. They are not a record layout. There is no count field and no stride sizing the payload; the ten-valued logical histogram is consistent with a fixed record set but the boundary is not established.

## Decode status

**Partial, scoped to actual structure.** Decoded and verified: the container on 518 of 518 slots; the two end-relative words `+0x08` and `+0x10`/`+0x14`; the duplicated pair and the `+0x18` constant; the identifier equality with `zcgc`. Not decoded: the record body, element semantics, the meaning of `+0x48` and `+0x60`, the three `+0x10` deltas, what `+0x08` addresses, and the store reader (`artifact: docs/formats/zcg.md`, Decode and Unknowns). The semantic "compute graph" label stays inferred. Write status W0; no source proves a writer.

## Verification

All verification steps are listed in `artifact: docs/formats/zcg.md` (Verification): `type_probe inventory artifact: type_census.csv 0000005f out zcg_slots.tsv` (1,255,039 rows in 0.14 s, 518 selected); `type_probe walk out\zcg_slots.tsv <archive-root> out\zcg_walk.txt` (numbers above); `type_probe join` over all 1,255,039 rows in about 2.2 s; `tail1` `hdr`, `fields`, `stride`, `ids`, `pair`, `pairid` passes over 518 slots; and a Python one-shot re-derivation (`+0x08 == logical - 32` in 518/518, `+0x10 == +0x14` with 132/128/140 in 496/16/6, the ten-class histogram, and the paired-identifier equality in 518/518). Counts cross-checked against `workspace: coverage_audit/out/tables.md`. Python was used only as a one-shot probe; the executable was never executed.

## Unknowns

Source for every bullet in this section: `artifact: docs/formats/zcg.md` (Unknowns and Decode).

- The record body: no count, stride or per-record boundary was found.
- The meaning of the `+0x48` identifier and why it is shared with `0x72`.
- What changes between the `-132`, `-128` and `-140` variants at `+0x10`.
- What the `+0x08` end-relative word addresses; the last 32 bytes were not decoded.
- The `ComputeGraphStore` reader and the meaning of `+0x60`.

## Changelog

- 2026-11-26: compiled from `artifact: docs/formats/zcg.md`, `workspace: coverage_audit/out/tables.md` and `workspace: CONTEXT_HANDOFF.md`. Exact slots/stored/logical taken from the `tables.md` census row, not re-scanned. Grade set to Partial (header/pointer structure, not semantics) although `tables.md` labels the row Classified with "no payload decoder". Store-registration VAs from the source Exe-path table were withheld; the class name and call-site reference are retained as the substantive claim. No index edits, no commit, no publish.
- 2026-11-26 (review): removed the rounded container byte-size paraphrase and the count-derived compression ratio; float percentages are now attributed as reported, not recomputed; Unknowns gained an explicit source path; `+0x48` confidence changed from measured to unknown to match its undecoded meaning. Fields table rechecked at four columns with no unescaped pipe.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zcg.md`. No count was selected by modification time.

