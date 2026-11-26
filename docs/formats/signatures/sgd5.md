# SGD5 payload family

Scope and grade: **C, signature layer only.** Two slots carry a four-byte stored magic;
their counts and location are exact. There is no locally verified shader decoder,
stage mapping, section directory, record stride, per-member semantic validation, encoder
or writer. The coverage page explicitly leaves the shader mapping open.

## Identity

`SGD5` is a census payload-signature family, not a resource type code. Both members
have a null resource type word
(`artifact: docs_complete/_evidence/signatures_b/nullword_family.tsv:L7`). The magic is
**four ASCII bytes at stored `+0x00`**, with `zlib_off = -1` for both slots; the census
label is `SGD5@0`
(`artifact: _unknown_audit/section_signature.md:L5,L21,L65,L73`;
`artifact: docs_complete/_evidence/signatures_b/family_magic.tsv:L4`). Recognition uses
raw stored bytes, not an inflated prefix and not the resource `+0x10` type word
(`artifact: unknown_accounting.md:L47`). Both slots sit in `shaders.rpf`
(`artifact: docs_complete/_evidence/signatures_b/family_root.tsv:L12`), but the archive
name is a location, not a field specification.

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 2 | 1,255,039 | `artifact: docs/coverage.md:L180`, `:L7` |
| Stored bytes | 274,135,376 | 305,820,985,968 | `artifact: docs_complete/_evidence/signatures_b/family_summary.tsv:L4`, `totals.tsv:L2-L3` |
| Logical bytes | 274,135,358 | 564,783,265,279 | same; `artifact: docs/coverage.md:L180`, `:L8` |

Both slots belong to the 92,614 signature-assigned null-word slots
(`artifact: unknown_accounting.md:L16,L44`). Root table, exhaustive with denominator two
(`family_root.tsv:L12`):

## Where it appears

| Root | Slots | Evidence |
|---|---:|---|
| `shaders.rpf` | 2 | `artifact: docs_complete/_evidence/signatures_b/family_root.tsv:L12` |
| **Total** | **2** | `artifact: docs/coverage.md:L180` |

The 18-byte stored minus logical difference is a declared-size fact; these sources do
not establish a padding or codec rule from it (`family_summary.tsv:L4`). Both slots are
a full population, and both were read in the independent re-probe
(`artifact: _unknown_audit/section_signature.md:L58,L61`).


The four-byte magic is reached directly at stored offset zero with no inflate step
(`artifact: _unknown_audit/section_signature.md:L49,L65,L73`); `sig_off = 0` and
`zlib_off = -1` for both members (`section_signature.md:L63-L74`). The generic CSV
zlib-probe status is `not-zlib-at-0-or-16` for both
(`artifact: docs_complete/_evidence/signatures_b/family_status.tsv:L5`), consistent with
the stored-magic path. No additional container structure is established for this family
by the cited sources.

## Layer status

### Decode status

Grade C. Coverage calls the family Classified: name and counts verified, shader mapping
an open question (`artifact: docs/coverage.md:L180,L212`). Signature recognition for two
of two members is supported; nothing beyond the magic is decoded locally
(`artifact: _unknown_audit/section_signature.md:L99-L103`). No encoder, round trip or
game-load test is reported (`artifact: docs/coverage.md:L193-L196`).

## Fields if any

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| stored `+0x00` | 4 | `SGD5` magic, four ASCII bytes | measured | `artifact: _unknown_audit/section_signature.md:L5,L73`; `family_magic.tsv:L4` |
| version/section directory/shader body | Not specified | no locally verified field map | unknown | `artifact: docs/coverage.md:L180` |
| external shader work | Not specified | external descriptions exist in locally cached material; not measured, decoded or validated here | external | no URL fetched for this page |

The external row is attribution only. It does not contribute a decode result or a local
offset, and no external label is adopted as an engine name.

## Verification

- Rust census aggregation: `census_agg.exe artifact: type_census.csv
  artifact: docs_complete/_evidence/signatures_b` → `data_rows: 1255039`,
  `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, zero integrity issues
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`; `README.md:L10-L19`).
- Bounded PowerShell re-sum of both published tables reproduced the exact totals
  (`artifact: docs_complete_work/format_evidence.md:L40-L50`).
- Independent signature re-probe: SGD5 2 sampled (full population) / 2 agreements /
  2 exact `@0`, zero inner-zlib path
  (`artifact: _unknown_audit/section_signature.md:L47-L61`, `:L57`, `:L88-L95`).
- No external URL was fetched for this page.

## Unknowns

- Shader mapping, section semantics and field layout remain open
  (`artifact: docs/coverage.md:L180`).
- Two slots are the entire local population, so no broader statistical conclusion is
  available (`artifact: _unknown_audit/section_signature.md:L103`).
- Writer behavior and game acceptance remain unverified
  (`artifact: docs/coverage.md:L193-L196`).

## Changelog

- 2026-11-26: Earlier page recorded exact two-slot accounting, null-word membership and
  the open shader mapping
  (`artifact: docs_complete/signatures/sgd5.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, grade C, four-byte stored
  magic and raw offset basis stated, and external shader work marked external. No count
  changed; no other file modified.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/sgd5.md`. No count was selected by modification time.


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
