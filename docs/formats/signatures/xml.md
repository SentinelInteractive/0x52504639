# XML payload family

Scope and grade: **C, signature layer only.** The local sources establish a four-byte
inflated magic, exact published totals and four roots. They do not supply a verified
XML parser, element/attribute schema, encoding census, per-document validation result,
encoder or writer. Readable text is not evidence of application semantics. The 128
BOM-prefixed documents found later are a residual shape and are not added to 221.

## Identity

`XML` is a recognized inner text-payload family, not a resource type code. Every member
has a null resource type word
(`artifact: docs_complete/_evidence/signatures_b/nullword_family.tsv:L9`). The magic is
**four ASCII bytes at inflated `+0x00`**, reached through a bounded zlib-inflate path;
the census label is `XML@0`
(`artifact: _unknown_audit/section_signature.md:L5,L21,L65,L74`;
`artifact: docs_complete/_evidence/signatures_b/family_magic.tsv:L5`). This differs from
BOM-prefixed residual documents, where bytes `EF BB BF` push `<?xml` to inflated offset
three (`artifact: unknown_accounting.md:L57`;
`artifact: _unknown_audit/section_residual.md:L81`). The bounded probe checks offsets
0, 8, 16, 32 and 48, so it missed that form
(`artifact: _unknown_audit/section_residual.md:L81`).

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 221 | 1,255,039 | `artifact: docs/coverage.md:L179`, `:L7` |
| Stored bytes | 3,639,664 | 305,820,985,968 | `artifact: docs_complete/_evidence/signatures_b/family_summary.tsv:L5`, `totals.tsv:L2-L3` |
| Logical bytes | 40,592,391 | 564,783,265,279 | same; `artifact: docs/coverage.md:L179`, `:L8` |

All 221 belong to the 92,614 signature-assigned null-word slots
(`artifact: unknown_accounting.md:L16,L43`). Exhaustive root table
(`artifact: docs_complete/_evidence/signatures_b/family_root.tsv:L13-L16`):

**Root distribution.**

| Root | Slots | Evidence |
|---|---:|---|
| `common.rpf` | 216 | `family_root.tsv:L13` |
| `pack/core_bvh4/core_bvh4.rpf` | 2 | same, `:L14` |
| `pack/shared_minigame000/shared_minigame000.rpf` | 2 | same, `:L15` |
| `pack/story000/story000.rpf` | 1 | same, `:L16` |
| **Total** | **221** | `artifact: docs/coverage.md:L179` |

The 221 are a **full population**, not a sample: the independent re-probe read all 221
(`artifact: _unknown_audit/section_signature.md:L58,L61`). The 128 BOM-prefixed shapes are
counted inside the 4,514 residual slots, not here
(`artifact: unknown_accounting.md:L17,L57`; `artifact: docs/coverage.md:L179`).

## Where it appears

The bounded census detects a zlib header at stored offset 0 or 16 and tests the magic
at inflated `+0x00` (`artifact: _unknown_audit/section_signature.md:L49,L65,L74`);
`sig_off = 0` and `zlib_off = 0` for every member
(`section_signature.md:L63-L74`). All 221 have generic `bounded-inflate` status
(`artifact: docs_complete/_evidence/signatures_b/family_status.tsv:L6`). The residual
BOM form is still XML text but has a different prefix layout and is deliberately left
in its original partition until an explicit versioned census change
(`artifact: unknown_accounting.md:L57,L75`;
`artifact: _unknown_audit/section_residual.md:L81`).

## Layer status

### Decode status

Grade C. Signature recognition and readability are the supported layers. No parser
verification, schema validation, semantic interpretation, encoder, round trip or
game-load result is reported (`artifact: docs/coverage.md:L179,L193-L196`;
`artifact: unknown_accounting.md:L57`). The full-population re-probe confirms identity,
not document validity (`artifact: _unknown_audit/section_signature.md:L58-L61`).

## Fields if any

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| inflated `+0x00` | 4 | `XML` magic, four ASCII bytes | measured | `artifact: _unknown_audit/section_signature.md:L5,L74`; `family_magic.tsv:L5` |
| stored `+0x00` or `+0x10` | 2 | zlib header for the bounded prefix, not an XML field | measured | `artifact: _unknown_audit/section_signature.md:L49` |
| residual BOM form: inflated `+0x00` | 3 | `EF BB BF`, with `<?xml` at inflated `+0x03`; separate residual shape only | measured | `artifact: unknown_accounting.md:L57`; `artifact: _unknown_audit/section_residual.md:L81` |
| element/attribute schema, encoding census, namespace map | Not specified | no locally verified parser or schema evidence | unknown | `artifact: docs/coverage.md:L179` |

The coverage note calls the documents readable text but verifies no parser
(`artifact: docs/coverage.md:L179`). External document-reader claims exist in locally
cached third-party material but are external, unverified here and contribute no field
row to this table; no URL was fetched for this page.

## Verification

- Rust census aggregation: `census_agg.exe artifact: type_census.csv
  artifact: docs_complete/_evidence/signatures_b` → `data_rows: 1255039`,
  `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, zero integrity issues
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`; `README.md:L10-L19`).
- Bounded PowerShell re-sum of both published tables reproduced the exact totals
  (`artifact: docs_complete_work/format_evidence.md:L40-L50`).
- Independent signature re-probe: XML 221 sampled (full population) / 221 agreements /
  221 exact `@0`, all 221 via the inner zlib path
  (`artifact: _unknown_audit/section_signature.md:L47-L61`, `:L58`, `:L88-L95`).
- The BOM-boundary caveat comes from the residual audit, which classifies by bytes and
  not by the producer's `sig_raw`/`sig_inner` columns
  (`artifact: _unknown_audit/section_residual.md:L70,L81`).
- No external URL was fetched for this page.

## Unknowns

- Complete parse success, validation rules and application-level meaning remain
  unverified (`artifact: docs/coverage.md:L179`).
- BOM-aware promotion would require a versioned partition change and is not applied
  (`artifact: unknown_accounting.md:L75`; `artifact: _unknown_audit/section_residual.md:L81`).
- Writer behavior and game acceptance remain unverified
  (`artifact: docs/coverage.md:L193-L196`).

## Changelog

- 2026-11-26: Earlier page recorded exact counts, four roots, the 128 BOM-prefixed
  residual shapes and the readability-versus-parser distinction
  (`artifact: docs_complete/signatures/xml.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, grade C, inflated-magic offset
  basis and four-byte width stated, BOM offset difference kept in its separate scope,
  and external reader claims not promoted. No count changed; no other file modified.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/xml.md`. No count was selected by modification time.


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
