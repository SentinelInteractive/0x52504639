# `zbn` bounds (type code `0x06`)

**Scope of this document, 2026-11-26.** The type-`0x06` prefix and **0x90-byte bound root record** were checked on all 92,199 slots; complete chain inflation reached the expected length on 90,546, with 1,653 short chains. The shape body remains undecoded: the proposed 16-byte-node interpretation passed 0 of 20 stratified slots, and the subtype is unresolved. Grade **B (partial structure)**. The newer BVH-store results are reconciled by type and sample scope in section 5. Sources: `artifact: docs/formats/zbn.md` L67-L75, L94-L119; `artifact: zbn_nodes/report.md` L145-L162.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

`zbn` is resource type word `0x00000006`, read at `+0x10` of the 20-byte RPF9 resource record, not from a payload signature. No ASCII magic is recognised at inflated `+0`, `+8`, `+16`, `+32` or `+48`, which is why the census family is `Unknown` (source: `artifact: docs/formats/zbn.md` L17).

The label is the engine's own static enum string, row 6 of the table at `0x1462fcd30`, stride `0x98`: variant 0 `zbn`, variant 1 `ibn`, variant 2 `#bn`. All 36 static naming call sites hardcode variant 0, so `zbn` is the generated label (source: `artifact: docs/formats/zbn.md` L7-L13, L134-L140; enum cross-check `artifact: enum_variant_discriminant_report.md` L34, L52).

Store-class name: unknown in the cited registration scan; the core `0x02`-`0x06` registration path was not located (`artifact: docs/formats/zft.md` L98).

Structurally the slot is a **leaf bounded-volume object**: one radius, one axis-aligned box, one margin, one centroid and gravity pair, four self-pointers and a body of index-like records. There is no member table, nested `9FPR`, name table, BCn block or UTF-8 pool (source: `artifact: docs/formats/zbn.md` L15, L146-L156). Locations are three roots, with `levels.rpf` holding 96.2 percent of slots (source: `artifact: docs/formats/zbn.md` L18, L22-L27). The exact bound class and subtype are **not** established; the executable was read as a PE image only and never run, RTTI is stripped and an image scan for `phBound` returned zero hits (source: `artifact: docs/formats/zbn.md` L141-L142, L214).

## Counts

**92,199 slots**, **11,093,949,168 stored bytes**, **17,156,781,648 logical bytes**; denominator **1,255,039 slots**, giving the exact slot share **92,199 / 1,255,039**. Fresh census source: `artifact: type_census.csv`, filter `type_hash=00000006`; aggregation and replay command: `artifact: docs_complete/evidence/census_counts.rs`, `census_counts.json`, and `census_evidence.md`. The totals agree with the earlier `workspace: coverage_audit/out/tables.md` L9 and `artifact: docs/formats/zbn.md` L27.

| Scope | Slots | Stored bytes | Logical bytes | Source |
|---|---:|---:|---:|---|
| `levels.rpf` | 88,719 | 10,718,017,008 | 16,578,426,944 | `artifact: docs/formats/zbn.md` L24 |
| `pack/story000/story000.rpf` | 2,989 | 269,405,696 | 414,154,000 | `artifact: docs/formats/zbn.md` L25 |
| `pack/shared_minigame000/shared_minigame000.rpf` | 491 | 106,526,464 | 164,200,704 | `artifact: docs/formats/zbn.md` L26 |
| **Total** | **92,199** | **11,093,949,168** | **17,156,781,648** | `artifact: docs/formats/zbn.md` L27 |

The totals equal the independent type-word join for code `0x06` on every field, delta zero slots and zero bytes (`06,zbn,92199,11093949168,17156781648`), and the census field matches for all 92,199 rows (sources: `artifact: docs/formats/zbn.md` L29, L217). All 92,199 are `Resource` slots, none binary; all carry distinct 64-bit name hashes, which does not prove distinct physical content because stored ranges can be shared (source: `artifact: docs/formats/zbn.md` L31, L35). Root generation is 4 in all three roots; containing-header generation is 4 in 271 slots, 5 in 59,716, 7 in 72 and 8 in 32,140 (source: `artifact: docs/formats/zbn.md` L33-L34).

Stored sizes span 272 to 1,328,784 bytes and logical sizes span 848 to 2,442,048 bytes across 92,199 slots, with p50 78,272 stored and 124,016 logical (source: `artifact: docs/formats/zbn.md` L36-L43). The mean sizes printed in that older source disagree with its totals; they are not adopted here. Exact means, if needed, are the census byte totals divided by 92,199.

Name layer: 0 slots were named before the 2026-11-26 expansion; 68,287 of 92,199 (74.06 percent) gained a name in the 407,040-key join, covering 9,566,397,904 stored bytes (sources: `artifact: name_verify/type_ranking.md` L7-L13, L27-L32, L50; `artifact: priority_2026-11-26.md` L13-L20). The older `zbn.md` statement of zero dictionary matches and 92,199 unresolved hashes remains correct for the pre-expansion state (source: `artifact: docs/formats/zbn.md` L32). No recovered name supplies a field semantic or a subtype.

## Container

Every slot uses the same page envelope: 16 zero bytes, then a zlib stream at `+0x10`, with a second zlib stream back to back when the payload crosses a 64 KiB boundary of logical space (source: `artifact: docs/formats/zbn.md` L47-L63).

```text
stored slot
  +0x00  16 zero bytes
  +0x10  zlib stream 1
  ...    zlib stream 2, back to back, when the payload crosses 64 KiB

inflated  (logical_bytes - 16 on 90,546 of 92,199 slots, 98.22 percent)
  +0x00  u64 0
  +0x08  u32 self-pointer, base 0x50000000, target in the last 64 bytes
  +0x0C  u32 0
  +0x10  root record, 0x90 bytes
  +0xA0  body
```

Measured on the whole population: 16 leading zero bytes in 92,199 of 92,199, zlib header at `+16` in 92,199 of 92,199, zlib header at `+0` in 0 of 92,199, `+0x08` word using the `0x50000000` base in 92,199 of 92,199, inflated length equal to declared logical minus 16 in 90,546 (98.22 percent), short in 1,653, over in 0 (source: `artifact: docs/formats/zbn.md` L67-L75).

Compression is plain zlib (RFC 1950 deflate wrapper), no encryption, no dictionary and no per-block table. One stream occurs in 35,759 slots, two streams in 56,440 (source: `artifact: docs/formats/zbn.md` L77-L83). The first-stream outputs include multiples of `0x10000` and those multiples minus 16 (source: L84). The detailed frequency list at L84 is internally inconsistent: its twelve listed counts sum to 61,653, exceeding the stated 56,440 two-stream slots, while its summary says 55,653. No frequency coverage percentage or universal boundary rule is adopted from that list; the original histogram must settle the discrepancy.

There is **no count or offset table for the blocks**. Streams are found by walking the stored range and testing zlib headers; two streams are the common case above 64 KiB (source: `artifact: docs/formats/zbn.md` L84). The 1,653 short chains are counted, not completed: 149 report a corrupt deflate stream and 1,504 end with stored bytes remaining but no further zlib header; everything up to the break inflates cleanly and carries the same root header (source: `artifact: docs/formats/zbn.md` L86, L181). Values are little-endian; stored ranges are sector-aligned in the archive and the payload carries no padding of its own (source: `artifact: docs/formats/zbn.md` L88).

The `+0x08` word is a self-pointer `0x50000000 | target`; its target lands in the final 64 bytes of the payload in 92,175 of 92,199 slots (99.97 percent) and points at a small trailer with two pointer fields and a 16-byte record ending in `0xFFFFFFFF` (source: `artifact: docs/formats/zbn.md` L121).

## Fields

Offsets are into the inflated payload. Confidence rates the offset, width and measured distribution; where the byte fact is solid but the semantic reading is an interpretation, the Meaning column says so (basis: `artifact: docs/formats/zbn.md` L90-L119).

| Offset | Width | Meaning | Confidence | Source |
|---|---|---|---|---|
| `+0x00` | u64 | zero word | measured | `artifact: docs/formats/zbn.md` L58, L67 |
| `+0x08` | u32 | self-pointer, base `0x50000000`, last-64-byte target in 92,175/92,199 | measured | `artifact: docs/formats/zbn.md` L59, L72, L121 |
| `+0x0C` | u32 | zero word | measured | `artifact: docs/formats/zbn.md` L60 |
| `+0x10` | u8 | shape type byte, `0x06` in 92,199 (semantic label inferred) | inferred | `artifact: docs/formats/zbn.md` L98 |
| `+0x11` | u8 | flags byte, `0x01` on root and `0x41` on an embedded child copy; bit reading unknown | inferred | `artifact: docs/formats/zbn.md` L99, L225 |
| `+0x12` | u16 | zero in 92,199; no reading | unknown | `artifact: docs/formats/zbn.md` L100 |
| `+0x14` | f32 | bounding radius, 0.0067 to 1,572.96, p5 10.46, p50 47.95, p95 110.11, never NaN | inferred | `artifact: docs/formats/zbn.md` L101 |
| `+0x18` | u64 | zero in 92,199; no reading | unknown | `artifact: docs/formats/zbn.md` L102 |
| `+0x20` | float3 | box corner A, finite world-scale coordinates | inferred | `artifact: docs/formats/zbn.md` L103 |
| `+0x2C` | f32 | margin, `0.005` in 91,442 and `0.65` in 757 | inferred | `artifact: docs/formats/zbn.md` L104 |
| `+0x30` | float3 | box corner B, finite world-scale coordinates | inferred | `artifact: docs/formats/zbn.md` L105 |
| `+0x3C` | u32 | constant `1` in 92,199; no reading | unknown | `artifact: docs/formats/zbn.md` L106 |
| `+0x40` | float3 + u32 `0` | centroid | inferred | `artifact: docs/formats/zbn.md` L107 |
| `+0x50` | float3 + u32 `0` | centre of gravity; equals the `+0x40` triple in 50,603 slots | inferred | `artifact: docs/formats/zbn.md` L108 |
| `+0x60` | float4 | volume and angular inertia placeholders; `(1,1,1,1)` in 51,695 slots (56.1 percent) | inferred | `artifact: docs/formats/zbn.md` L109 |
| `+0x70` | ptr | first sub-array, base `0x50000000`, in range in 92,199 | measured | `artifact: docs/formats/zbn.md` L110, L119 |
| `+0x78` | ptr | sub-array, equals `+0x80` in 92,199 | measured | `artifact: docs/formats/zbn.md` L111, L119 |
| `+0x80` | ptr | same array as `+0x78` | measured | `artifact: docs/formats/zbn.md` L112 |
| `+0x88` | ptr | fourth sub-array, base `0x50000000`, in range in 92,199 | measured | `artifact: docs/formats/zbn.md` L113, L119 |
| `+0x90` | u32 | zero in 92,199; no reading | unknown | `artifact: docs/formats/zbn.md` L114 |
| `+0x94` | u32 | zero in 92,199; no reading | unknown | `artifact: docs/formats/zbn.md` L115 |
| `+0x98` | u16, u16 | two counts, range 1 to 56, halves equal in 90,385 slots (98.03 percent) | measured | `artifact: docs/formats/zbn.md` L116 |
| `+0x9C` | u32 | constant `5` in 92,199; no reading | unknown | `artifact: docs/formats/zbn.md` L117 |

Every "measured" row above was checked offset by offset on all 92,199 slots; the first `0xA0` bytes of stream one inflate for every slot and all four `0x50000000`-based pointers resolve inside the declared logical size (source: `artifact: docs/formats/zbn.md` L119). Treating `+0x20` and `+0x30` as opposite corners, the half-diagonal matches the `+0x14` radius within 0.5 percent in 42,002 slots (45.6 percent) and within 11 percent in 90.8 percent; the radius is stored, not derived (source: `artifact: docs/formats/zbn.md` L132).

Body from `+0xA0`, located but not decoded: a 16-byte zero run, then 16-byte records of `u16` values with `0x7F` and `0xFFFF` sentinels; `0xFFFFFFFF` appears in the first 4 KiB of 63,526 payloads (68.9 percent); 16-bit index pools reach `0x2183` and `0x2470`; a repeated 16-byte family of two `f32` and four `u16` fields with constant `0xBE55` was observed on three payloads; a dense byte array of small values (`0x02`, `0x0F`, `0x11`, `0x14`, `0x15`) sits near the end of the largest payloads (source: `artifact: docs/formats/zbn.md` L123-L130). These are measured byte families, not field semantics (source: `artifact: docs/formats/zbn.md` L130).

## Decode status

**Grade B, partial structure.** Prefix and root-field checks cover all 92,199 slots; full chain inflation reaches the expected length on 90,546, with 1,653 short chains. The body record semantics, subtype, four sub-array contents and writer remain unresolved (sources: `artifact: docs/formats/zbn.md` L67-L75, L158-L183; `artifact: docs/coverage.md` L131).

The 16-byte-node reading is **refuted**. The pre-declared T-NODES test required a derivable count, every referenced value in range and a traversal from the declared root visiting exactly that many records. It passed 0 of 20 stratified slots: C2 in-range failed with mean fraction 0.670240 (only idx 19 reached 1.0), C3 closed in 0 of 20, and the stored `+0x98` count never equalled the length-derived count. Controls at stride 12, stride 20, base `+0xA4` and a foreign root all failed; one stride-20 sample closed, which is why a single closing sample is not evidence (sources: `artifact: zbn_nodes/report.md` L26-L83, L145-L185, L198-L200). The uniform-remainder clause also holds at the shifted base, so it does not pin the body start (source: `artifact: zbn_nodes/report.md` L177-L180). No layout was refitted after the negative result (source: `artifact: zbn_nodes/report.md` L207-L220).

**Reconciliation with the newest structural BVH evidence.** The BVH4 interior-node layout is now structurally decoded: an external public BVH4 document was adopted mechanically and checked against 141 retained diagnostic bodies, giving 141/141 header and end-word matches, 195,341 parsed nodes, 499,178 TRI0 pointers, 140/140 closed traversals and zero bad count, mask or pointer words (sources: `artifact: bvh_nodes/adopt.md` L14-L16 for the explicit external URLs, L21-L84 for the adopted layout, L153-L174 and L243-L266 for results and clause verdicts). The population probe for that family covered 22,440 slots from `zbft_slots.tsv`, with T2, T3 and T4 surviving 22,440/22,440 and T1 refuted by 469 counterexamples (sources: `artifact: bvh_population/summary.md` L6, L13-L16, L22-L25, L34-L39; `artifact: bvh_population/rows.tsv` L1-L2).

Neither artifact contains a type-`0x06` slot: the retained bodies are the 141-body diagnostic set of 140 BOX16 roots plus one TRI0 root (source: `artifact: bvh_nodes/adopt.md` L277-L278), and the population probe input is the `zbft` slot list (source: `artifact: bvh_population/summary.md` L6). The adopted BVH4 structure starts with a 64-byte header at body `0x100` and carries `flags == 0x81020006` (source: `artifact: bvh_nodes/adopt.md` L23-L31), whereas the type-`0x06` root is the measured 0x90-byte record at inflated `+0x10` with a `0x06` type byte (source: `artifact: docs/formats/zbn.md` L94-L119). The BVH result therefore settles the sibling BVH store types, not `zbn`, and does **not** upgrade this grade. The older line in `workspace: coverage_audit/out/tables.md` L9 that labels `zbn` `Classified` with "no payload decoder" is a stale coverage snapshot, superseded by `artifact: docs/coverage.md` L131 and the full-population checks in `artifact: docs/formats/zbn.md` L67-L75, L119. The older zbn subtype question (`composite, geometry or BVH`) stays open (source: `artifact: docs/formats/zbn.md` L222).

Write status is **W0, extract-only**. Rebuilding the container would be a copy because the body has no proven field map; no W1 or W2 claim is made (source: `artifact: docs/formats/zbn.md` L185-L189).

Recorded container/header proof commands, not re-run for this revision; operands follow the saved usage strings (`artifact: docs/formats/zbn.md` L193-L203):

```text
zbn_probe <census-csv> <archive-root> <out-dir> full
zbn_hdr <census-csv> <archive-root> <out-file> 00000006
```

## Verification

**Recorded commands, not re-run in this session.** All figures attributed to these tools come from their saved outputs; no decoder was executed to write this page (sources: `artifact: docs/formats/zbn.md` L193-L218; `artifact: zbn_nodes/report.md` L87-L105; `artifact: bvh_population/summary.md` L8; `artifact: bvh_nodes/adopt.md` L127-L138).

```text
cargo build --release --offline --bin zbn_report --bin zbn_probe --bin zbn_inv --bin zbn_win --bin zbn_hdr --bin strscan
zbn_report  <census-csv> <archive-root> <out-dir>
zbn_probe   <census-csv> <archive-root> <out-dir> <samples|full>
zbn_inv     <census-csv> <archive-root> <out-dir> 00000006 <dump|quiet>
zbn_hdr     <census-csv> <archive-root> <out-file> 00000006
zbn_win     <census-csv> <archive-root> <out-file> 00000006 <first|last>
strscan     <game-exe> phBound zbn 3
cargo build --release --offline --bin zbn_nodes
zbn_nodes.exe <census-csv> <archive-root> <out-dir> 20
cargo run --release --offline --bin bvh_pop_probe -- artifact: bvh_population
cd artifact: bvh_nodes
rustc -O adopt_scan.rs -o adopt_scan.exe
./adopt_scan.exe
```

Recorded results and what each established: census filter over a 312.7 MB CSV in 1.1 s at 287 MB/s yielded the 92,199 rows; header verification over 92,199 slots and 24 offset checks had 20 hold on all slots, the three inertia words on 56.1 percent and the count pair on 98.03 percent; the full pass covered 92,199 slots, 11.09 GB stored and 15.62 GB inflated in 183.7 s at 502 slots/s; 20 stratified selections across 3 roots and 4 header generations passed container and header checks; the string scan of a 120,181,760-byte image found `zbn` 1 hit and `phBound` 0 hits; two full passes produced identical histograms (source: `artifact: docs/formats/zbn.md` L205-L218). The `zbn_nodes` run took 1.134 s internal for 20 slots and all inflated to `logical - 16` after the disclosed extraction correction (source: `artifact: zbn_nodes/report.md` L100-L114). The BVH adoption scan ran in 1,053 ms for 141 bodies and 60,013,056 bytes (source: `artifact: bvh_nodes/adopt.md` L129-L137); the population probe ran in 0.507 s at 44,291.0 slots/s (source: `artifact: bvh_population/summary.md` L8-L9).

Independent checks of the recorded figures exist and were read, not rerun: `artifact: zbn_nodes/report.md` L187-L205 records a fast-worker recount that confirmed 0/20 closed and the control verdicts; `artifact: bvh_nodes/adopt.md` L306-L318 records a recount confirming 141/141 flags, 499,178 TRI0 pointers and 140/140 closed traversals; `artifact: bvh_population/verify_report.md` L7-L110 recomputed every `summary.md` number with native PowerShell reads and re-extracted five slots with a separate one-shot zlib script, with 22,440 data rows, 469 T1 failures and zero T2/T3/T4 failures.

**Fresh runs in this session.** Only targeted native PowerShell reads and line counts, no archive scan, no decoder and no Python:

```powershell
$rows = Get-Content 'artifact: bvh_population/rows.tsv'; $rows.Count
# rows_total_lines=22441; rows_data=22440 (22,440 header records, matching summary.md L13)
[math]::Round(100*92199/1255039,4)
# 7.3463 percent
Select-String -Path 'artifact: docs/coverage.md' -Pattern '0x06.*zbn'   # L131: Partial
Select-String -Path 'workspace: coverage_audit/out/tables.md' -Pattern '0x06.*zbn'   # L9: Classified
```

Fresh reads confirmed: `artifact: docs/formats/zbn.md` L27 totals, L67-L75 container invariants and L116 count pair; `artifact: zbn_nodes/report.md` L145-L162 refutation; `artifact: bvh_nodes/adopt.md` L243-L266 clause verdicts and L277-L278 sample scope; `artifact: bvh_population/rows.tsv` L1 header and L2 first data row (`idx 0`, `N 369`, `L 231`, `rootref_low3 4`, `T1..T4 = 1`). The fresh line count and the recorded 22,440-slot total agree. No fresh result changed a grade.

## Unknowns

1. **The subtype (composite, geometry or BVH).** Settling evidence: the factory behind code `0x06` must be disassembled and the child-record path read. The absence of `phBound` strings and stripped RTTI means no string-based shortcut exists (`artifact: docs/formats/zbn.md` L141-L142, L222). The newly decoded BVH4 store layout does not settle it because no type-`0x06` body was in that test (`artifact: bvh_nodes/adopt.md` L277-L278).
2. **Body record semantics.** Settling evidence: a discriminator that maps the 16-byte families to count, index pool and per-element flags and survives a shifted-base control; T-NODES failed all three pre-declared criteria on 20 of 20 (`artifact: zbn_nodes/report.md` L145-L185).
3. **The two counts at `+0x98` (1 to 56, equal in 98.03 percent) and constants `+0x3C = 1`, `+0x9C = 5`.** Settling evidence: an accessor or writer that consumes those offsets; 1,814 unequal-halve slots are unexplained (`artifact: docs/formats/zbn.md` L116-L117, L224).
4. **The `+0x11` flag bits (`0x01` root, `0x41` embedded copy).** Settling evidence: the branch that tests the bit; "is a child" is a guess, not a verified reading (`artifact: docs/formats/zbn.md` L99, L225).
5. **The 1,653 short chains (149 corrupt deflate, 1,504 with no second zlib header).** Settling evidence: a byte-level classification of the remaining stored tail as damage, a third compression form or an uncompressed tail (`artifact: docs/formats/zbn.md` L86, L226).
6. **The 757-slot `0.65` margin cohort.** Settling evidence: a join of those slots to a generation or shape family; at present `0.005` in 91,442 slots and `0.65` in 757 is only a distribution (`artifact: docs/formats/zbn.md` L104, L227).
7. **The `+0x08` trailer role (fixup target, owner back-reference or per-resource table).** Settling evidence: trace the consumer and classify the 24 exceptions to the last-64-byte observation; that observation holds on 92,175 of 92,199 slots (`artifact: docs/formats/zbn.md` L121, L228).
8. **Semantic target of each bound.** Settling evidence: a name or placement join from the 68,287 newly named slots (`artifact: name_verify/type_ranking.md` L50) to a world object; names alone supply no field semantics (`artifact: docs/formats/zbn.md` L229).
9. **Write path.** Settling evidence: a recompression plus game-load test; nothing has been written back (`artifact: docs/formats/zbn.md` L185-L189, L230).
10. **Older first-block histogram and printed means.** The listed histogram counts exceed the two-stream population, and the means disagree with exact byte totals (`artifact: docs/formats/zbn.md` L36-L43, L84). Settling evidence: recount the retained probe output histogram and calculate means directly from the exact census totals; no archive decode is needed for the means.

## Changelog

- 2026-11-26, supervising review: separated 92,199 readable root records from 90,546 complete inflations and 1,653 short chains; corrected T-NODES wording to 0/20 passes; resolved exact census counts; disclosed the impossible older histogram total and inconsistent printed means; corrected the last-64-byte observation to 92,175/92,199. Sources: `artifact: docs/formats/zbn.md` L36-L43,L67-L75,L84,L121; `artifact: zbn_nodes/report.md` L145-L162; `artifact: docs_complete/evidence/census_counts.json`.
- 2026-11-26. Created `artifact: docs_complete/zbn.md` from `artifact: docs/formats/zbn.md`, `artifact: zbn_nodes/report.md`, `artifact: bvh_nodes/adopt.md`, `artifact: bvh_population/summary.md`, `artifact: bvh_population/rows.tsv`, `artifact: bvh_population/verify_report.md`, `artifact: docs/coverage.md`, `artifact: name_verify/type_ranking.md`, `workspace: CONTEXT_HANDOFF.md` and `workspace: coverage_audit/out/tables.md`. Count placeholders resolved to 92,199 slots / 11,093,949,168 stored bytes / 17,156,781,648 logical bytes against the 1,255,039-slot denominator.
- 2026-11-26. Grade set to **B (partial structure)** on the measured root and chain: the body is located but not decoded and T-NODES passed 0/20 (`artifact: zbn_nodes/report.md` L145-L162).
- 2026-11-26. Stale `Classified` label in `workspace: coverage_audit/out/tables.md` L9 reconciled to `Partial` at `artifact: docs/coverage.md` L131; the older "no payload decoder" sentence is not repeated as current.
- 2026-11-26. Newest structural BVH evidence recorded as external and scoped to the BVH store types: URLs at `artifact: bvh_nodes/adopt.md` L14-L16, 141-body adoption at L153-L174, 22,440-slot population probe at `artifact: bvh_population/summary.md` L13-L25. No competitor project is named here and no external claim is presented as our own decode of type `0x06`.
- 2026-11-26. Name state updated from zero named (`artifact: docs/formats/zbn.md` L32) to 68,287 newly joined slots (74.06 percent) at `artifact: name_verify/type_ranking.md` L50; the two figures are different states, not a contradiction.
- 2026-11-26. No key, game asset, extracted payload, executable offset beyond the cited enum-table address, public-queue write or decoder run was produced for this page.
- 2026-11-26, audit repair: headings normalized to the eight exact names; count values re-verified against `artifact: docs/coverage.md:131` and `artifact: docs_complete_work/type_counts.tsv` (92,199 / 11,093,949,168 / 17,156,781,648). Grade unchanged at **B (partial payload structure)**; no decoder was run for this repair.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zbn.md`. No count was selected by modification time.

