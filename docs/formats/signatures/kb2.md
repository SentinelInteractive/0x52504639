# KB2 payload family

Scope and grade: **C, signature layer only.** The local sources establish a four-byte
stored magic, exact counts and roots. There is no locally decoded frame table, no
validated header field map, no per-slot dimension or frame-count audit and no playback
or writer. Any similarly named external video-header layout is **external attribution**
and is not promoted to a local measurement here.

## Identity

`KB2` is a census payload-signature family, not a resource type code. Every member has
a null resource type word
(`artifact: docs_complete/_evidence/signatures_b/nullword_family.tsv:L4`). The magic is
**four ASCII bytes at stored `+0x00`** and needs no inflate step for recognition;
`zlib_off = -1` for all 797 slots and the census label is `KB2@0`
(`artifact: _unknown_audit/section_signature.md:L5,L21,L65,L70`;
`artifact: docs_complete/_evidence/signatures_b/family_magic.tsv:L2`). This is the same
offset basis as ADAT and SGD5, not the inflated-prefix path used by PSIN, RBF0 and XML
(`artifact: unknown_accounting.md:L47`).

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 797 | 1,255,039 | `artifact: docs/coverage.md:L178`, `:L7` |
| Stored bytes | 13,520,694,880 | 305,820,985,968 | `artifact: docs_complete/_evidence/signatures_b/family_summary.tsv:L2`, `totals.tsv:L2-L3` |
| Logical bytes | 13,520,690,172 | 564,783,265,279 | same; `artifact: docs/coverage.md:L178`, `:L8` |

All 797 belong to the 92,614 signature-assigned null-word slots
(`artifact: unknown_accounting.md:L16,L42`). The stored/logical difference is retained
exactly; these sources do not establish a family-wide padding rule from it
(`family_summary.tsv:L2`). Exhaustive root table (`family_root.tsv:L2-L5`):

**Root distribution.**

| Root | Slots | Evidence |
|---|---:|---|
| `movies.rpf` | 515 | `family_root.tsv:L2` |
| `pack/story000/story000.rpf` | 264 | same, `:L4` |
| `pack/core_restofworld/core_restofworld.rpf` | 11 | same, `:L3` |
| `pack/story000_restofworld/story000_restofworld.rpf` | 7 | same, `:L5` |
| **Total** | **797** | `artifact: docs/coverage.md:L178` |

The only census type value is `<null>` for all 797 rows
(`artifact: docs_complete/_evidence/signatures_b/family_type_hash.tsv`, KB2 row).
The 797 distinct `(root, slot)` pairs equal the 797 rows
(`artifact: docs_complete/_evidence/signatures_b/family_distinct_slots.tsv:L3`).

## Where it appears

Recognition reads **raw stored bytes** at slot `+0x00`; the four-byte token is reached
without any inflate step (`artifact: _unknown_audit/section_signature.md:L49,L65,L70`).
`sig_off = 0` and `zlib_off = -1` for every member
(`section_signature.md:L63-L74`). The generic CSV zlib-probe labels are
`not-zlib-at-0-or-16` for 795 and `inflate-error-or-truncated` for two
(`artifact: docs_complete/_evidence/signatures_b/family_status.tsv:L2-L3`); these labels
do not change the stored-magic evidence and are not a codec-validation result.

## Layer status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/kb2.md`.

## Fields if any

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| stored `+0x00` | 4 | `KB2` magic, four ASCII bytes | measured | `artifact: _unknown_audit/section_signature.md:L5,L70`; `family_magic.tsv:L2` |
| header size/frame/dimension fields | Not specified | no locally verified field map | unknown | `artifact: docs/coverage.md:L178` |
| external header layout (`+0x04` size, `+0x08` frame count, `+0x14`/`+0x18` width/height) | Not specified | external description only; not measured, used or validated in the cited local sources | external | locally cached third-party reference material; no URL fetched for this page |

The external row is explicitly not a local measurement and contributes no decode status.
No frame table, stream index, codec parameter block or padding rule is asserted from the
local sources (`artifact: docs/coverage.md:L178`;
`artifact: docs_complete/_evidence/signatures_b/README.md`).

**Source classification retained.**

### Decode status

Grade C. The coverage page calls this family Classified: name and counts verified,
payload not decoded (`artifact: docs/coverage.md:L178`). Signature recognition, including
the independent raw-byte re-probe, validates identity only
(`artifact: _unknown_audit/section_signature.md:L47-L61,L99-L103`). No encoder, round trip,
playback or game-load result is reported (`artifact: docs/coverage.md:L193-L196`).

## Verification

- Rust census aggregation: `census_agg.exe artifact: type_census.csv
  artifact: docs_complete/_evidence/signatures_b` → `data_rows: 1255039`,
  `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, zero integrity issues
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`; `README.md:L10-L19`).
- Bounded PowerShell re-sum of both published tables reproduced the exact totals
  (`artifact: docs_complete_work/format_evidence.md:L40-L50`).
- Independent signature re-probe: KB2 400 sampled / 400 agreements / 400 exact `@0`,
  zero inner-zlib path
  (`artifact: _unknown_audit/section_signature.md:L47-L61`, `:L54`, `:L88-L95`).
- No external URL was fetched for this page.

## Unknowns

- Payload decoding and field-level structure are unverified in the supplied local
  sources (`artifact: docs/coverage.md:L178`).
- The meaning of the stored/logical difference is not established
  (`family_summary.tsv:L2`).
- The two `inflate-error-or-truncated` probe labels are not explained as damage or as a
  distinct shape (`family_status.tsv:L2`).
- Writer behavior, round-trip fidelity and game acceptance remain unverified
  (`artifact: docs/coverage.md:L193-L196`).

## Changelog

- 2026-11-26: Earlier page recorded exact counts, four roots and the distinction
  between stored-magic recognition and a payload decoder
  (`artifact: docs_complete/signatures/kb2.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, grade C, four-byte stored
  magic and raw offset basis stated, and external header fields marked external rather
  than measured. No count changed; no other file modified.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/kb2.md`. No count was selected by modification time.


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
