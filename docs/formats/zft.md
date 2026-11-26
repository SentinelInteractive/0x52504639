# `zft` resources (type code `0x03`)

Local format record, 2026-11-26. **Decode limit:** the container layer is decoded across all **55,488 slots**; the inflated payload body and its object graph remain undecoded. No geometry, physics body, child list or material binding has been read out of a `zft` payload, and no mesh, texture or text has been exported from this type. Write status **W0**; no encoder or round-trip exists. Sources: `artifact: docs/formats/zft.md`, Decode and Encode; `artifact: zft_final.txt` L1-L13.

**Grade B (partial structure).** Scope: container layer decoded on every slot, root-field layout partially measured; body graph and object semantics undecoded. The older Classified label in `workspace: coverage_audit/out/tables.md`, row `0x03`, is superseded by Partial in `artifact: docs/coverage.md:133`; its "no payload decoder" limitation still applies to the body.

Index denominator throughout is **1,255,039 census slots**, including Resource and Binary rows. Fresh type totals come from `artifact: type_census.csv`, filter `type_hash=00000003`, as aggregated by `artifact: docs_complete/evidence/census_counts.rs` and retained in `census_counts.json`. Recorded payload-probe breakdowns below remain historical measurements, not new decodes.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The resource descriptor type word is `0x03`. The executable's type-name table at `0x1462fcd30 + variant*0x98 + code*8` resolves variant 0 to `zft` (entry `0x1462fcd48` → string at `0x14677a829`). Strings `ift` and `#ft` are present in the candidate variant-1/2 slots at `0x14677a831` and `0x14677a877`; their discriminant meanings and runtime use are unverified. Sources: `artifact: docs/formats/zft.md`, Exe path; `artifact: zft_exe.txt`; `workspace: CONTEXT_HANDOFF.md:136`.

The payload carries no inner magic; the bounded-prefix census put every slot in "inflate succeeded, no recognised signature", which is why `zft` sits in the `none` signature family. (Sources: `artifact: docs/formats/zft.md`, Identity; `workspace: coverage_audit/out/tables.md`, signature-family row `none`.)

Measured: the strong same-name-hash relation is to type `0x11`, whose store registration says `BvhFragmentStore`. The interpretation as a base fragment asset is inferred from that relation, not a decoded object class (sources: `artifact: zft_join.txt` L4; `artifact: docs/formats/zft.md`, Identity).

- 22,438 of 55,488 slots share a 64-bit TOC name hash with a type `0x11` slot; 22,438 of the 22,440 `0x11` slots are matched. The executable registers `0x11` as `BvhFragmentStore` at `0x145ba62d0` (`lea rdx,["BvhFragmentStore"]`, `mov r8d,0x11`, `call 0x1419ca0b0`), corroborated by 28 sibling registrations. Sources: `artifact: zft_join.txt` line 4; `artifact: docs/formats/zft.md`, Identity and Exe path.
- Zero `0x03` slots share a name hash with `0x02` (`zdr`), `0x05` (`ztd`), `0x0f` (`zbdr`), `0x10` (`zbdd`) or `0x12` (`zvert`). There is no drawable companion by hash. (Source: `artifact: zft_join.txt` lines 14-19.)
- The exe string scan found exactly one fragment-related class string, `BvhFragmentStore`; no `FragmentStore`, `fragType` or `fragDrawable`. No registration site carries `r8d = 3`, and the `0x02`–`0x06` core registration path was not located. (Source: `artifact: docs/formats/zft.md`, Exe path.)

Reading that the fragment and its drawable/physics bodies are stored inline in the same resource is **inferred**, not proven; see section 7.

## Counts

- Slots: **55,488** of the **1,255,039-slot** index. Stored bytes: **5,915,592,480**. Logical bytes: **14,211,185,152**. Exact slot share: **55,488 / 1,255,039**. Source: `artifact: docs_complete/evidence/census_counts.json`, `types[name=zft]`; input and replay command in `census_evidence.md`.
- **External, recorded claim only:** the older report says a published description agrees on all three totals; that external claim was not independently checked in this revision. Local totals stand on the census, not that claim. Source: `artifact: docs/formats/zft.md:19`.

Recorded breakdowns from `artifact: zft_census.txt`, produced by the census command in section 6; their totals agree with the fresh census aggregation above:

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `levels.rpf` | 50,802 | 5,783,431,008 | 13,803,288,000 |
| `packs.rpf` | 2,865 | 22,560,576 | 61,504,448 |
| `data.rpf` | 1,758 | 96,991,792 | 318,303,136 |
| `core_restofworld` | 53 | 11,278,736 | 23,998,096 |
| `shared_minigame000` | 10 | 1,330,368 | 4,091,472 |
| **Recorded total** | **55,488** | **5,915,592,480** | **14,211,185,152** |

| Header generation | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| 5 | 52,603 | 5,889,164,368 | 14,140,076,720 |
| 4 | 2,865 | 22,560,576 | 61,504,448 |
| 8 | 20 | 3,867,536 | 9,603,984 |

Every slot is kind `Resource`; every root has generation 4; all 55,488 name hashes are distinct (0 duplicate slots). Name origins: 50,362 dictionary matches (5,524,453,312 stored / 13,295,000,576 logical) and 5,126 unresolved hashes (391,139,168 / 916,184,576). Names are not reproduced here.

Recorded size distribution over all 55,488 rows: stored min 1,456, p25 9,184, median 26,288, p75 70,992, p95 311,120, max 9,343,728; logical min 4,448, p25 24,672, median 65,472, p75 168,768, p95 771,760, max 26,028,240. Logical/stored ratio 1.301 to 14.080, median 2.513; `logical == stored` occurs zero times. (Sources: `artifact: zft_census.txt` lines 1-44; `artifact: docs/formats/zft.md`, Counts.)

## Container

Verified on the whole population, not a sample. (Source for every figure in this section: `artifact: zft_final.txt` lines 1-13; `artifact: docs/formats/zft.md`, Container.)

- **Prefix:** stored `+0x00..+0x0F` is sixteen zero bytes in all 55,488 slots (`zero_prefix_run_top=[(16, 55488)]`).
- **Compression:** stored `+0x10` begins a standard zlib stream (`78 da` in sampled slots) in all 55,488 slots; no slot lacks a head and no earlier head was found at `+0`, `+8`, `+32` or `+48` (`zlib_head_offset={16: 55488}`).
- **Stream chain / alignment:** each slot holds 2, 3 or 4 streams (2 in 34,234, 3 in 19,009, 4 in 2,245). Each stream after the first begins at the next 16-byte-aligned stored offset. Measured gap from the end of one stream's compressed bytes to the next head is 0 in 60,434 boundaries and 1..15 otherwise; no boundary exceeds 15 bytes. All-zero padding cannot pass the `CMF` test, so a head found in a gap is a real stream head.
- **Inflate:** zero errors (`inflate_err={}`). The concatenation of a slot's streams is exactly `logical − 16` bytes on all 55,488 slots: decoded total 14,210,297,344 against 14,211,185,152 − 55,488 × 16 = 14,210,297,344; `len_exact=55488`, `len_short=0`, `len_long=0`. For `zft` the declared logical size **includes** the 16-byte prefix; contrast `zdd`/`zbdd`, which exclude it. (Sources: `artifact: zft_final.txt` line 13; `workspace: CONTEXT_HANDOFF.md`, section 5; `artifact: public_queue/zft.md`, Container.)
- **Pages / blocks:** the most common intermediate stream output is 65,536 bytes (7,615 occurrences), then 131,072 (3,988) and 196,608 (2,266). The older format report records an intermediate output of 25,362,432 bytes (`artifact: docs/formats/zft.md:64`), disproving a universal 64 KiB stream cap; it does not establish the absence of every possible cap. **Unknown:** the encoder's split rule. Only 2 slots have every intermediate boundary on a 64 KiB multiple (`all_intermediate_boundaries_64k={0: 55486, 1: 2}`), and only 8,594 have stream count equal to `ceil((logical−16)/65536)` (`stream_count_equals_ceil_64k_pages={0: 46894, 1: 8594}`). Those two proposed population-wide page rules are false. Source for the distributions and tests: `artifact: zft_final.txt` lines 6-11.
- **No page map, table of contents or trailer** exists outside the streams. After inflation the payload starts with eight zero bytes, then virtual pointers (section 4); nothing in the stored prefix other than the sixteen zeros describes block layout. (Source: `artifact: docs/formats/zft.md`, Container.)

## Fields

Offsets are relative to the concatenated inflated payload, little-endian. The engine exposes no symbol labels for these words, so offset labels are used throughout. In the Confidence column: **measured** = direct measurement of the stated observation; **inferred** = interpretation from indirect evidence; **external** = from an outside implementation; **unknown** = no evidence for a semantic claim. (Source for conventions: `artifact: docs/formats/zft.md`, Fields.)

| Offset | Width | Meaning | Confidence | Source |
|---|---|---|---|---|
| `+0x00` | 8 | Zero in all 55,488 slots; first four and first eight bytes zero everywhere; semantic role not established | measured | `artifact: zft_final.txt` L14-L18; `artifact: docs/formats/zft.md` Fields |
| `+0x08`, `+0x10`, `+0x18`, `+0x20`, `+0x28` | 8 each | Five 64-bit fields. High word zero in all 277,440. Low word zero or a `0x50000000`-based virtual pointer whose target falls inside the payload; 45,390 slots have all five resolving, 10,098 exactly two. Targets are not monotonically ordered in any slot; 229,291 of 247,146 resolved targets start with a zero word. Semantics unknown | measured | `artifact: zft_final.txt` L20-L27; `artifact: docs/formats/zft.md` Fields |
| `+0x30` | 8 | Four `u16`: `0001 0001 0001 0001` in 18,702 slots, `0001 0001 0001 0002` in 3,295, `0001 0001 0002 0002` in 2,619, lone `0001` in the 10,098 two-pointer slots; role unknown | measured | `artifact: zft_final.txt` L28; `artifact: docs/formats/zft.md` Fields |
| `+0x60` | 16 | Four `f32`, small magnitudes (0.285, −5.1e−5 in one sample); measured on sampled slots only; role unknown | measured | `artifact: docs/formats/zft.md` Fields |
| `+0x90`, `+0xa8` | 8 each | Further `0x50000000`-based pointers in sampled slots; population-wide distribution not measured | inferred | `artifact: docs/formats/zft.md` Fields |
| `+0xb8` | 4 | `0x40000021` in 35,792 slots, `0x41010021` in 7,929, `0x40020061` in 1,983, `0x41030061` in 1,728, followed by other values in the `0x40`/`0x41` high-byte family; no semantic interpretation is established | unknown | `artifact: zft_final.txt` L29; `artifact: docs/formats/zft.md` Fields |
| `+0xc0..+0xc8` | 12 | Three `−1.0f` in 55,099 slots; role unknown | measured | `artifact: zft_final.txt` L30; `artifact: docs/formats/zft.md` Fields |
| `+0xcc` | 4 | `+1.0f` in 55,276 slots; role unknown | measured | `artifact: zft_final.txt` L31 |
| `+0xd0` | 4 | `0x3f333333` (0.7f) in 55,304 slots; role unknown | measured | `artifact: zft_final.txt` L32 |
| inside payload, variable | — | TOC name appears verbatim as a NUL-terminated string in 50,355 of 50,362 dictionary-matched slots (99.99 percent); distance from payload end spans under 1 KiB to 32 MB, so it is not a fixed trailer. The containing record is not identified | measured | `artifact: zft_final.txt` L34-L35; `artifact: docs/formats/zft.md` Fields |
| anywhere in payload | — | Every payload has at least 7 printable runs of 4 or more characters; 41,939 have 64 or more | measured | `artifact: zft_final.txt` L36 |

Non-field interpretations, kept out of the table: the inline drawable/physics reading is inferred (`artifact: docs/formats/zft.md`, Identity); the count agreement from the independent registry is external (`artifact: docs/formats/zft.md`, Counts).

## Decode status

**Grade B, partial structure.** Scope, honestly:

- Container layer decoded on all 55,488 slots: zero-prefix, zlib head, aligned stream chain, zero inflate errors, exact `logical − 16` identity. (Source: `artifact: zft_final.txt` L1-L13.)
- Root-field layout partially measured on all or sampled slots, as listed in section 4. There are no engine labels for these words.
- Body not decoded. Nothing beyond the eight leading zero bytes, the five `0x50000000`-based pointers, the measured constant blocks and the verbatim TOC name is interpreted. No geometry, physics body, child list or material binding has been read out; no mesh, texture or text exported. (Source: `artifact: docs/formats/zft.md`, Decode.)
- No encoder, no pack-back test, no game-load test; W0 extract-only in the limited sense that only the container layer can be extracted. Recompression would not reproduce the stream split, and the pointer fields are image-base-relative. (Source: `artifact: docs/formats/zft.md`, Encode.)

Recorded container-proof command, not executed in this revision; substitute the archive-root directory (source: `artifact: docs/formats/zft.md` L116-L120):

```text
zft_probe probe artifact: type_census.csv <archive-root> artifact: zft_final.txt full
```

## Verification

All commands and counts in this section are **recorded** from `artifact: docs/formats/zft.md`, Verification (lines 114-122) and the saved evidence files. **No fresh decode command was run for this document**: the task scope excludes heavy decoders and archive scans, and this write used native reads plus a single file write only. A fresh native check did confirm the evidence artifacts are present with sizes `zft_census.txt` 1,387 B, `zft_final.txt` 3,703 B, `zft_exe.txt` 26,195 B, `zft_join.txt` 3,880 B.

Recorded build: `cargo build --release --offline --bin zft_probe` in `sentinel-rpf9-core`; four subcommands `census`, `exe`, `join`, `probe`. (Source: `artifact: docs/formats/zft.md` L116.)

Recorded verification replay commands (same source; not executed here):

```text
cargo build --release --offline --bin zft_probe
zft_probe census artifact: type_census.csv artifact: zft_census.txt
zft_probe probe artifact: type_census.csv <archive-root> artifact: zft_final.txt full
zft_probe join artifact: type_census.csv artifact: zft_join.txt
```

| Command (recorded) | Exact counts and scope |
|---|---|
| `zft_probe census artifact: type_census.csv artifact: zft_census.txt` | 312.7 MB of CSV; 0.78 s / 401 MB/s in the format report, 0.83 s in the artifact header; 55,488 rows selected. Whole type population. |
| `zft_probe probe artifact: type_census.csv <archive-root> artifact: zft_final.txt full` | All 55,488 slots read and inflated in 90.31 s: 614 slots/s, 55.5 stored MB/s, 157.3 logical MB/s; 0 inflate errors; exact length on all 55,488; 14 stratified sample dumps. |
| `zft_probe exe <game-exe> artifact: zft_exe.txt` | 120,181,760 bytes scanned in 0.79 s (152 MB/s), 28 registration call sites, prologue and string scans. Executable read as PE data, never executed. |
| `zft_probe join artifact: type_census.csv artifact: zft_join.txt` | 1,255,039 rows in 9.57 s (131,122 rows/s) in `zft_join.txt:67`; the older prose reports 9.36 s / 134,082 rows/s, so timings disagree. The artifact's companion matrix has 22,438 `0x11` hits and 0 `0x02` hits. |
| `llvm-objdump -d --start-address=0x145b7cc00 --stop-address=0x145b7d100`; 3.7 MB disassembly `0x145978700..0x145cf2000` | Store registration sites read; exe never loaded or executed. |

Sources: `artifact: docs/formats/zft.md` L116-L122; `artifact: zft_census.txt` L1-L2; `artifact: zft_final.txt` L1, L13, L37; `artifact: zft_join.txt` L1, L4, L14, L67.

## Unknowns

Each item states the evidence that would settle it.

- **Object graph and semantics of the five root pointers, the `0x40`/`0x41` high-byte word family at `+0xb8`, and the `−1,−1,−1,+1, 0.7` constant block.** Settling evidence: a typed reader for the code-3 store that walks each pointer target and applies a field order, with results checked against decoded geometry. (Source: `artifact: docs/formats/zft.md`, Unknowns.)
- **Whether drawable and physics bodies are inline in the same resource, and whether the same-hash `zbft` is its acceleration-structure companion.** The name-hash relation is measured; the companion function is inferred. Settling evidence: a walked `zft` payload showing geometry/material/physics records, followed by the native geometry-fingerprint check against the candidate `zbft`. No `zdr` same-hash twin is established. Sources: `artifact: zft_join.txt` L4,L14-L19; `artifact: docs/formats/zft.md`, Identity and Unknowns; fingerprint-check precedent: `artifact: docs/formats/drawables.md:218`.
- **Stream split rule.** Alignment and the concatenation identity are proven; the encoder's cut positions are not. Settling evidence: an encoder-side trace, or a boundary invariant that survives the whole population (the two 64 KiB hypotheses already failed). (Source: `artifact: zft_final.txt` L9-L10.)
- **`zft` loader / code-3 store registration.** No site carries `r8d = 3`; the string scan found only `BvhFragmentStore`. Settling evidence: locate the `0x02`–`0x06` core registration path around `0x145b7cd10`-shaped initializers and read the code-3 store reader. (Source: `artifact: docs/formats/zft.md`, Exe path and Unknowns.)
- **33,050 slots with no same-hash `zbft`** (55,488 minus 22,438). Settling evidence: a subtype marker or another relation that classifies them; currently unexplained. Source: `artifact: zft_join.txt` L4.
- **Two `zbft` slots with no `zft` twin.** Settling evidence: identify their companion or an exception path. (Source: `artifact: docs/formats/zft.md`, Unknowns.)
- **5,126 unresolved name hashes.** Settling evidence: a name source outside the exhausted public namehash corpus. Names are not published here. (Sources: `artifact: zft_census.txt` L39; `workspace: CONTEXT_HANDOFF.md`, section 6.)

## Changelog

- **2026-11-26:** initial record from `artifact: docs/formats/zft.md` and the saved `zft_census.txt`, `zft_final.txt`, `zft_exe.txt`, `zft_join.txt` evidence. Fresh census totals were inserted from `artifact: docs_complete/evidence/census_counts.json`; no payload decoder was rerun. Corrected the distinction between hash matches and proven companions, variant-string confidence, the `0x40`/`0x41` word family, the overstated stream-cap conclusion and the conflicting historical join timings. Preserved the body and writer limitations.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zft.md`. No count was selected by modification time.

