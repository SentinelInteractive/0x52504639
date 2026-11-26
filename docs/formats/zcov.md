# `zcov` (type code `0x73`)

**Grade: C — container/wrapper only.** No type-specific beyond-container decoder is verified for `zcov`: no cited local artifact establishes a `zcov`-specific payload field map, record stride, encoder or game-load result. Family-level `0DRPz` wrapper, descriptor-table and text/localisation support exists, but it is family evidence, not a type-wide decode of `0x73`, and no decode count below is attributed to this code alone. Written 2026-11-26 from already-summarized local artifacts cited inline; no archive, executable or census rescan was run for this page. Counts are index slots; byte sums of nested containers overlap and are not unique physical bytes (`artifact: type_census.md`:7; `workspace: CONTEXT_HANDOFF.md`:section 4).

Short-path aliases used below, each resolving to a local artifact: `0drpz.md` = `artifact: docs/formats/0drpz.md`; `drpz-localisation.md` = `artifact: repo-publisher/docs/drpz-localisation.md`; `coverage.md` = `artifact: docs/coverage.md`; `tables.md` = `workspace: coverage_audit/out/tables.md` (older snapshot; its counts agree with `coverage.md`, its status column is not imported); `CONTEXT_HANDOFF.md` = `workspace: CONTEXT_HANDOFF.md`; `drpz_report.md` = `artifact: drpz_report.md`. Every citation is a local path with a line, section or recorded command output.


Additional citation aliases: `type_inventory.md` = `artifact: docs_complete_work/type_inventory.md`; `rpf9-container.md` = `artifact: repo-publisher/docs/rpf9-container.md`.

Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The `+0x10` resource descriptor word is `0x73`. The executable's variant-0 callback-table label is `zcov`; the same table carries `icov` and `#cov` for variants 1 and 2, which are reachable but unverified (`artifact: enum_variant_discriminant_report.md`:83,86; `CONTEXT_HANDOFF.md`:section 8). `0x73` is the last code in the callback table at `0x14618d9e0`, not a static-enum code (`0drpz.md`, "Exe path"; `artifact: enum_variant_discriminant_report.md`:93).

`0DRPz` is a payload signature at inflated `+0x10`, not the type word; eight codes share it, so the family is a wrapper, not one type (`0drpz.md`, "Identity"). The type-word join gives 8,415 slots for `00000073` (`artifact: type_census.json`, `by_family["0DRPz"].type_hashes`). The label is a three-letter tag; no payload-side semantic identification of `zcov` was verified in the cited artifacts, so none is claimed here. Status is Partial in the current table (`coverage.md`:146).

## Counts

| Code | Name | Slots | Stored bytes | Logical bytes | Evidence |
|---|---|---:|---:|---:|---|
| `0x73` | zcov | 8,415 | 758,246,352 | 2,773,527,664 | `coverage.md`:146; `artifact: docs_complete_work/type_inventory.md` section 3; `artifact: type_census.json`, `by_family["0DRPz"].type_hashes["00000073"]` |

The same totals appear in `CONTEXT_HANDOFF.md`, section 9. Family totals for all eight `0DRPz` codes are 290,294 slots, 12,137,708,928 stored bytes and 51,368,850,240 logical bytes; the type-word join and the census agree on every code and every byte total with delta zero (`0drpz.md`, "Counts" and "Verification"). Per-root splits are published for the family, not per code (`0drpz.md`, "Counts"); this page does not claim a per-code root split. Census denominator: **1,255,039** data rows (`coverage.md`:164).

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
| `+0x10` (`root+0x00`) | 5 bytes | ASCII `0DRPz` magic; 290,294 of 290,294 family slots | measured | `0drpz.md`, "Verification"; `artifact: type_census.json`, `by_family["0DRPz"].type_hashes["00000073"]` |
| `+0x20` (`root+0x10`) | u32 | Variant word; constant 2 over 14,388 tables | measured | `drpz_report.md`, layout block |
| `+0x28` (`root+0x18`) | u64 | Pointer | measured | `0drpz.md`, inflated-payload block |
| `+0x38` (`root+0x28`) | u64 | Pointer to the blob descriptor table | measured | `0drpz.md`, inflated-payload block; `drpz_report.md`, layout block |
| `+0x40` (`root+0x30`) | u64 | Pointer | measured | `0drpz.md`, inflated-payload block |
| `+0x48` (`root+0x38`) | u32 | Field with unresolved semantics; reading it as a u32 count is explicitly wrong | unknown | `0drpz.md`, "Container"; `drpz_report.md`, correction 2 |
| `+0x4C` (`root+0x3C`) | u32 | Low u16 = descriptor count, high u16 = other bits, semantics not established; the low-half reading is the verified count | unknown | `0drpz.md`, "Container"; `drpz_report.md`, correction 2 |
| descriptor entry | 16 bytes | `{u32 blob_id, u32 byte_len, u64 pointer}` per descriptor | measured | `0drpz.md`, "Container" |
| derived virtual base (not a stored field) | not applicable | Observed address bases `0x50000000`, `0x60000000`, `0x40000000` and zero; no physical field offset is asserted | measured | `0drpz.md`, "Container"; `drpz_report.md`, correction 3 |
| blob `0x10` | blob | NUL-separated UTF-8 string pool; all 25,868 pool rows use blob id `0x10` | measured | `drpz_report.md`, section 4, classifier table |
| blob `0x101` | 16-byte records | Hash table `{u32 hash, u32 0, u32 (n<<16) &#124; 1, u32 0}`; 7,115,455 records against 7,289,933 strings | measured | `0drpz.md`, "Container"; `drpz_report.md`, section 4 |
| blob `0xA8478889` | blob | Per-string offsets | external | `0drpz.md`, "Container" |
| blob `0x99331089` | blob | Pool descriptor | external | `0drpz.md`, "Container" |

Two source contradictions are retained rather than silently reconciled. (1) `drpz-localisation.md`:39 calls the descriptor a "12-byte" record while its own field list `u32 id`, `u32 len`, `u64 ptr` (`drpz-localisation.md`:41-45) totals 16 bytes, as does `0drpz.md`:52; the 16-byte field total is used here. (2) `drpz-localisation.md`:28-29 labels both `root+0x38` and `root+0x3C` as descriptor counts, while `0drpz.md`, "Container" says reading `+0x38` as the count is wrong; the verified count is the low u16 of `+0x3C`.

## Decode status

- Container layer: decoded at family scope. 290,294 of 290,294 family slots carry the `0DRPz` signature at `+0x10` (`0drpz.md`, "Verification"). No separate per-code container re-measurement for `0x73` is published, so none is claimed.
- Root and descriptor layer: decoded at family scope. Descriptor count comes from the low u16 at `root+0x3C`; out-of-range pointers occur in valid tables and 29 of 14,388 pools overrun and are clamped to the stream end (`0drpz.md`, "Container"; `drpz_report.md`, corrections 2 and 4).
- Text blob layer: decoded for blob `0x10` pools. The cited sweep reports 25,834 tables, 7,289,933 strings, 231,374,054 characters, 7,283,266 readable strings, zero invalid UTF-8 and zero control-bearing strings, with classifier precision 0.9649 and recall 1.0000 on a 2,000-stream sample (`0drpz.md`, "Decode"; `drpz_report.md`, sections 2 and 4). These are family-wide figures, not a per-code yield; no `0x73`-only yield was measured.
- Type payload semantics: **not decoded. Beyond-container decode is unavailable for this type.** The `0DRPz` root is parsed by the PSIN wrapper path, not by a separate text parser (`0drpz.md`, "Exe path"). No `zcov`-specific parser, record stride, count or field role is established by the cited artifacts. Status is Partial (`coverage.md`:146); the older `tables.md` status column is not imported.
- Write path: W0, extract-only; no encoder or round trip is verified and the external key-name hash is the main semantic gap (`0drpz.md`, "Encode"; `CONTEXT_HANDOFF.md`, section 9).
- Compression, block, alignment and chain: compression measured as zlib at stored `+0x10` for the family (`0drpz.md`, "Container") and string blobs as plain NUL-separated UTF-8 (`0drpz.md`, "Fields and limits"); any additional stage unknown. Block unknown: no per-type record stride beyond the descriptor. Alignment unknown: the measured 16-byte prefix does not establish page or stream alignment. Chain unknown: 29 of 14,388 pools overrun family-wide (`drpz_report.md`, correction 4), but chaining is not attributed and the known page is dropped (`0drpz.md`, "Unknowns").

## Verification

- Counts: `coverage.md`:146 and `type_inventory.md` section 3, cross-checked against `artifact: type_census.json`, `by_family["0DRPz"].type_hashes["00000073"]`, and `CONTEXT_HANDOFF.md`, section 9. All report 8,415 / 758,246,352 / 2,773,527,664.
- Census reproduction recorded in `artifact: type_census.md`, "Reproduction and verification": Rust release builds `cargo build --release --offline --features private-exe-toc --bin type_census` and `cargo build --release --offline --bin type_census_merge`, then `type_census <db> <root> <exe-data> <exact-root> <out.jsonl>` per root and `type_census_merge --out game-data: . --expect 1255039 <root-jsonl...>`. Merge: 1,255,039 records, zero malformed, 80.427 seconds, about 15,604 records/s; that is merge throughput, not aggregate scan throughput (`type_census.md`:111).
- Wrapper and sweep, copied from `0drpz.md`, "Verification": signature in 290,294 of 290,294 family slots; zero delta for all eight codes; 287,361 streams, 24,234,233,148 raw bytes, 2,072.1 MB/s; byte-identical table files across two runs; 0 invalid UTF-8 and 0 control characters in the sample. These are family-level figures, not `0x73`-measurements.
- Extractor commands, all Rust release and offline, recorded in `drpz_report.md`, section 7: `cd workspace: drpz`, `cargo build --release --offline`, then `drpz.exe --archive "data_rpf,pack__story000__story000_rpf,packs_rpf,pack__story000_restofworld__story000_restofworld_rpf" --out artifact: drpz` and the `--redact` / `--text` variants. The reported sweep measured 2,072.1 MB/s, 25,764 streams/s, 11.15 s wall (`drpz_report.md`, section 4). No verified per-type semantic decoder exists for `0x73`.
- No Python and no new command were run for this page; every number above is copied from the cited artifacts.

## Unknowns

- The external key-name hash behind blob `0x101`; the 32-bit record hash does not hash the string text under JOAAT, FNV-1a, MurmurHash3 or CRC-32 (`0drpz.md`, "Decode").
- Continuation pages that overrun a stream; the known page is dropped, not guessed (`0drpz.md`, "Unknowns"); 29 of 14,388 pools overrun (`drpz_report.md`, correction 4).
- Weak pools that fail the text classifier and the unresolved `roa`/`und` discrimination (`drpz_report.md`, section 6).
- The exact semantics of `root+0x38` and the high 16 bits of `root+0x3C` (`0drpz.md`, "Unknowns").
- Alignment for `0x73`: unknown. The 16-byte prefix does not establish page or stream alignment and no per-code histogram exists.
- The 12-byte descriptor label versus the 16-byte field total; retained, not resolved in favour of the prose.
- No `zcov`-specific payload semantics, count or stride is available in the cited artifacts. This is a scope limit, not a negative result about the game format.
- Whether a rebuilt pool would be accepted by the game; no test exists (`0drpz.md`, "Unknowns").

## Changelog

- 2026-11-26, initial page: sources used with no rescan and no number changed, including `tables.md`, `artifact: type_census.md`, `artifact: type_census.json`, `0drpz.md`, `drpz_report.md`, `coverage.md`, `artifact: enum_variant_discriminant_report.md` and `CONTEXT_HANDOFF.md`.
- 2026-11-26, repair: set Grade C explicitly with a first-paragraph beyond-container disclosure; added a five-column Fields table with a per-row Evidence column and retained both source contradictions; stated that the 16-byte prefix does not imply alignment; cited the current `coverage.md`:146 for status instead of the older snapshot's status column; and expanded short-path alias explanations. No counts, measurements or sources were added from outside the cited local artifacts.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zcov.md`. No count was selected by modification time. Reconciliation decisions: rejected the measured-flags interpretation of the high u16 at root+0x3C; its meaning is unknown (`artifact: docs/formats/0drpz.md:112`).

