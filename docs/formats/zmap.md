# `zmap` (type code `0x49`)

**Grade: C — container/wrapper only.** No type-specific beyond-container decoder is verified for `zmap`: no cited local artifact establishes a `zmap`-specific payload field map, record stride, encoder or game-load result. Family-level `0DRPz` wrapper, descriptor-table and text/localisation support exists, but it is family evidence, not a type-wide decode of `0x49`, and no decode count below is attributed to this code alone. Written 2026-11-26 from already-summarized local artifacts cited inline; no archive scan, executable read or new census aggregation was run for this page. Counts are index slots; nested-container byte sums overlap and are not unique physical bytes (`artifact: type_census.md`:7; `workspace: CONTEXT_HANDOFF.md`:section 4).

Short-path aliases used below, each resolving to a local artifact: `0drpz.md` = `artifact: docs/formats/0drpz.md`; `drpz-localisation.md` = `artifact: repo-publisher/docs/drpz-localisation.md`; `drpz_report.md` = `artifact: drpz_report.md`; `coverage.md` = `artifact: docs/coverage.md`; `tables.md` = `workspace: coverage_audit/out/tables.md` (older snapshot; its counts agree with `coverage.md`, its status column is not imported); `CONTEXT_HANDOFF.md` = `workspace: CONTEXT_HANDOFF.md`. Every citation is a local path with a line, section or recorded command output.


Additional citation aliases: `type_inventory.md` = `artifact: docs_complete_work/type_inventory.md`; `rpf9-container.md` = `artifact: repo-publisher/docs/rpf9-container.md`.

Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

- The resource type word at `+0x10` is `0x49`; the verified variant-0 label is `zmap` (`0drpz.md`:11-22; `CONTEXT_HANDOFF.md`:133-136).
- `0DRPz` is a payload signature at inflated `+0x10`, not the type word. Eight type codes carry it, including `0x49` (`0drpz.md`:9,16).
- The executable read records a store registration `0x49` -> `MapDataStore` (`artifact: docs/formats/zft.md`:97). That is an exe-path label, not a decoded payload or a field name used below.
- The type-word join and the census agree on every code and byte total for the family, delta zero (`0drpz.md`:32,101).
- Structural identity: a paged resource with a 16-zero prefix and zlib at `+0x10`, whose inflated stream holds a u64 zero, a virtual reference pointer, a `0x50`-byte root struct and a relative blob descriptor table (`0drpz.md`:36-53).
- Status is Partial in the current table (`coverage.md`:129). The older `tables.md` status column is not used.

## Counts

| Quantity | Value | Source |
|---|---:|---|
| Slots | 166,072 | `coverage.md`:129; `artifact: docs_complete_work/type_inventory.md` section 3; `0drpz.md`:16 |
| Stored bytes | 4,770,055,552 | `coverage.md`:129; `type_inventory.md` section 3 |
| Logical bytes | 8,063,899,008 | `coverage.md`:129; `type_inventory.md` section 3 |
| Denominator | 1,255,039 slots | `coverage.md`:164; `CONTEXT_HANDOFF.md`:11 |

The three type totals are taken from the independently verified inventory (Rust scan of `artifact: type_census.csv`: `data_rows: 1255039`, `distinct_type_hash_keys: 37`, `malformed_or_unparsable_rows: 0`; `type_inventory.md` sections 2-3), not from a scan run for this page. The share is the expression 166,072 / 1,255,039; no rounded percentage is asserted. Family-wide wrapper counts (`0drpz.md`:26-32) are a different scope and are not substituted for the `0x49` subset.

## Container

- Outer RPF9 archive: 64-byte header, two directory tables, payload region and trailer. Headers sit on 4 KiB boundaries; both table lengths and the trailer are multiples of 16 bytes (`artifact: repo-publisher/docs/rpf9-container.md`:3,9,29,104-110).
- Table 2 stride is `8 + low(0x2C)`, 9 or 10 bytes, length `ceil(stride * count / 16) * 16`, fitting 2,383 of 2,616 generation-4 headers (91.1 percent). For the high-2 group the count does not derive the record count, so that layout is unknown, not 16-byte records (`rpf9-container.md`:57-80).
- Each resource record is 20 bytes: logical size at `+0x00`/`+0x04` with masks, stored size at `+0x08`, offset at `+0x0C` in 16-byte units, type word at `+0x10` (`CONTEXT_HANDOFF.md`:99).
- Resource page: 16 zero bytes before zlib, outside both the compressed and the encrypted stream; zlib at `+0x10` with `78 01`, `78 5E`, `78 9C` or `78 DA` headers (`0drpz.md`:39-41,72; `rpf9-container.md`:90-94). Large resources split into consecutive 64 KiB pages, each its own zlib stream, stitched before parsing (`rpf9-container.md`:96).
- Alignment: the 16-byte zero prefix is a measured field and does not by itself imply page or stream alignment. The cited container page states that streams are 16-byte aligned and not necessarily 4 KiB aligned (`rpf9-container.md`:92); that is a general container-layer observation, not a `0x49`-slot histogram and not derived from the prefix. No type-specific alignment is established here, so alignment remains unknown.
- Chain status: a blob pointer resolves as `ptr - base` inside the same resource. The base is per resource, with observed values `0x50000000`, `0x60000000`, `0x40000000` and zero; do not assume one base (`0drpz.md`:55). No verified linkage exists between a root struct and a continuation page: overrunning pools are clamped to the stream end and the continuation dropped, not guessed (`0drpz.md`:64; `drpz-localisation.md`:117; `drpz_report.md`:108-110). Page-chain linkage is unknown.

## Fields

Offsets are labels relative to the resource stream or to the inflated root as stated. Integers are little-endian. Confidence is exactly one of measured, inferred, external, unknown.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| stream `+0x00` | 16 bytes | Zero prefix, outside compressed and encrypted stream | measured | `0drpz.md`:39,72 |
| stream `+0x10` | variable | zlib stream starting with `78 01`/`78 5E`/`78 9C`/`78 DA` | measured | `rpf9-container.md`:92-94 |
| inflated `+0x00` | 8 | u64 zero | measured | `0drpz.md`:42 |
| inflated `+0x08` | 8 | Virtual reference pointer | measured | `0drpz.md`:43 |
| inflated `+0x10` | 0x50 | Root struct start, magic `0DRPz` | measured | `0drpz.md`:44-45 |
| root `+0x10` | 4 | Variant word | measured | `0drpz.md`:46 |
| root `+0x18` | 8 | Pointer, target role not identified | unknown | `drpz-localisation.md`:25 |
| root `+0x28` | 8 | Virtual pointer to blob descriptor table | measured | `0drpz.md`:48 |
| root `+0x30` | 8 | Pointer, target role not identified | unknown | `drpz-localisation.md`:27 |
| root `+0x38` | 4 | Word before the count; reading it as descriptor count is wrong | inferred | `0drpz.md`:51,64 |
| root `+0x3C` | 4 | Low u16 descriptor count, high u16 other bits, semantics not established | unknown | `0drpz.md`:51 |
| descriptor `+0x00` | 4 | Blob id | measured | `0drpz.md`:52; `drpz-localisation.md`:39-45 |
| descriptor `+0x04` | 4 | Blob byte length | measured | `drpz-localisation.md`:44 |
| descriptor `+0x08` | 8 | Virtual blob pointer | measured | `drpz-localisation.md`:45 |
| blob `0x10` | variable | NUL-separated UTF-8 string pool | measured | `0drpz.md`:59 |
| blob `0x101` | 16 per record | Hash table `{u32 hash, u32 0, u32 ((n<<16) &#124; 1), u32 0}` | measured | `0drpz.md`:60 |
| blob `0xA8478889` | variable | Per-string offsets | measured | `0drpz.md`:61 |
| blob `0x99331089` | variable | Pool descriptor or schema blob | measured | `0drpz.md`:62 |
| hash `0x101` target | 4 | External key name, not the string text | unknown | `0drpz.md`:90 |
| unknown offset | unknown | No type-specific payload field or semantic interpretation is established | unknown | `artifact: docs/formats/0drpz.md:109-113`; `artifact: docs/formats/zft.md:97` (registration only) |

Two source contradictions are retained rather than silently reconciled. (1) Descriptor stride: `drpz-localisation.md`:39 calls the record "12-byte" while its own field list `u32 id`, `u32 len`, `u64 ptr` (`drpz-localisation.md`:41-45) totals 16 bytes, as does `0drpz.md`:52. This page uses the 16-byte total from the field widths and records the 12-byte label as a discrepancy. (2) Root count offset: `drpz-localisation.md`:28-29 labels both `root+0x38` and `root+0x3C` as descriptor counts, whereas `0drpz.md`:64 states that reading `+0x38` as the count is wrong; the verified count is the low u16 of `+0x3C`. Pointer guards must accept zero and unusual values because zero-length blobs and stubs are normal (`drpz-localisation.md`:35).

## Decode status

Grade C applies to the wrapper and descriptor layer only. Decoded at family scope: 16-zero prefix, zlib page stream, inflated root at `+0x10`, magic, variant word, descriptor table at `root+0x28`, the four text blob ids and the text-pool classifier (`0drpz.md`:36-64,78-90). No `zmap`-specific payload decode is established.

Recorded family wrapper/text decoder command, captured from a prior artifact and not re-run for this revision (`drpz_report.md`:188-202):

```powershell
cd "workspace: drpz"
cargo build --release --offline
.\target\release\drpz.exe --archive "data_rpf,pack__story000__story000_rpf,packs_rpf,pack__story000_restofworld__story000_restofworld_rpf" --out artifact: drpz
```

This is the recorded multi-archive family sweep, not a command proving a `zmap`-specific map decoder; no such local decoder is established (`0drpz.md`:109-113). Not decoded: any `zmap`-specific map payload, the targets of root `+0x18` and `+0x30`, the external key name behind blob `0x101`, continuation-page linkage, a `zmap`-only record stride or field map, the writer, and any round-trip or game-load acceptance (`0drpz.md`:90,94-96,109-113; `drpz_report.md`:174-186).

Scope caution: the sweep matches the `0DRPz` root magic inside four archives, not the `0x49` type word, and its signature-index figure is a different measure (`drpz-localisation.md`:98). The family results below are not `zmap`-only measurements.

## Verification

Fresh metadata check by the supervising worker, separate from the historical payload measurements below: the Rust counter selected `type_hash=00000049` from all 1,255,039 CSV rows and reproduced **166,072 slots**, **4,770,055,552 stored bytes** and **8,063,899,008 logical bytes**, with no schema or checked numeric parse errors. Source: `artifact: docs_complete/evidence/census_counts.json`, `types[name=zmap]`; method and supervising-worker rerun in `census_evidence.md`.

```powershell
rustc -O artifact: docs_complete/evidence/census_counts.rs -o artifact: docs_complete/evidence/census_counts.exe
& artifact: docs_complete/evidence/census_counts.exe
```

Captured measurements, all copied from prior artifacts and none re-run for this page:

- `0DRPz` signature at `+0x10` in 290,294 of 290,294 family slots; type-word join delta zero slots and zero bytes across all eight codes (`0drpz.md`:100-101). Scope: the full `0DRPz` family census.
- Four-archive sweep, 287,361 streams and 24,234,233,148 raw bytes: 68,412 classified `0DRPz` resources, 25,834 tables, 7,289,933 strings, 7,283,266 readable (99.91 percent), 0 invalid UTF-8, 0 control-bearing, 231,374,054 characters, 7,115,455 hash records, 5,752 schema groups (`drpz_report.md`:117-129; `0drpz.md`:80-88). Scope: `data`, `story000`, `story000_restofworld`, `packs`; not the whole install and not `zmap` alone.
- Classifier precision 0.9649 and recall 1.0000 on 2,000 streams; two consecutive runs gave byte-identical `tables.csv` (`0drpz.md`:88,103; `drpz_report.md`:147-149).
- 29 of 14,388 pools overrun, 0.20 percent, clamped and flagged (`drpz_report.md`:108-110).
- Reference table `data.rpf @ 0x1607010`: 4 blobs, 471 strings, locale `en`, printable ratio 1.0000 (`drpz_report.md`:153-154). No string content is carried here.

Captured decode command, from `drpz_report.md`:188-202 (shown in Decode status). Source file `workspace: drpz/src/main.rs` was confirmed present by a prior bounded PowerShell `Test-Path` check on 2026-11-26; no build or decode was run now. The counts above are captured measurements, not measurements made in this session. The only commands run for this repair were bounded local PowerShell read-only checks (`Get-ChildItem`, `Test-Path`, `Get-Item`) over the input artifacts and the source path. No decoder, archive scan, GPU job, game execution, Python batch work or publication was performed. Language of the captured tool: Rust, release, offline.

## Unknowns

- Which blob ids beyond the four text ids carry `zmap` map data, and their record layout. Settles: a `zmap`-only slot decode with field-level cross-checks, not a continuation of the family sweep.
- Role of root `+0x38` and of the high u16 at `+0x3C`. Settles: concordant reads over the complete table set plus an executable parse path consuming those words.
- External key name hashed into blob `0x101`. Settles: an independent key-name corpus; the text alone cannot yield it (`0drpz.md`:90).
- Continuation pages that overrun a stream. Settles: demonstrated page-chain linkage between a root struct and its continuation; currently dropped, not guessed (`drpz_report.md`:108-110).
- Per-resource virtual base selection. Settles: resolving each pointer against its own measured resource base; one global base is not established (`0drpz.md`:55).
- Type-specific alignment and stream-start histogram for `0x49`. Settles: a per-code histogram; the measured 16-byte prefix does not establish it (`rpf9-container.md`:92 is a general container observation).
- The 12-byte descriptor label in `drpz-localisation.md`:39 versus the 16-byte field total. Settles: a stride measurement that accounts for the discrepancy; the 12-byte prose is not imported.
- Whether a rebuilt wrapper would be accepted by the game. Settles: an encoder, a round-trip and a game-load test, none of which exists (`0drpz.md`:94-96,113).

## Changelog

- 2026-11-26, supervising verification: added the fresh Rust metadata-counter command and the independently rerun exact `0x49` slot/byte totals in Verification, without extending the wrapper-only decoding grade. Sources: `artifact: docs_complete/evidence/census_counts.json`; `artifact: docs_complete/evidence/census_evidence.md`.
- 2026-11-26, initial draft: header layout, descriptor table and blob ids taken from `artifact: docs/formats/0drpz.md`, `artifact: repo-publisher/docs/drpz-localisation.md` and `artifact: drpz_report.md`; slot and byte counts left as placeholders pending a census worker.
- 2026-11-26, repair: replaced the three unresolved count placeholders with the independently verified 166,072 / 4,770,055,552 / 8,063,899,008 from `type_inventory.md` section 3 and `coverage.md`:129. Renumbered headings to the exact required order, changed self-grade B to C (wrapper only), added a five-column Fields table with a per-row Evidence column and per-row evidence, removed an external map-placement claim from an unrequested competitor reference, rewrote the alignment text so the 16-byte prefix does not imply page alignment, retained both source contradictions, added short-path alias explanations, and removed imported stale statuses. No decode, archive scan, GPU job, game execution or publication was performed.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zmap.md`. No count was selected by modification time. Reconciliation decisions: rejected the measured-flags interpretation of the high u16 at root+0x3C; its meaning is unknown (`artifact: docs/formats/0drpz.md:112`); rejected the unsourced map-entities/placements field and its invented offset label; retained only an unknown-offset limitation.

