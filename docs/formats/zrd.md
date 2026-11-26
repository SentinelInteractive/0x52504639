# `zrd` resources (type code `0x6d`)

Compiled 2026-11-26 from local artifacts. Decode scope: the shared zlib container plus the measured `RIG\x02` magic, the record count and the located-but-unparsed record area; the record chain rule and element semantics are not decoded. This is not a container-only result. Grade **Partial**, scoped to that magic/count structure and not to semantics. Write status **W0**: no writer, no encoder, no pack-back and no game-load test in any source. Sources: `artifact: docs/formats/zrd.md`; `workspace: coverage_audit/out/tables.md` (counts derived from `artifact: type_census.csv`); `workspace: CONTEXT_HANDOFF.md`. With 4 slots the whole population was examined individually. All population scans were Rust release binaries, offline; the executable was read as a PE file and never executed.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x6d`. It resolves to the label `zrd` through the executable callback type-name table by string xref (PE read as data; `artifact: docs/formats/zrd.md`, Exe path table; full VAs withheld from this compiled copy). The word is registered with store class `RigStore` at the shared store-register call site (same source, Exe path table). The semantic reading "rig" is **inferred** from the class name and the payload's own `RIG` magic; no bone, joint or transform field was decoded (`artifact: docs/formats/zrd.md`, Identity).

Structural identity, **measured** on 4 of 4 slots by the `tail3` `zrd` shape pass and a Python one-shot (`artifact: docs/formats/zrd.md`, Verification): the four bytes `RIG\x02` sit at inflated `+0x70` in all slots and open each record in the payload; and the count at `+0x58` equals both the number of `RIG\x02` occurrences and the number of `RIG0` occurrences in 4 of 4 slots. The record chain rule is not resolved: the step from one `RIG\x02` to the next is neither constant nor `4 + size`. No reader or list function was located.

## Counts

Exact counts from `workspace: coverage_audit/out/tables.md` (`0x6d` row; derived census `artifact: type_census.csv`): **4 slots, 6,641,616 stored bytes, 16,922,688 logical bytes**. These agree across the census, the join and the slot index (`type_probe inventory`; `artifact: docs/formats/zrd.md`, Verification).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `anim.rpf` | 4 | 6,641,616 | 16,922,688 |
| **Total** | **4** | **6,641,616** | **16,922,688** |

Distribution facts from `artifact: docs/formats/zrd.md` (Counts): every slot is a resource entry, generation 4 at root and containing header, each in a different archive header (4 headers, 1 slot each); 4 unresolved hashes and 4 distinct name hashes. Per-row stored/logical/first-stream/count/magic counts from that source:

| Row | Stored | Logical | First stream | Count `+0x58` | `RIG\x02` | `RIG0` |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 39,040 | 95,936 | 65,536 | 22 | 22 | 22 |
| 1 | 262,224 | 1,247,136 | 1,245,184 | 543 | 543 | 543 |
| 2 | 5,523,248 | 9,709,120 | 9,699,328 | 2,076 | 2,076 | 2,076 |
| 3 | 817,104 | 5,870,496 | 5,832,704 | 1,256 | 1,256 | 1,256 |

Logical sizes are the exact per-row values in `artifact: docs/formats/zrd.md` (Counts).

## Container

Verified on 4 of 4 slots by the own `tail3` `container` pass (0.045 s at 88.8 slots/s, 147.5 stored MB/s, 375.8 logical MB/s; `artifact: docs/formats/zrd.md`, Verification). Stored `+0x00..+0x0F` are sixteen zero bytes in 4 of 4 and `78 da` sits at `+0x10` in 4 of 4. Exactly two streams in all 4 slots, both large: the first stream is 65,536, 1,245,184, 9,699,328 or 5,832,704 bytes; there is no small header stream and the header lives at the start of the inflated payload. Gaps: 0 at four boundaries, and 13, 2, 8, 6 once each. `logical == sum(inflated)` in 4 of 4; zero inflate errors; stored accounted for byte-exactly. Exception list empty. Byte-exact account of row 3 (817,104 stored / 5,870,496 logical): `16 + 2 + 817,075 + 11 = 817,104` stored and `5,832,704 + 37,792 = 5,870,496` inflated.

## Fields

Offsets relative to the inflated payload, little-endian, verified on 4 of 4 slots. Source for every row: `artifact: docs/formats/zrd.md` (Fields table), from the `tail3` `zrd` shape/perfield passes and a Python one-shot re-derivation (Verification). Confidence vocabulary is limited to measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence |
|---|---:|---|---|
| `+0x08`, `+0x38`, `+0x48` | 4 | `0x50000000`-relative pointers, 4 distinct values each, targets in range (`tail3` perfield) | measured |
| `+0x40` | 4 | `0x00110010`, a `u16` pair (16, 17); meaning unknown (`tail3` perfield) | unknown |
| `+0x44` | 4 | Constant `1` in 4 of 4 (`tail3` perfield) | measured |
| `+0x50` | 4 | 29 / 647 / 1,291 / 2,591; likely a capacity, not the record count (`tail3` perfield) | inferred |
| `+0x58` | 4 | The record count: {22, 543, 1,256, 2,076} as a set, mapped per row in the Counts table; equals the `RIG\x02` and `RIG0` counts in 4 of 4 (`tail3` zrd pass; Python one-shot) | measured |
| `+0x5c` | 4 | Constant `0x01000000` (`tail3` perfield) | measured |
| `+0x68` | 4 | Distinct hash-like word per slot; not the name hash (0 of 4) (`tail3` perfield; companion join) | measured |
| `+0x70` | 8 | `RIG\x02` magic plus a `u32` (5,932 / 128,011 / 112,340 / 118,752), measured in 4 of 4 (`tail3` zrd pass; Python one-shot); whether the `u32` is a size or an id is unknown | unknown |
| `+0x00`, `+0x04`, `+0x0c..+0x34`, `+0x3c`, `+0x4c`, `+0x54`, `+0x60`, `+0x64`, `+0x6c`, `+0x78` onward | 4 | Zero in 4 of 4 (`tail3` perfield) | measured |

No field name beyond an offset is asserted where no role was decoded. The record area: the first `RIG\x02` is at `+0x70`, the same cell as the header magic, so the header's last field opens the first record. Later `RIG\x02` occurrences are spaced 2,224-4,736 bytes in the smallest slot and 496-720 bytes in the largest, with a different spacing set per slot; records are variable-length. Each `RIG\x02` is followed by a `u32` and each record contains exactly one `RIG0` block. The `4 + size` step rule fails (record 0 of the smallest slot: 112 + 4 + 5,932 = 6,048, which is the next magic; record 1 lands 6 bytes past its own size). A `RigStore` dictionary shape is **negated**: no ascending `u32` index array exists, no `size = stride*count + c` fit exists for offsets `0..0xff` and strides 2/4/8/12/16/24/32/40/48, and the `(16, 17)` pair seeds 16- and 17-word runs at offsets 432-1,596 while the payload sizes are the exact per-row values above.

## Decode status

**Partial, scoped to actual structure.** Decoded and verified: the container on 4 of 4 slots; the `RIG\x02` magic at `+0x70`; the record count at `+0x58` against both magic counts; the header constants; and the location of N variable-length records each with one `RIG0` block. Not decoded: the record chain rule, the contents of the `RIG0` block, the relationship between `+0x50` and `+0x58`, the `(16, 17)` pair, the other pointer cells, element semantics and the store reader (`artifact: docs/formats/zrd.md`, Decode and Unknowns). Companion join: zero name-hash companions in any other code; one incidental hit where the stored size appears as a `u32` in one payload (1 of 4, 48 occurrences), reported without interpretation. Write status W0; no source proves a writer.

## Verification

All verification steps are listed in `artifact: docs/formats/zrd.md` (Verification): `type_probe inventory artifact: type_census.csv 0000006d out zrd_slots.tsv` (1,255,039 rows in 0.13 s, 4 selected); the own `tail3` crate `container` (0.045 s), `profile`, `stride`, `cross` and `zrd` shape pass (0.624 s at 6.4 slots/s); a companion join over 1,255,039 rows with zero companions; cross-checks showing neither the name hash nor the logical size occurs in a payload (0 of 4 each) and the stored size occurs in one payload only; and a Python one-shot re-derivation (`RIG\x02` at `+0x70` in 4/4, `RIG\x02` count = `RIG0` count = the `u32` at `+0x58` in 4/4 as 22, 543, 1,256, 2,076, second `RIG\x02` at 6,048 / 128,128 / 112,464 / 139,600, and the `4 + size` rule failing). Counts cross-checked against `workspace: coverage_audit/out/tables.md`. Python was used only as a one-shot probe; the executable was never executed.

## Unknowns

Source for every bullet in this section: `artifact: docs/formats/zrd.md` (Unknowns and Decode).

- The record chain rule: what the `u32` after each `RIG\x02` measures, and why the next record does not start at `4 + size`.
- What the `RIG0` block inside each record holds.
- The relationship between the two counts at `+0x50` and `+0x58`.
- The `(16, 17)` pair at `+0x40`.
- The `RigStore` reader.

## Changelog

- 2026-11-26: compiled from `artifact: docs/formats/zrd.md`, `workspace: coverage_audit/out/tables.md` and `workspace: CONTEXT_HANDOFF.md`. Exact slots/stored/logical taken from the `tables.md` census row, not re-scanned. Grade set to Partial (magic/count/record-location structure, not semantics) although `tables.md` labels the row Classified with "nothing decoded". Source note: the Fields and Verification paragraphs in the source list the four `+0x58` counts as 22 / 543 / 1,256 / 2,076 while its per-row Counts table maps 2,076 to row 2 and 1,256 to row 3; this compiled copy presents the set and defers the row mapping to the per-row table. Store-registration VAs from the source Exe-path table were withheld; the class name and call-site reference are retained. No index edits, no commit, no publish.
- 2026-11-26 (review): removed the count-derived compression ratio and the size-spread paraphrase in favour of the exact per-row byte values; `+0x70` confidence changed from measured to unknown to match its unresolved size-or-id meaning; Unknowns gained an explicit source path. Fields table rechecked at four columns with no unescaped pipe.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zrd.md`. No count was selected by modification time.

