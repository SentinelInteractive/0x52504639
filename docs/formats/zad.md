# `zad` (type code `0x4e`)

Decode scope, stated plainly: this is a container-and-header report, not an end-to-end payload decode. The zlib container is verified on every slot; the root header is decoded to a bounded depth near `0xC0`; the body and its track encoding are not decoded. Header progress is bounded separately in Decode status and is not a body decode. Date 2026-11-26. No key, asset, payload content, matched name or source path is reproduced. Underlying census: `artifact: type_census.csv` (1,255,039 rows), cited only; no census or archive rescan was run for this document.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x4e`. The executable's own type-name table resolves it to variant-0 `zad`, with `iad` and `#ad` as the other two variant strings; the table entry was read from the image bytes (`artifact: docs/formats/zad.md`, Identity and Exe path). No store class, constructor, vtable, RTTI name or handler was located for this word, so **no engine class label is claimed**; the literals `.anim`, `cin@`, `?zad` and `AnimDictionary` do not occur in the 120,181,760-byte image (`artifact: docs/formats/zad.md`, Exe path).

- Structural identity, **verified**: one resource record per slot; the inflated payload carries a single NUL-terminated name string, a literal `.anim` token and long runs of numeric track data; `.anim` occurs in 25,608 of 25,608 slots (`artifact: docs/formats/zad.md`, Verification, literal scan).
- Semantic identity, **inferred**: a named animation-clip payload with float track data. The metadata-table, placement-dictionary and localisation-blob readings were measured and rejected (`artifact: docs/formats/zad.md`, Verification). The word "dictionary" in the label is not supported by the payload: there is one clip object per slot, not a keyed set (`artifact: docs/formats/zad.md`, Identity).

Grade: **Partial**, scope = container plus the `0xC0`-byte root header, body and track layout open (`artifact: docs/formats/zad.md`, Decode; `workspace: CONTEXT_HANDOFF.md` §9). The coverage snapshot `coverage_audit/out/tables.md` row `0x4e` carries the coarser label Classified with note "Name and count verified; no payload decoder"; that label is recorded here, not silently adopted, because the detailed report measures the container and header on 100 percent of the population (`artifact: docs/formats/zad.md`, Verification).

## Counts

Authoritative totals are transcribed from `coverage_audit/out/tables.md`, row `0x4e`; `artifact: type_census.csv` is the underlying census and was not rescanned.

| Code | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `0x4e` | 25,608 | 1,275,304,768 | 1,717,098,288 |

Per-root split, from the type report (`artifact: docs/formats/zad.md`, Counts):

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `pack/story000/story000.rpf` | 25,341 | 1,263,722,656 | 1,700,950,704 |
| `pack/story000_restofworld/story000_restofworld.rpf` | 267 | 11,582,112 | 16,147,584 |
| **Total** | **25,608** | **1,275,304,768** | **1,717,098,288** |

The two passes that agree are a Rust whole-census aggregation and a Rust re-read of the per-slot scan (`artifact: docs/formats/zad.md`, Counts). Header generation 4 and root generation 4 hold in 25,608 slots; every slot is a `Resource` entry (`artifact: docs/formats/zad.md`, Counts). Name origins: 25,483 unresolved hashes and 125 dictionary matches, each matched path used by exactly one slot, paths not reproduced (`artifact: docs/formats/zad.md`, Counts). Logical size ranges from 688 B to 1,860,256 B with median 10,928 B (`artifact: docs/formats/zad.md`, Counts). Four slots resolve to variant-2 `#dr` labels and are ordinary members by size and layout (`artifact: docs/formats/zad.md`, Counts).

## Container

All statements in this section are measured on 25,608 of 25,608 slots (`artifact: docs/formats/zad.md`, Container and Verification):

- Stored `+0x00..+0x0F` are sixteen zero bytes; stored `+0x10` begins a zlib stream with header `0x78DA`: 25,608 of 25,608.
- The chain rule is `logical == sum(inflated stream lengths)`. It holds on 25,606 of 25,608. The two exceptions are short by exactly 16 bytes (131,088 against 131,072 and 196,624 against 196,608); the shortfall is unexplained and a page-boundary or footer accounting artefact is a working hypothesis, not a finding.
- Stream count: one stream in 21,876 slots, two in 3,732, none with three. Inter-stream padding is 0 to 15 bytes and every stream start is 16-byte aligned (0 unaligned starts in 169,337 slots across the batch); 253 of 3,732 boundaries carry no padding.
- A zero run before the end of the stored range occurs in 24,009 slots, also 0 to 15 bytes. Stored accounting is `stored = 16 + sum(compressed extents) + sum(padding) + trailing`.
- The alternative formulas `16 + sum(streams) + padding == logical` (0 of 25,608) and `sum + padding == logical` (22,127 of 25,608) were tested and rejected (`artifact: docs/formats/zad.md`, Verification). First-inflated-stream sizes in the census tables are truncated at 32 KiB and are not stream sizes (`artifact: docs/formats/zad.md`, Verification).

## Fields

Offsets are relative to the first inflated byte; integers little-endian. Population counts come from the first inflated stream of every slot, so fields beyond the first 32 KiB are covered only where that stream reaches them (`artifact: docs/formats/zad.md`, Fields). Confidence vocabulary is strictly `measured`, `inferred`, `external`, `unknown`. Every Meaning cell names its source artifact.

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00` | u64 | Zero in 25,608 of 25,608 slots (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x08` | u32 | Relative pointer `0x50000000 + offset`, resolves inside the inflated buffer in 25,608 of 25,608; target is a named record (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x10`–`+0x30` | 8 × u32 | Zero in 25,608 of 25,608 (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x38` | u32 | Relative pointer; target begins with a NUL-terminated printable string in 25,608 of 25,608; remaining region 64 to 129,568 bytes (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x40` | u16 | Count 24–64 with 41 distinct values; whether it is a channel count is not established (`artifact: docs/formats/zad.md`, Fields) | unknown |
| `+0x42` | u16 | Equals `+0x40` + 1 in 25,608 of 25,608, a capacity identity (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x44` | u32 | 1 in 25,608 of 25,608 (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x48` | u32 | Relative pointer; resolves in 25,608 of 25,608; remaining region 176 to 129,680 bytes (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x50` | u32 | 11 in 25,567 slots, 29 in 41; meaning not established (`artifact: docs/formats/zad.md`, Fields) | unknown |
| `+0x54` | u32 | Zero in 25,608 (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x58` | u32 | Small count 1–21; whether it is a track count is not established (`artifact: docs/formats/zad.md`, Fields) | unknown |
| `+0x5c` | u32 | `0x01000000` in 25,608 of 25,608 (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x60` | u64 | Zero in 25,608 (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x68` | u32 | 25,608 distinct values in 25,608 slots; hash role inferred, not established (`artifact: docs/formats/zad.md`, Fields) | inferred |
| `+0x6c` | u32 | Zero in 25,608 (`artifact: docs/formats/zad.md`, Fields) | measured |
| `+0x70` | u32 | High entropy, 288 zeros; largest groups 114 and 50 slots; role unknown (`artifact: docs/formats/zad.md`, Fields) | unknown |
| `+0x74`–`+0x8c` | u32 × 7 | Mixed small offsets and hash-like words; `+0x78` is 0 in 25,584 and 4 in 24 (`artifact: docs/formats/zad.md`, Fields) | unknown |
| `+0x88` | u32 | Zero in 11,731 slots, otherwise multiples of 4 (`artifact: docs/formats/zad.md`, Fields) | measured |
| `≥0x90` | floats / u16 | 113,943 words equal `1.0f` population-wide; quaternion-like constants such as 0.707107 appear; record layout unknown (`artifact: docs/formats/zad.md`, Fields) | unknown |

No frame-count / duration / frame-rate triple occurs at any population-stable offset among `+0x40`, `+0x44`, `+0x50`, `+0x58`, `+0x5c`, `+0x68` or `+0x70`–`+0x8c`; frame-rate tokens occur 0, 1 and 0 times (`artifact: docs/formats/zad.md`, Fields).

## Decode status

- Container: **decoded and verified** on 25,608 of 25,608 slots with the two 16-byte logical shortfalls recorded above (`artifact: docs/formats/zad.md`, Decode).
- Root header: **decoded and verified** to roughly `0xC0`, including the three relative pointers at `+0x08`, `+0x38` and `+0x48`, the count/capacity pair at `+0x40/+0x42`, the version word at `+0x44` and the constant at `+0x5c` (`artifact: docs/formats/zad.md`, Decode).
- Beyond `0xC0`: **not decoded**. The former description of this point as a per-channel record array is withdrawn as unproven; no global stride has been established and no clip can be walked to its end (`artifact: docs/formats/zad.md`, Decode).
- Local pattern: a Rust probe on a 103,008-byte inflated sample found 128 candidate triples at `0x1f0` on `0x0c` spacing under a permissive predicate (`zad_stride.exe trip`, source `artifact: docs/formats/zad.md`, Follow-up). This supports a local 12-byte pattern, not a keyframe record; the roughly `0x48`-byte record near `0x148` was withdrawn. In a separate 832-byte sample, four pointer-shaped words at `0x1d8`, `0x1f0`, `0x210` and `0x220` resolve to in-buffer offsets `0`, `0x290`, `0x338` and `0x140`, inconsistent with a uniform numeric array but not identifying objects (`artifact: docs/formats/zad.md`, Follow-up).
- Grade **Partial**, scope = container and root header only (`artifact: docs/formats/zad.md`, Decode and Encode). Write status **W0**, extract-only: no encoder, no re-pack, no byte-stable round trip; the obstacle is the unverified clip record layout, not the zlib container (`artifact: docs/formats/zad.md`, Encode).

## Verification

All commands and figures below are from Rust release artifacts recorded in `artifact: docs/formats/zad.md`, Verification and Follow-up; nothing was re-run for this document.

- Whole-census reconciliation: 312,661,753 bytes and 1,255,039 rows in 1.1 s (284 MB/s, 1.14 M rows/s); per-type totals reproduce 25,608 / 1,275,304,768 / 1,717,098,288 and package totals 305,820,985,968 stored / 564,783,265,279 logical.
- Population chain walk: 79.7 s over all 169,337 slots of the batch (about 1,760 slots/s); `sum(inflated) == logical` on 25,606 of 25,608, stream histogram 1→21,876 and 2→3,732, zero unaligned starts.
- Population verifier: 1.4 s for the type (about 1.2 GB/s), re-inflating every slot and asserting prefix, zlib header, `u64@0 == 0` and the `+0x08` pointer range: 25,608 of 25,608 on each.
- Literal scan: `.anim` in 25,608 slots, 38,184 occurrences, 1 to 21 per slot; the clip-name token appears exactly once in 25,608 slots.
- Root-record walk: 25,608 of 25,608 pass the full assertion set (`u64@0 == 0`, three resolving pointers, `capacity == count + 1`, `u32@0x44 == 1`, `u32@0x5c == 0x01000000`, at least one name string, every aligned `0x50000000 + offset` header word in range).
- Stratified samples: smallest 880 B, median 10,928 B, largest 1,860,256 B, one slot per root and one `#dr` slot; all eight inflated to exactly `logical`.
- `zad_stride.exe trip` on the existing full 103,008-byte sample, starting at offset zero (`artifact: docs/formats/zad.md`, Follow-up); the predicate is permissive and no independent semantic decoder validated it.

## Unknowns

1. Record stride and channel layout beyond `0xC0`; cheapest next probe is to diff two slots with the same `+0x40` count and test `count × stride + header` against the `+0x48` region length (`artifact: docs/formats/zad.md`, Unknowns).
2. Whether `+0x40` (24–64) and `+0x58` (1–21) are channel and track counts (`artifact: docs/formats/zad.md`, Unknowns).
3. Meaning of the per-slot words at `+0x68` and `+0x70`, including whether either hashes the clip name (`artifact: docs/formats/zad.md`, Unknowns).
4. The 16-byte logical shortfall in the two exception slots (`artifact: docs/formats/zad.md`, Container).
5. Any handler, vtable or RTTI name on the executable side (`artifact: docs/formats/zad.md`, Exe path).
6. Grade reconciliation: `coverage_audit/out/tables.md` labels this code Classified ("no payload decoder") while `artifact: docs/formats/zad.md` and `workspace: CONTEXT_HANDOFF.md` §9 label it Partial with container and header scope; the discrepancy is recorded, not resolved by a new scan.

## Changelog

- 2026-11-26: created `artifact: docs_complete/zad.md` by consolidating `artifact: docs/formats/zad.md`, `workspace: CONTEXT_HANDOFF.md` and `coverage_audit/out/tables.md`; counts transcribed from the latter, `artifact: type_census.csv` cited as underlying census. No index edit, no commit, no publish, no rescan. Language: no new code; read-only PowerShell text inspection of source artifacts only. Write status unchanged at W0; grade recorded as Partial with the Classified snapshot noted above.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zad.md`. No count was selected by modification time.

