# `zcgc` resources (type code `0x72`)

Compiled 2026-11-26 from local artifacts. Decode scope: the shared zlib container plus the measured header structure and identifier pairing; payload element semantics are not decoded. This is not a container-only result. Grade **Partial**, scoped to that structure and not to semantics. Write status **W0**: no writer, no encoder, no pack-back and no game-load test in any source. Sources: `artifact: docs/formats/zcgc.md`; `workspace: coverage_audit/out/tables.md` (counts derived from `artifact: type_census.csv`); `workspace: CONTEXT_HANDOFF.md`. All population scans were Rust release binaries, offline; the executable was read as a PE file and never executed.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x72`. It resolves to the label `zcgc` through the executable callback type-name table by string xref (PE read as data; `artifact: docs/formats/zcgc.md`, Exe path table; full VAs withheld from this compiled copy). The word is registered with store class `ComputeGraphConstantsStore` at the shared store-register call site (same source, Exe path table). The semantic reading "constants side of a compute graph" is **inferred** from the class name and the pairing; no constant, block or graph was interpreted (`artifact: docs/formats/zcgc.md`, Identity).

Structural identity, **measured** on 518 of 518 slots by `tail1` and a Python one-shot (`artifact: docs/formats/zcgc.md`, Verification): a zlib chain of one or two streams behind the 16-zero prefix with `logical == sum(inflated)`; a 176-byte first stream in 490 slots; a dense float region in which, as reported in `artifact: docs/formats/zcgc.md` (Verification) and not recomputed here, 99.98 percent of 319,014,184 32-bit words parse as `|f| <= 1` with 11.55 percent zero; and an 8-byte identifier at `+0x20` equal to `zcg` (`0x5f`) `+0x48` for the same 64-bit name hash in 518 of 518 pairs. The pairing is not a numeric reference: no `zcg` size, offset or hash occurs in a `zcgc` payload (0 of 518). The reader was not located.

## Counts

Exact counts from `workspace: coverage_audit/out/tables.md` (`0x72` row; derived census `artifact: type_census.csv`): **518 slots, 919,033,488 stored bytes, 1,276,056,736 logical bytes**. These agree across the census, the verified type-word join and the slot index (`type_probe inventory/join`; `artifact: docs/formats/zcgc.md`, Verification).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 518 | 919,033,488 | 1,276,056,736 |
| **Total** | **518** | **919,033,488** | **1,276,056,736** |

Distribution facts from `artifact: docs/formats/zcgc.md` (Counts; `tail1` passes): every slot is a resource entry, generation 4 at root and containing header; the same two headers as `zcg` carry 421 and 97 slots; 18 dictionary matches and 500 unresolved hashes, all name hashes distinct and the same 18 names resolving on both sides of the pairing; stored 224/3,280/718,400/901,104/3,204,944/3,865,168/15,244,736 (min/p05/p25/median/p75/p95/max), logical 1,536/6,016/1,048,752/1,310,896/4,456,624/5,177,520/17,825,968. This is the largest tail type by stored bytes on the same slot count as `zcg`.

## Container

Verified on 518 of 518 slots by `type_probe walk out\zcgc_slots.tsv <archive-root> out\zcgc_walk.txt` (518 slots, 3.69 s; 140.4 slots/s, 249.2 stored MB/s, 345.9 logical MB/s; `artifact: docs/formats/zcgc.md`, Verification). Stored `+0x00..+0x0F` are sixteen zero bytes in 518 of 518 and `78 da` sits at `+0x10` in 518 of 518. Stream count: two streams in 490 slots, one in 28, 1,008 streams total. The first stream is exactly 176 bytes in the 490 two-stream slots; the 28 single-stream slots carry the whole logical size in one stream (131,072 in 15, 1,536 in 2, with 262,144, 2,816 and others as singletons). Every stream after the first starts at the next 16-byte-aligned stored offset; gaps are 0 at 631 boundaries, 15 at 360, and 1 to 14 elsewhere, none above 15. `logical == sum(inflated)` in 518 of 518; the `+16` convention never occurs; zero inflate errors; exception list empty.

## Fields

Offsets relative to the inflated payload, little-endian. Source for every row: `artifact: docs/formats/zcgc.md` (Fields table), from the `tail1` `fields`/`hdr` passes over 518 slots and a Python one-shot re-derivation (Verification). Confidence vocabulary is limited to measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence |
|---|---:|---|---|
| `+0x00`, `+0x04`, `+0x0c`, `+0x24`, `+0x28` | 4 | Zero in 518 of 518 (`tail1` fields) | measured |
| `+0x08` | 4 | `0x50000000 + 144` in 490 slots; in the 28 single-stream slots the target is larger (76,208 in 8, 71,568 in 5, 1,504 in 2, then singletons) (`tail1` fields) | measured |
| `+0x10` | 4 | `0x50000000 + 48` in 490 slots, zero in the 28 single-stream slots (`tail1` fields) | measured |
| `+0x14` | 4 | Zero in 518 of 518 (`tail1` fields) | measured |
| `+0x18` | 4 | Zero in 490 slots; `0x50000000 + 48` in the 28 single-stream slots (`tail1` fields) | measured |
| `+0x20` | 8 | Identifier-shaped 8-byte value; equals `zcg +0x48` in 518 of 518 pairs (`tail1` `pairid`; Python one-shot). Meaning unknown | unknown |
| `+0x30`..`+0xAF` | 4 each | Remainder of the 176-byte first stream, float-shaped words (`tail1` hdr) | measured |
| `+0xB0` onward | 4 each | Body region (`tail1` hdr) | measured |

No field name beyond an offset is asserted where no role was decoded. Both pointer targets in the 490-slot variant (144 and 48) land inside the 176-byte header, so the header is a relocation graph over itself, not a pointer table into the body; the 28-slot variant swaps two of the three pointer cells (`artifact: docs/formats/zcgc.md`, Fields). The 28 single-stream slots remain an open structural question; grouping on stream count and comparing the first 176 bytes was proposed but not run.

## Decode status

**Partial, scoped to actual structure.** Decoded and verified: the container on 518 of 518 slots; the two in-header pointer targets (144 and 48) and the 176-byte first extent for 490 slots; the swapped pointer pattern for 28 slots; the identifier equality with `zcg`; and a float-shaped body region (319,014,184 words; float percentages as reported in `artifact: docs/formats/zcgc.md`, not recomputed: 99.98 percent `|f| <= 1`, 11.55 percent zero). Not decoded: field roles in the header beyond those words, element semantics of the float region, the 28-slot variant's header layout, why the pairing is a shared identifier, and the store reader (`artifact: docs/formats/zcgc.md`, Decode and Unknowns). The "constants half of `zcg`'s graph" reading stays inferred. Write status W0; no source proves a writer.

## Verification

All verification steps are listed in `artifact: docs/formats/zcgc.md` (Verification): `type_probe inventory artifact: type_census.csv 00000072 out zcgc_slots.tsv` (1,255,039 rows in 0.15 s, 518 selected); `type_probe walk out\zcgc_slots.tsv <archive-root> out\zcgc_walk.txt` (numbers above); `tail1` `hdr`, `fields`, `stride`, `ids`, `pair`, `pairid` passes over 518 slots; and a Python one-shot re-derivation (176-byte first stream in 490 of 518; stream count 2 in 490 and 1 in 28; paired-identifier equality in 518/518; 319,014,184 words with float percentages as reported in `artifact: docs/formats/zcgc.md` (11.55 percent zero, 99.98 percent `|f| <= 1`; not recomputed)). Counts cross-checked against `workspace: coverage_audit/out/tables.md`. Python was used only as a one-shot probe; the executable was never executed.

## Unknowns

Source for every bullet in this section: `artifact: docs/formats/zcgc.md` (Unknowns and Decode).

- The 28 single-stream slots: whether the 176-byte header is absent, inlined or replaced by a variant.
- Field roles in the 176-byte header beyond the measured pointer words.
- Element semantics of the float region: node constants, weights or sampled curves.
- Why the pairing is a shared identifier rather than a numeric reference.
- The `ComputeGraphConstantsStore` reader.

## Changelog

- 2026-11-26: compiled from `artifact: docs/formats/zcgc.md`, `workspace: coverage_audit/out/tables.md` and `workspace: CONTEXT_HANDOFF.md`. Exact slots/stored/logical taken from the `tables.md` census row, not re-scanned. Grade set to Partial (header/pointer structure, not semantics) although `tables.md` labels the row Classified with "no payload decoder". Store-registration VAs from the source Exe-path table were withheld; the class name and call-site reference are retained. No index edits, no commit, no publish.
- 2026-11-26 (review): removed the rounded container byte-size paraphrase, the count-derived compression ratio and the group-share percentage; float percentages are attributed as reported, not recomputed; Unknowns gained an explicit source path; `+0x20` confidence changed from measured to unknown to match its undecoded meaning. Fields table rechecked at four columns with no unescaped pipe.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zcgc.md`. No count was selected by modification time.

