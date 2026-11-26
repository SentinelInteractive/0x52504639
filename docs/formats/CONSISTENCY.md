# Consistency audit, 2026-11-26

## Identity

This is the mechanical consistency audit of the format documents in this folder. It records heading schemes, confidence tokens and path-reference counts for the subject documents; it is not a resource-format record, a decoder or a writer.

Mechanical audit of every document in this folder. Headings are checked against the scheme for its document type. Path hygiene is checked separately because local drive-letter paths are not publishable.

| Document | Scheme | Missing headings | Confidence values used | Drive-letter refs |
|---|---|---|---|---:|
| null-word-partition.md | type | none | measured=6 unknown=1 | 90 |
| type-null-word.md | type | none | measured=3 unknown=1 | 83 |
| zad.md | type | none | inferred=1 measured=12 unknown=6 | 62 |
| zas.md | type | none | external=2 measured=13 unknown=2 | 26 |
| zascd.md | type | none | external=2 measured=13 unknown=2 | 37 |
| zbdd.md | type | none | inferred=1 measured=14 unknown=4 | 71 |
| zbdr.md | type | none | external=10 inferred=1 measured=14 unknown=1 | 154 |
| zbft.md | type | none | external=16 measured=11 unknown=1 | 95 |
| zbn.md | type | none | inferred=9 measured=8 unknown=6 | 134 |
| zcd.md | type | none | inferred=1 measured=9 | 43 |
| zcg.md | type | none | measured=5 unknown=2 | 24 |
| zcgc.md | type | none | measured=7 unknown=1 | 27 |
| zcov.md | type | none | external=2 measured=13 unknown=2 | 27 |
| zcps.md | type | none | inferred=1 measured=2 unknown=1 | 25 |
| zdd.md | type | none | inferred=3 measured=9 unknown=1 | 24 |
| zdr.md | type | none | inferred=5 measured=25 | 96 |
| zfd.md | type | none | measured=3 unknown=5 | 24 |
| zfid.md | type | none | measured=12 unknown=4 | 69 |
| zft.md | type | none | inferred=1 measured=9 unknown=1 | 89 |
| zjd.md | type | none | inferred=1 measured=7 unknown=1 | 55 |
| zkit.md | type | none | external=2 measured=13 unknown=2 | 26 |
| zldbmt.md | type | none | external=2 measured=13 unknown=2 | 37 |
| zmap.md | type | none | inferred=1 measured=14 unknown=6 | 31 |
| zmmd.md | type | none | inferred=1 measured=10 unknown=1 | 65 |
| zmt.md | type | none | inferred=5 measured=10 unknown=6 | 41 |
| znv.md | type | none | inferred=8 measured=11 unknown=6 | 24 |
| zpm.md | type | none | inferred=1 measured=16 unknown=4 | 77 |
| zpmd.md | type | none | inferred=1 measured=9 unknown=1 | 65 |
| zpt.md | type | none | measured=4 unknown=4 | 33 |
| zrd.md | type | none | inferred=1 measured=6 unknown=2 | 24 |
| zscript.md | type | none | external=3 measured=18 | 85 |
| zsm.md | type | none | inferred=3 measured=15 unknown=3 | 26 |
| zsmam.md | type | none | inferred=1 measured=6 unknown=1 | 55 |
| zsp.md | type | none | inferred=2 measured=14 unknown=3 | 111 |
| ztd.md | type | none | inferred=1 measured=16 | 72 |
| ztsl.md | type | none | measured=11 | 23 |
| ztyp.md | type | none | external=2 measured=13 unknown=2 | 26 |
| zvert.md | type | none | inferred=1 measured=9 unknown=1 | 58 |
| evidence/census_evidence.md | type | none | unknown=1 | 13 |
| evidence/seven_types_index_section.md | type | none | unknown=1 | 12 |
| signatures/0drpz.md | signature | none | measured=15 unknown=1 | 61 |
| signatures/9fpr.md | signature | none | measured=11 unknown=8 | 44 |
| signatures/adat.md | signature | none | measured=5 unknown=1 | 37 |
| signatures/container-layer.md | signature | none | external=1 inferred=12 measured=2 unknown=11 | 68 |
| signatures/kb2.md | signature | none | external=1 measured=1 unknown=1 | 30 |
| signatures/null-word.md | signature | none |  | 1 |
| signatures/psin.md | signature | none | measured=2 unknown=1 | 39 |
| signatures/rbf0.md | signature | none | measured=2 unknown=1 | 39 |
| signatures/README.md | signature | none | unknown=1 | 7 |
| signatures/sgd5.md | signature | none | external=1 measured=1 unknown=1 | 29 |
| signatures/xml.md | signature | none | measured=3 unknown=1 | 40 |

## Summary

- Documents checked: 51
- Documents with a missing heading: 0
- Documents containing drive-letter paths: 51
- Total drive-letter path references: 2554

Heading audit: PASS. Path hygiene: FAIL, and it must be repaired before any publication. Every citation must become a neutral artifact reference such as `artifact: bvh_nodes/adopt.md` with no drive letter and no user name.
