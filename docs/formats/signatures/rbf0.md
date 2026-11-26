# RBF0 payload family

Scope and grade: **C, signature layer only.** The local evidence establishes the
four-byte inflated magic, exact published totals, root distribution and recognition
counts. There is no locally verified field map, record stride, blob decoder, full
logical-size inflate audit or writer. The 156 deep-inflate `RBF0` shapes found later are
a **separate residual population** and are not promoted into the published 1,278.

## Identity

`RBF0` is an inner payload signature, not a resource type code. Every published member
has a null resource type word
(`artifact: docs_complete/_evidence/signatures_b/nullword_family.tsv:L6`). The magic is
**four ASCII bytes at inflated `+0x00`**, reached through the bounded zlib-inflate path;
the census label is `RBF0@0`
(`artifact: _unknown_audit/section_signature.md:L5,L21,L65,L72`;
`artifact: docs_complete/_evidence/signatures_b/family_magic.tsv:L3`). This is the same
offset basis as PSIN and XML and differs from stored-magic ADAT, KB2 and SGD5
(`artifact: unknown_accounting.md:L47`). The deeper raw-DEFLATE shapes also place `RBF0`
at inflated offset zero, but they were found by a different, deeper pass and remain in
the residual (`artifact: unknown_accounting.md:L56,L75`).

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 1,278 | 1,255,039 | `artifact: docs/coverage.md:L177`, `:L7` |
| Stored bytes | 2,129,984 | 305,820,985,968 | `artifact: docs_complete/_evidence/signatures_b/family_summary.tsv:L3`, `totals.tsv:L2-L3` |
| Logical bytes | 16,004,417 | 564,783,265,279 | same; `artifact: docs/coverage.md:L177`, `:L8` |

All 1,278 belong to the 92,614 signature-assigned null-word slots
(`artifact: unknown_accounting.md:L16,L41`). A cross-check counts **1,153 distinct
`(root, slot)` pairs** against 1,278 rows, because some pairs repeat
(`artifact: docs_complete/_evidence/signatures_b/family_distinct_slots.tsv:L2`,
`README.md:L31-L32`). Both figures are retained under their own definitions.

Exhaustive root table (`family_root.tsv:L6-L11`):

**Root distribution.**

| Root | Slots | Evidence |
|---|---:|---|
| `data.rpf` | 1,263 | `family_root.tsv:L7` |
| `levels.rpf` | 9 | same, `:L8` |
| `pack/core_restofworld/core_restofworld.rpf` | 3 | same, `:L9` |
| `anim.rpf` | 1 | same, `:L6` |
| `pack/story000/story000.rpf` | 1 | same, `:L10` |
| `packs.rpf` | 1 | same, `:L11` |
| **Total** | **1,278** | `artifact: docs/coverage.md:L177` |

The only census type value is `<null>` for all 1,278 rows
(`artifact: docs_complete/_evidence/signatures_b/family_type_hash.tsv`, RBF0 row).

**Promotion caveat, retained as a source dispute.** `artifact: unknown_accounting.md:L75`
states that promoting the 156 deep-inflate RBF0 rows would make `RBF0 = 1,434` and the
signature-assigned null-word count `92,770`, although the same sentence also mentions
one deeper PSIN row. The 92,770 figure adds only the 156 RBF0 slots (`92,614 + 156`).
If both shapes were promoted, `PSIN` would be 18,641, `RBF0` 1,434 and the
signature-assigned total 92,771. No promotion is applied: this page keeps the published
`RBF0 = 1,278`, `PSIN = 18,640` and `92,614`
(`artifact: docs/coverage.md:L175,L177`; `artifact: unknown_accounting.md:L16`). The source
wording is preserved, not silently repaired.

## Where it appears

The bounded census detects a zlib header at stored offset 0 or 16, inflates a limited
prefix and tests for the magic at inflated `+0x00`
(`artifact: _unknown_audit/section_signature.md:L49,L65,L72`); all 1,278 published members
carry `zlib_off = 0` and `sig_off = 0`
(`section_signature.md:L65,L72`; `artifact: docs_complete/_evidence/signatures_b/family_status.tsv:L4`).
The independent residual pass used raw DEFLATE and reports **157 of 157** exact-size
inflations, comprising 156 `RBF0` and one `PSIN`
(`artifact: unknown_accounting.md:L56,L65,L73`). Exact inflation identifies bytes and a
shape; it is not a decoder result. The census probe is capped at 8,192 stored and 4,096
inflated bytes (`artifact: type_census.md:L7`).

## Layer status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/rbf0.md`.

## Fields if any

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| inflated `+0x00` | 4 | `RBF0` magic, four ASCII bytes | measured | `artifact: _unknown_audit/section_signature.md:L5,L72`; `family_magic.tsv:L3` |
| stored `+0x00` or `+0x10` | 2 | zlib header for the bounded prefix, not an RBF0 field | measured | `artifact: _unknown_audit/section_signature.md:L49` |
| header/count/stride fields | Not specified | no locally measured RBF0 field map | unknown | `artifact: docs/coverage.md:L177` |

Coverage says blob counts and a name set were recorded locally, but there is no field
report and no decoder (`artifact: docs/coverage.md:L177`). That statement is retained as a
status note; no blob-count offset is invented. External descriptions of a binary-XML
record grammar exist in locally cached third-party material but are **external and
unverified here**; no URL was fetched for this page and no external offset is promoted
to a local measurement.

**Source classification retained.**

### Decode status

Grade C. Signature recognition and exact inflation of a separate residual set are the
supported layers; no field-level RBF0 decoder, record validation or semantic mapping is
locally demonstrated (`artifact: docs/coverage.md:L177,L212`;
`artifact: unknown_accounting.md:L73,L75`). All published members carry the generic
`bounded-inflate` status (`family_status.tsv:L4`). No encoder, round trip or game-load
test is reported (`artifact: docs/coverage.md:L193-L196`).

## Verification

- Rust census aggregation: `census_agg.exe artifact: type_census.csv
  artifact: docs_complete/_evidence/signatures_b` → `data_rows: 1255039`,
  `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, zero integrity issues
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`; `README.md:L10-L19`).
- Bounded PowerShell re-sum of both published tables reproduced the exact totals
  (`artifact: docs_complete_work/format_evidence.md:L40-L50`).
- Independent signature re-probe: RBF0 400 sampled / 400 agreements / 400 exact `@0`,
  all 400 on the inner zlib path
  (`artifact: _unknown_audit/section_signature.md:L47-L61`, `:L56`, `:L88-L95`).
- Two independent implementations agree on the residual's 157/157 exact raw-DEFLATE
  inflations (`artifact: unknown_accounting.md:L73`).
- No external URL was fetched for this page.

## Unknowns

- No verified field map, semantic blob decoder or record validation
  (`artifact: docs/coverage.md:L177`).
- The deep-inflate RBF0 shapes remain a residual subpopulation pending an explicit
  versioned reclassification (`artifact: unknown_accounting.md:L75`).
- The 92,770/92,771 promotion arithmetic is unresolved; the published partition stands
  (`artifact: unknown_accounting.md:L75`).
- Writer behavior and game acceptance remain unverified
  (`artifact: docs/coverage.md:L193-L196`).

## Changelog

- 2026-11-26: Earlier page recorded exact counts, six roots, the 156 deep-inflate
  shapes and their non-promotion
  (`artifact: docs_complete/signatures/rbf0.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, grade C, inflated-magic
  offset basis and four-byte width stated, the distinct-slot caveat retained, and the
  92,770/92,771 arithmetic dispute recorded without changing published counts. No other
  file modified.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/rbf0.md`. No count was selected by modification time.


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
