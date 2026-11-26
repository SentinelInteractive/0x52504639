# `zldbmt` (type code `0x6f`)

**Grade: C — wrapper/container only.** Family-level text-blob interpretation exists: the shared eight-code `0DRPz` family has a decoded blob `0x10` NUL-separated UTF-8 pool, a blob `0x101` hash table and a classifier that labels localisation tables (`artifact: drpz_report.md`: sections 1 to 4). That interpretation is family evidence, not a type-wide decode, and is not attributed to `0x6f` slots. No type-specific beyond-container decoder is verified for `zldbmt`: no cited local artifact establishes a `zldbmt`-specific payload field map, record stride, encoder or game-load result. Written 2026-11-26 from already-summarized local artifacts cited inline; no extraction, archive scan or census aggregation was run for this page and the historical sweep was not rerun. A read-only `--help` proof of the currently available family extractor was supplied by the parent and is recorded in Verification. Counts are index slots; byte sums of nested containers overlap and are not unique physical bytes (`artifact: type_census.md`:7; `workspace: CONTEXT_HANDOFF.md`:section 4).

Short-path aliases used below, each resolving to a local artifact: `0drpz.md` = `artifact: docs/formats/0drpz.md`; `drpz-localisation.md` = `artifact: repo-publisher/docs/drpz-localisation.md`; `coverage.md` = `artifact: docs/coverage.md`; `tables.md` = `workspace: coverage_audit/out/tables.md` (older snapshot; its counts agree with `coverage.md`, its status column is not imported); `CONTEXT_HANDOFF.md` = `workspace: CONTEXT_HANDOFF.md`; `seven_types_census.parent_verified.txt` = `artifact: docs_complete/evidence/seven_types_census.parent_verified.txt`; `drpz_report.md` = `artifact: drpz_report.md`. Every citation is a local path with a line, section or recorded command output.


Additional citation aliases: `type_inventory.md` = `artifact: docs_complete_work/type_inventory.md`; `rpf9-container.md` = `artifact: repo-publisher/docs/rpf9-container.md`.

Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The `+0x10` resource descriptor word is `0x6f`. The executable's variant-0 callback-table label is `zldbmt`; the same table carries `ildbmt` and `#ldbmt` for variants 1 and 2, which are reachable but unverified (`artifact: enum_variant_discriminant_report.md`:80; `CONTEXT_HANDOFF.md`:section 8). `0x6f` resolves through the callback table at `0x14618d9e0`, not the static enum table (`0drpz.md`, "Exe path").

`0DRPz` is a payload signature at inflated `+0x10`, not the type word; eight codes share it, so the family is a wrapper, not one type (`0drpz.md`, "Identity"). The independent per-type census assigns all 30,511 slots of `0000006f` to family `0DRPz`, magic `0DRPz@16` and kind `Resource`, with one distinct value in each column (`seven_types_census.parent_verified.txt`, `[DISTRIBUTIONS] [0000006f]`). The type-word join gives the same 30,511 slots (`artifact: type_census.json`, lines 204 and 2897). The label is a tag; no payload-side semantic identification of `zldbmt` was verified, so none is claimed. Status is Partial in the current table (`coverage.md`:137).

## Counts

| Code | Name | Slots | Stored bytes | Logical bytes | Evidence |
|---|---|---:|---:|---:|---|
| `0x6f` | zldbmt | 30,511 | 217,945,568 | 680,928,064 | `coverage.md`:137; `artifact: docs_complete_work/type_inventory.md` section 3; `seven_types_census.parent_verified.txt`, `[PER_TARGET] [0000006f]` |

The independent census reports 0 zero-stored, 0 zero-logical, 0 zero-both, 0 unparsable-stored and 0 unparsable-logical for this code. The denominator is **1,255,039 all census data rows**, comprising **1,153,560 Resource** and **101,479 Binary** rows; 0 rows are malformed. The header is excluded. The seven target types together account for 235,446 slots, 18,437,133,488 stored bytes and 69,980,587,296 logical bytes (`seven_types_census.parent_verified.txt`, `[DENOMINATOR]`, `[ALL_ROWS_KIND_DISTRIBUTION]`, `[TOTALS]`, `[PER_TARGET]`). The per-code root split below is independently counted from the same CSV, not inferred from a family-wide table (`seven_types_census.parent_verified.txt`, `[PER_TARGET_ROOT]`).

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `data.rpf` | 14,482 | 122,807,568 | 383,112,352 |
| `pack/shared_minigame000/shared_minigame000.rpf` | 78 | 882,256 | 2,690,512 |
| `pack/story000/story000.rpf` | 15,951 | 94,255,744 | 295,125,200 |

## Container

Every slot in the family is a page resource: 16 zero bytes, a zlib stream at stored `+0x10`, then an inflated payload with a `0x50`-byte root struct at `+0x10` and a pointer-addressed blob table (`0drpz.md`, "Container"; `drpz_report.md`, layout block, confirmed on `data.rpf @ 0x1607010` and 25,834 tables). A blob pointer minus the resource's virtual base gives an offset inside that same resource; the base is per resource and is not one constant (`0drpz.md`, "Container"; `drpz_report.md`, correction 3). The 16-byte prefix is outside both the compressed and the encrypted stream (`0drpz.md`, "Fields and limits"); it is a measured field and does not by itself establish page or stream alignment, which stays unknown here. The descriptor fields `u32 id`, `u32 len`, `u64 ptr` total 16 bytes; see the retained discrepancy in Fields.

## Fields

Offsets are relative to the first inflated byte unless marked `stored`; `root+` offsets are relative to the `0x50`-byte root at `+0x10`. Integers are little-endian. Confidence is exactly one of measured, inferred, external, unknown: measured = observed in the cited data, external = taken from the cited artifact without a per-code re-measurement, inferred = derived from a cited rule, unknown = semantics not determined.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| stored `+0x00` | 16 bytes | 16 zero bytes before the zlib stream | measured | `0drpz.md`, "Container"; `drpz_report.md`, layout block |
| stored `+0x10` | zlib stream | Page starts with a zlib stream at stored `+0x10` | measured | `0drpz.md`, "Container" |
| `+0x00` | u64 | Zero in the inflated payload | measured | `0drpz.md`, inflated-payload block; `drpz_report.md`, layout block |
| `+0x08` | u64 | Reference pointer | measured | `0drpz.md`, inflated-payload block |
| `+0x10` (`root+0x00`) | 5 bytes | ASCII `0DRPz` magic; 290,294/290,294 family slots and all 30,511 slots of this code per the census magic column | measured | `0drpz.md`, "Verification"; `seven_types_census.parent_verified.txt`, `[DISTRIBUTIONS] [0000006f]` |
| `+0x20` (`root+0x10`) | u32 | Variant word; constant 2 over 14,388 tables | measured | `drpz_report.md`, layout block |
| `+0x28` (`root+0x18`) | u64 | Pointer | measured | `0drpz.md`, inflated-payload block |
| `+0x38` (`root+0x28`) | u64 | Pointer to the blob descriptor table | measured | `0drpz.md`, inflated-payload block; `drpz_report.md`, layout block |
| `+0x40` (`root+0x30`) | u64 | Pointer | measured | `0drpz.md`, inflated-payload block |
| `+0x48` (`root+0x38`) | u32 | Field with unresolved semantics; reading it as a u32 count is explicitly wrong | unknown | `0drpz.md`, "Container"; `drpz_report.md`, correction 2 |
| `+0x4C` (`root+0x3C`) | u32 | Low u16 = descriptor count, high u16 = other bits, semantics not established; the low-half reading is the verified count | unknown | `0drpz.md`, "Container"; `drpz_report.md`, correction 2 |
| descriptor entry | 16 bytes | `{u32 blob_id, u32 byte_len, u64 pointer}` per descriptor | measured | `0drpz.md`, "Container"; local Rust stride, see Verification |
| per-resource virtual base | u32 | Observed `0x50000000`, `0x60000000`, `0x40000000` and zero | measured | `0drpz.md`, "Container"; `drpz_report.md`, correction 3 |
| blob `0x10` | blob | NUL-separated UTF-8 string pool; all 25,868 pool rows use blob id `0x10` | measured | `drpz_report.md`, section 4, classifier table |
| blob `0x101` | 16-byte records | Hash table `{u32 hash, u32 0, u32 (n<<16) &#124; 1, u32 0}`; 7,115,455 records against 7,289,933 strings in the same four-archive sweep | measured | `0drpz.md`, "Container"; `drpz_report.md`, section 4 |
| blob `0xA8478889` | blob | Per-string offsets | external | `0drpz.md`, "Container" |
| blob `0x99331089` | blob | Pool descriptor | external | `0drpz.md`, "Container" |

Two source contradictions are retained rather than silently reconciled. (1) `drpz-localisation.md`:39 calls the descriptor a "12-byte" record while its own field list `u32 id`, `u32 len`, `u64 ptr` (`drpz-localisation.md`:41-45) totals 16 bytes, as does `0drpz.md`:52; the 16-byte field total is used here. (2) `drpz-localisation.md`:28-29 labels both `root+0x38` and `root+0x3C` as descriptor counts, while `0drpz.md`, "Container" says reading `+0x38` as the count is wrong; the verified count is the low u16 of `+0x3C`.

## Decode status

- Container layer: decoded at family scope. 290,294 of 290,294 family slots carry the `0DRPz` signature at `+0x10` (`0drpz.md`, "Verification"). No separate per-code container re-measurement for `0x6f` is published, so none is claimed; the census only classifies family/magic/kind for this code (`seven_types_census.parent_verified.txt`, `[DISTRIBUTIONS] [0000006f]`).
- Root and descriptor layer: decoded at family scope. Descriptor count comes from the low u16 at `root+0x3C`; out-of-range pointers occur in valid tables, and 29 of 14,388 pools overrun and are clamped to the stream end (`0drpz.md`, "Container"; `drpz_report.md`, corrections 2 and 4).
- Text blob layer: decoded for blob `0x10` pools. The cited sweep reports 25,834 tables, 7,289,933 strings, 231,374,054 characters, and 7,283,266 readable strings (`drpz_report.md`, section 4, extraction table). These are family-wide figures, not a per-code yield; no `0x6f`-only yield was measured.
- Type payload semantics: **not decoded. Beyond-container decode is unavailable for this type.** The `0DRPz` root is parsed by the PSIN wrapper path, not by a separate text parser (`0drpz.md`, "Exe path"). No `zldbmt`-specific parser, record stride, count or field role is established by the cited artifacts. Status is Partial (`coverage.md`:137); the older `tables.md` status column is not imported.
- Write path: W0, extract-only; no encoder or round trip is verified and the external key-name hash is the main semantic gap (`0drpz.md`, "Encode"; `CONTEXT_HANDOFF.md`, section 9).
- Compression, block, alignment and chain: compression measured as zlib at stored `+0x10` for the family (`0drpz.md`, "Container") and string blobs as plain NUL-separated UTF-8 (`0drpz.md`, "Fields and limits"); any additional stage unknown. Block unknown: no per-type record stride beyond the descriptor. Alignment unknown: the measured 16-byte prefix does not establish page or stream alignment. Chain unknown: 29 of 14,388 pools overrun family-wide (`drpz_report.md`, correction 4), but chaining is not attributed and the known page is dropped (`0drpz.md`, "Unknowns").
- Family extractor availability, fresh read-only proof: the parent ran `workspace: drpz/target/release/drpz.exe --help` with exit 0. Captured output is `artifact: docs_complete/evidence/drpz_help.txt`; it matches the CLI source `workspace: drpz/src/main.rs`:871-924, help branch 906-916. This proves a currently available family-level extractor, not a `0x6f` decoder. The sweep below is historical and was not rerun here; no extraction output was produced for this page and no per-type semantics are claimed.
- Historical sweep command, preserved as recorded and not rerun for this page (`drpz_report.md`, section 7):

```powershell
cd workspace: drpz
cargo build --release --offline
.\target\release\drpz.exe --archive "data_rpf,pack__story000__story000_rpf,packs_rpf,pack__story000_restofworld__story000_restofworld_rpf" --out artifact: drpz
.\target\release\drpz.exe --archive data_rpf --out artifact: drpz_redact --redact
```

## Verification

- Counts: `coverage.md`:137 and `type_inventory.md` section 3, cross-checked against `artifact: type_census.json` (lines 204, 2897) and `0drpz.md` (identity row `0x6f`). All report 30,511 / 217,945,568 / 680,928,064.
- Independent per-type census, Rust release (`rustc -O`), reproduced from the recorded command below. Result: denominator 1,255,039 data rows, 0 malformed; `0000006f` = 30,511 slots, 217,945,568 stored bytes, 680,928,064 logical bytes; 0 zero-stored, 0 zero-logical, 0 zero-both, 0 unparsable-stored, 0 unparsable-logical (`seven_types_census.parent_verified.txt`, `[TOTALS]` and `[PER_TARGET]`). A second run to `seven_types_census.debug.txt` reproduces every count exactly.

```powershell
cd artifact: docs_complete/evidence
rustc -O seven_types_census.rs -o seven_types_census.exe
.\seven_types_census.exe "artifact: type_census.csv" "artifact: docs_complete/evidence/seven_types_census.parent_verified.txt"
```

- The parent-verified census used Rust (`rustc -O`), reading 312,661,753 bytes and processing 1,255,039 rows in the recorded 0.660435 seconds (`seven_types_census.parent_verified.txt`, `[TIMING]` and `[DENOMINATOR]`). Timings from other runs are not attributed to this report.
- Wrapper and historical sweep, copied from `0drpz.md`, "Verification": signature in 290,294 of 290,294 family slots; zero delta for all eight codes; 287,361 streams and 24,234,233,148 raw bytes; byte-identical table files across two runs. These are family-level figures, not `0x6f` measurements.
- Historical sweep command, Rust release and offline, family-level, not rerun for this page: `Set-Location 'workspace: drpz'`, `cargo build --release --offline`, then `.\target\release\drpz.exe --archive "data_rpf,pack__story000__story000_rpf,packs_rpf,pack__story000_restofworld__story000_restofworld_rpf" --out artifact: drpz` (`drpz_report.md`, section 7). No verified per-type semantic decoder exists for `0x6f`.
- Fresh CLI proof, parent-run on 2026-11-26, read-only, exit 0. It proves the family extractor is currently available and nothing more:

```powershell
& "workspace: drpz/target/release/drpz.exe" --help
```

Output: `artifact: docs_complete/evidence/drpz_help.txt`. Source: `workspace: drpz/src/main.rs`:871-924, help branch 906-916. No extraction was run for this page and no per-type semantics are inferred.
- External attribution, not a local measurement: a prior process recorded a historical check on 2026-11-26 of an external copy at `https://raw.githubusercontent.com/SentinelInteractive/0x52504639/main/docs/drpz-localisation.md`. That URL was not re-fetched for this page, so no current external verification is asserted and the external text is not used as a measurement. The 12-byte-versus-16-byte discrepancy is verified locally from `drpz-localisation.md`:39,41-45 and retained above.
- No Python, no bulk decode, no archive scan and no new census aggregation were run for this page; every number above is copied from the cited artifacts. Language used for the cited census and decoder: Rust, release.

## Unknowns

Each item pairs the open question with a concrete settling action. No result for any action is claimed here.

- The external key-name hash behind blob `0x101`; the 32-bit record hash does not hash the string text under JOAAT, FNV-1a, MurmurHash3 or CRC-32 (`0drpz.md`, "Decode"). Settle: obtain an independent key-name corpus or a hash-to-name table in the executable, then test the 7,115,455 records for exact matches under one of those four functions on a held-out table; an exact match reproducing a known key name settles it.
- Continuation pages and page chaining; the known page is dropped, not guessed (`0drpz.md`, "Unknowns"); 29 of 14,388 pools overrun (`drpz_report.md`, correction 4). Settle: for each overrun pool, search subsequent magic-less pages for a string-boundary continuation in stream order and verify a whole-string join on held-out overruns.
- Weak pools that fail the text classifier and the unresolved `roa`/`und` discrimination (`drpz_report.md`, section 6). Settle: hand-label a fresh held-out sample of weak and `roa`/`und` pools, then re-run the classifier with a stricter Latin discriminator and report precision and recall against that sample.
- The exact semantics of `root+0x38` and the high 16 bits of `root+0x3C` (`0drpz.md`, "Unknowns"). Settle: vary those bits across a controlled sample of family streams and record which values change descriptor count or pointer resolution; agreement with the low-u16 count on a held-out set settles the field roles.
- Per-type block size, alignment and any compression stage beyond the measured zlib page are unknown; the 16-byte prefix does not establish alignment and no measurement establishes these for `0x6f`. Settle: run a bounded per-type offset probe over a held-out sample of the 30,511 slots and test descriptor and blob boundaries for a constant stride and alignment; a constant observed across that sample settles the layout claim.
- The 12-byte descriptor label versus the 16-byte field total is retained as a discrepancy; it is not resolved in favour of the prose. Settle: re-read the public page for a later correction and re-measure the descriptor stride on a fresh held-out sample; agreement of the corrected prose and the local stride settles the discrepancy.
- No `zldbmt`-specific payload semantics, count or stride is available in the cited artifacts. This is a scope limit, not a negative result about the game format. Settle: locate a type-code-to-parser registration for `0x6f` in the executable callback-table region and demonstrate a per-type parse on a held-out slot; without that the question stays open.
- Whether a rebuilt pool would be accepted by the game; no write test exists (`0drpz.md`, "Unknowns"). Settle: rebuild a pool and attempt to load it in the game on an owned copy, recording the load outcome; no such test exists here.

## Changelog

- 2026-11-26, final reconciliation: restored the parent-verified all-kind denominator and per-code root split; replaced rounded shares with exact counts; corrected the census timing attribution to the cited parent report. No extraction or new census scan was performed for this correction.

- 2026-11-26, initial page: sources used with no rescan and no number changed, including `tables.md`, `artifact: type_census.md`, `artifact: type_census.json`, `0drpz.md`, `drpz_report.md`, `artifact: enum_variant_discriminant_report.md`, `seven_types_census.parent_verified.txt` and `CONTEXT_HANDOFF.md`.
- 2026-11-26, repair: set Grade C explicitly with a first-paragraph beyond-container disclosure; added a five-column Fields table with a per-row Evidence column and retained both source contradictions; stated that the 16-byte prefix does not imply alignment; switched status citation to the current `coverage.md`:137 instead of the older `tables.md` status column; reattributed the external URL check as historical and not re-fetched; expanded short-path alias explanations. No counts, measurements or sources were added from outside the cited local artifacts.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zldbmt.md`. No count was selected by modification time. Reconciliation decisions: rejected the measured-flags interpretation of the high u16 at root+0x3C; its meaning is unknown (`artifact: docs/formats/0drpz.md:112`).

