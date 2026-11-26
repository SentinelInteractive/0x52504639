# `zfd` resources (type code `0x56`)

Compiled 2026-11-26 from local artifacts. Decode scope: the shared zlib container plus the measured header count and the decoded path-string table; the record area between them is not decoded. This is not a container-only result. Grade **Partial**, scoped to that count/string structure and not to semantics. Write status **W0**: no writer, no encoder, no pack-back and no game-load test in any source. Sources: `artifact: docs/formats/zfd.md`; `workspace: coverage_audit/out/tables.md` (counts derived from `artifact: type_census.csv`); `workspace: CONTEXT_HANDOFF.md`. With 11 slots the whole population was examined individually; there is no sampling. All population scans were Rust release binaries, offline; the executable was read as a PE file and never executed.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x56`. It resolves to the label `zfd` through the executable callback type-name table by string xref (PE read as data; `artifact: docs/formats/zfd.md`, Exe path table; full VAs withheld from this compiled copy). The word is registered with store class `FrameFilterStore` at the shared store-register call site (same source, Exe path table). The semantic reading "frame filter" is **inferred** from the class name and the shared three-letter extension on the paths; path names themselves are private and are not reproduced (`artifact: docs/formats/zfd.md`, Identity).

Structural identity, **measured** on 11 of 11 slots by the `tail3` passes and a Python one-shot (`artifact: docs/formats/zfd.md`, Verification): the header carries a count at `+0x28` that equals the number of path strings in the payload in 11 of 11 slots; the string table is ascending, 4-byte aligned and NUL-terminated, with a 33 to 68 byte tail of further structure before the payload end. The record area between the header and the string table is not decoded. No reader or list function was located.

## Counts

Exact counts from `workspace: coverage_audit/out/tables.md` (`0x56` row; derived census `artifact: type_census.csv`): **11 slots, 51,312 stored bytes, 827,344 logical bytes**. These agree across the census, the join and the slot index (`type_probe inventory`; `artifact: docs/formats/zfd.md`, Verification).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `anim.rpf` | 11 | 51,312 | 827,344 |
| **Total** | **11** | **51,312** | **827,344** |

Distribution facts from `artifact: docs/formats/zfd.md` (Counts): every slot is a resource entry, generation 4 at root and containing header, all in one archive header; 11 unresolved hashes and zero dictionary matches, all name hashes distinct. Per-row stored/logical/count from that source:

| Row | Stored | Logical | Count at `+0x28` | Path strings |
|---:|---:|---:|---:|---:|
| 0 | 160 | 448 | 1 | 1 |
| 1 | 3,856 | 46,416 | 8 | 8 |
| 2 | 1,824 | 14,016 | 7 | 7 |
| 3 | 3,344 | 64,080 | 13 | 13 |
| 4 | 144 | 400 | 1 | 1 |
| 5 | 144 | 352 | 1 | 1 |
| 6 | 272 | 1,264 | 1 | 1 |
| 7 | 352 | 1,792 | 1 | 1 |
| 8 | 39,824 | 684,144 | 262 | 262 |
| 9 | 320 | 1,600 | 2 | 2 |
| 10 | 1,072 | 12,832 | 13 | 13 |

The count identity holds on 11 of 11 slots, including the 262-entry largest slot.

## Container

Verified on 11 of 11 slots by the own `tail3` `container` pass (0.016 s at 702 slots/s, 3.28 stored MB/s, 52.83 logical MB/s; `artifact: docs/formats/zfd.md`, Verification). Stored `+0x00..+0x0F` are sixteen zero bytes in 11 of 11 and `78 da` sits at `+0x10` in 11 of 11. Stream count: one stream in 10 slots, two in 1 (the 684,144-byte logical slot). Gaps: 0 at 11 boundaries and 6 at 1. `logical == sum(inflated)` in 11 of 11; zero inflate errors; the stored buffer is accounted for byte-exactly as `16 + gaps + compressed + trailing`. Exception list empty. Byte-exact account of the median slot (row 7, 352 stored / 1,792 logical): `16 + 0 + 335 + 1 = 352` stored and 1,792 inflated, with no trailing zero bytes.

## Fields

Offsets relative to the inflated payload, little-endian. Source for every row: `artifact: docs/formats/zfd.md` (Fields table), from `tail3` `perfield`/`profile` passes and a Python one-shot re-derivation over 11 slots. Confidence vocabulary is limited to measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence |
|---|---:|---|---|
| `+0x28` | 2 | The count: 1, 2, 7, 8, 13 or 262; equals the number of path strings in 11 of 11 slots (`tail3` cross; Python one-shot) | measured |
| `+0x38` | 2 | Equals `+0x28` in 11 of 11 (`tail3` perfield); whether the second copy is a capacity is unproven | unknown |
| `+0x08`, `+0x20`, `+0x30` | 4 | Pointer-shaped `0x5000xxxx`, 11 distinct values each; meaning unknown (`tail3` perfield) | unknown |
| `+0x18` | 4 | Constant `1` in 11 of 11 (`tail3` perfield) | measured |
| `+0x44` | 4 | `1.0f` (`0x3f800000`) in 9 slots, 0 in 2; meaning unknown (`tail3` perfield) | unknown |
| `+0x40`, `+0x70`, `+0xa0`, `+0xd0` | 4 | Repeated high word `0x3f800000` at a 0x30-byte stride (`tail3` perfield); no decoded record role | unknown |
| `+0x68`, `+0x98`, `+0xc8`, `+0xf8` | 4 | Repeated 32-bit word at the same 0x30 stride (`tail3` perfield); no decoded record role | unknown |
| `+0x00`, `+0x04`, `+0x0c`, `+0x10`, `+0x1c`, `+0x2c`, `+0x34`, `+0x3c` | 4 | Zero in 11 of 11 (`tail3` perfield) | measured |

No field name beyond an offset is asserted where no role was decoded. The string table, **verified** in 11 of 11: `N` strings from `+0x28`, in ascending offset order, all at 4-byte-aligned offsets, NUL-terminated, 19 to 65 bytes long with one shared three-letter extension, followed by a 33 to 68 byte tail of zero words and pointer-shaped words before the payload end. No 32-bit word before the first string equals a string's start offset (0 references in 11 of 11), so the strings are not addressed by an offset table. No `size = stride*count + c` fit exists for offsets `0..0xff` and strides 2/4/8/12/16/24/32/40/48 for either logical or body size.

## Decode status

**Partial, scoped to actual structure.** Decoded and verified: the container on 11 of 11 slots; the count at `+0x28` and its duplicate at `+0x38`; the constant `+0x18`; and the string layer (ascending, aligned, NUL-terminated strings with a trailing tail). Not decoded: the record area between the header and the string table, its stride and fields, how a record maps to a string, the pointer cells, the `1.0f` constants, and the store reader (`artifact: docs/formats/zfd.md`, Decode and Unknowns). The 0x30-byte repeating pattern is a measured observation, not a decoded record. Write status W0; no source proves a writer.

## Verification

All verification steps are listed in `artifact: docs/formats/zfd.md` (Verification): `type_probe inventory artifact: type_census.csv 00000056 out zfd_slots.tsv` (1,255,039 rows in 0.14 s, 11 selected); the own `tail3` crate (`artifact: type_reports/tail3`) `container` (0.016 s), `profile`, `stride`, `cross` and `perfield` passes over 11 slots; a companion join over 1,255,039 census rows with zero 64-bit name-hash companions in any other code; cross-checks showing the payload embeds neither its own 64-bit name hash nor its stored or logical size (0 of 11 each); and a Python one-shot multi-stream inflate re-derivation (count at `+0x28` equals the number of path strings in 11 of 11: 1, 8, 7, 13, 1, 1, 1, 1, 262, 2, 13; same at `+0x38`; ascending 4-byte-aligned table with a 33-68 byte tail; zero offset-table references). Counts cross-checked against `workspace: coverage_audit/out/tables.md`. Python was used only as a one-shot probe; the executable was never executed.

## Unknowns

Source for every bullet in this section: `artifact: docs/formats/zfd.md` (Unknowns and Decode).

- The record area between the header and the string table: stride, fields and record-to-string mapping.
- The meaning of the pointer cells and the `1.0f` constants at the 0x30 stride.
- What the two counts at `+0x28`/`+0x38` denote if they are not both the string count.
- The `FrameFilterStore` reader.

## Changelog

- 2026-11-26: compiled from `artifact: docs/formats/zfd.md`, `workspace: coverage_audit/out/tables.md` and `workspace: CONTEXT_HANDOFF.md`. Exact slots/stored/logical taken from the `tables.md` census row, not re-scanned. Grade set to Partial (count/string structure, not semantics) although `tables.md` labels the row Classified with "nothing decoded". Source correction: the source Identity and Decode paragraphs say the string table "ends exactly at the payload end", but its own Fields and Verification paragraphs measure a 33-68 byte tail after the last terminator; this compiled copy uses the measured tail version. Store-registration VAs from the source Exe-path table were withheld; the class name and call-site reference are retained. No index edits, no commit, no publish.
- 2026-11-26 (review): removed the count-derived compression ratio; `+0x38`, `+0x40` group and `+0x68` group confidences changed from measured to unknown to match their undecoded meanings; Unknowns gained an explicit source path. Fields table rechecked at four columns with no unescaped pipe.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zfd.md`. No count was selected by modification time.

