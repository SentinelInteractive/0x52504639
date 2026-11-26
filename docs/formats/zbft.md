# `zbft` (type code `0x11`)

Decode scope, stated plainly: the zlib container and the virtual-root / body-header fields are verified on every slot, and an externally derived BVH structure layout is adopted for the structural clauses and tested on a retained 141-body diagnostic set. This is still not an end-to-end payload decode: group packing, child pointers and traversal are decoded on the retained bodies, while leaf geometry and reconstructed runtime node boxes are not produced and byte-exact rehydration is not reproduced. Header/structural progress is bounded separately in Decode status and is not a claim about runtime adoption. Date 2026-11-26. No key, asset, payload content, matched name or source path is reproduced. Underlying census: `artifact: type_census.csv` (1,255,039 rows), cited only; no census or archive rescan was run for this document.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x11`. The executable's type-name table at `0x1462fcd30 + variant*0x98 + code*8` resolves it to `zbft` (variant 0) and `ibft` (variant 1) (`artifact: docs/formats/zbft.md`, Identity and Exe path). The word is registered by a verified PE read: `lea rdx,["BvhFragmentStore"]` at `0x145ba62dc`, `mov r8d,0x11` at `0x145ba62e3`, `call 0x1419ca0b0` (`artifact: docs/formats/zbft.md`, Identity and Exe path). That class name is the only engine label claimed here, and it is verified by the image bytes, not inferred from the payload.

- Structural identity, **verified**: two zlib streams, a virtual-root stream of 208 bytes in 91.6 percent of slots, body entries addressed through `0x50000000`-relative virtual pointers, and a 32-bit tag `0x81020006` appearing exactly once per payload at a position fixed by the virtual-root field (`artifact: docs/formats/zbft.md`, Identity and Container).
- Format identity, **inferred**: a serialized ray-tracing acceleration structure, from the 64-byte record stride, the root reference with a three-bit discriminator and the columnar leaf table (`artifact: docs/formats/zbft.md`, Identity). No Microsoft header was consulted and no emulator was run (`artifact: docs/formats/zbft.md`, Identity).
- Structural layout, **external and adopted mechanically**: the BVH4 structure layout recorded in `artifact: bvh_nodes/adopt.md` §2, read from an external source at a fixed SHA (URLs recorded in that note §1). No code was copied; the scanner is an independent Rust implementation of the described arithmetic (`artifact: bvh_nodes/adopt.md`, §1 and §4). No upstream project name is repeated here.
- Companion relation, **verified as a population statement**: 22,438 of 22,440 slots share their 64-bit name hash with a `0x03` `zft` slot, 21,356 of those also by name string, and no hash is shared by two `zft` slots; two slots are unpaired. No numeric correspondence was found over 22,438 pairs: CRC coincidence in 2 pairs, a six-float bounds vector in 2, an extent value in 1,659 (7.39 percent, consistent with common small integers), a leaf count in none (`artifact: docs/formats/zbft.md`, Identity).

Grade: **Partial**, scope = container, virtual root, body header, adopted group packing and traversal on a 141-body retained set; leaf geometry and reconstructed runtime node boxes open (`artifact: bvh_nodes/adopt.md` §8; `artifact: docs/formats/zbft.md`, Decode). `workspace: CONTEXT_HANDOFF.md` §9 grades this Partial as "64-byte body stride; node/geometry open"; `coverage_audit/out/tables.md` row `0x11` carries the coarser Classified note "Name and count verified; no payload decoder". This document supersedes the stale handoff with the adopted structural result but keeps the partial grade (`artifact: bvh_nodes/adopt.md` §8).

## Counts

Authoritative totals are transcribed from `coverage_audit/out/tables.md`, row `0x11`; `artifact: type_census.csv` is the underlying census and was not rescanned.

| Code | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `0x11` | 22,440 | 414,772,768 | 6,733,343,200 |

Per-root split, from the type report (`artifact: docs/formats/zbft.md`, Counts):

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `core_bvh4` | 22,430 | 414,695,840 | 6,731,696,832 |
| `shared_minigame000_bvh4` | 10 | 76,928 | 1,646,368 |
| **Total** | **22,440** | **414,772,768** | **6,733,343,200** |

The type-word join, the registry and the census agree on all three numbers (`artifact: docs/formats/zbft.md`, Counts). Every slot is a resource entry; roots and containing headers are generation 4; the population sits in 263 distinct headers, the largest with 2,286 slots (`artifact: docs/formats/zbft.md`, Counts). Name origins: 21,356 dictionary matches and 1,084 unresolved hashes; all 22,440 name hashes are distinct (`artifact: docs/formats/zbft.md`, Counts). Stored sizes run 160 to 1,686,432 bytes and logical sizes 720 to 26,870,112 bytes, with a median logical-to-stored ratio of 14.428 (`artifact: docs/formats/zbft.md`, Counts).

## Container

All statements in this section are measured on 22,440 of 22,440 slots (`artifact: docs/formats/zbft.md`, Container):

- Stored `+0x00..+0x0F` are sixteen zero bytes and stored `+0x10` begins a zlib stream (`78 da` in every slot).
- Every slot holds exactly two streams. The second begins at the next 16-byte-aligned stored offset; the measured gap is 0 in 26,135 boundaries and 1 to 15 otherwise, never more.
- `logical == sum(inflated)` on 22,440 of 22,440 slots; zero inflate errors.
- The first stream is **not** a fixed 208-byte header: 208 bytes in 20,552 slots (91.6 percent), 256 in 1,395, 352 in 244, 544 in 245, 400 in 2, 1,936 in 1 and 6,544 in 1. A constant-208 assumption would be wrong for 1,888 slots.
- The second stream carries the body, up to 26,869,760 bytes in the largest slot.
- One probe reports a logical-length mismatch because it caps the retained stream-one length at 4,096 bytes; the container walk has no such cap and finds zero mismatches. Use the container walk for length validation (`artifact: docs/formats/zbft.md`, Verification).

## Fields

Offsets are relative to the concatenated inflated payload unless stated; integers little-endian. Confidence vocabulary is strictly `measured`, `inferred`, `external`, `unknown`. Every Meaning cell names its source artifact. `P` is the body base and `H` the body-header base (`artifact: docs/formats/zbft.md`, Fields).

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00` | 8 | Zero qword in the virtual-root stream (`artifact: docs/formats/zbft.md`, Fields) | measured |
| `+0x20` | 4 | `0x60000000` in all 22,440 slots; a tagged word, not a `0x50` pointer, and pointer treatment yields no in-range target (`artifact: docs/formats/zbft.md`, Fields and Decode) | measured |
| `+0x28` | 4 | Virtual pointer with seven distinct values whose frequencies equal the seven first-stream length classes (`artifact: docs/formats/zbft.md`, Fields) | measured |
| `+0x38` | 4 | `0x50000050` in all slots (`artifact: docs/formats/zbft.md`, Fields) | measured |
| inside stream | — | TOC name appears verbatim as a NUL-terminated string in matched slots; record not identified (`artifact: docs/formats/zbft.md`, Fields) | measured |
| tag at `P+0x100` | 4 | `0x81020006` in 22,440 of 22,440 slots, exactly once per payload; distance from the `+0x28` pointer is 288 bytes in 21,947 slots, 352 in 246, 384 in 245, 704 in 1 and 1,728 in 1 (`artifact: docs/formats/zbft.md`, Fields) | measured |
| `P+0x20` | 4 | Equals `P+0x28 + 0x100` in 22,440 of 22,440 (`artifact: docs/formats/zbft.md`, Fields) | measured |
| `P+0x28` | 4 | Equals `64·(node_count + 1)` in 22,440 of 22,440, i.e. the body is a 64-byte record array (`artifact: docs/formats/zbft.md`, Fields) | measured |
| `H+0x04` | 4 | Node count, used by the 64-byte-stride identity (`artifact: docs/formats/zbft.md`, Fields) | measured |
| `H+0x08` | 4 | Checksum-like word; CRC reading inferred (`artifact: docs/formats/zbft.md`, Fields) | unknown |
| `H+0x0c` | 4 | Leaf count (`artifact: docs/formats/zbft.md`, Fields) | measured |
| `H+0x30` | 4 | Root reference; low three bits are `4` (box) in 22,439 slots and `0` (triangle) in the single 720-byte slot (`artifact: docs/formats/zbft.md`, Fields) | measured |
| structure `+0x00` | 4 | `flags`, adopted as `0x81020006`; maps to the measured tag above (`artifact: bvh_nodes/adopt.md` §2, external layout at body `0x100`) | external |
| structure `+0x04` | 4 | `size_units`, the 64-byte node count excluding the header; adopted from external layout (`artifact: bvh_nodes/adopt.md` §2) | external |
| structure `+0x08` | 4 | `crc32`, adopted from external layout; no independent CRC check was reproduced (`artifact: bvh_nodes/adopt.md` §2 and §9) | external |
| structure `+0x0c` | 4 | `numElements`, adopted from external layout (`artifact: bvh_nodes/adopt.md` §2) | external |
| structure `+0x10`–`+0x27` | 6 × 4 | `sceneBounds.min` xyz then `sceneBounds.max` xyz as f32, adopted from external layout (`artifact: bvh_nodes/adopt.md` §2) | external |
| structure `+0x28` | 4 | `offsetToNodes`, adopted from external layout (`artifact: bvh_nodes/adopt.md` §2) | external |
| structure `+0x2c` | 4 | `offsetToPrimRemap`, adopted from external layout (`artifact: bvh_nodes/adopt.md` §2) | external |
| structure `+0x30` | 4 | `rootNodePtr`, adopted from external layout (`artifact: bvh_nodes/adopt.md` §2) | external |
| structure `+0x34` | 4 | `offsetToElements`, adopted from external layout (`artifact: bvh_nodes/adopt.md` §2) | external |
| structure `+0x38` | 4 | `offsetToParents`; the probe prints it but does not follow it (`artifact: bvh_nodes/adopt.md` §2 and Unknowns) | external |
| structure `+0x3c` | 4 | `compressionParams`; not `0x007f7f7f` in 141 of 141 samples, so containment in `sceneBounds` is untestable (`artifact: bvh_nodes/adopt.md` §2 and §5) | external |
| node pointer | 4 | `kind = ptr & 7`, `unit = ptr >> 3`, address = structure start + unit·64; kinds 0–3 TRI0–TRI3, 4 BOX16, 5 BOX32, 6 INSTANCE, 7 AABB_GEOMETRY (`artifact: bvh_nodes/adopt.md` §2) | external |
| level table at structure end | 4 × (2C+1) | Last u32 is level count `C`; the `C` preceding pairs are `(BOX32_end, BOX16_end)` as byte offsets from `offsetToNodes` (`artifact: bvh_nodes/adopt.md` §2) | external |
| group header word | 4 | `count = word >> 24`, `mask = word & 0xffffff`, one word per node at the group base (`artifact: bvh_nodes/adopt.md` §2) | external |
| child pointer words | 4 each | Packed separately after the group header words; three-bit type plus 29-bit 64-byte unit (`artifact: bvh_nodes/adopt.md` §2) | external |
| override values | 2 or 4 | `popcount(mask)` values after child pointers; u16 half for BOX16, f32 for BOX32, applied at slot bit `6*slot + c` with c = min xyz then max xyz (`artifact: bvh_nodes/adopt.md` §2) | external |

Two pre-declared end words at body `0x20` and `0x28` match `0x140 + 64·size_units` and that value minus `0x100` in 141 of 141 retained bodies (`artifact: bvh_nodes/adopt.md` §5). A candidate leaf table in the original report checked at most 64 entries on 20,576 of 22,440 slots under a single-group assumption; it does not validate the full table or the 2,048-entry group stride (`artifact: docs/formats/zbft.md`, Fields).

## Decode status

- Container: **decoded and verified** on 22,440 of 22,440 slots (`artifact: docs/formats/zbft.md`, Decode).
- Virtual root and body header: **decoded and verified** for the fields listed above, including three identities holding on 100 percent of the population (`artifact: docs/formats/zbft.md`, Decode).
- Adopted structure, **consistent on retained bodies, not a census**: `flags` 141/141, pre-header end words 141/141, structure fits body 141/141, level table ordered and divisible 141/141; 140 BOX16 roots and 1 TRI0 root; 1,218 BOX16 and 2,972 BOX32 groups; 29,234 BOX16 and 166,107 BOX32 nodes; child-count histogram `2: 28,900`, `3: 29,185`, `4: 137,256`, none 0, 1 or above 4 (`artifact: bvh_nodes/adopt.md` §5).
- Pointer and traversal clauses, **consistent**: zero invalid type, zero invalid pointer, zero out-of-body, zero wrong-level box pointer, zero non-TRI leaf pointer; 499,178 TRI0 pointers equal the summed manifest leaf count; 140 of 140 box samples traverse `closed` with no cycle, dangling pointer, orphan or multi-parent node (`artifact: bvh_nodes/adopt.md` §5 and §8).
- Override clause, **partially consistent and partly untestable**: BOX16 masks are zero on every parsed node; 2,260 BOX32 nodes in 73 samples carry 11,775 stored f32 overrides, all finite, with 5,058 paired min/max components all ordered; containment in `sceneBounds` is not testable because `compressionParams` is not the identity frame in 141 of 141 (`artifact: bvh_nodes/adopt.md` §5 and §8). An earlier draft wrongly said all 195,341 masks were zero; the correction in `artifact: bvh_nodes/adopt.md` §10 supersedes it and changed no table value.
- Controls: a +1 byte shift produced 385,578 invalid count/mask words and 195,320 of 195,341 invalid nodes; +4 produced 8,380 and 4,190; the triangle-root sample gives a header-only false positive rejected by its out-of-range child pointer (`artifact: bvh_nodes/adopt.md` §6).
- Leaf geometry and reconstructed runtime node boxes: **not decoded**. Group packing, child pointers and traversal are decoded and consistent on the retained bodies; no vertex, index or triangle data was read out from this type (`artifact: docs/formats/zbft.md`, Decode). Byte-exact rehydration is not reproduced: no source geometry and no builder DLL were available, and the published claim is on 8 private samples (`artifact: bvh_nodes/adopt.md` §2 and §9).
- Grade **Partial**, scope = container, header and adopted structural clauses on a retained 141-body set (`artifact: bvh_nodes/adopt.md` §8). Write status **W0**: no encoder, no pack-back test and no game-load test; even a re-emitter of the measured fields would not reproduce a loadable acceleration structure (`artifact: docs/formats/zbft.md`, Encode).

## Verification

All commands and figures below are from Rust release artifacts recorded in the cited sources; nothing was re-run for this document.

- `type_probe inventory artifact: type_census.csv 00000011 out` — 1,255,039 census rows, 22,440 selected, 0.22 s (`artifact: docs/formats/zbft.md`, Verification).
- `type_probe walk out\zbft_slots.tsv <archive-root> out\zbft_walk.txt 256 288` — 22,440 slots in 5.71 s (3,929 slots/s, 72.6 MB/s stored, 1.18 GB/s logical) (`artifact: docs/formats/zbft.md`, Verification).
- `verify hdrlen`, `verify hdrclass`, `verify u32 … 256 32 40` — 22,440 slots each in 4.6 to 4.8 s at 4,708 to 4,911 slots/s (`artifact: docs/formats/zbft.md`, Verification).
- `verify magic out\zbft_slots.tsv <archive-root> 0x81020006` — 22,440 slots in 4.65 s, 4,829 slots/s (`artifact: docs/formats/zbft.md`, Verification).
- `paircheck artifact: type_census.csv` — 1,255,039 rows in 2.32 s; 22,438 unambiguous pairings and two unpaired slots (`artifact: docs/formats/zbft.md`, Verification).
- `zbft_probe header|body|join` — 64,980 slots/s header, 2,419.7 slots/s body (44.7 stored MB/s, about 726 logical MB/s), 379.9 pairs/s twin test (`artifact: docs/formats/zbft.md`, Verification).
- `cd artifact: bvh_nodes; rustc -O adopt_scan.rs -o adopt_scan.exe; ./adopt_scan.exe` — 1,053 ms for 141 bodies and 60,013,056 bytes read, `rustc` 1.95.0, std only (`artifact: bvh_nodes/adopt.md` §4). Outputs `artifact: bvh_nodes/adopt_results.tsv` (141 rows, 47 columns) and `artifact: bvh_nodes/adopt_detail.txt`.
- Independent recount of the TSV, detail file and manifest by a read-only fast-worker confirmed `flags_ok` 141/141, `end_words_ok` 141/141, `level_ok` 141/141, `nc` sum 968, `bad_count = 0`, `bad_mask = 0`, all five pointer-error columns zero, `ptr_leaf` 499,178, 140/140 `traversal=closed`, `visited` sum 195,341, `ctrl1_bad = 385,578`, `ctrl1_nbad = 195,320`, `ctrl4_bad = 8,380`, `ctrl4_nbad = 4,190`, and the separated triangle-root sample (`artifact: bvh_nodes/adopt.md` §11).
- The executable was never loaded or executed; no Python was used (`artifact: docs/formats/zbft.md`, Verification; `artifact: bvh_nodes/adopt.md` §1).

## Unknowns

1. Leaf geometry and reconstructed runtime node boxes, and the role of `H+0x38`; the group packing and traversal are decoded, but no child box was recomputed without source geometry and the probe prints `H+0x38` without following it (`artifact: docs/formats/zbft.md`, Unknowns; `artifact: bvh_nodes/adopt.md` §9).
2. Meaning of `V+0x40`, `V+0xa0`, `H+0x3c` and the CRC-like word at `H+0x08` (`artifact: docs/formats/zbft.md`, Unknowns).
3. The rule choosing the first-stream length; seven classes observed, no rule inferred (`artifact: docs/formats/zbft.md`, Unknowns).
4. Why 1,864 slots fall outside the bounded leaf-table plausibility result; reasons are not tallied separately (`artifact: docs/formats/zbft.md`, Unknowns).
5. How the acceleration structure is derived from its name-matched twin, given that no numeric field correlates (`artifact: docs/formats/zbft.md`, Unknowns).
6. Whether the builder is an external DLL or an internal path; not analysed, and analysing a DLL on disk would not prove the game executes it (`artifact: docs/formats/zbft.md`, Unknowns).
7. BOX16 half overrides are untestable on retained bytes, and `sceneBounds` containment is untestable because no sample uses the identity frame (`artifact: bvh_nodes/adopt.md` §9). Byte-exact rehydration and runtime adoption are not established (`artifact: bvh_nodes/adopt.md` §8).
8. The 141 bodies are a retained diagnostic set, not a census of the packs (`artifact: bvh_nodes/adopt.md` §9). Grade reconciliation: `coverage_audit/out/tables.md` row `0x11` says Classified while the detailed report and this document say Partial with a bounded scope.

## Changelog

- 2026-11-26: created `artifact: docs_complete/zbft.md` by consolidating `artifact: docs/formats/zbft.md`, `workspace: CONTEXT_HANDOFF.md`, `coverage_audit/out/tables.md` and the new authoritative `artifact: bvh_nodes/adopt.md`; counts transcribed from the coverage table, `artifact: type_census.csv` cited as underlying census. No index edit, no commit, no publish, no rescan. Language: no new code; read-only PowerShell text inspection of source artifacts only. Key correction: the adopted layout supersedes the stale handoff and resolves the earlier trailing-word refutations as level-table offsets; the earlier "all masks zero" overstatement is corrected to 2,260 BOX32 nodes with non-zero masks. Write status unchanged at W0; grade Partial with structural scope on 141 retained bodies.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zbft.md`. No count was selected by modification time.

