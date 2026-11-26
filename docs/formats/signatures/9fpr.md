# 9FPR nested-container family

Scope and grade: **B, partial structural/container decode.** Enumeration of all 4,373
headers succeeds and 4,351 of 4,351 nested header lengths parse below their stored
extents, but the Table-2 formula resolves only 2,383 of 2,616 reported generation-4
headers with 233 exceptions unresolved, several field meanings are not supplied, and
RSA verification is locally 0 verified / 0 failed / 4,373 unknown. The published
coverage row says **Full** for this family; that is the source's container-read
classification, not an editorial grade A and not a complete container format. No
contained leaf format is decoded by this family status.

## Identity

`9FPR` is a **four-byte ASCII magic at stored `+0x00`** (`0x52504639`), identifying a
nested RPF9 container rather than a resource type code. All 4,351 members have a null
resource type word and are archive headers, not leaf payloads
(`artifact: docs_complete/signatures/container-layer.md`;
`artifact: unknown_accounting.md:L24-L27`). The census label is `9FPR@0`
(`artifact: docs_complete/_evidence/signatures_b/nullword_magic.tsv:L2`;
`artifact: docs_complete/_evidence/signatures_a/census_aggregates.json:L317-L337`). The
magic is read from **stored bytes with no inflate step**; `unknown_accounting.md:L27`
states these extents are stored raw and never deflated. The supplemental
`container-layer.md` describes the shared read model; this page counts only the 4,351
nested slots, while the 22 standalone roots are separate on-disk files, not additional
census slots (`artifact: unknown_accounting.md:L30`; `artifact: docs/coverage.md:L7`).

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 4,351 | 1,255,039 | `artifact: docs/coverage.md:L176`, `:L7` |
| Stored bytes | 147,279,874,016 | 305,820,985,968 | `artifact: docs_complete/_evidence/signatures_b/all_families.tsv:L3`, `totals.tsv:L2-L3` |
| Logical bytes | 147,279,874,016 | 564,783,265,279 | same; `artifact: docs/coverage.md:L176`, `:L8` |

Stored equals logical for every member (`artifact: unknown_accounting.md:L27`). Header
reconciliation is `22 roots + 4,351 nested = 4,373`
(`artifact: docs_complete/signatures/container-layer.md`; `artifact: unknown_accounting.md:L25`).
The older 4,375 total is superseded as internally contradictory, and 4,330 is an even
older correction in the handoff retraction table
(`artifact: docs_complete/signatures/container-layer.md`;
`artifact: docs_complete_work/type_inventory.md:L132`). Nested extents contain children
also enumerated in the flat slot list, so these byte sums are not unique physical
occupancy (`artifact: docs/coverage.md:L10`; `artifact: unknown_accounting.md:L30`).

Exhaustive root table (`census_aggregates.json:L338-L424`):

**Root distribution.**

| Root | Slots | Evidence |
|---|---:|---|
| `levels.rpf` | 2,050 | `census_aggregates.json:L354-L357` |
| `pack/core_bvh4/core_bvh4.rpf` | 1,281 | same, `:L364-L367` |
| `pack/story000/story000.rpf` | 441 | same, `:L394-L397` |
| `anim.rpf` | 235 | same, `:L339-L342` |
| `audio.rpf` | 103 | same, `:L344-L347` |
| `packs.rpf` | 59 | same, `:L409-L412` |
| `data.rpf` | 41 | same, `:L349-L352` |
| `navmeshes.rpf` | 28 | same, `:L359-L362` |
| `textures.rpf` | 20 | same, `:L419-L422` |
| `pack/story000_restofworld/story000_restofworld.rpf` | 18 | same, `:L404-L407` |
| `pack/core_restofworld/core_restofworld.rpf` | 10 | same, `:L374-L377` |
| `pack/shared_minigame000_bvh4/shared_minigame000_bvh4.rpf` | 8 | same, `:L389-L392` |
| `pack/shared_minigame000/shared_minigame000.rpf` | 49 | same, `:L384-L387` |
| `pack/story000/story000_script.rpf` | 4 | same, `:L399-L402` |
| `script.rpf` | 2 | same, `:L414-L417` |
| `pack/core_licenses/core_licenses_data.rpf` | 1 | same, `:L369-L372` |
| `pack/core_restofworld001/core_restofworld001.rpf` | 1 | same, `:L379-L382` |
| **Total** | **4,351** | `artifact: docs/coverage.md:L176` |

Counts per root equal `headers - 1` for all 22 roots; for 17 roots the nested count is
nonzero (`artifact: unknown_accounting.md:L25,L29`; `census_aggregates.json:L338-L424`).

## Where it appears

The fixed header is 64 bytes at stored offset zero; this is not the entire variable
header area (`artifact: docs_complete/signatures/container-layer.md`). The stored
extent header itself measures 592 to 1,926,016 bytes, median 4,704
(`artifact: unknown_accounting.md:L28`); that is a different measure from the fixed 64-byte
prefix and is retained as a scope distinction, not treated as a contradiction to be
resolved by guessing. Table 1 is a variable name/offset payload and Table 2 is a
directory index (`container-layer.md:L46-L47`). Table 2 stride is `8 + low(+0x2C)` with
extent `ceil(stride * count / 16) * 16`; it reproduces 2,383 of 2,616 well-formed
generation-4 headers, while 233 have high word 2 at `+0x20` and a larger table
(`container-layer.md:L50,L60`). The rule therefore must not be described as universal.

A common stored resource form is a 16-zero-byte prefix followed by zlib at stored
`+0x10`; that convention is separate from an inflated payload signature, and logical
size conventions differ by type (`zft` includes the prefix, `zdd` and `zbdd` exclude it)
(`artifact: docs_complete/signatures/container-layer.md`;
`artifact: docs/coverage.md:L234`).

## Layer status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/9fpr.md`.

## Fields if any

Offsets are relative to the archive header unless the row says resource record. Widths
are given only where a cited source states them; an unreported width is marked unknown
rather than inferred from a type name.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| stored `+0x00` | 4 | `9FPR` magic (`0x52504639`) | measured | `artifact: docs_complete/signatures/container-layer.md`; `nullword_magic.tsv:L2` |
| fixed header extent | 64 | fixed header, not whole variable area | measured | `container-layer.md:L39` |
| `+0x04` | unknown | header length, checked against stored extent | measured | `container-layer.md:L41`; `artifact: unknown_accounting.md:L26` |
| `+0x08` | unknown | table split separating variable regions | measured | `container-layer.md:L42` |
| `+0x1C`, `+0x30` | unknown | generation tags; no interpretation supplied | unknown | `container-layer.md:L43` |
| `+0x20` high word | unknown | value 2 in the 233 stride exceptions | measured | `container-layer.md:L50` |
| `+0x24` | unknown | container-local entry count | measured | `container-layer.md:L44` |
| low part of `+0x2C` | unknown | table-2 width input to the stride rule | measured | `container-layer.md:L45,L50` |
| Table 1 / Table 2 | variable | name/offset payload; directory index | measured | `container-layer.md:L46-L47` |
| resource record `+0x00`/`+0x04` | 4 each | logical-size words; mask details not specified by the summary | unknown | `container-layer.md:L48`; `artifact: docs/formats/script-resources.md:L51-L52` |
| resource record `+0x08` | 4 | stored size in 16-byte units | measured | `container-layer.md:L48`; `script-resources.md:L53` |
| resource record `+0x0C` | 4 | slot offset in 16-byte units, relative to containing archive | measured | `container-layer.md:L48`; `script-resources.md:L54` |
| resource record `+0x10` | 1 | type word byte; `<null>` for nested members | measured | `container-layer.md:L48`; `artifact: unknown_accounting.md:L35` |

The resource-record width evidence comes from the verified script-resource record
(`script-resources.md:L49-L56`), a generic RPF9 record, not from a nested-container
field decoder. No per-container field beyond the cited summary is asserted here.

**Source classification retained.**

### Decode status

Grade B. The published **Full** row is retained as the source classification
(`artifact: docs/coverage.md:L176`), but it is limited to container reading: header,
table split, trailer and signed index are enumerated for every header and the whole tree
parses with zero reported failures
(`artifact: docs_complete/signatures/container-layer.md`). The partial grade reflects
exact unresolved boundaries: the Table-2 formula succeeds on 2,383 of 2,616
well-formed generation-4 headers and leaves 233 exceptions
(`container-layer.md:L50,L60`; `workspace: CONTEXT_HANDOFF.md:L94-L104`);
generation tags and the logical-size masks have no supported interpretation
(`container-layer.md:L43,L48`); and RSA verification is a **local result** of
0 verified / 0 failed / 4,373 unknown because the signed message representation is
unresolved (`container-layer.md:L31,L61`; `CONTEXT_HANDOFF.md:L94-L104`). No contained
leaf format is decoded (`container-layer.md:L62`), and no encoder, round trip or
game-load claim is made (`artifact: docs/coverage.md:L193-L196`).

## Verification

- Rust census aggregation (release, offline):
  `census_agg.exe artifact: type_census.csv artifact: docs_complete/_evidence/signatures_b`
  → `data_rows: 1255039`, `stored_bytes: 305820985968`,
  `logical_bytes: 564783265279`, zero integrity issues
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`; `README.md:L10-L19`).
- Bounded PowerShell re-sum of both published tables reproduced the exact totals
  (`artifact: docs_complete_work/format_evidence.md:L40-L50`).
- Independent raw-byte audit: on-disk `9FPR` prefixes read for all 4,351 slots; header
  length parses in 4,351 of 4,351 and is below the stored extent in every case;
  `headers - 1` equals nested slots for each of the 22 roots
  (`artifact: unknown_accounting.md:L22-L31`;
  `artifact: _unknown_audit/section_signature.md:L80-L82`).
- The audit's CSV class and DB membership come from the same header table and are not
  independent; the on-disk prefix reads are independent
  (`artifact: unknown_accounting.md:L31`;
  `artifact: _unknown_audit/section_signature.md:L97`).
- No external URL was fetched for this page.

## Unknowns

- The signed message representation for the local RSA verifier is unresolved
  (`artifact: docs_complete/signatures/container-layer.md`).
- The Table-2 rule leaves 233 generation-4 exceptions unexplained
  (`container-layer.md:L50,L60`).
- Container success does not establish leaf codecs, field semantics, writers or game
  acceptance (`container-layer.md:L62`; `artifact: docs/coverage.md:L193-L196`).
- The mask details on logical-size words are not specified by the cited summary
  (`container-layer.md:L48`).

## Changelog

- 2026-11-26: Earlier page restricted Full to container reading, documented all 17
  nonzero roots and used the corrected 4,373-header total
  (`artifact: docs_complete/signatures/9fpr.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, four-byte stored magic width,
  a five-column confidence table and the fixed-prefix versus parsed-header-extent
  distinction. Grade changed from the earlier draft's published-Full reading to **B**:
  structural enumeration succeeds for all headers, but 233 Table-2 exceptions,
  unmapped fields and the local 0/0/4,373 RSA result keep this short of a complete
  container format. No count changed; `container-layer.md` and all other files were
  left untouched.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/9fpr.md`. No count was selected by modification time. Reconciliation decisions: 4,375 and/or 4,330 are retained only as historical rejected header totals; the cited current total is 4,373 = 22 roots + 4,351 nested headers (`workspace: CONTEXT_HANDOFF.md:101,345,361,366`).


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
