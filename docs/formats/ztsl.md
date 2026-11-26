# `ztsl` resources (type code `0x65`)

Compiled 2026-11-26 from local artifacts. Decode scope: the shared zlib container plus the measured 160-byte header, the body count and the byte-equality of that header with the `zfid` template; element semantics are not decoded. This is not a container-only result. Grade **Partial**, scoped to that header/count structure and not to semantics. Write status **W0**: no writer, no encoder, no pack-back and no game-load test in any source. Sources: `artifact: docs/formats/ztsl.md`; `workspace: coverage_audit/out/tables.md` (counts derived from `artifact: type_census.csv`); `workspace: CONTEXT_HANDOFF.md`. With 5 slots the whole population was examined individually. All population scans were Rust release binaries, offline; the executable was read as a PE file and never executed.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x65`. It resolves to the label `ztsl` through the executable callback type-name table by string xref (PE read as data; `artifact: docs/formats/ztsl.md`, Exe path table; full VAs withheld from this compiled copy). The word is registered with store class `FacialTangentSpaceLutStore` at the shared store-register call site (same source, Exe path table). The semantic reading "facial tangent-space lookup table" is **inferred** from the class name; no element was mapped to a tangent-space entry (`artifact: docs/formats/ztsl.md`, Identity).

Structural identity, **measured** on 5 of 5 slots by the `tail3` passes and a Python one-shot (`artifact: docs/formats/ztsl.md`, Verification): two zlib streams with the first exactly 160 bytes; a count at `+0x28` sizing the body as `4 × count` in 4 slots and `4 × count + 8` in 1; and the 160-byte header being the same serialised template as the `0x67` `zfid` 240-byte header shifted by exactly `0x50` bytes, a measured byte equality over all 33,810 pairs. No reader or list function was located.

## Counts

Exact counts from `workspace: coverage_audit/out/tables.md` (`0x65` row; derived census `artifact: type_census.csv`): **5 slots, 182,736 stored bytes, 228,416 logical bytes**. These agree across the census, the join and the slot index (`type_probe inventory`; `artifact: docs/formats/ztsl.md`, Verification).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 5 | 182,736 | 228,416 |
| **Total** | **5** | **182,736** | **228,416** |

Distribution facts from `artifact: docs/formats/ztsl.md` (Counts): every slot is a resource entry, generation 4 at root and containing header, all in one archive header; 5 unresolved hashes and 5 distinct name hashes. Per-row stored/logical/count/body/residual from that source:

| Row | Stored | Logical | Count at `+0x28` | Body | Residual |
|---:|---:|---:|---:|---:|---:|
| 0 | 43,616 | 53,648 | 13,372 | 53,488 | 0 |
| 1 | 9,776 | 13,824 | 3,414 | 13,664 | 8 |
| 2 | 43,232 | 53,648 | 13,372 | 53,488 | 0 |
| 3 | 43,184 | 53,648 | 13,372 | 53,488 | 0 |
| 4 | 42,928 | 53,648 | 13,372 | 53,488 | 0 |

## Container

Verified on 5 of 5 slots by the own `tail3` `container` pass (0.002 s at 2,070 slots/s, 75.64 stored MB/s, 94.55 logical MB/s; `artifact: docs/formats/ztsl.md`, Verification). Stored `+0x00..+0x0F` are sixteen zero bytes in 5 of 5 and `78 da` sits at `+0x10` in 5 of 5. Exactly two streams in all 5 slots, the first exactly 160 bytes. Gaps: 0 and 13 at each slot's boundary (four slots with gap 13, one with gap 0). `logical == sum(inflated)` in 5 of 5; zero inflate errors; stored accounted for byte-exactly. Exception list empty. Byte-exact account of row 3 (43,184 stored / 53,648 logical): `16 + 13 + 43,149 + 6 = 43,184` stored and `160 + 53,488 = 53,648` inflated, no trailing zero bytes.

## Fields

Offsets relative to the inflated payload, little-endian. Source for every row: `artifact: docs/formats/ztsl.md` (Fields table and the `zfid` header-template section), from `tail3` `profile`/`perfield` passes and a Python one-shot over 5 `ztsl` plus 6,762 `zfid` slots. Confidence vocabulary is limited to measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence |
|---|---:|---|---|
| `+0x08` | 4 | Constant `0x50000080` in 5 of 5 (`tail3` perfield) | measured |
| `+0x10` | 4 | Constant `0x50000020` in 5 of 5 (`tail3` perfield) | measured |
| `+0x28` | 4 | The count: 3,414 in one slot and 13,372 in four; body = `4 × count` with residual {0, 8} (`tail3` stride; Python one-shot) | measured |
| `+0x2c` | 4 | Constant `0x00090004`; `0x50` below `zfid +0x7c` (`tail3` perfield; Python one-shot) | measured |
| `+0x30` | 4 | Constant `0x00001601`; `0x50` below `zfid +0x80` (`tail3` perfield; Python one-shot) | measured |
| `+0x38` | 4 | Constant `0x60000000`; `0x50` below `zfid +0x88` (`tail3` perfield; Python one-shot) | measured |
| `+0x48` | 4 | Constant `0x50000060`; differs from `zfid +0x98` (`0x500000b0`) by exactly `0x50` (`tail3` perfield; Python one-shot) | measured |
| `+0x70` | 4 | Constant `0xffff0214`; `0x50` below `zfid +0xc0` (`tail3` perfield; Python one-shot) | measured |
| `+0x74` | 4 | Constant `0xffffffff`; `0x50` below `zfid +0xc4` (`tail3` perfield; Python one-shot) | measured |
| `+0x88` | 4 | Constant `0x00000101`; `0x50` below `zfid +0xd8` (`tail3` perfield; Python one-shot) | measured |
| `+0x00`, `+0x04`, `+0x0c`, `+0x14`, `+0x18`, `+0x1c`, `+0x20`, `+0x24`, `+0x34`, `+0x3c`, `+0x40`, `+0x44`, `+0x4c..+0x6c`, `+0x78..+0x86`, `+0x8c..+0x9e` | 4 | Zero in 5 of 5 (`tail3` perfield) | measured |

No field name beyond an offset is asserted where no role was decoded. The `zfid` header template, **verified** by re-inflating the first stream of all 5 `ztsl` and all 6,762 `zfid` slots and comparing `ztsl[0..160]` against `zfid[0x50..0xEF]`: 141 to 153 of 160 bytes equal in every one of the 33,810 pairs (most common 151); the differing offsets are exactly `{+0x08..+0x17, +0x28, +0x29, +0x48}`; six constant words sit exactly `+0x50` below their `zfid` counterparts; the one pointer differing in value differs by exactly `0x50`. Whether the two share a reader is unknown: byte equality does not prove a common loader. What each body word denotes is not decoded; the count sizes the body but does not name its elements. The strict single-fit stride search reports zero perfect fits because of the 8-byte residual; the correct statement is the two-valued residual set `{0, 8}`.

## Decode status

**Partial, scoped to actual structure.** Decoded and verified: the container on 5 of 5 slots; the fixed 160-byte header with its nine constant cells and zero cells; the count at `+0x28` with body = `4 × count` plus a `{0, 8}` residual; and the byte-equality of that header with the `zfid` template shifted by `0x50`. Not decoded: which float is which tangent-space entry, the 8-byte residual in the smallest slot, why four of five slots pair by name hash with three other codes at once, whether `ztsl` and `zfid` share a reader, and the store reader (`artifact: docs/formats/ztsl.md`, Decode and Unknowns). Write status W0; no source proves a writer.

## Verification

All verification steps are listed in `artifact: docs/formats/ztsl.md` (Verification): `type_probe inventory artifact: type_census.csv 00000065 out ztsl_slots.tsv` (1,255,039 rows in 0.14 s, 5 selected); the own `tail3` crate `container` (0.002 s), `profile`, `stride`, `cross` and `perfield` passes over 5 slots; a companion join over 1,255,039 rows (4 of 5 pair with each of `0x5f`, `0x72` and `0x63` by name hash, zero name matches, no measured numeric relation); cross-checks showing the payload embeds neither its own name hash nor its stored or logical size (0 of 5 each); and a Python one-shot re-derivation over 5 `ztsl` plus 6,762 `zfid` slots (equality histogram 141-153 equal bytes over 33,810 pairs, exact differing-offset set and the `0x50` relocation delta). Counts cross-checked against `workspace: coverage_audit/out/tables.md`. Python was used only as a one-shot probe; the executable was never executed.

## Unknowns

Source for every bullet in this section: `artifact: docs/formats/ztsl.md` (Unknowns and Decode).

- Which float in the body is which tangent-space entry.
- The 8-byte residual in the smallest slot.
- Why four of five slots pair by name hash with three other codes at once.
- Whether `ztsl` and `zfid` share a reader or only a serialiser.
- The `FacialTangentSpaceLutStore` reader.

## Changelog

- 2026-11-26: compiled from `artifact: docs/formats/ztsl.md`, `workspace: coverage_audit/out/tables.md` and `workspace: CONTEXT_HANDOFF.md`. Exact slots/stored/logical taken from the `tables.md` census row, not re-scanned. Grade set to Partial (header/count/template structure, not semantics) although `tables.md` labels the row Classified with "nothing decoded". Store-registration VAs from the source Exe-path table were withheld; the class names and call-site references are retained. No index edits, no commit, no publish.
- 2026-11-26 (review): removed the "element meaning unknown" claim from the `+0x28` field row and placed it in the Fields prose where the count role is not contradicted; Unknowns gained an explicit source path. Fields table rechecked at four columns with no unescaped pipe.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/ztsl.md`. No count was selected by modification time.

