# `zpt` resources (type code `0x48`)

Compiled 2026-11-26 from local artifacts. Decode scope: the shared zlib container plus the measured 64-bit pointer table and seven-segment partition; payload element semantics are not decoded. This is not a container-only result. Grade **Partial**, scoped to that pointer/segment structure and not to semantics. Write status **W0**: no writer, no encoder, no pack-back and no game-load test in any source. Sources: `artifact: docs/formats/zpt.md`; `workspace: coverage_audit/out/tables.md` (counts derived from `artifact: type_census.csv`); `artifact: final_tail_report.md` (vtable correction); `workspace: CONTEXT_HANDOFF.md`. All population scans were Rust release binaries, offline; the executable was read as a PE file and never executed.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x48`. It resolves to the label `zpt` through the executable callback type-name table by string xref (PE read as data; `artifact: docs/formats/zpt.md`, Exe path table; full VAs withheld from this compiled copy). The word is registered with store class `PtFxAssetStore` at the shared store-register call site (same source, Exe path table). The semantic reading "particle-effect asset" is **inferred** from the class name and the sparse numeric payload; no field is mapped to an emitter, particle or texture (`artifact: docs/formats/zpt.md`, Identity).

The dispatch link was traced and stops at bookkeeping (`artifact: docs/formats/zpt.md`, Identity; correction retained in `artifact: final_tail_report.md`): the final store vtable differs from the shared base in 19 of 36 slots and the first vtable in 13 of 36; the differing overrides are destructors, key-to-index lookup, map clear, getters, a stub and thunks. None touches the payload. The earlier "20 slots, four differ" sentence described the first vtable only and is superseded. Structural identity, **measured** on 226 of 226 slots by `zpt2.exe`: six 64-bit `0x50000000`-relative pointers in the first 64 bytes plus a seventh at `+0xe0`, all targets inside the payload, and the sorted targets partition the payload into seven segments. There is no count field and no record stride. The class-name resolver is the shared one; static enum rows are 19 codes wide and callback rows 52 (`0x1A0`). No payload reader was located: both store vtables were read, neither parses the payload, and no code reading payload `+0x48`, `+0x50` or `+0x80` was found; the base vtable's unimplemented slots are `_purecall` thunks. This is a bounded negative, not an unexamined path.

## Counts

Exact counts from `workspace: coverage_audit/out/tables.md` (`0x48` row; derived census `artifact: type_census.csv`): **226 slots, 8,472,768 stored bytes, 110,748,448 logical bytes**. These agree across the census, the verified type-word join and the slot index (`type_probe inventory`; `artifact: docs/formats/zpt.md`, Verification).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `data.rpf` | 147 | 6,671,616 | 89,105,872 |
| `pack/story000/story000.rpf` | 77 | 1,716,592 | 20,529,552 |
| `pack/story000_restofworld/story000_restofworld.rpf` | 1 | 32,656 | 417,328 |
| `pack/core_restofworld/core_restofworld.rpf` | 1 | 51,904 | 695,696 |
| **Total** | **226** | **8,472,768** | **110,748,448** |

Distribution facts from `artifact: docs/formats/zpt.md` (Counts; `zpt2.exe`): every slot is a resource entry, generation 4 at root and containing header; four archive headers carry 147, 77, 1 and 1 slots; 24 dictionary matches and 202 unresolved hashes, all name hashes distinct; stored 1,776/4,848/9,952/24,928/87,552/1,036,720 (min/p25/median/p75/p95/max), logical 9,088/43,552/97,024/281,456/1,027,312/15,234,336. Logical size takes 221 distinct values over 226 slots, a continuum rather than a small class set; 213 slots are below 1,048,576 bytes logical and 13 are at or above it.

## Container

Verified on 226 of 226 slots by the `zpt2` container pass (0.147 s; earlier `type_probe walk` 0.13 s; `artifact: docs/formats/zpt.md`, Container). Stored `+0x00..+0x0F` are sixteen zero bytes in 226 of 226 and `78 da` sits at `+0x10` in 226 of 226; no slot begins with a bare zlib head. Stream count: 1 stream in 3 slots, 2 in 90, 3 in 87, 4 in 46; 628 streams total, never more than four. Every stream after the first starts at the next 16-byte-aligned stored offset; gaps are 0 at 249 boundaries and 1 to 15 at the rest, with every value 0 to 15 observed. `logical == sum(inflated)` in 226 of 226; the `+16` convention never occurs; zero inflate errors, zero read failures, zero stored-accounting mismatches; `stored == logical` in 0 of 226, so no slot is uncompressed. Exception list empty. First-stream lengths: 8,704/35,824/65,536/196,608/851,968/12,124,160 (min/p25/median/p75/p95/max).

## Fields

Offsets relative to the inflated payload, little-endian, from the 226-slot u64/u32 grid produced by `zpt2.exe` (raw output `artifact: type_reports/out/zpt2_scan.txt`; `artifact: docs/formats/zpt.md`, Fields and Pointer table). Confidence vocabulary is limited to measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence |
|---|---:|---|---|
| `+0x00` | 8 | Zero in 226 of 226 (`zpt2.exe` pattern pass) | measured |
| `+0x08`, `+0x10`, `+0x20`, `+0x28`, `+0x30`, `+0x38` | 8 each | Six `0x50000000`-relative pointers, targets in range in 226 of 226 (`zpt2.exe`) | measured |
| `+0x18` | 8 | Zero in 226 of 226 (`zpt2.exe` pattern pass) | measured |
| `+0xe0` | 8 | Seventh pointer-shaped word, in range in 226 of 226, 225 distinct targets, not block-aligned; lands on a NUL-terminated ASCII identifier in the median sample (`zpt2.exe`). Segment start, not a record-table start; role unknown | unknown |
| `+0x40` | 8 | Optional pointer, present in 72 slots and zero in 154 (`zpt2.exe`) | measured |
| `+0x48` | 4 | `0` in 154, `11` in 43, `29` in 22, `53` in 4, `103` in 2, `211` in 1 (`zpt2.exe`). Meaning unknown | unknown |
| `+0x50` | 4 | 24 distinct small values, `0` in 154 (`zpt2.exe`). Meaning unknown | unknown |
| `+0x80` | 4 | `2` in 199, `3` in 12, `4` in 3 (`zpt2.exe`). Strongly modal but meaning unknown | unknown |

No field name beyond an offset is asserted where no role was decoded. The high `u32` of every pointer is zero, so the unit is a 64-bit word, not a 32-bit grid. No target equals `logical`, so none is an end sentinel; targets are not ascending in header order (0 of 226) and not equally spaced (0 of 226). Sort the seven targets, keep distinct ones, run the last segment to `logical`: the block-count histogram is 7 in 226 of 226 slots. Header extent equals the smallest target, takes 216 distinct values (6,864 min, 59,712 median, 1,591,856 max) and is strictly less than `logical` in 226 slots; it equals the first zlib stream length in 1 slot, is less in 200 and greater in 25. An exhaustive `size = stride*count + c` search over offsets `0..0x100`, `u32` and `u16` halves, k in a fixed set and c in a fixed range, finds no fit above 220 of 226 for either `logical` or `body_len`, and the best near-miss is 1 of 226. Best stride is 4 and divides every segment size in only 93 of 226. Float metrics are reported in `artifact: docs/formats/zpt.md` (Fields), not recomputed here: 27,687,112 words, 71.29 percent exact zero and 87.47 percent `|f| <= 1`.

## Decode status

**Partial, scoped to actual structure.** Decoded and verified: the container on 226 of 226 slots; the seven-pointer table with all targets in range; and the seven-segment partition with header extent equal to the smallest target, on 226 of 226 slots. Not decoded: the record layer, for which a clean negative was measured (no count sizes the payload, no fixed stride divides the segment sizes, and one segment start is a string); element semantics; the roles of `+0x48`, `+0x50` and `+0x80`; the optional pointer at `+0x40`; and the consumer of the parsed asset. The store path is bookkeeping-only and no type-word-to-parser function was found (`artifact: docs/formats/zpt.md`, Decode; `artifact: final_tail_report.md`, Generic resource path). Write status W0; no source proves a writer.

## Verification

All verification steps are listed in `artifact: docs/formats/zpt.md` (Verification): `type_probe inventory artifact: type_census.csv 00000048 out zpt_slots.tsv` (1,255,039 rows, 226 selected); `zpt2.exe artifact: type_reports/out/zpt_slots.tsv <archive-root> artifact: type_reports/out/zpt2_scan.txt` (226 slots, 8,472,768 stored bytes and 110,748,448 logical bytes in 0.147 s: 1,537.1 slots/s, 57.63 stored MB/s, 753.25 logical MB/s), producing the u64 pattern histogram, seven pointer rows, segment histograms, count/stride grids and parse-back check; parse-back reproduces header bytes `0x00..0x3f` exactly from zeros plus six pointers, with full-payload byte equality false at 11,971 mismatching bytes, all inside the header region; PE section map plus capstone one-shots of the initialisers, constructor, resolver and both vtables (each a one-shot Python PE read under 100 lines); a Rust release xref scanner and capstone one-shots for the generic-path negative; and earlier cross-checks (no companion shares a name hash; neither name hash nor stored/logical size is embedded, 0 of 226 each). Counts cross-checked against `workspace: coverage_audit/out/tables.md`. Python was used only for one-shot PE reads; the executable was never executed.

## Unknowns

Source for every bullet in this section: `artifact: docs/formats/zpt.md` (Unknowns and Decode) and `artifact: final_tail_report.md` (generic resource path and the vtable correction).

- What the seven pointers address, and why the header region runs from 6,864 to 1,591,856 bytes before the first target.
- Whether `+0x48`, `+0x50` and the modal `+0x80 = 2` are counts, flags or variant selectors.
- The optional pointer at `+0x40` in 72 of 226 slots and its companion fields.
- The consumer of the parsed asset: no type-word-to-parser function was found, so field roles must come from a consumer not linked from the store object.
- Whether the 13 slots at or above 1,048,576 bytes logical form a separate variant.

## Changelog

- 2026-11-26: compiled from `artifact: docs/formats/zpt.md`, `workspace: coverage_audit/out/tables.md`, `artifact: final_tail_report.md` and `workspace: CONTEXT_HANDOFF.md`. Exact slots/stored/logical taken from the `tables.md` census row, not re-scanned. Grade set to Partial (pointer/segment structure, not semantics) although `tables.md` labels the row Classified with "no payload decoder". The corrected vtable figures (final 19/36, first 13/36) supersede the earlier "20 slots, four differ" claim. Store-registration VAs from the source Exe-path table were withheld; the class name and call-site reference are retained. No index edits, no commit, no publish.
- 2026-11-26 (review): all four `final_tail_report.md` references corrected to `artifact: final_tail_report.md`; rounded container totals replaced by exact census byte totals; count-derived compression ratio removed and the size threshold written as an exact byte value; the header-range paraphrase replaced by its exact endpoints; float percentages attributed as reported; `+0xe0` confidence changed from measured to unknown to match its undecoded role; Unknowns gained explicit source paths. Fields table rechecked at four columns with no unescaped pipe.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zpt.md`. No count was selected by modification time.

