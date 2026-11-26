# `zsp` (type `0x64`)

Compiled 2026-11-26 from saved local artifacts. Decode reach is explicit: the container is decoded on 27,482/27,482 slots, and structure beyond the container (0x60 header, bucket array, key/value pairs, token fields, flag array, tail header) is decoded on 4 full samples plus 300 population slots. It cannot be decoded semantically: token meaning, flag meaning, key namespace and the tail beyond its first 16 bytes are unknown. Confidence values below are `measured`, `inferred`, `external`, `unknown`.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

- Type word `0x64`; the executable's variant-0 name is `zsp`, with `isp` and `#sp` as the other two variant strings (`artifact: type_registry.md` L51; `artifact: t5/findings_zsp.md` L104-105; `artifact: docs/formats/zsp.md` L7). Confidence: measured.
- Structural identity: a per-resource hash-to-dense-index table. A 32-bit key maps to a dense `0..N−1` index in a power-of-two bucket array of 0x110-byte buckets, 16 pairs per bucket, a 16-byte token field at each bucket head and one 32-bit flag word per entry (`artifact: t5/findings_zsp.md` L82; `artifact: repo-publisher/docs/zsp.md` L9). Confidence: measured (layout), inferred (that it is an index structure).
- Semantic identity: a metadata/index structure attached to navigation content, not navmesh geometry. All 27,482/27,482 slots live in `navmeshes.rpf`; N is an explicit header field matching pair count; no coordinates, polygons or material records appear in the decoded regions; token bytes are not readable region/path labels (`artifact: t5/findings_zsp.md` L84). Confidence: inferred.
- The "shader payload" label in the coverage audit is rejected: wrong archive and no shader-shaped structure in the decoded regions (`artifact: t5/findings_zsp.md` L89; `artifact: docs/formats/zsp.md` L12). Confidence: inferred.
- Store class: unknown. No handler, constructor or RTTI class name for this type is sourced, and no store-class registration was found in the executable (`artifact: t5/findings_zsp.md` L108; `artifact: docs/formats/zsp.md` L87). Confidence: unknown.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `navmeshes.rpf` | 27,482 (27,482/27,482) | 376,513,072 | 2,325,782,256 |
| **Total** | **27,482** | **376,513,072** | **2,325,782,256** |

- Totals reproduced by the Rust inventory probe `zsp_probe inv` and by a direct `type_census.csv` check (`artifact: t5/out/64_zsp_stats.txt` L2; `artifact: t5/findings_zsp.md` L8-13; `artifact: type_census.csv`, rows with `type_hash=00000064`: 27,482). Stored and logical denominators are the 27,482 slots, not the 1,255,039-slot index.
- Parent rerun of the common Rust census (2026-11-26) agrees exactly: PER_TARGET row for `00000064` is 27,482 slots / 376,513,072 stored / 2,325,782,256 logical with 0 stored and 0 logical parse failures; PER_TARGET_ROOT places all 27,482 slots / 376,513,072 / 2,325,782,256 in `navmeshes.rpf` (`artifact: docs_complete/evidence/seven_types_census.parent_verified.txt` L46, L67, L125). Its denominator is 1,255,039 CSV data rows = 1,153,560 Resource + 101,479 Binary, not a Resource-only count (L22, L25-27).
- Header generation 4: 27,482/27,482. Root generation 4: 27,482/27,482. Root `navmeshes.rpf`: 27,482/27,482. `Resource` entry kind: 27,482/27,482 (`artifact: t5/findings_zsp.md` L11; `artifact: t5/out/64_zsp_stats.txt` L7-9).
- Name origin `UnresolvedHash`: 27,482/27,482; dictionary-matched paths 0/27,482; `hash32` present 0/27,482, `hash64` present 27,482/27,482 (`artifact: t5/findings_zsp.md` L12; `artifact: t5/out/64_zsp_stats.txt` L10). No name-level cross-check is possible.
- Logical size (bytes): min 2,656; p1/p5/p10/p25 2,656; p50 **41,904**; p75 131,072; p90 196,608; p95 196,608; p99 327,680; max 649,440 (`artifact: t5/findings_zsp.md` L14).
- 11 distinct archive headers hold these slots; intersection with the 12 headers of `0x4f` (`znv`) in the same archive is 0 (`artifact: t5/findings_zsp.md` L90; `artifact: docs/formats/zsp.md` L25).

## Container

All statements below are measured over 27,482 slots unless a smaller denominator is given (`artifact: docs/formats/zsp.md` L29-35; `artifact: t5/findings_zsp.md` L31-36; `artifact: t5/out/64_zsp_stats.txt` L3-5).

- **Prefix — measured:** 16 stored zero bytes at offset 0 in 27,482/27,482 slots (`artifact: t5/out/64_zsp_stats.txt` L4).
- **Compression — measured:** zlib header `0x78DA` at stored `+0x10` in 27,482/27,482 slots; the rule `logical == sum(inflated stream lengths)` holds in 27,482/27,482 with no exceptions (`artifact: t5/out/64_zsp_stats.txt` L5; `artifact: docs/formats/zsp.md` L31-32).
- **Page/block — measured:** one continuous inflated buffer per slot, not a fixed page grid; one stream in 27,476/27,482 slots and two in 6/27,482. The repeating structural block inside the buffer is the 0x110-byte bucket (`artifact: docs/formats/zsp.md` L33; `artifact: t5/findings_zsp.md` L82). A page grid beyond this is unknown.
- **Alignment — measured:** inter-stream padding is 0..15 stored bytes to the next 16-byte boundary and is not counted in `logical`; the 202-slot `zsp_probe chain 201` recheck found its single two-stream slot with a 10-byte gap (`artifact: docs/formats/zsp.md` L34; `artifact: t5/findings_zsp.md` L33-34; `artifact: t5/out/zsp_chain.tsv`).
- **Chain — measured:** stream histogram 1→27,476/27,482 and 2→6/27,482; exactly six slots carry two streams; 0 unterminated streams in the population walk, 202/202 in the stratified recheck (`artifact: docs/formats/zsp.md` L33, L107; `artifact: t5/findings_zsp.md` L34).
- The alternative rule `16 + sum(streams) + gaps == logical` is rejected at 0/202 because it mixes stored and inflated units (`artifact: t5/findings_zsp.md` L35, L112).
- 26,597/27,482 slots have a zero run between the last stream and the end of the stored range (`artifact: docs/formats/zsp.md` L35).
- `slot.exe navmeshes.rpf 6253502464 560 2656 out.bin` reports `exact=true` only because it caps output at `logical−16`; its 2,640 bytes are a byte-identical prefix of the uncapped 2,656-byte stream. Do not use that flag to define the logical-size rule (`artifact: t5/findings_zsp.md` L29).

## Fields

Offsets are relative to the first inflated byte. Evidence: `artifact: t5/out/64_zsp_fields.txt` (all 27,482 slots), `zsp_probe struct` on s00/s01/s02/s04 full buffers, `zsp_probe pop 300` (`artifact: t5/out/zsp_pop.tsv`); `artifact: t5/findings_zsp.md` L40-64 and `artifact: repo-publisher/docs/zsp.md` L39-71.

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00` | u64 | Zero field; 0 in 27,482/27,482 | measured |
| `+0x08` | u32 rel | `0x50000000 + tail_offset`; points at a 16-byte tail header `{u64 0, u64 k}`, in range 27,482/27,482 on the population pointer check and parsed on 4/4 samples; `k` is 1 on s00/s01/s04 and 2 on s02 | measured |
| `+0x0c` | u32 | Zero field; 0 in 27,482/27,482 | measured |
| `+0x10` | u32 | Bucket count, a power of two: 9 distinct values 8..2,048; 8 in 12,778/27,482, 256 in 7,131/27,482, 512 in 6,263/27,482 | measured |
| `+0x14` | u32 | Entry count N; equals `+0x50` in 300/300 sampled slots (85 on s00, 1,738 on s01, 3,153 on s04, 14,903 on s02) | measured |
| `+0x18` | u32 rel | Constant `0x50000060` in 27,482/27,482; bucket array starts at inflated 0x60 | measured |
| `+0x1c` | u32 | Zero field; 0 in 27,482/27,482 | measured |
| `+0x20` | u32 rel | `0x50000000 + flags_offset`; flag array follows the bucket array (on s02 it lies in the second zlib stream); 13,719/27,482 in-range by the population relptr check | measured |
| `+0x24` | u32 | Zero field; 0 in 27,482/27,482 | measured |
| `+0x28`, `+0x2c`, `+0x30` | 3 × u32 | Identical power-of-two value in every slot: 128 (16,487/27,482), 256 (7,466/27,482), 1,024 (2,662/27,482), 512 (866/27,482), 4,096 (1/27,482); semantic role not established | unknown |
| `+0x34` | u32 | 24,480 distinct values in a narrow band (91,808..183,591 in the 300-slot sample); never a valid in-buffer relative pointer; role not established | unknown |
| `+0x38`, `+0x3c` | 2 × u32 | Zero fields; 0 in 27,482/27,482 | measured |
| `+0x40`, `+0x44` | 2 × f32 | Values such as −12288/−9856 (s00) and −3456/−768 (s01); read as fixed-point extents, but no coordinate array exists in the decoded regions | inferred |
| `+0x48` | u32 | 0 in 16,826/27,482; otherwise one of 7 values including `0xC3500000` and `0xC4100000`; role not established | unknown |
| `+0x50` | u32 | Duplicate of the entry count N | measured |
| `+0x54`..`+0x5c` | 3 × u32 | Zero fields; 0 in 27,482/27,482 | measured |
| `0x60` onward | 0x110 B/bucket | Bucket array, `bucket_count × 0x110`: a 16-byte token field then sixteen `(u64 key, u64 value)` pairs; `(flags_offset−0x60)/0x110` integral in 4/4 fully parsed samples (8, 128, 256, 2,048 buckets) | measured |
| after buckets | 4 B/entry | Flag array, `round_up(N,4)` u32 words: 88 for N=85, 1,740 for N=1,738, 3,156 for N=3,153, 14,904 for N=14,903 | measured |
| after flags | variable | Tail: first 16 bytes parse as a header, the rest is mostly zero in examined samples | inferred |

- Token field within each bucket: 16-byte array terminated by the first byte with the high bit set (normally `0x80`), remainder `0x80`; no NUL and no length prefix. Lengths 0..16 bytes, including five empty buckets in the 300-slot scan; the earlier 4..16 range was too narrow (`artifact: docs/formats/zsp.md` L68; `artifact: t5/out/zsp_tokens_pop_report.txt` L8; `artifact: t5/findings_zsp.md` L70-73). Confidence: measured.
- Keys are 32-bit-wide values stored in eight bytes; values are a dense `0..N−1` index; keys and values distinct within a slot. Token-array length equals populated-pair count with 0 mismatches on 300/300 sampled slots and 4/4 samples; total token bytes = pair count = header N (`artifact: t5/findings_zsp.md` L71, L75; `artifact: docs/formats/zsp.md` L67-70). Confidence: measured.

## Decode status

- Real structural decoder found. Build and run (Rust release, offline), from `artifact: t5/findings_zsp.md` L93-98 and L130, with the CLI declared in `artifact: t5/zsp_probe/src/main.rs` L1-7:
  ```powershell
  cd artifact: t5/zsp_probe
  cargo build --release --offline
  .\target\release\zsp_probe.exe one 6253502464
  .\target\release\zsp_probe.exe struct artifact: t5/out/zsp_one_6253502464.bin
  .\target\release\zsp_probe.exe pop 300
  .\target\release\zsp_probe.exe chain 201
  cd artifact: t5/zsp_tokens_leaf
  .\target\release\zsp_tokens_leaf.exe pop 300
  ```
- Source inspection command to confirm the decoder's scope: `Get-Content artifact: t5/zsp_probe/src/main.rs -TotalCount 7` (lists `inv`, `chain`, `struct`, `pop`, `exe`; none decodes token or key semantics). Token scanner source: `artifact: t5/zsp_tokens_leaf/src/main.rs`.
- Reported decode depth: container on 27,482/27,482 slots; header, bucket array, key/value pairs, token locations/counts, flag array and tail header on 4 full samples plus 300 population slots. Layout is decoded; semantics are not (`artifact: t5/findings_zsp.md` L95; `artifact: repo-publisher/docs/zsp.md` L75-79).
- No verified semantic decoder exists, and no writer/encoder exists. Write status W0: no round-trip, no game-load test (`artifact: repo-publisher/docs/zsp.md` L81-83; `artifact: docs/formats/zsp.md` L100-102).
- Status reconciliation, newest first: `artifact: repo-publisher/docs/zsp.md` L3 and L75-79 (2026-11-25) says Partial, container and hash-table structure decoded; `artifact: docs/formats/zsp.md` L1 and L98 (2026-11-24) says Partial, layout decoded and semantics not; `workspace: CONTEXT_HANDOFF.md` L175 says Partial, full container and hash table, tokens undecoded; `artifact: type_registry.md` L51 says Partial. The Classified/"shader payload not decoded" line at `workspace: coverage_audit/out/tables.md` L18 reports the same 27,482 / 376,513,072 / 2,325,782,256 totals but is stale on status and wrong on the "shader" label. This document follows the newer per-type notes: **Partial**.

## Verification

- Whole-census reconciliation reproduces 27,482 / 376,513,072 / 2,325,782,256 exactly (`artifact: docs/formats/zsp.md` L106; `artifact: repo-publisher/docs/zsp.md` L87).
- Parent rerun of the common census, 2026-11-26, from `artifact: docs_complete/evidence`: `rustc -O seven_types_census.rs -o seven_types_census.exe`, then `.\seven_types_census.exe artifact: type_census.csv artifact: docs_complete/evidence/seven_types_census.parent_verified.txt`. Saved output: `total_data_rows_denominator: 1255039`, `malformed_rows: 0`, exact zsp PER_TARGET and PER_TARGET_ROOT rows, and a 0.660435 s run over 312,661,753 bytes (`artifact: docs_complete/evidence/seven_types_census.parent_verified.txt` L8-9, L12-17, L22-27, L46, L67).
- Population chain walk: prefix and `0x78DA` 27,482/27,482; `sum(inflated) == logical` 27,482/27,482; stream histogram 1→27,476, 2→6; 0 unterminated (`artifact: docs/formats/zsp.md` L107; `artifact: t5/findings_zsp.md` L33).
- Independent population verifier, Rust: prefix, `0x78DA`, `u64@0 == 0` and the `+0x08` pointer range, 27,482/27,482 on each (`artifact: docs/formats/zsp.md` L108).
- Printable-run scan over all 27,482 inflated payloads: 0 slots with a printable run of 32 bytes or more; longest run under 32 (`artifact: docs/formats/zsp.md` L81, L109; `artifact: repo-publisher/docs/zsp.md` L73).
- Structural parse: 300/300 sampled slots agree on token bytes = pair count = header N, per-bucket pair length = bucket token count with zero mismatches, and `(flags_offset−0x60)/0x110` integral (`artifact: docs/formats/zsp.md` L110; `artifact: t5/findings_zsp.md` L64).
- Byte accounting: 2,656 = 96 header + 8×0x110 (2,176) buckets + 88×4 (352) flags + 32 tail; 41,904 = 96 + 34,816 + 6,960 + 32; 649,440 = 96 + 557,056 buckets + 32,672 zero padding + 59,616 flags (`artifact: t5/findings_zsp.md` L96; `artifact: docs/formats/zsp.md` L71).
- Token population, 300 slots: 511,945 token bytes in 52,536 buckets, 128 distinct values, entropy 6.9957 bits vs 7 for uniform; 0 of 84,114 distinct keys carry conflicting token values; 52,111/52,536 buckets have ascending values. Arithmetic tests against key/value/flag bits stayed at chance level, so no deterministic token function was established (`artifact: t5/out/zsp_tokens_pop_report.txt` L1-2, L9-12, L15; `artifact: t5/findings_zsp.md` L75-77).
- 253,304/511,945 token bytes are in `[a-z0-9_]` (106,580 lower + 102,884 upper + 39,782 digit + 4,058 underscore) and 126,883/511,945 are control bytes: readable names in the token field are rejected (`artifact: t5/findings_zsp.md` L74; `artifact: t5/out/zsp_tokens_pop_report.txt` L1; `artifact: docs/formats/zsp.md` L112).
- Executable path: name string VA `0x14677e46b` holds `zsp\0isp\0`; literal `zsp` occurs twice in the 120,181,760-byte image; no stored pointer to the name-table slot VA `0x14618db00` was found, so no static xref or handler was established (`artifact: t5/findings_zsp.md` L104-108; `artifact: docs/formats/zsp.md` L85-87).
- Rejected hypotheses: multi-stream chain, readable token names, hash-to-own-name map, arithmetic token derivation, shared header with `0x4f`, coordinates or material records in decoded regions (`artifact: t5/findings_zsp.md` L110-119).
- Batch timings reported by the cited Rust probes: `zsp_probe inv` 2.81 s over a 312,661,753-byte census; `zsp_probe chain 201` 0.129 s warm for 202 slots; `zsp_probe pop 300` 0.2 s warm for 300 fully inflated and parsed slots. Model/effort for those probes: hy4-flash-free, medium (`artifact: t5/findings_zsp.md` L2, L128-145).

## Unknowns

Each item states an open question and a proposed evidence criterion. Every "To settle" clause is a proposal, not a measured result; none was run for this document.

1. **Open question:** what the 7-bit token byte and the per-entry 32-bit flag word encode. Token bytes are located and counted, but arithmetic tests against key, value and flag bits stayed at chance level (`artifact: t5/findings_zsp.md` L74-78; `artifact: t5/out/zsp_tokens_pop_report.txt` L9-12). **To settle:** a static xref to code that reads the 0x110-byte bucket stride and touches the token/flag fields, with each field's input and output identified; or a bounded runtime trace of that consumer showing the value computed for one entry. No such reference is in the saved artifacts (`artifact: repo-publisher/docs/zsp.md` L97; `artifact: t5/findings_zsp.md` L123).
2. **Open question:** whether the `u32` keys are RPF name hashes, object IDs or another domain. The type has 0/27,482 resolved names; the 300-slot sample holds 84,114 distinct keys (`artifact: t5/findings_zsp.md` L76; `artifact: t5/out/zsp_tokens_pop_report.txt` L16). **To settle:** obtain a candidate namespace dictionary, test exact equality against the observed keys with the documented hash function, and report match count with its denominator plus a control rate on a disjoint corpus; a high exact-match rate identifies the namespace and a chance-level rate refutes that dictionary. No such dictionary covers this type (`artifact: repo-publisher/docs/zsp.md` L98; `artifact: t5/findings_zsp.md` L126).
3. **Open question:** the meaning of the `+0x28`/`+0x2c`/`+0x30` power-of-two triple and the `+0x34` counter/id (`artifact: t5/out/64_zsp_fields.txt` L11-14). **To settle:** a formula or code reference that reproduces every observed value across all 27,482 slots with zero exceptions and states its provenance, either an archive-header metadata field or a documented invariant; histogram correlation alone does not settle it (`artifact: repo-publisher/docs/zsp.md` L99; `artifact: t5/findings_zsp.md` L124).
4. **Open question:** contents of the tail beyond its first 16 bytes; examined slots are mostly zero (`artifact: repo-publisher/docs/zsp.md` L100). **To settle:** locate a slot with non-zero tail bytes past +0x10, dump the exact byte range with its offset and length relative to `logical`, and parse it under a candidate layout with a complete byte-accounting identity; the alternative is a population report of the exact non-zero tail-byte count over all 27,482 slots (`artifact: t5/findings_zsp.md` L125).
5. **Open question:** any handler, constructor, RTTI class name or vtable on the executable side; no static xref was found (`artifact: docs/formats/zsp.md` L87). **To settle:** a stored pointer to the name-table slot VA `0x14618db00`, or an RTTI/class-name reference whose code path reads the 0x110 stride or the `+0x10` bucket count; the literal and pointer searches were clean negatives, so this needs a different static entry point or a bounded runtime consumer trace (`artifact: t5/findings_zsp.md` L104-108).
6. **Open question:** whether a fixed page grid exists beyond the single continuous buffer. **To settle:** demonstrate a repeated boundary with a constant stride and page-header signature across all 27,482 slots, or prove the negative by showing `logical = sum(inflated stream lengths)` with one stream in 27,476 slots and two in 6 and no repeated boundary pattern (`artifact: docs/formats/zsp.md` L31-34; `artifact: t5/findings_zsp.md` L33).

## Changelog

- 2026-11-24: evidence tree written. Rust probes `zsp_probe` and `zsp_tokens_leaf` built release/offline under `artifact: t5/`; notes at `artifact: t5/findings_zsp.md`, report at `artifact: docs/formats/zsp.md` L1, both Partial with token semantics undecoded.
- 2026-11-25: `artifact: repo-publisher/docs/zsp.md` L3 rewritten; still Partial, container and hash-table structure decoded, token/key semantics not decoded, W0. This is the newest per-type note.
- 2026-11-26: this file created. Status reconciled to Partial against the Classified/"shader" line at `workspace: coverage_audit/out/tables.md` L18; no count changed (27,482 / 376,513,072 / 2,325,782,256). Confidence vocabulary mapped to the four allowed values: `verified` observations became `measured`, layout readings such as fixed-point extents became `inferred`, unestablished meanings became `unknown`. Corrections retained: token lengths 0..16 supersede 4..16; the uncapped `zsp_probe one` stream, not `slot.exe`'s capped `exact` flag, defines the logical-size rule; the six two-stream slots are reported as an exact count. Parent reran the common Rust census; its PER_TARGET and PER_TARGET_ROOT rows match 27,482 / 376,513,072 / 2,325,782,256 in `navmeshes.rpf` against the 1,255,039-row all-kind denominator (`artifact: docs_complete/evidence/seven_types_census.parent_verified.txt` L22, L25-27, L46, L67). No common report is pending.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zsp.md`. No count was selected by modification time.

