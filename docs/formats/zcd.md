# `zcd` resources (type word `0x43`)

Decode scope, 2026-11-26. This page records what is actually established for type word `0x43`: the RPF9 container layer, the inflated-header field inventory, and a sampled near-end record hypothesis. The clip body, record semantics and writer are not decoded. Grade **B (partial payload structure)** on the plan scale A complete verified payload decode / B partial payload structure / C container or signature only / D identity and count only. Aggregate counts are resolved: 62,384 slots, 6,794,403,072 stored bytes, 11,262,899,120 logical bytes, from `artifact: docs/coverage.md:132` and `artifact: docs_complete_work/type_counts.tsv`; the slot denominator is 1,255,039 [coverage_audit/out/tables.md:42]. All work here is read-only: no game asset, key, encoder, GPU job or executable execution. The fresh batch count is Rust, std only [fresh command, section 6]. Externally sourced BVH work is cited by local artifact and SHA only, not as a local decode of `0x43` [artifact: bvh_nodes/adopt.md:8-16].


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

**Source alias resolution.** Every relative path and bare filename used below resolves to these absolute local artifacts; no other file of the same name is implied.

| Alias used in this page | Absolute local artifact |
|---|---|
| `zcd.md` | `artifact: docs/formats/zcd.md` |
| `adopt.md` | `artifact: bvh_nodes/adopt.md` |
| `summary.md` | `artifact: bvh_population/summary.md` |
| `verify_report.md` | `artifact: bvh_population/verify_report.md` |
| `report.md` | `artifact: bvh_nodes/report.md` |
| `context.md` | `artifact: type_reports/out/context.md` |
| `type_ranking.md` | `artifact: name_verify/type_ranking.md` |
| `priority_2026-11-26.md` | `artifact: priority_2026-11-26.md` |
| `zpm_findings.md` | `artifact: type_reports/out/zpm_findings.md` |
| `type_census.csv`, `rows.tsv` | `artifact: type_census.csv`, `artifact: bvh_population/rows.tsv` |
| `zpm.md`, `zft.md`, `zbft.md`, `zbn.md` | `artifact: docs/formats/<name>` |
| `tables.md` | `workspace: coverage_audit/out/tables.md` |
| `CONTEXT_HANDOFF.md` | `workspace: CONTEXT_HANDOFF.md` |
| `zbn_hdr.rs`, `zbn_inv.rs` | `workspace: sentinel-rpf9-core/src/bin/<name>` |

- The resource descriptor type word is `0x43`; the recorded variant-0 label is `zcd` [artifact: docs/formats/zcd.md:1,7]. The label alone does not establish payload semantics [zcd.md:7; artifact: type_reports/out/context.md:20-21].
- The executable PE string xref registers `0x43` with the class string `ClipStore`: `lea` at `0x145badf3c`, `mov r8d,0x43` at `0x145badf43`, in the shared store-registration pattern [type_reports/out/context.md:22-27]. Separate call sites with the same initializer pattern carry `0x0f` `BvhDrawableStore`, `0x10` `BvhDwdStore`, `0x11` `BvhFragmentStore`, `0x46` `MotionStore` and `0x4e` `AnimStore` [context.md:24-29; artifact: docs/formats/zft.md:97; artifact: docs/formats/zbft.md:11]. This establishes a store-class string, not a clip decoder.
- The bounded-prefix census records these slots under the unknown inner-signature family, not a recognised inner magic [docs/formats/zcd.md:7].
- BVH scope note: the externally adopted BVH4 structure was tested on retained `zbft` bodies, while `zbdr` shares the serialized header in its separate sampled evidence [bvh_nodes/adopt.md:1-4,8-16; bvh_nodes/report.md:18-20; bvh_population/summary.md:6; artifact: docs/formats/drawables.md:224]. The Resource rows in the cited census excerpt under `pack/core_bvh4/core_bvh4.rpf` carry `0x0f`; two Binary rows have null type words [artifact: type_census.csv:92225-92244]. That excerpt is not a whole-root type census. No cited artifact assigns a BVH body to `0x43`.

## Counts

- Population: **62,384 slots**, **6,794,403,072 stored bytes**, **11,262,899,120 logical bytes**; denominator **1,255,039 slots** [coverage_audit/out/tables.md:42]. Share is `62,384 / 1,255,039` (`artifact: docs/coverage.md:132`; `artifact: docs_complete_work/type_counts.tsv`).
- These exact totals are recorded, not re-computed here (census is a separate worker), and agree across [artifact: docs/coverage.md:132; coverage_audit/out/tables.md:10; docs/formats/zcd.md:11; workspace: CONTEXT_HANDOFF.md:167].
- Recorded root split: `anim.rpf` 52,923, `levels.rpf` 170, `core_restofworld` 1, `core_restofworld001` 22, `shared_minigame000` 2, `story000` 9,189, `story000_restofworld` 77 [docs/formats/zcd.md:13-22]. Every slot has kind `Resource` [zcd.md:24]. Containing-header generations split 62,211 / 81 / 92 for generation 4 / 5 / 8 [zcd.md:26-30].
- Stale name note reconciled: the 2026-11-24 report records 1,525 dictionary matches and 60,859 unresolved hashes [zcd.md:32]. The 2026-11-26 join records 1,532 named before, 53,259 newly named (85.37 percent of type), 87.83 percent named now, 3,821,104,896 newly named stored bytes [artifact: name_verify/type_ranking.md:46-51; artifact: priority_2026-11-26.md:14]. The 1,525 figure is superseded for population naming; paths are not reproduced here [zcd.md:32; type_ranking.md:3-4].

## Container

- Stored layout: 16-zero prefix followed by zlib at stored offset `+0x10` [CONTEXT_HANDOFF.md:100; docs/formats/zcd.md:36]. The zero prefix was measured in 304 directly probed samples, not population-wide [zcd.md:36]. A zlib header at `+0x10` was read on all 62,384 slots [zcd.md:36,77].
- Page and block chain: a Rust chain walk reached the cap of declared logical size minus 16 in all 62,384 slots, allowing up to 128 bytes between streams; before the cap it found one stream in 32,072 slots, two in 30,310, three in two [zcd.md:38]. Many first-block output lengths are multiples of 64 KiB or 16 bytes less, an observation rather than a placement rule [zcd.md:38]. The release `zbn_inv` scan took 100.8 s for 62,384 slots, 619 slots/s, with a logical-minus-16 cap and 128-byte resynchronisation window [zcd.md:77].
- Alignment: the enclosing resource record stores sizes and offsets in 16-byte units [CONTEXT_HANDOFF.md:99], and the compressed page starts at stored `+0x10` [zcd.md:36]. No claim is made that a stream ends at the cap or that no later stream exists [zcd.md:38].
- Sampled near-end record: a pointer-like word at inflated `+0x08` minus `0x50000000` resolves to a 16-byte record near the inflated end; its first eight and last six bytes are zero with two intervening one-byte values, and the second byte is zero in 304 of 304 samples [zcd.md:40]. Reading it as a page map with virtual and physical page counts is a working hypothesis, not a verified semantic decode [zcd.md:40]. Thirteen values outside the strict `0x50xxxxxx` test must not be rejected on that ground; two large sampled resources resolve with larger offsets [zcd.md:57].

## Fields

Offsets are relative to inflated data; integers are little-endian [docs/formats/zcd.md:44]. Meaning entries use observed facts only; no field name is invented.

| Offset | Width | Meaning | Confidence | Source |
|---|---:|---|---|---|
| `+0x00` | 8 | Zero in all 62,384 headers; meaning unknown | measured | docs/formats/zcd.md:48 |
| `+0x08` | 8 | Upper 32 bits zero in all headers; low word begins with byte `0x50` in big-endian display in 62,371 headers; pointer reading sampled only | measured | docs/formats/zcd.md:49,40 |
| `+0x18` | 8 | Zero in all headers; meaning unknown | measured | docs/formats/zcd.md:50 |
| `+0x2c` | 4 | Zero in all headers; meaning unknown | measured | docs/formats/zcd.md:51 |
| `+0x4c` | 4 | Zero in all headers; meaning unknown | measured | docs/formats/zcd.md:52 |
| `+0x68` | 4 | 32-bit identifier on `zcd`, equal to the paired `zpm` `+0x68` in 729 of 729 re-inflated pairs with 729 distinct values; role inferred | measured | artifact: docs/formats/zpm.md:18,61; artifact: type_reports/out/zpm_findings.md:122 |
| `+0x90` | 4 | Nonzero in all headers; value 3 in 31,154; meaning unknown | measured | docs/formats/zcd.md:53 |
| `+0x94` | 4 | `0x01000000` in all headers; meaning unknown | measured | docs/formats/zcd.md:54 |
| `+0x98`, `+0x9c` | 4 each | Zero in all headers; meaning unknown | measured | docs/formats/zcd.md:55 |
| near inflated end | 16 | First eight and last six bytes zero, two intervening one-byte values, second byte zero in 304 samples; page-map reading inferred | inferred | docs/formats/zcd.md:40 |

The BVH4 header words at structure offsets `+0x00` through `+0x3c` in the adopted external layout are fields of `zbdr`/`zbft` bodies, not of `0x43` [bvh_nodes/adopt.md:25-41; bvh_nodes/report.md:1-4,23-34]. They are not entered in this field table.

## Decode status

- Grade **B (partial structure)**. Established: container layer and zlib prefix [docs/formats/zcd.md:36,77], chain reach to cap [zcd.md:38], header field inventory measured across all slots [zcd.md:46-55], pair identifier equality [docs/formats/zpm.md:18]. Not established: body record structure, object semantics, encoder [zcd.md:65,69,81]. Write status is W0 [zcd.md:69; CONTEXT_HANDOFF.md:201].

**Type-`0x43` container/header proof command, recorded and unexecuted here.** The tool usage strings are in `workspace: sentinel-rpf9-core/src/bin/zbn_hdr.rs:51` and `zbn_inv.rs:113`; the build line and sibling form are in `artifact: docs/formats/zbn.md:196-201`; the recorded rerun with type `00000043` is in `zcd.md:77`. This proves the container and header layer only, not the clip body [zcd.md:65,81].

```text
cargo build --release --offline --bin zbn_report --bin zbn_probe --bin zbn_inv --bin zbn_win --bin zbn_hdr --bin strscan
zbn_hdr <census-csv> <archive-root> <out-file> 00000043
zbn_inv <census-csv> <archive-root> <out-dir> 00000043 <dump|quiet>
```

The concrete `<census-csv>`, `<archive-root>`, `<out-file>` and `<out-dir>` values are not preserved in `zcd.md:77`; the `<dump|quiet>` operand is left exactly as in the tool usage string, with no claim about which mode was used [zbn_inv.rs:113].

- Stale "object identity undecoded" narrowed: the store-class string is measured as `ClipStore` by PE string xref [type_reports/out/context.md:27; docs/formats/zft.md:100], while the role of the clip record identifier remains a hypothesis [docs/formats/zpm.md:130; type_reports/out/zpm_findings.md:156]. The older coverage row saying "no payload decoder" remains correct for the body [coverage_audit/out/tables.md:10]; the handoff row saying "zlib at +0x10, header" matches grade B [CONTEXT_HANDOFF.md:167]. Registration resolves the class-string question but does not establish the body's dictionary or clip-record semantics; those require a reader trace and payload checks [zcd.md:81; context.md:27].
- Latest BVH structural evidence, exact scope: an external BVH4 layout fetched at SHA `bd6ba97ab6366777f76a080861017df5366f5a28`, with raw-file URLs recorded locally, was adopted as arithmetic only [bvh_nodes/adopt.md:8-16,18-21]. On 141 retained bodies the scanner measured flags 141/141, end words 141/141, level table 141/141, 195,341 nodes in 4,190 groups (1,218 BOX16 + 2,972 BOX32), child-count histogram `2:28,900`, `3:29,185`, `4:137,256`, zero bad count/mask and zero pointer errors, 499,178 TRI0 pointers and 140/140 closed traversals [adopt.md:129-138,153-175]. BOX16 masks are zero on every parsed node; 11,775 BOX32 f32 overrides on 2,260 nodes decode finite with 5,058 ordered min/max pairs, and `sceneBounds` containment is not testable [adopt.md:251-264,268-284]. Controls at `base+1` and `base+4` fail [adopt.md:191-212]. An independent recount confirmed these figures [adopt.md:306-336]. This is a `zbdr`/`zbft` result [bvh_nodes/report.md:1-4,18-20], and census rows for `pack/core_bvh4/core_bvh4.rpf` carry `0x0f` [type_census.csv:92225-92244]. It does not raise `0x43` above grade B.
- Population header rules for the sibling BVH type: 22,440 `zbft` slots, 0 read failures; T1 refuted with 469 counterexamples, T2, T3 and T4 survived 22,440/22,440 [bvh_population/summary.md:6-39]; independently recomputed with all checks passing except one non-claim equivalence [bvh_population/verify_report.md:3-6,9-27,70-77,100-110]. Multi-group candidates number 2,813 and are unverified beyond the first group [summary.md:47-76]. This is a header-field count only, with no decode or node indexing [summary.md:3-4].
- Grade A is not claimed: no cited artifact produces a complete `0x43` body decode [docs/formats/zcd.md:65,79-81]. A future body decode supplied by a separate worker would require revisiting this grade [zcd.md:81].

## Verification

**Recorded commands, unexecuted in this revision.** Replay form only: the cited artifacts preserve tool usage strings and aggregate results, not concrete private argument values, so path operands stay as placeholders as they are in the cited source [zbn_hdr.rs:51; zbn_inv.rs:113; artifact: docs/formats/zbn.md:193-203]. Nothing below was replayed to write this page.

```text
cargo build --release --offline --bin zbn_report --bin zbn_probe --bin zbn_inv --bin zbn_win --bin zbn_hdr --bin strscan
zbn_hdr <census-csv> <archive-root> <out-file> 00000043
zbn_inv <census-csv> <archive-root> <out-dir> 00000043 <dump|quiet>
cargo run --release --offline --bin bvh_pop_probe -- artifact: bvh_population
cd artifact: bvh_nodes; rustc -O adopt_scan.rs -o adopt_scan.exe; ./adopt_scan.exe
```

Results attributed to those recorded commands: release `zbn_hdr` for `00000043` read 62,384 headers with zlib at `+0x10`; release `zbn_inv` reported 100.8 s for 62,384 slots, 619 slots/s, with a logical-minus-16 cap and 128-byte resynchronisation window [zcd.md:77]. The BVH population probe ran in 0.507 s at 44,291 slots/s [summary.md:8-9]; the BVH adoption scan ran in 1,053 ms for 141 bodies and 60,013,056 bytes [adopt.md:127-138]. The `<dump|quiet>` operand is left as the tool's usage string; which mode was used is not recorded [zbn_inv.rs:113].

**Recorded figures without a preserved command line, unexecuted here.** The census scanner re-read all 1,255,039 CSV rows and joined 62,384 keys with zero mismatches for stored size, logical size, kind, name origin or path: 5.467 s, 229,548 rows/s; a separate join of 62,384 keys took 0.930 s, 67,069 keys/s [zcd.md:73]. The join does not decode payload [zcd.md:73]. A one-shot Python 3 probe read 8,192 bytes from one slot with `zlib.decompressobj` and a 512-byte output cap; its exact command line is not preserved, and a 300-record, 21.21 MB sample run was reported at 0.42 s [zcd.md:75,77]. No Python pipeline was run here or in the earlier drafting pass.

**Fresh command from the earlier drafting pass, not re-run in this revision.** Rust std only, no Python, no game data opened.

```text
cd workspace: temp; rustc -O zcd_scope_count.rs -o zcd_scope_count.exe; .\zcd_scope_count.exe
```

Source `workspace: temp/zcd_scope_count.rs`; input `artifact: bvh_population/rows.tsv`. Output: `rows=22440 ok=22440 bad_fields=0`, `rootref_low3={"0":1,"4":22439}`, `mg_group_1=2813`, `elapsed_ms=11`. This re-checks the BVH population scope only, not any `0x43` count, and is not a decoder or census run. Language: Rust 1.95.0, `rustc -O`, std only; no heavy decoder run and no GPU job.

## Unknowns

- Complete body structure and page semantics. Settling evidence: a full chain scan without an output cap plus a body field census over 62,384 slots; current chain results are cap-limited [docs/formats/zcd.md:38,81].
- Clip record semantics. Settling evidence: a static trace from the `0x43` registration site [type_reports/out/context.md:27] to the clip loader, checked against the 729 re-inflated `zpm` pairs [docs/formats/zpm.md:18]; the identifier role is inferred only [type_reports/out/zpm_findings.md:156].
- Zero prefix population-wide. Settling evidence: a 16-byte prefix check over all 62,384 slots; currently 304 samples [docs/formats/zcd.md:36].
- Near-end 16-byte record interpretation. Settling evidence: decode that record across all slots and test its two one-byte values against stream count [docs/formats/zcd.md:40].
- Residual unresolved names. Settling evidence: a further name source joined by root, header offset and slot [name_verify/type_ranking.md:8-13]; the 60,859 figure is stale relative to 87.83 percent named now [docs/formats/zcd.md:32; type_ranking.md:51].
- Writer, round-trip and game load. Settling evidence: an encoder and a parse-back test; status is W0 [docs/formats/zcd.md:69].

## Changelog

- 2026-11-24: the source format report established the container prefix, header field inventory, sampled near-end record, chain-cap observation and W0 status, with no body decoder [docs/formats/zcd.md:3,36-55,65,69,77]. The coverage table listed `0x43` as Classified with no payload decoder [coverage_audit/out/tables.md:10]; the handoff listed Partial [CONTEXT_HANDOFF.md:167].
- 2026-11-26: this page. Store-class identity reconciled as `ClipStore` [type_reports/out/context.md:27]; name counts reconciled to the 2026-11-26 join [name_verify/type_ranking.md:51]; the BVH structural decode bounded to `zbdr`/`zbft` with exact counts [bvh_nodes/adopt.md:153-175; bvh_nodes/report.md:1-4; type_census.csv:92225-92244]; grade B assigned with explicit scope [docs/formats/zcd.md:36-81]; fresh Rust population scope count recorded [fresh command, section 6]. No published number changed here and nothing was queued for publication.
- 2026-11-26 revision: source alias resolution added under Identity; type-`0x43` container/header proof command added to section 5 from the shared `zbn_hdr`/`zbn_inv` usage strings and the recorded rerun; section 6 split into fenced recorded/unexecuted replay blocks and a labeled earlier fresh scope count; the stale collision-versus-drawable Unknown removed after the measured `ClipStore` registration; clip-record semantics kept open [zbn_hdr.rs:51; zbn_inv.rs:113; artifact: docs/formats/zbn.md:196-201; type_reports/out/context.md:27; docs/formats/zcd.md:77,81]. No decoder run, census scan or publication added.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zcd.md`. No count was selected by modification time.

