# `zbdd` (type code `0x10`)

Decode scope, stated plainly: this is a container-and-header report with a decoded index and pointer array; the payload's element semantics are not decoded. The zlib container, the 64-byte header, the ascending 32-bit value index and the in-range pointer array are verified on every slot. The 0x20-byte records behind the pointers are measured but not interpreted, and no spatial structure was found despite the store class name. Header progress is bounded separately in Decode status and is not a claim about element meaning. Date 2026-11-26. No key, asset, payload content, matched name or source path is reproduced. Underlying census: `artifact: type_census.csv` (1,255,039 rows), cited only; no census or archive rescan was run for this document.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x10`. The executable's type-name table at `0x1462fcd30 + variant*0x98 + code*8` resolves it to `zbdd` (variant 0) and `ibdd` (variant 1); a variant-2 label was not located and none is claimed (`artifact: docs/formats/zbdd.md`, Identity and Exe path). The word is registered by a verified PE read: `lea rdx,["BvhDwdStore"]` at `0x145b92bdc`, `mov r8d,0x10` at `0x145b92be3`, `call 0x1419ca0b0` (`artifact: docs/formats/zbdd.md`, Identity and Exe path). `BvhDwdStore` is the only engine label claimed here, and it is verified by image bytes rather than inferred from payload content.

- Structural identity, **verified**: a fixed 64-byte header carrying a `(count, count)` pair, an ascending 32-bit value index of exactly `count` entries and a `count`-entry pointer array whose targets are 0x20-byte records beginning with two zero words (`artifact: docs/formats/zbdd.md`, Identity and Decode).
- Relation, **verified**: all 22,382 slots share their 64-bit name hash with a `0x04` `zdd` slot, and the pairing is a strict one-to-one bijection with 22,382 distinct hashes, one twin each and no hash shared by two slots (`artifact: docs/formats/zbdd.md`, Identity; `paircheck` result in Verification). Two slots carry a resolvable name, so the 100 percent is hash-based, not name-based.
- Interpretation, **inferred**: a per-asset lookup table over the named entries of its `zdd` twin, keyed by a 32-bit hash. The measured overlap is 62.753 percent of probed index values found verbatim in the twin's payload; what the hashes denote is not established (`artifact: docs/formats/zbdd.md`, Identity and Decode).
- The class name was not taken as the answer: every payload was tested for a spatial structure and none was found. The addressed records hold no coordinate or bounds data, no finite float field exists in the population, and every pointer-array target begins with two zero words (`artifact: docs/formats/zbdd.md`, Identity and Decode). The contradiction is recorded as open, not resolved.

Grade: **Partial**, scope = container, header, value index, pointer array and one-to-one companion relation; element semantics open (`artifact: docs/formats/zbdd.md`, Decode; `workspace: CONTEXT_HANDOFF.md` §9). `coverage_audit/out/tables.md` row `0x10` carries the coarser Classified note "Name and count verified; no payload decoder"; it is recorded here, not silently adopted, because the detailed report measures the container and arrays on 100 percent of the population.

## Counts

Authoritative totals are transcribed from `coverage_audit/out/tables.md`, row `0x10`; `artifact: type_census.csv` is the underlying census and was not rescanned.

| Code | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `0x10` | 22,382 | 3,591,712 | 8,019,200 |

Per-root split, from the type report (`artifact: docs/formats/zbdd.md`, Counts):

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `core_bvh4` | 22,301 | 3,581,296 | 7,996,832 |
| `shared_minigame000_bvh4` | 81 | 10,416 | 22,368 |
| **Total** | **22,382** | **3,591,712** | **8,019,200** |

The verified type-word join, the registry and the census agree on all three numbers, each equal to the sum of the per-root rows (`artifact: docs/formats/zbdd.md`, Counts). Every slot is a resource entry; roots and containing headers are generation 4; the population sits in 132 distinct archive headers, the largest with 2,152 slots (`artifact: docs/formats/zbdd.md`, Counts). Name origins: 2 dictionary matches and 22,380 unresolved hashes; all 22,382 name hashes are distinct (`artifact: docs/formats/zbdd.md`, Counts). Stored sizes run 80 to 3,648 bytes and logical sizes 160 to 10,096 bytes, with means of 160.5 and 358.3 bytes (`artifact: docs/formats/zbdd.md`, Counts).

## Container

All statements in this section are measured on 22,382 of 22,382 slots (`artifact: docs/formats/zbdd.md`, Container):

- Stored `+0x00..+0x0F` are sixteen zero bytes and stored `+0x10` begins a zlib stream (`78 da` in every slot).
- Every slot holds exactly one stream, with no alignment padding because there is no second stream.
- `logical == sum(inflated)` on 22,382 of 22,382 slots; zero inflate errors. This is the `zfid` convention and the `zft`/`zdd` convention minus the 16-byte prefix term: `zft` measured `logical == sum + 16` (`artifact: docs/formats/zbdd.md`, Container).
- No stream exceeds 10,096 decoded bytes, so every statement below is a whole-population statement, not a sample (`artifact: docs/formats/zbdd.md`, Container).

## Fields

Offsets are relative to the inflated payload; integers little-endian; counts are out of 22,382 slots (`artifact: docs/formats/zbdd.md`, Fields). Confidence vocabulary is strictly `measured`, `inferred`, `external`, `unknown`. Every Meaning cell names its source artifact. The table has exactly four columns.

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00` | 4 | Zero in all slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x04` | 4 | Zero in all slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x08` | 4 | Virtual pointer (`0x500000e0`, `0x50000060`, `0x50000080`, …) in range in all slots; target class not decoded (`artifact: docs/formats/zbdd.md`, Fields) | unknown |
| `+0x0c` | 4 | Zero in all slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x10` | 8 | Zero in all slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x18` | 8 | `1` in all slots; meaning unknown (`artifact: docs/formats/zbdd.md`, Fields) | unknown |
| `+0x20` | 4 | Virtual pointer to the value index (`artifact: docs/formats/zbdd.md`, Fields and Decode) | measured |
| `+0x24` | 4 | Zero in all slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x28` | 2 | `count`, equal to the index length and the pointer-array length in 22,382 of 22,382 slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x2a` | 2 | Equal to `+0x28` in all slots; zero above the two u16 (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x2c` | 4 | Zero in all slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x30` | 4 | Virtual pointer to the pointer array (`artifact: docs/formats/zbdd.md`, Fields and Decode) | measured |
| `+0x34` | 4 | Zero in all slots (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x38` | 8 | Repeats the `(count, count)` pair of `+0x28` (`artifact: docs/formats/zbdd.md`, Fields) | measured |
| `+0x40..+0x9f` | 8 each | A run of u64s that is either zero or a virtual pointer; target class not decoded (`artifact: docs/formats/zbdd.md`, Fields) | unknown |
| `+0xa0` and higher | — | In the largest slots the `+0x08`-class pointers repeat at higher offsets, one per sub-structure; sampled only (`artifact: docs/formats/zbdd.md`, Fields) | unknown |
| index at the `+0x20` target | 4 each | Exactly `count` strictly ascending u32 values, 130,496 in total and 105,112 distinct (`artifact: docs/formats/zbdd.md`, Decode) | measured |
| pointers at the `+0x30` target | 8 each | Exactly `count` in-range targets, 0 of 130,496 out of range, first word zero at every target (`artifact: docs/formats/zbdd.md`, Decode) | measured |
| index semantics | — | Per-asset hash over the `zdd` twin is a reading, not a decode (`artifact: docs/formats/zbdd.md`, Identity and Decode) | inferred |

The count distribution over the whole population is `4` in 11,982 slots, `1` in 3,904, `2` in 1,979, `16` in 847, `3` in 645, `8` in 354, `5` in 301, `6` in 292, with a tail up to 227 (`artifact: docs/formats/zbdd.md`, Fields). The 160-byte smallest slot was partitioned byte for byte into a 64-byte header, 32-byte descriptor, 16-byte root record, 16 bytes of padding and the pointer and index arrays with their own padding, with zero unaccounted bytes (`artifact: docs/formats/zbdd.md`, Fields; `zbdd_probe struct`).

## Decode status

- Container: **decoded and verified** on the whole population (`artifact: docs/formats/zbdd.md`, Decode).
- Header and count field: **decoded and verified**; `count` sizes both arrays in 22,382 of 22,382 slots (`artifact: docs/formats/zbdd.md`, Decode).
- Value index: **decoded and verified**; the array at the `+0x20` target holds exactly `count` 32-bit values, strictly ascending at a 4-byte step in 22,382 of 22,382 slots, so no value repeats inside a slot. There are 130,496 index values in total, of which 105,112 are distinct across the population (`artifact: docs/formats/zbdd.md`, Decode).
- Pointer array: **decoded and verified**; exactly `count` entries at the `+0x30` target, every target inside the payload (0 of 130,496 out of range), and the first 32-bit word at every one of the 130,496 targets is zero (`artifact: docs/formats/zbdd.md`, Decode).
- Element semantics: **not decoded**. What the 32-bit values denote is unknown and the 0x20-byte descriptor's remaining words are not interpreted (`artifact: docs/formats/zbdd.md`, Decode).
- Companion test, **verified**: 500 hash-paired `zdd` twins were re-inflated; every pair has at least one index value found verbatim in the twin, 2,170 of 3,458 probed values match (62.753 percent), and in an inspected pair 28 consecutive index values appear at twin offsets spaced exactly 0x20 apart in ascending order (`artifact: docs/formats/zbdd.md`, Decode).
- Negative results: no spatial BVH in the sense of `zbdr`, and the index is not the slot's name hash because the values are 32-bit and the 64-bit TOC hash appears in neither half (`artifact: docs/formats/zbdd.md`, Decode).
- Grade **Partial**, scope = container, header, index, pointer array and companion relation; element semantics and the descriptor layout open (`artifact: docs/formats/zbdd.md`, Decode). Write status **W0**: a writer could be built from the field map alone, but the descriptor semantics, padding rule and zlib parameters are unestablished and no round trip was attempted (`artifact: docs/formats/zbdd.md`, Encode).

## Verification

All commands and figures below are from Rust release artifacts recorded in the cited source; nothing was re-run for this document.

- `type_probe inventory artifact: type_census.csv 00000010 out` — 1,255,039 census rows, 22,382 selected, 0.24 s (`artifact: docs/formats/zbdd.md`, Verification).
- `type_probe walk out\zbdd_slots.tsv <archive-root> out\zbdd_walk.txt 256 288` — 22,382 slots in 0.20 s (61,634 slots/s, 22.1 MB/s logical) (`artifact: docs/formats/zbdd.md`, Verification).
- `verify zbddidx out\zbdd_slots.tsv <archive-root>` — 22,382 slots in 0.20 s, 112,967 slots/s; produced the ascending-index result, the 130,496/105,112 value counts, the 130,496 in-range pointer targets and the all-zero first word (`artifact: docs/formats/zbdd.md`, Verification).
- `paircheck artifact: type_census.csv` — 1,255,039 rows in 2.32 s, 540,157 rows/s; proved the `zbdd`↔`zdd` pairing is one-to-one with no ambiguity (`artifact: docs/formats/zbdd.md`, Verification).
- `zbdd_probe fields|struct|verify|zdd|zdetail` — 0.40 s for the whole population (56,361 slots/s, 20.2 logical MB/s) for the field pass; 44 pairs/s and 51.7 MB/s for the twin test (`artifact: docs/formats/zbdd.md`, Verification).
- `exe_stores` — PE read only; produced the registration row and the class string (`artifact: docs/formats/zbdd.md`, Verification).
- The executable was never loaded or executed; no Python was used (`artifact: docs/formats/zbdd.md`, Verification).

## Unknowns

1. What the 32-bit index values denote. They are found verbatim in the twin `zdd` payload, but 22,380 of 22,382 slots have no resolvable name, so they cannot be resolved to strings from the index alone (`artifact: docs/formats/zbdd.md`, Unknowns).
2. Meaning of the constant at `+0x18` (`1`), the zero fields at `+0x00/+0x04/+0x10` and the virtual-pointer run at `+0x40..+0x9f` (`artifact: docs/formats/zbdd.md`, Unknowns).
3. The 0x20-byte descriptor's full layout: first two words are zero and one later word matched in the twin test, but field boundaries beyond the size are not established (`artifact: docs/formats/zbdd.md`, Unknowns).
4. Whether pointer-array order follows ascending index order one to one (`artifact: docs/formats/zbdd.md`, Unknowns).
5. Why the class is named `BvhDwdStore` when no spatial data was measured. Either the name covers a wider family or a second record layout exists elsewhere in the code path that was not located; this is an open contradiction (`artifact: docs/formats/zbdd.md`, Unknowns).
6. The `0x10` reader in the executable; the field table is measured from payload, not read from code (`artifact: docs/formats/zbdd.md`, Unknowns and Exe path).
7. Grade reconciliation: `coverage_audit/out/tables.md` row `0x10` says Classified while the detailed report and this document say Partial with a bounded scope.

Next checks, in order: resolve one index value to a string by testing whether it is a 32-bit truncation of a `zdd` entry name hash; then locate the reader behind the `BvhDwdStore` registration and read its descriptor field order (`artifact: docs/formats/zbdd.md`, Unknowns).

## Changelog

- 2026-11-26: created `artifact: docs_complete/zbdd.md` by consolidating `artifact: docs/formats/zbdd.md`, `workspace: CONTEXT_HANDOFF.md` and `coverage_audit/out/tables.md`; counts transcribed from the coverage table, `artifact: type_census.csv` cited as underlying census. No index edit, no commit, no publish, no rescan. Language: no new code; read-only PowerShell text inspection of source artifacts only. Fields table has exactly four columns with source artifacts in Meaning. Write status unchanged at W0; grade Partial with index and pointer-array scope. A concurrent draft with a five-column field table, an undefined grade label and a self-attributed census rerun was superseded by this version on the parent's explicit audit finding.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zbdd.md`. No count was selected by modification time.

