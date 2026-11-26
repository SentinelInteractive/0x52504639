# ADAT payload family

Scope and grade: **C, signature/container layer only.** The local sources establish the
four-byte `ADAT` magic at stored offset zero, exact slot and byte totals and a partial
local observation about one stream-table word. They do **not** supply a per-slot bank
header map, a complete inflate audit, a stream/codec decoder or any writer. The reported
Opus path is an external pipeline claim, not a local measurement or a family-wide decode
result; no bank content is claimed decoded here.

## Identity

`ADAT` is a recognized payload signature, not a resource type code. All 71,676 members
have a null resource type word. The magic occupies **four bytes at stored `+0x00`** and
is reachable without inflation: the null-word audit records `zlib_off = -1` for all
71,676 slots, while PSIN, RBF0 and XML reach their magics only after an inflate step
(`artifact: _unknown_audit/section_signature.md:L5,L21,L65,L69`). The census label is
`ADAT@0` (`artifact: docs_complete/_evidence/signatures_b/family_magic.tsv:L2`;
`artifact: docs_complete/_evidence/signatures_a/census_aggregates.json:L538-L558`). Calling
every signature family an "inflated magic" would misdescribe this one.

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 71,676 | 1,255,039 | `artifact: docs/coverage.md:L174`, `:L7` |
| Stored bytes | 38,297,906,160 | 305,820,985,968 | `artifact: docs_complete/_evidence/signatures_b/all_families.tsv:L4`, `totals.tsv:L2-L3` |
| Logical bytes | 38,297,508,464 | 564,783,265,279 | same; `artifact: docs/coverage.md:L174`, `:L8` |

Every member belongs to the 92,614 signature-assigned subset of the 101,479 null-word
slots; the six-family sum is exact and the residual and nested-container thirds are
separate (`artifact: unknown_accounting.md:L7-L18,L33-L47`). The stored/logical difference
is a declared-size fact, not an audited padding rule
(`artifact: docs_complete/_evidence/signatures_b/all_families.tsv:L4`).
The signature and type tables partition the same slots independently and are never added
(`artifact: docs/coverage.md:L12-L16`).

Exhaustive root table from the per-slot aggregation
(`census_aggregates.json:L559-L578`):

**Root distribution.**

| Root | Slots | Evidence |
|---|---:|---|
| `pack/story000/story000.rpf` | 63,861 | `census_aggregates.json:L570-L573` |
| `audio.rpf` | 7,162 | same, `:L560-L563` |
| `pack/shared_minigame000/shared_minigame000.rpf` | 638 | same, `:L565-L568` |
| `pack/story000_restofworld/story000_restofworld.rpf` | 15 | same, `:L575-L578` |
| **Total** | **71,676** | `artifact: docs/coverage.md:L174` |

The only census type value is `<null>`
(`artifact: docs_complete/_evidence/signatures_a/census_aggregates.json:L593-L627`).

## Where it appears

The four-byte magic sits at the **stored** offset, so recognition uses raw archive
bytes, not an inflated prefix and not the resource `+0x10` type word
(`artifact: _unknown_audit/section_signature.md:L49,L65,L69`;
`artifact: unknown_accounting.md:L47`). The generic zlib-probe labels are
`not-zlib-at-0-or-16` for 71,616 slots and `inflate-error-or-truncated` for 60
(`census_aggregates.json:L548-L555`); these are probe labels, not evidence that a bank
is corrupt or that a particular padding rule applies. The stored slot layout itself is
not mapped by the cited census or audit.

## Layer status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/adat.md`.

## Fields if any

Only two field-level facts are locally available; neither is a bank header map.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| stored `+0x00` | 4 | `ADAT` magic, four ASCII bytes | measured | `artifact: _unknown_audit/section_signature.md:L5,L69`; `family_magic.tsv:L2` |
| bank stream-table word | 4 | `id[28:0] \| tag_count[31:29]`; low 29 bits are the AWC stream id, top three bits the per-stream tag count | measured | `artifact: audio_naming.md:L16-L21` |
| stream tag `0x55` | 1 | data tag in the validated music records | measured | `artifact: audio_naming.md:L43-L45` |
| stream tag `0x76` | 1 | format tag in the validated music records | measured | `artifact: audio_naming.md:L43-L45` |
| stream tag `0x48` | 1 | streamed-music descriptor; 16 bytes per channel hold id, samples, rate, codec | measured | `artifact: audio_naming.md:L43-L46` |
| bank header/stride/version | Not specified | no supported local field map | unknown | `artifact: docs/coverage.md:L174` |

The stream-table and tag observations were measured while matching 1,589 of 1,589
music records by id and duration against 69,679 banks in `audio_catalog.csv`
(`artifact: audio_naming.md:L41-L65`). That is a *narrow naming-join probe*, not a
per-slot decode audit of all 71,676 banks; its offsets are relative to the parsed AWC
record, not general `ADAT` bank offsets. An earlier statement that the container
carries no stream id is explicitly retracted there (`artifact: audio_naming.md:L20-L21`).
Any fuller bank layout would be external attribution and is not imported as a local
measurement.

**Source classification retained.**

### Decode status

Grade C. The coverage page calls this family Partial because an audio pipeline reads
banks through to Opus, but the same row states there is no per-slot decode audit and no
format report (`artifact: docs/coverage.md:L174,L211`). That pipeline statement is
**external** to the local measurements on this page; no URL was fetched and no external
field layout is promoted here. The independent raw-byte re-probe confirms only the
signature, not payload semantics
(`artifact: _unknown_audit/section_signature.md:L47-L61,L99-L103`). No encoder,
round trip, game-load test or writer is reported (`artifact: docs/coverage.md:L193-L196`).

## Verification

- Rust census aggregation, release/offline:
  `census_agg.exe artifact: type_census.csv artifact: docs_complete/_evidence/signatures_b`
  → `data_rows: 1255039`, `stored_bytes: 305820985968`,
  `logical_bytes: 564783265279`, zero integrity issues
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`; `README.md:L10-L19`).
- Bounded PowerShell re-sum of the published type and signature tables reproduced both
  totals exactly (`artifact: docs_complete_work/format_evidence.md:L40-L50`).
- Independent signature re-probe: SplitMix64 seed `0x52504639`, k=400 per family,
  `min(stored,8192)` bytes read directly; ADAT 400 sampled / 400 agreements / 400 exact
  `@0`, zero inner-zlib path
  (`artifact: _unknown_audit/section_signature.md:L47-L61`, `:L53`, `:L88-L95`).
- Local naming-join check: 1,589/1,589 id matches and 1,589/1,589 duration checks,
  maximum duration error 0.00100 s (`artifact: audio_naming.md:L51-L65`).
- Negative local probe: no `ADAT` at the tested offsets in `anim.rpf`
  (`artifact: animation_feasibility.md:L19-L24,L41-L44`).
- No external URL was fetched for this page.

## Unknowns

- No per-slot decode audit and no ADAT format report in the cited local sources
  (`artifact: docs/coverage.md:L174,L211`).
- No verified bank header, version, stream index or codec configuration map
  (`artifact: docs_complete/_evidence/signatures_b/README.md`).
- The 60 `inflate-error-or-truncated` probe labels are not explained as bank damage or
  as a distinct shape (`census_aggregates.json:L548-L555`).
- Writer behavior, round-trip fidelity and game acceptance remain unverified
  (`artifact: docs/coverage.md:L193-L196`).

## Changelog

- 2026-11-26: Earlier page recorded exact counts, four roots, null-word membership and
  the distinction between the reported Opus path and a census-wide decode
  (`artifact: docs_complete/signatures/adat.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, grade C, stored-offset and
  four-byte magic width made explicit, locally measured stream-table/tag facts added
  with their narrow scope, and the external pipeline claim marked external. No count
  changed; no other file modified.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/adat.md`. No count was selected by modification time.


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
