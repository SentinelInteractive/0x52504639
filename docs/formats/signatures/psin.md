# PSIN payload family

Scope and grade: **C, signature layer only.** Locally supported facts are the four-byte
inflated magic, exact slot/byte totals, root distribution and the bounded-inflate
recognition path. No complete PSIN decoder, record walk, field map, end-to-end inflate
audit or writer is demonstrated. The commonly cited section chain is **external**
attribution, not a local measurement; one deeper-inflate PSIN remains in the residual
and is not promoted into the published 18,640.

## Identity

`PSIN` is an inner payload signature, not a resource type code. All 18,640 census
members have a null resource type word
(`artifact: docs_complete/_evidence/signatures_a/census_aggregates.json:L709-L780`;
`artifact: docs_complete/_evidence/signatures_b/nullword_token.tsv:L2`). The magic is
**four ASCII bytes at inflated `+0x00`**, reached through a bounded zlib inflate at the
stored layer; the census label is `PSIN@0`
(`artifact: _unknown_audit/section_signature.md:L5,L21,L65,L71`;
`artifact: docs_complete/_evidence/signatures_b/nullword_magic.tsv:L6`). This differs from
`0DRPz`, whose five-byte signature sits at inflated `+0x10`
(`artifact: docs/formats/0drpz.md:L9`). The `0DRPz` root is parsed through a PSIN wrapper
path (`artifact: docs/formats/0drpz.md:L76`), but that implementation relationship does
not reclassify the 290,294 `0DRPz` slots into this signature row.

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 18,640 | 1,255,039 | `artifact: docs/coverage.md:L175`, `:L7` |
| Stored bytes | 154,829,776 | 305,820,985,968 | `artifact: docs_complete/_evidence/signatures_b/all_families.tsv:L6`, `totals.tsv:L2-L3` |
| Logical bytes | 487,573,772 | 564,783,265,279 | same; `artifact: docs/coverage.md:L175`, `:L8` |

The family is a subset of the 92,614 signature-assigned null-word slots
(`artifact: unknown_accounting.md:L16,L33-L47`). Exhaustive root table from the per-slot
aggregation (`census_aggregates.json:L645-L701`;
`artifact: docs_complete/_evidence/signatures_b/nullword_family.tsv:L5`):

**Root distribution.**

| Root | Slots | Evidence |
|---|---:|---|
| `levels.rpf` | 6,982 | `census_aggregates.json:L656-L659` |
| `pack/story000/story000.rpf` | 5,348 | same, `:L676-L679` |
| `pack/story000/story000_script.rpf` | 2,309 | same, `:L681-L684` |
| `data.rpf` | 2,281 | same, `:L651-L654` |
| `packs.rpf` | 586 | same, `:L691-L694` |
| `pack/shared_minigame000/shared_minigame000.rpf` | 73 | same, `:L671-L674` |
| `navmeshes.rpf` | 22 | same, `:L661-L664` |
| `anim.rpf` | 18 | same, `:L646-L649` |
| `pack/core_restofworld/core_restofworld.rpf` | 6 | same, `:L666-L669` |
| `pack/story000_restofworld/story000_restofworld.rpf` | 3 | same, `:L686-L689` |
| `script.rpf` | 1,012 | same, `:L696-L699` |
| **Total** | **18,640** | `artifact: docs/coverage.md:L175` |

**Promotion caveat, retained as a source dispute.** The residual section records
156 deep-inflate `RBF0` and one deep-inflate `PSIN` row at inflated offset zero, and
states that promotion would make `RBF0` 1,434 and the signature-assigned null-word count
92,770 (`artifact: unknown_accounting.md:L56,L65,L75`). That 92,770 arithmetic adds only
the 156 RBF0 rows: `92,614 + 156 = 92,770`, although the same sentence refers to both
shapes. Promoting **both** would give `RBF0 = 1,434`, `PSIN = 18,641` and signature-assigned
`92,771`. No promotion is applied here: the published totals remain `PSIN 18,640`,
`RBF0 1,278` and signature-assigned `92,614`
(`artifact: docs/coverage.md:L175,L177`; `artifact: unknown_accounting.md:L16`). The source
wording at `:L75` is preserved rather than silently corrected.

## Where it appears

Recognition is at the **inflated** prefix: the census test detects a zlib header at
stored offset 0 or 16, inflates a bounded prefix and then tests for the magic at
inflated `+0x00` (`artifact: _unknown_audit/section_signature.md:L49,L65,L71`;
`artifact: unknown_accounting.md:L47`). `sig_off` is 0 for every member and `zlib_off` is 0
for every member; this is different from the raw-magic families ADAT, KB2 and SGD5
(`section_signature.md:L63-L74`). The bounded prefix is not a whole-payload inflate:
`artifact: type_census.md:L7` records the 8,192 stored / 4,096 inflated probe cap. The
one residual PSIN is a deeper-inflate shape, not a 19th root or an extra published slot
(`artifact: unknown_accounting.md:L65,L75`).

## Layer status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/psin.md`.

## Fields if any

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| inflated `+0x00` | 4 | `PSIN` magic, four ASCII bytes | measured | `artifact: _unknown_audit/section_signature.md:L5,L71`; `nullword_magic.tsv:L6` |
| stored `+0x00` or `+0x10` | 2 | zlib header used by the bounded prefix test, not a PSIN field | measured | `artifact: _unknown_audit/section_signature.md:L49` |
| section chain and record layouts | Not specified | no locally measured PSIN field table; external descriptions exist but are not adopted | unknown | `artifact: docs/coverage.md:L175` |

The coverage note that "several header records are partly mapped" is retained as a
status statement, not expanded into a table
(`artifact: docs/coverage.md:L175`). External material describes a tagged section chain
with big-endian lengths; no URL was fetched for this page, no external code was copied,
and none of those offsets is presented as a local measurement. The `0DRPz` root table
belongs on its own page (`artifact: docs_complete/signatures/0drpz.md`, Fields) and is not
copied onto PSIN slots.

**Source classification retained.**

### Decode status

Grade C. Recognition of the magic through a bounded inflate is the supported layer;
all 18,640 rows carry the generic `bounded-inflate` status
(`census_aggregates.json:L702-L708`). There is no complete decoder, no local field
report and no semantic interpretation of the tagged sections
(`artifact: docs/coverage.md:L175,L211`). No encoder, round trip or game-load test is
reported (`artifact: docs/coverage.md:L193-L196`).

## Verification

- Rust census aggregation: `census_agg.exe artifact: type_census.csv
  artifact: docs_complete/_evidence/signatures_b` → `data_rows: 1255039`,
  `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, zero integrity issues
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`; `README.md:L10-L19`).
- Bounded PowerShell re-sum of both published tables reproduced the totals exactly
  (`artifact: docs_complete_work/format_evidence.md:L40-L50`).
- Independent signature re-probe: PSIN 400 sampled / 400 agreements / 400 exact `@0`,
  all 400 on the inner zlib path
  (`artifact: _unknown_audit/section_signature.md:L47-L61`, `:L55`, `:L88-L95`).
  Aggregate re-probe was 1,823/1,823 with 1,021 inner-path samples, so the audit has no
  PSIN-only semantic decoder result (`section_signature.md:L59-L61,L99-L103`).
- The deeper residual PSIN was found during the separate residual pass, not by the
  bounded census (`artifact: unknown_accounting.md:L65,L75`).
- No external URL was fetched for this page.

## Unknowns

- Header field meanings, record boundaries and a complete decoder remain open
  (`artifact: docs/coverage.md:L175`).
- Bounded recognition does not establish complete inflation or traversal of all
  18,640 logical payloads (`census_aggregates.json:L702-L708`; `artifact: type_census.md:L7`).
- The 92,770 versus 92,771 promotion arithmetic is an unresolved source discrepancy;
  the published partition is retained (`artifact: unknown_accounting.md:L75`).
- Writer behavior and game acceptance remain unverified
  (`artifact: docs/coverage.md:L193-L196`).

## Changelog

- 2026-11-26: Earlier page added exact family/type/root accounting, separated the
  `0DRPz` implementation path and kept the deeper residual out of the published family
  (`artifact: docs_complete/signatures/psin.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, grade C, inflated-magic
  offset basis and four-byte width stated, the promotion arithmetic caveat recorded
  without changing published counts, and external section claims kept external. No
  other file modified.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/psin.md`. No count was selected by modification time.


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
