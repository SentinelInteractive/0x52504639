# `zcps` resources (type code `0x63`)

Compiled 2026-11-26 from local artifacts. Decode scope: the shared zlib container plus the measured 448-byte header extent and pointer-cell shapes; payload element semantics are not decoded. This is not a container-only result. Grade **Partial**, scoped to that header structure and not to semantics. Write status **W0**: no writer, no encoder, no pack-back and no game-load test in any source. Sources: `artifact: docs/formats/zcps.md`; `workspace: coverage_audit/out/tables.md` (counts derived from `artifact: type_census.csv`); `workspace: CONTEXT_HANDOFF.md`. All population scans were Rust release binaries, offline; the executable was read as a PE file and never executed.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x63`. It resolves to the label `zcps` through the executable callback type-name table by string xref (PE read as data; `artifact: docs/formats/zcps.md`, Exe path table; full VAs withheld from this compiled copy). The word is registered with store class `ComputeSchemeStore` at the shared store-register call site (same source, Exe path table). The semantic reading "compute scheme" is **inferred** from the class name; no scheme, stage or binding was decoded (`artifact: docs/formats/zcps.md`, Identity).

Structural identity, **measured** on 98 of 98 slots by `tail2` and a Python one-shot (`artifact: docs/formats/zcps.md`, Verification): one zlib stream behind the 16-zero prefix with `logical == sum(inflated)`; a 448-byte header (28 cells of 16 bytes) with no `0x50000000`-relative target below 448 and 448 itself a target in every slot; pointer cells each followed by a zero word and duplicated equal 32-bit pairs; and a non-uniform record shape, with 90 slots showing one pattern and 8 an extra pointer cell. No reader or list function was located.

## Counts

Exact counts from `workspace: coverage_audit/out/tables.md` (`0x63` row; derived census `artifact: type_census.csv`): **98 slots, 107,312 stored bytes, 214,160 logical bytes**. These agree across the census, the join and the slot index (`type_probe inventory`; `artifact: docs/formats/zcps.md`, Verification).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 98 | 107,312 | 214,160 |
| **Total** | **98** | **107,312** | **214,160** |

Distribution facts from `artifact: docs/formats/zcps.md` (Counts; `tail2` passes): every slot is a resource entry, generation 4 at root and containing header; all 98 sit in one archive header; 15 dictionary matches and 83 unresolved hashes, all name hashes distinct; stored 288/624/832/1,152/2,688/2,688 (min/p25/median/p75/p95/max), logical 736/1,312/1,744/2,176/5,136/5,168. Logical size takes 26 distinct values, all between 736 and 5,168 bytes.

## Container

Verified on 98 of 98 slots by `type_probe walk` and the `tail2` `container` pass (0.003 s at 31,140 slots/s; shared pass 1,760 slots/s, 66.0 stored MB/s, 862.4 logical MB/s; `artifact: docs/formats/zcps.md`, Container). Stored `+0x00..+0x0F` are sixteen zero bytes in 98 of 98 and `78 da` sits at `+0x10` in 98 of 98. Exactly one stream in 98 of 98 slots, gap 0, no second stream. `logical == sum(inflated)` in 98 of 98; the `+16` convention never occurs; zero inflate errors; exception list empty. First-stream length equals the logical size in every slot, 736 to 5,168 bytes over 26 distinct values.

## Fields

Offsets relative to the inflated payload, little-endian. Source for every row: `artifact: docs/formats/zcps.md` (Fields table; header extent, header pattern and byte-exact minima), from `tail2` `profile`/`perfield` passes and a Python one-shot re-derivation over 98 slots. Confidence vocabulary is limited to measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence |
|---|---:|---|---|
| `+0x08` | 4 | `0x50000000`-relative pointer, followed by a zero word at `+0x0c` in 98 of 98 (`tail2` profile) | measured |
| `+0x10`, `+0x14` | 4 | Equal `0xa3239802`-shaped pair in the smallest slot; duplicated hash-like word, meaning unknown (`tail2` perfield) | unknown |
| `+0x18`, `+0x1c` | 4 | Duplicated equal `u32` pair (4 and 4 in the smallest slot); count/capacity shape, role unproven (`tail2` perfield) | inferred |
| `+0x20`, `+0x30`, `+0x40`, `+0x60`, `+0x70`, `+0x80`, `+0x90`, `+0x130`, `+0x140`, `+0x150`, `+0x160` | 4 each | Further pointer cells, each followed by a zero word (`tail2` profile) | measured |

No field name beyond an offset is asserted where no role was decoded. Header extent is 448 bytes in 98 of 98 slots: scanning every `0x50000000`-relative pointer in bytes `0..448`, the minimum target is exactly 448 and no target is below it (`tail2` profile; Python one-shot). Classifying the first sixteen 32-bit words gives `ZZPZOOOOPZOOPZOO` in 90 slots and `ZZPZPPOOPZOOPZOO` in 8, i.e. a pointer at `+0x08` in all 98 and an extra pointer at `+0x10` in 8. Byte-exact accounting of the two smallest slots: `448 + 288 = 736` and `448 + 320 = 768`, header plus body with no unaccounted byte. No `size = stride*count + c` fit exists for offsets `0..447` and strides 2/4/8/12/16/24/32. Float metrics are reported in `artifact: docs/formats/zcps.md` (Decode; Python one-shot), not recomputed here: 53,540 32-bit words, 18.04 percent exact zero and 82.03 percent `|f| <= 1`.

## Decode status

**Partial, scoped to actual structure.** Decoded and verified: the container on 98 of 98 slots; the 448-byte header extent; the pointer-cell shapes and the 90/8 pattern split; and the byte-exact minima. Not decoded: the block layout after 448, what the duplicated pairs count, whether the 8-slot variant is a version, the element semantics of the floats, and the store reader. The header is not a fixed-stride array and no count sizes the payload (`artifact: docs/formats/zcps.md`, Decode and Unknowns). On the three-name relationship: 4 of 5 `ztsl` slots share a name hash with a `zcps` slot and 95 `zcps` slots pair with `0x5f` and `0x72` by name hash; re-inflating both sides found zero shared nonzero pointer words (0 of 95 for each twin), so this is name identity, not a numeric reference. Write status W0; no source proves a writer.

## Verification

All verification steps are listed in `artifact: docs/formats/zcps.md` (Verification): `type_probe inventory artifact: type_census.csv 00000063 out zcps_slots.tsv` (1,255,039 rows in 0.14 s, 98 selected); `type_probe walk` and `type_probe samples` with stratified dumps of both header patterns and both size extremes; the own `tail2` crate `container` (0.003 s), `profile`, `stride` and `cross` passes over 98 slots; a companion join over 1,255,039 rows (95 pair with `0x5f` and with `0x72`, 4 with `0x65`, zero numeric relations); and a Python one-shot re-derivation (minimum pointer target exactly 448 in 98/98, pattern split 90/8, 53,540 words with float percentages as reported in `artifact: docs/formats/zcps.md` (18.04 percent zero, 82.03 percent `|f| <= 1`; not recomputed), 26 distinct logical sizes). Counts cross-checked against `workspace: coverage_audit/out/tables.md`. Python was used only as a one-shot probe; the executable was never executed.

## Unknowns

Source for every bullet in this section: `artifact: docs/formats/zcps.md` (Unknowns and Decode).

- What the duplicated pairs at `+0x18` and elsewhere count.
- Whether the 8 slots with the extra pointer at `+0x10` are a version or a variant.
- The block layout after 448 and the element semantics of the floats.
- The `ComputeSchemeStore` reader.

## Changelog

- 2026-11-26: compiled from `artifact: docs/formats/zcps.md`, `workspace: coverage_audit/out/tables.md` and `workspace: CONTEXT_HANDOFF.md`. Exact slots/stored/logical taken from the `tables.md` census row, not re-scanned. Grade set to Partial (header extent/pointer shapes, not semantics) although `tables.md` labels the row Classified with "no payload decoder". Store-registration VAs from the source Exe-path table were withheld; the class name and call-site reference are retained. No index edits, no commit, no publish.
- 2026-11-26 (review): removed the count-derived compression ratio; float percentages are attributed as reported, not recomputed; Unknowns gained an explicit source path. Fields table rechecked at four columns with no unescaped pipe.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zcps.md`. No count was selected by modification time.

