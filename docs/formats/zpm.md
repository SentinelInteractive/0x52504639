# `zpm` (type code `0x46`)

Decode scope, stated plainly: this is a container-and-header report. The zlib container, the header field inventory, the count/capacity pair, the pointer set and the 32-bit identifier are verified on every slot; a companion identifier equality is verified on 729 pairs. There is no global record stride and the record array is not decoded. Header progress is bounded separately in Decode status and is not a body decode. Date 2026-11-26. No key, asset, payload content, matched name or source path is reproduced. Underlying census: `artifact: type_census.csv` (1,255,039 rows), cited only; no census or archive rescan was run for this document.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x46`. The executable's type-name table at `0x1462fcd30 + variant*0x98 + code*8` resolves it to `zpm` (variant 0) and `ipm` (variant 1) (`artifact: docs/formats/zpm.md`, Identity and Exe path). The word is registered by a verified PE read: `lea rdx,["MotionStore"]` at `0x145b54eac`, `mov r8d,0x46` at `0x145b54eb3`, `call 0x1419ca0b0` (`artifact: docs/formats/zpm.md`, Identity and Exe path). `MotionStore` is the only engine label claimed here, and it is verified by image bytes.

- Structural identity, **verified**: a fixed header of at least 0x120 bytes followed by variable-length data; a `(count, capacity)` u16 pair at `+0x40/+0x42` with `capacity == count + 1` in 8,443 of 8,443 slots; six `0x50000000`-relative pointers resolving inside the payload in 8,443 of 8,443; a high-entropy 32-bit identifier at `+0x68` distinct in all 8,443 slots (`artifact: docs/formats/zpm.md`, Identity).
- Every payload contains the literal path-scheme token `pack:/` in 8,443 of 8,443 slots and none contains `.anim` in 0 of 8,443; the companion animation-clip type `zad` is the reverse with `.anim` in 25,608 of 25,608 (`artifact: docs/formats/zpm.md`, Identity).
- Companion, **verified**: exactly one other type shares this population's name hashes, `0x43` `zcd` (`ClipStore`), with 729 slots by 64-bit name hash and 68 of those by name string; no hash is shared by two `zcd` slots. Re-inflating all 729 pairs shows the 32-bit word at `+0x68` equal on both sides in 729 of 729 pairs with 729 distinct values (`artifact: docs/formats/zpm.md`, Identity; `verify idpair` in Verification).
- Semantic identity, **inferred**: a motion or movement record referencing external assets by path and carrying numeric parameters, paired with an animation clip of the same name. The payload was searched for key times, quaternions and radian channels and all three signatures were ruled out by measured counts (`artifact: docs/formats/zpm.md`, Identity and Decode).

Grade: **Partial**, scope = container, header inventory, count/capacity identity, pointer set and shared identifier; record array and key semantics open (`artifact: docs/formats/zpm.md`, Decode; `workspace: CONTEXT_HANDOFF.md` §9). `coverage_audit/out/tables.md` row `0x46` carries the coarser Classified note "Name and count verified; no payload decoder"; it is recorded here, not silently adopted, because the detailed report measures the header on 100 percent of the population.

## Counts

Authoritative totals are transcribed from `coverage_audit/out/tables.md`, row `0x46`; `artifact: type_census.csv` is the underlying census and was not rescanned.

| Code | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `0x46` | 8,443 | 38,500,896 | 204,265,984 |

Per-root split, from the type report (`artifact: docs/formats/zpm.md`, Counts):

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `anim.rpf` | 8,440 | 38,471,568 | 204,184,160 |
| `story000` | 3 | 29,328 | 81,824 |
| **Total** | **8,443** | **38,500,896** | **204,265,984** |

The verified type-word join, the registry and the census agree on all three numbers (`artifact: docs/formats/zpm.md`, Counts). Every slot is a resource entry; roots and containing headers are generation 4; the population sits in 67 distinct headers, the largest with 1,406 slots (`artifact: docs/formats/zpm.md`, Counts). Name origins: 725 dictionary matches and 7,718 unresolved hashes; all 8,443 name hashes are distinct (`artifact: docs/formats/zpm.md`, Counts). Stored sizes run 400 to 1,334,288 bytes and logical sizes 1,536 to 8,589,696 bytes, with means of 4,560.1 and 24,193.5 bytes (`artifact: docs/formats/zpm.md`, Counts).

## Container

All statements in this section are measured on 8,443 of 8,443 slots (`artifact: docs/formats/zpm.md`, Container):

- Stored `+0x00..+0x0F` are sixteen zero bytes and stored `+0x10` begins a zlib stream (`78 da` in every slot).
- One stream in 8,017 slots, two in 426. Where there are two, the second begins at the next 16-byte-aligned stored offset with a measured gap of 0 to 15 bytes. No rule was found for the 426 two-stream splits; the container admits them but the cause is unknown.
- `logical == sum(inflated)` on 8,443 of 8,443 slots; zero inflate errors (`artifact: docs/formats/zpm.md`, Container).

## Fields

Offsets are relative to the inflated payload; integers little-endian; denominator 8,443 slots (`artifact: docs/formats/zpm.md`, Fields). The full grid is in `artifact: type_reports/out/zpm_fields.txt`. Confidence vocabulary is strictly `measured`, `inferred`, `external`, `unknown`. The table has exactly four columns and every Meaning cell names its source artifact.

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00`, `+0x04`, `+0x0c`, `+0x10..+0x34`, `+0x3c`, `+0x4c`, `+0x54`, `+0x60`, `+0x64`, `+0x6c`, `+0x74`, `+0x7c`, `+0x84`, `+0x8c`, `+0x98`, `+0x9c`, `+0xa4`, `+0xac` | 4 | Zero in all slots at 27 offsets (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x08`, `+0x38`, `+0x48`, `+0x70`, `+0x80`, `+0xa0`, `+0x100`, `+0x108` | 4 | `0x50000000`-relative virtual pointer in range in all slots; pointer shape verified, target class undecoded (`artifact: docs/formats/zpm.md`, Fields) | unknown |
| `+0x18`-class u64s | 8 | Pointer or zero; `0x500000b0` recurs 7,381 times at `+0xa0` and 5,026 times at `+0x100`, a shared default sub-record is the working reading (`artifact: docs/formats/zpm.md`, Fields) | inferred |
| `+0x40` | 2 | `count`, range 20 to 114, median 74 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x42` | 2 | `capacity`, equal to `count + 1` in 8,443 of 8,443 slots (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x44` | 4 | `1` in all slots (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x50` | 4 | Small enum `0x0b` in 8,255 slots, `0x1d` in 186, `0x67` in 1, `0x35` in 1; meaning unknown (`artifact: docs/formats/zpm.md`, Fields) | unknown |
| `+0x58` | 4 | Partial histogram of a small counter: `1` in 5,853 slots, `2` in 959, `3` in 679, `4` in 292, `5` in 96 and `6` in 133, which sums to 8,012 of 8,443; the source does not itemise the remaining 431 slots, so values 1 to 6 are not asserted as exhaustive (`artifact: docs/formats/zpm.md`, Fields) | unknown |
| `+0x5c`, `+0x94` | 4 | `0x01000000` in all slots (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x68` | 4 | High-entropy 32-bit identifier, 8,443 distinct values, never zero; equal to the `zcd` twin's `+0x68` in 729 of 729 pairs (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x78` | 4 | Two equal u16 halves: `0001 0001` in 4,466 slots, `0002 0002` in 1,597, then 3/577, 4/428, 5/275, 6/169; the pair repeats at `+0x90` as two u32 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x88` | 4 | Small enum `0x0b` in 7,830 slots, `0x1d` in 544, `0x35` in 66, `0x67` in 3 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x90` | 4 | 1 to 6, matching the halves at `+0x78` (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0xa8` | 4 | Small counts, 464 in 381 slots, 720 in 246, 480 in 231, 1,084 in 185 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0xc8` | 4 | `3` in 6,537 slots, `5` in 469, `4` in 375, `0` in 24 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0xd0` | 4 | `8` in 5,026 slots, `56` in 2,355, `0` in 24 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0xf8` | 4 | `1` in 6,267 slots, `392` in 522, `408` in 249, `440` in 212 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x110` | 4 | `0xffff0001` in 5,026 slots, zero in 2,355, scattered otherwise; a sentinel pair (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x120` | 4 | `1` in 5,087 slots, zero in 1,267, `2` in 371, `4` in 185 (`artifact: docs/formats/zpm.md`, Fields) | measured |
| `+0x160` | 4 | `0xbcd351dd` in 4,198 slots, `1` in 2,347, `0x32b4a037` in 656; high entropy, meaning unknown (`artifact: docs/formats/zpm.md`, Fields) | unknown |
| `+0x1e8` | 4 | `0x40` in 3,804 slots, zero in 2,379, `0xffff0001` in 828 (`artifact: docs/formats/zpm.md`, Fields) | measured |

The `+0x40/+0x42` idiom is the same count/capacity pair documented for `zad`, with a different range (20 to 114 here, 24 to 64 there); that is a header-family resemblance, **inferred**, and the objects counted are not identified (`artifact: docs/formats/zpm.md`, Fields).

## Decode status

- Container: **decoded and verified** on 8,443 of 8,443 slots (`artifact: docs/formats/zpm.md`, Decode).
- Header field inventory: **decoded and verified**; constants, count/capacity pair, pointer set and identifier measured on 100 percent of the population (`artifact: docs/formats/zpm.md`, Decode).
- Header semantics: **partially inferred**; the count is a count, but what it counts is unknown (`artifact: docs/formats/zpm.md`, Decode).
- Record array: **not decoded**. The greatest common divisor of all 8,443 logical sizes is 16 and only 4, 8 and 16 divide every slot (32 divides 4,115, 48 divides 2,826, 64 divides 2,100). A residual test with header at `0x120` and stride 12 divides only 2,826 slots and its three residual classes are simply the `logical mod 16` classes (`artifact: docs/formats/zpm.md`, Decode).
- Key semantics: **not decoded**. Float tests from offset `0x120` over 50,458,600 words: 49,627,620 finite (98.353 percent), 36,921,640 finite non-zero with `|f| < 1e4` (73.172 percent), 576,436 within `1e-6` of `1.0f` (1.142 percent). Only 4,850 of 355,883 contiguous float runs of length at least 4 are strictly increasing and 2,060 are decreasing. Four-word quaternion test: 2,878 of 939,840 quartets (0.306 percent) have squared norm within 0.01 of 1. There is no monotone time axis, no quaternion array and no radian-angle support (`artifact: docs/formats/zpm.md`, Decode). The floats are normalised parameters, plausibly weights or blend factors; keyframes, quaternions and angle channels are ruled out by counts, not opinion (`artifact: docs/formats/zpm.md`, Decode).
- Grade **Partial**, scope = container and header; record array and key semantics open (`artifact: docs/formats/zpm.md`, Decode). Write status **W0**: no encoder, no pack-back test and no game-load test; the container could be re-emitted but the array stride, the count's referent and the sending of pointers are unresolved (`artifact: docs/formats/zpm.md`, Encode).

## Verification

All commands and figures below are from Rust release artifacts recorded in the cited source; nothing was re-run for this document.

- `type_probe inventory artifact: type_census.csv 00000046 out` — 1,255,039 census rows, 8,443 selected, 0.21 s (`artifact: docs/formats/zpm.md`, Verification).
- `type_probe walk out\zpm_slots.tsv <archive-root> out\zpm_walk.txt 256 288` — 8,443 slots in 0.75 s (11,254 slots/s, 272 MB/s logical) (`artifact: docs/formats/zpm.md`, Verification).
- `verify hdrlen` — 8,443 slots in 0.47 s, 18,111 slots/s: one stream in 8,017, two in 426 (`artifact: docs/formats/zpm.md`, Verification).
- `verify idpair out\zpm_slots.tsv <archive-root> 104 104 00000043 artifact: type_census.csv` — 62,384 `zcd` rows indexed, 729 pairs re-inflated in 1.05 s, 8,023 slots/s, 729/729 equal and 729 distinct values (`artifact: docs/formats/zpm.md`, Verification).
- `paircheck artifact: type_census.csv` — 1,255,039 rows in 2.32 s; the 729 pairings are unambiguous (`artifact: docs/formats/zpm.md`, Verification).
- `zpm_probe fields|body|floats|floatrun|tracks|tokens|pair|pair2` — 21,260 slots/s for fields, 15,078 slots/s for body (365 MB/s), 5,501 slots/s for 50.5 M words, 10,866 slots/s for tokens, 915 pairs/s for the twin test (`artifact: docs/formats/zpm.md`, Verification).
- `exe_stores` — PE read only (`artifact: docs/formats/zpm.md`, Verification).
- The executable was never loaded or executed; no Python was used (`artifact: docs/formats/zpm.md`, Verification).

## Unknowns

1. The header boundary and the meaning of the six pointer targets (`artifact: docs/formats/zpm.md`, Unknowns).
2. What `u16@+0x40` counts, despite its measured range of 20 to 114 (`artifact: docs/formats/zpm.md`, Unknowns).
3. Any population-wide record stride; the 12-byte and 0x48-byte sentinel runs cover 6,287 and 2,902 slots respectively and divide nothing globally (`artifact: docs/formats/zpm.md`, Unknowns).
4. Why `+0x68` is shared with the `zcd` twin; a common clip identifier is the working hypothesis and is unverified (`artifact: docs/formats/zpm.md`, Unknowns).
5. What causes 426 slots to carry a second stream (`artifact: docs/formats/zpm.md`, Unknowns).
6. What the `pack:/` token addresses and whether the referenced paths are external or internal to the package (`artifact: docs/formats/zpm.md`, Unknowns).
7. The `0x46` reader and any handler behind the registration; no vtable, constructor or handler was located (`artifact: docs/formats/zpm.md`, Unknowns and Exe path).
8. Grade reconciliation: `coverage_audit/out/tables.md` row `0x46` says Classified while the detailed report and this document say Partial with a bounded scope.
9. The residual 431 slots in the partial `+0x58` histogram are not itemised by the source; the counter's full value range is therefore unknown (`artifact: docs/formats/zpm.md`, Fields).

Next checks, in order: resolve whether the `+0x68` identifier is a hash of the resource name using the 725 matched slots; then decode one header pointer target to classify the sub-record class (`artifact: docs/formats/zpm.md`, Unknowns).

## Changelog

- 2026-11-26: created `artifact: docs_complete/zpm.md` by consolidating `artifact: docs/formats/zpm.md`, `workspace: CONTEXT_HANDOFF.md` and `coverage_audit/out/tables.md`; counts transcribed from the coverage table, `artifact: type_census.csv` cited as underlying census. No index edit, no commit, no publish, no rescan. Language: no new code; read-only PowerShell text inspection of source artifacts only. Fields table has exactly four columns with source artifacts in Meaning. Write status unchanged at W0; grade Partial with header scope and the record array open. The `+0x58` histogram is presented as partial with an unknown residual of 431 slots. A concurrent draft with a five-column field table, an undefined grade label and a self-attributed census rerun was superseded by this version on the parent's explicit audit finding.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zpm.md`. No count was selected by modification time.

