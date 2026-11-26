# Null-word partition (101,479 slots)

The null word is the **absence of a candidate type classification**, not a fully decoded format and not an entirely unexplained residue. This document details how the 101,479 type-word Unknown slots are partitioned at slot and byte level: 4,351 nested containers, 92,614 word-less slots with a recognized inner signature, and a 4,514-slot residual (`artifact: unknown_accounting.md:7-18,99`; `artifact: docs/coverage.md:130`). Accounting is not decoding: no part of this partition is presented as a decoded payload (`artifact: unknown_accounting.md:99`).

Grade: **C** (container and signature classification only; no payload decode). No full-decode implication. Companion identity/count page: `artifact: docs_complete/type-null-word.md`.


Editorial coverage grade: **C**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

- The partition answers one question about one population: the 101,479 slots with no `type_hash` value in the census, row 4 of the 37-row type table. The literal token `<null>` is the only representation used; there are zero empty or bare `null` rows, and there is no `9FPR`-not-header class (`artifact: docs/coverage.md:123,130,213`; `artifact: census_recount/report.md:32,63`; `artifact: docs_complete/_evidence/signatures_b/README.md`; `artifact: _unknown_audit/section_signature.md:5,78-82`; `artifact: type_census.csv:1`; `artifact: docs_complete_work/type_counts.tsv:38`).
- It is a partition **within** the type table. The signature table is a different question about the same 1,255,039 slots; signature `none` (867,780) is not type Unknown (101,479), and the two tables must not be added (`artifact: docs/coverage.md:12-16,172,183`).
- The 4,351 `9FPR` slots appear in both the type Unknown group and the signature `9FPR` row. They are the same slots seen under two questions, not an extra population (`artifact: unknown_accounting.md:15`; `artifact: docs/coverage.md:176`).
- Terminology: "word-less" means no `+0x10` candidate type word; "signature-assigned" means a recognized inner signature is present in the payload; "residual" means neither a container classification nor a recognized top-level signature was assigned (`artifact: unknown_accounting.md:35,49`).

## Counts

Reconciliation, exact at slot and byte level (`artifact: unknown_accounting.md:13-20`; `artifact: docs_complete_work/nullword_family.tsv:1-9`):

| Population | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| Nested containers `9FPR` | 4,351 | 147,279,874,016 | 147,279,874,016 |
| Signature-assigned (six families) | 92,614 | 52,253,335,840 | 52,636,504,574 |
| No-signature residual | 4,514 | 232,400,208 | 543,626,465 |
| **Total** | **101,479** | **199,765,610,064** | **200,460,005,055** |

Verified arithmetic: 4,351 + 92,614 + 4,514 = 101,479; 147,279,874,016 + 52,253,335,840 + 232,400,208 = 199,765,610,064; 147,279,874,016 + 52,636,504,574 + 543,626,465 = 200,460,005,055. Both byte totals match the null-word row in `artifact: docs/coverage.md:130` to the byte (`artifact: unknown_accounting.md:20`).

Signature-assigned, exact (`artifact: unknown_accounting.md:37-47`; `nullword_family.tsv`):

| Signature | Slots | Stored bytes | Logical bytes | Roots |
|---|---:|---:|---:|---:|
| `ADAT` | 71,676 | 38,297,906,160 | 38,297,508,464 | 4 |
| `PSIN` | 18,640 | 154,829,776 | 487,573,772 | 11 |
| `RBF0` | 1,278 | 2,129,984 | 16,004,417 | 6 |
| `KB2` | 797 | 13,520,694,880 | 13,520,690,172 | 4 |
| `XML` | 221 | 3,639,664 | 40,592,391 | 4 |
| `SGD5` | 2 | 274,135,376 | 274,135,358 | 1 |
| **Total** | **92,614** | **52,253,335,840** | **52,636,504,574** | |

Slot sum 71,676 + 18,640 + 1,278 + 797 + 221 + 2 = 92,614. Stored sum 38,297,906,160 + 154,829,776 + 2,129,984 + 13,520,694,880 + 3,639,664 + 274,135,376 = 52,253,335,840. Logical sum 38,297,508,464 + 487,573,772 + 16,004,417 + 13,520,690,172 + 40,592,391 + 274,135,358 = 52,636,504,574. These family totals match the published signature table (`artifact: docs/coverage.md:174-180`; `artifact: unknown_accounting.md:45`). The magic layer is not uniform: `ADAT`, `KB2` and `SGD5` carry magic at stored offset 0; `PSIN`, `RBF0` and `XML` are reached only after a bounded zlib inflate (`artifact: unknown_accounting.md:47`).

Residual, exact (`artifact: unknown_accounting.md:49-71`):

| Group | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `texture-page-map-header` (`PAMH`) | 1,477 | — | — |
| `texture-page-record` (`01 00 01 02 80 00 80 00`) | 1,476 | — | — |
| `movie-chunk-index` (`MoVE`, version `0x13`) | 443 | — | — |
| `RBF0` at deep inflate | 156 | — | — |
| `xml-with-bom` (`EF BB BF` + `<?xml`) | 128 | — | — |
| `scaleform-gfx` (`GFX*`) | 87 | — | — |
| `EA885A04` | 34 | — | — |
| plain-text manifests | 16 | — | — |
| `placeholder-forced-empty` (`FORCE_EMPTY_RPF\0`) | 30 | 480 | 450 |
| `magic-edup` (`EDUP`) | 5 | — | — |
| `MHIU` | 2 | — | — |
| `SPS1` | 1 | — | — |
| `PSIN` at deep inflate | 1 | — | — |
| `PS\0` shader table | 1 | — | — |
| **Known total** | **3,827** | **195,216,032** | **405,428,345** |
| **Placeholders** | **30** | **480** | **450** |
| **Raw no-magic, high entropy** | **615** | **33,926,464** | **126,978,572** |
| **Truly unknown** | **42** | **3,257,232** | **11,219,098** |
| **Total** | **4,514** | **232,400,208** | **543,626,465** |

Named groups are reported at slot level only; byte totals are given by the four summary rows above, not per named group (`artifact: unknown_accounting.md:53-71`). Named-group slot sum: 1,477 + 1,476 + 443 + 156 + 128 + 87 + 34 + 16 + 5 + 2 + 1 + 1 + 1 = 3,827. Partition sums: 3,827 + 30 + 615 + 42 = 4,514; 195,216,032 + 480 + 33,926,464 + 3,257,232 = 232,400,208; 405,428,345 + 450 + 126,978,572 + 11,219,098 = 543,626,465. Of the 42 truly unknown, 38 are partial deflate streams and 4 are unmatched compressed binaries (`artifact: unknown_accounting.md:70`). Compression split across the residual: zlib 3,671; raw deflate 157, with 157 of 157 inflating exactly to the declared logical size; deflate-partial 38; none 648, and 3,671 + 157 + 38 + 648 = 4,514 (`artifact: unknown_accounting.md:73`).

## Container

- The 4,351 nested slots are archive headers, not leaf payloads. Per root, container slots equal `headers - 1`; all 22 differences are zero: 4,373 - 22 = 4,351 (`artifact: unknown_accounting.md:24-25`; `workspace: CONTEXT_HANDOFF.md:101`).
- All 4,351 carry `9FPR`; header length parses on 4,351 of 4,351 and is below stored size for every slot. Stored equals logical, 147,279,874,016 bytes, stored raw and never deflated (`artifact: unknown_accounting.md:26-27`).
- Stored-size range 720 to 14,159,487,680 bytes, median 4,133,056; header extent 592 to 1,926,016 bytes, median 4,704, below stored size for every slot. Largest roots: `levels.rpf` 2,050, `core_bvh4` 1,281, `story000` 441, `anim.rpf` 235 (`artifact: unknown_accounting.md:28-29`).
- The 22 named roots are separate files on disk. A container slot is deeper nesting inside one root, and its contents are enumerated in that root's flat slot list. No size or prefix match against pack roots is expected; finding none is a clean negative, not a missing mapping (`artifact: unknown_accounting.md:30`).
- Container header fields: 64-byte header, magic `9FPR` (`0x52504639`), length at `+0x04`, split at `+0x08`, count at `+0x24`, width from low `+0x2C`, generation tags `0x1C` and `0x30` (`workspace: CONTEXT_HANDOFF.md:96-99`).
- Byte sums are sums over rows, not unique physical bytes; nested container ranges contain descendants (`artifact: docs/coverage.md:8-10`; `artifact: type_census.md:7`). For this partition both byte totals match the null-word row exactly (`artifact: unknown_accounting.md:20`).

## Fields

No payload field layout is decoded by this partition. The table lists the census CSV columns used to form and check it, plus the general resource-record descriptor word at `+0x10` where that word is present; "Offset" labels a CSV column or a documented record byte, not a decoded payload field, and no on-disk field width is claimed for null slots.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| `type_hash` (CSV column) | n/a | Missing value selects the null group; only token `<null>` occurs, no empty/bare `null` rows | measured | `artifact: type_census.csv:1`; `census_recount/report.md:32,63`; `_evidence/signatures_b/README.md:26-27`; `count_inventory.rs:108,131`; `type_counts.tsv:38` |
| `+0x10` (resource record descriptor word `w4`) | 4-byte word (u32), low byte = code, where present | Engine type enum word: the whole word measures `0x00000059` on 746 script slots. Not applicable to this group, where no `type_hash` value is present; no on-disk null-field width is asserted | measured | `artifact: docs/formats/script-resources.md:7,55`; `workspace: CONTEXT_HANDOFF.md:99,133`; `artifact: docs/coverage.md:123`; `artifact: type_census.csv:1` |
| distinct null marker / null bits | n/a | No such on-disk field or offset established; do not assert one | unknown | `artifact: type_census.csv:1`; `count_inventory.rs:131` |
| `family` (CSV column) | n/a | Assigns each slot to `9FPR`, one of six signatures, or residual `Unknown` | measured | `count_inventory.rs:108,131`; `nullword_family.tsv:1-9`; `artifact: unknown_accounting.md:13-18` |
| `stored_bytes`, `logical_bytes` (CSV columns) | n/a | Byte reconciliation to the null-word row | measured | `nullword_family.tsv:1-9`; `type_counts.tsv:38`; `artifact: unknown_accounting.md:20` |
| magic at stored offset 0 | variable | Holds for `ADAT`, `KB2`, `SGD5` only; not a uniform claim for all six families | measured | `artifact: unknown_accounting.md:47` |
| magic after bounded inflate | variable | Path for `PSIN`, `RBF0`, `XML`; not claimed for the other three | measured | `artifact: unknown_accounting.md:47` |

## Decode status

- Coverage status of the parent row is Unknown (`artifact: docs/coverage.md:25,130`). This page grades **C** for container and signature accounting only (`artifact: docs_complete_work/plan.md:9`); it does not upgrade the parent row.
- The 4,351 containers are read at the container layer; the `9FPR` signature row is Full for the container layer only, not for leaf payloads (`artifact: docs/coverage.md:176,183`).
- The 92,614 signature-assigned slots have recognized shapes but several families have only name and count verified, with no field report or decoder (`artifact: docs/coverage.md:174-180`; `artifact: unknown_accounting.md:35,47`).
- The residual is accounted, not decoded. The 615 slots are a codec-identification gap rather than unknown content; the 42 genuinely unknown slots are split into 38 deflate-partial and 4 unmatched compressed binaries, and the 38 may contain false positives and are reported as a group (`artifact: unknown_accounting.md:69-71,77,88-89`).
- No encoder, round-trip, game-load test or field semantics is claimed (`workspace: CONTEXT_HANDOFF.md:201`).

## Verification

Own bounded checks, no bulk archive reads and no Python:

```
Import-Csv 'artifact: docs_complete_work/nullword_family.tsv' -Delimiter "`t" | Measure-Object slots,stored_bytes,logical_bytes -Sum
# rows=8 slots_sum=101479 stored_sum=199765610064 logical_sum=200460005055

Import-Csv 'artifact: docs_complete_work/type_counts.tsv' -Delimiter "`t" | Where-Object type_hash -eq '<null>'
# slots=101479 stored=199765610064 logical=200460005055  match_slots/stored/logical = True/True/True

Get-Content 'artifact: type_census.csv' -TotalCount 1
# header includes family,type_hash,magic,stored_bytes,logical_bytes,...

PowerShell arithmetic (full log in artifact: docs_complete_work/null_write.md):
# part_slots=101479  part_stored=199765610064  part_logical=200460005055
# sig_slots=92614  sig_stored=52253335840  sig_logical=52636504574
# known_groups=3827  residual_part=4514  residual_stored=232400208  residual_logical=543626465
# codec_part=4514
```

Path aliases used in this document, all resolved with `Test-Path -LiteralPath` on 2026-11-26: `count_inventory.rs`, `nullword_family.tsv`, `type_counts.tsv`, `inventory_log.txt`, `type_inventory.md` and `format_evidence.md` mean `artifact: docs_complete_work/<filename>`; `census_recount/report.md` means `artifact: census_recount/report.md`; `_evidence/signatures_b/README.md` means `artifact: docs_complete/_evidence/signatures_b/README.md`. All other cited paths are written in full.

Prior independent checks on record: an earlier Rust scan read 1,255,039 data rows with 0 malformed rows and matched `artifact: docs/coverage.md:127-181` byte for byte (`artifact: docs_complete_work/type_inventory.md:24-45`; `inventory_log.txt`). An independent Rust re-probe reproduced the CSV family on 1,823 of 1,823 sampled slots, 1,021 on the inner path (`artifact: unknown_accounting.md:47`). Two independent implementations agree on the 157 exact raw-deflate inflations (`artifact: unknown_accounting.md:73`). The residual leaf was still running at report time (`artifact: unknown_accounting.md:87`); the consolidated handoff later records the audit as done (`workspace: CONTEXT_HANDOFF.md:21,154`).

## Unknowns

- Stale counts: residual `unknown` 621 was superseded by 615 (`artifact: unknown_accounting.md:88`); 4,375 headers is superseded by 4,373 = 22 + 4,351, and 4,330 is an older correction (`workspace: CONTEXT_HANDOFF.md:101,345,361,366`); the earlier 55 deflate-partial hits were killed as garbage-offset matches (`artifact: unknown_accounting.md:83`).
- Status snapshot conflict: the older `workspace: coverage_audit/out/tables.md:5-41` shows 25 Classified and 9 Partial; current `artifact: docs/coverage.md:127-163` shows 4 Classified and 30 Partial after 21 promotions. The later file (mtime 19:58Z vs 14:32Z on 2026-11-24) is authoritative. The null-word row stays Unknown in both (`artifact: docs_complete_work/type_inventory.md:138`).
- RBF0 deeper-promotion caveat, **not applied**: the 156 deep-inflate `RBF0` and 1 deep-inflate `PSIN` rows sit at offset 0 of the inflated payload, not at the bounded-prefix layer (`artifact: unknown_accounting.md:75`). That source sentence says promoting both would give `RBF0` 1,434 and signature-assigned 92,770. The arithmetic is internally inconsistent: 92,614 + 156 = 92,770, but 92,614 + 156 + 1 = 92,771, which would also make `PSIN` 18,641 rather than the published 18,640 (`artifact: unknown_accounting.md:35-47`). The source's 92,770 therefore matches promoting **only** the 156 `RBF0` rows, not both populations. This document records the inconsistency, does **not** reproduce 92,770 as a both-populations result, and keeps the published `RBF0` 1,278, `PSIN` 18,640 and signature-assigned 92,614 unchanged. No promotion is applied.
- Container classification and membership come from the same header table, so they are consistent but not independent; on-disk `9FPR` reads are independent (`artifact: unknown_accounting.md:31`).
- Producer caveat: the CSV column `sig_raw` actually holds the deep-inflated magic while `sig_inner` holds the raw magic; classification must use bytes, not those column names (`artifact: _unknown_audit/section_residual.md:81`; `artifact: docs_complete_work/format_evidence.md:310-312`). Only the nested-container subgroup of the partition is decoded (`artifact: docs_complete_work/format_evidence.md:305-309`).
- The 615 are a codec-identification gap, not encryption: 16-byte alignment is archive-wide, and the 0.03 to 1.07 stored/logical spread with entropy around 7.9 is consistent with real compression (`artifact: unknown_accounting.md:77,81-82`). 543 of 615 are at or above 7.5 bits per byte, 614 of 615 have stored below logical, and there are 610 distinct first-16-byte prefixes (`artifact: unknown_accounting.md:77`).
- The 38 deflate-partial slots may include false positives and are not decoded formats (`artifact: unknown_accounting.md:89`).
- Signature verification is unresolved locally: our verifier records 0 verified, 0 failed, 4,373 unknown (`workspace: CONTEXT_HANDOFF.md:104`; `artifact: docs_complete_work/format_evidence.md:262-264`). No external RSA claim is used as a local measurement here.
- No distinct on-disk null marker, null bits or offset is asserted for the null word: the source provides only a missing CSV value (`artifact: type_census.csv:1`; `count_inventory.rs:131`).

## Changelog

- 2026-11-26: created this detailed partition document from `artifact: unknown_accounting.md:7-99`, `artifact: docs/coverage.md:12-16,123-183`, `workspace: CONTEXT_HANDOFF.md:96-99,101,131-154,341-371`, `artifact: docs_complete_work/plan.md` and `type_inventory.md`. Grade C for container/signature accounting only. All counts, sums and sub-partitions re-verified with bounded PowerShell probes against the independently scanned TSVs; no bulk archive reads, no Python, no keys, assets or publication. No RBF0 promotion applied.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/null-word-partition.md`. No count was selected by modification time. Reconciliation decisions: 4,375 and/or 4,330 are retained only as historical rejected header totals; the cited current total is 4,373 = 22 roots + 4,351 nested headers (`workspace: CONTEXT_HANDOFF.md:101,345,361,366`).


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
