# Null word (type-word Unknown group)

The null word is the **absence of a candidate type classification** for a slot in the census: 101,479 slots carry no `type_hash` value in `artifact: type_census.csv` and occupy row 4 of the 37-row type table (`artifact: docs/coverage.md:130`; `artifact: docs_complete_work/type_counts.tsv:38`, key `<null>`). It is **not a fully decoded format** and it is **not an entirely unexplained residue**. The population is accounted for at slot and byte level by three populations, but accounting is not a payload decode (`artifact: unknown_accounting.md:7-18,99`). Coverage status is Unknown: no type word, or no verified name for it (`artifact: docs/coverage.md:25`).

Grade: **D** (identity, counts and partition accounting only; no decoded payload, no field layout, no writer). This page makes no full-decode implication. Detailed partition reasoning is in `artifact: docs_complete/null-word-partition.md`.


Editorial coverage grade: **D**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

- The `+0x10` word of the 20-byte resource record is the engine's resource type enum; static codes `0x00..0x12`, callback codes `0x40..0x73` (`workspace: CONTEXT_HANDOFF.md:99,133-135`). The null group is the rows with **no** such word (`artifact: docs/coverage.md:123`).
- In the census, the group is a **missing value in the CSV `type_hash` column**, represented by the literal token `<null>`. It is the only token used for this group; there are zero empty or bare `null` rows (`artifact: type_census.csv:1`; `artifact: census_recount/report.md:32,63`; `artifact: docs_complete/_evidence/signatures_b/README.md`; `artifact: docs_complete_work/count_inventory.rs:108,131`; `artifact: docs_complete_work/type_counts.tsv:38`). No distinct on-disk null marker, null-bit field or special offset is established by the source; do not assert one.
- It is one row in the type partition, not a signature. It must not be added to the signature partition: signature `none` is 867,780 slots and means "no recognized inner signature", not "unexamined" (`artifact: docs/coverage.md:12-16,172,183`; `artifact: docs_complete_work/plan.md:9`).
- The 4,351 `9FPR` slots are inside this group and also inside the signature `9FPR` row; they are not extra slots (`artifact: docs/coverage.md:176`; `artifact: unknown_accounting.md:15,22-31`).

## Counts

| Measure | Value | Source |
|---|---:|---|
| Slots | 101,479 | `artifact: docs/coverage.md:130`; `type_counts.tsv:38` |
| Stored bytes | 199,765,610,064 | `artifact: docs/coverage.md:130`; `type_counts.tsv:38` |
| Logical bytes | 200,460,005,055 | `artifact: docs/coverage.md:130`; `type_counts.tsv:38` |
| Share of 1,255,039 slots | 101,479 / 1,255,039 (exact fraction; no rounded share used) | `artifact: docs/coverage.md:39`; `artifact: docs_complete_work/type_counts.tsv:38` |

Three-population partition (`artifact: unknown_accounting.md:13-20`; confirmed by `artifact: docs_complete_work/nullword_family.tsv`):

| Population | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| Nested containers `9FPR` | 4,351 | 147,279,874,016 | 147,279,874,016 |
| Signature-assigned (six families) | 92,614 | 52,253,335,840 | 52,636,504,574 |
| No-signature residual | 4,514 | 232,400,208 | 543,626,465 |
| **Total** | **101,479** | **199,765,610,064** | **200,460,005,055** |

Arithmetic verified: 4,351 + 92,614 + 4,514 = 101,479; 147,279,874,016 + 52,253,335,840 + 232,400,208 = 199,765,610,064; 147,279,874,016 + 52,636,504,574 + 543,626,465 = 200,460,005,055. Both byte sums match the null-word row exactly (`artifact: unknown_accounting.md:20`).

Signature-assigned subcount (`artifact: unknown_accounting.md:37-47`; `nullword_family.tsv`): `ADAT` 71,676; `PSIN` 18,640; `RBF0` 1,278; `KB2` 797; `XML` 221; `SGD5` 2. Sum: 71,676 + 18,640 + 1,278 + 797 + 221 + 2 = 92,614 (`artifact: unknown_accounting.md:45`).

Residual subpartition, exact (`artifact: unknown_accounting.md:49-71`): known or recognizable 3,827 (195,216,032 stored / 405,428,345 logical); placeholders 30 (480 / 450); raw no-magic high-entropy codec gap 615 (33,926,464 / 126,978,572); genuinely unknown 42 (3,257,232 / 11,219,098, of which 38 deflate-partial and 4 unmatched compressed binaries). 3,827 + 30 + 615 + 42 = 4,514. Compression split zlib 3,671 + raw deflate 157 + deflate-partial 38 + none 648 = 4,514 (`artifact: unknown_accounting.md:73`).

## Container

- The 4,351 nested `9FPR` slots are archive headers, not leaf payloads. Per root, container slots equal `headers - 1`; all 22 differences are zero, 4,373 - 22 = 4,351 (`artifact: unknown_accounting.md:24-31`; `workspace: CONTEXT_HANDOFF.md:101`).
- All 4,351 carry `9FPR`, header length parses on 4,351 of 4,351, and length is below stored size for every slot. Stored equals logical: 147,279,874,016 bytes, raw, never deflated (`artifact: unknown_accounting.md:26-27`).
- The container header is 64 bytes with magic `9FPR` (`0x52504639`), header length at `+0x04`, split at `+0x08`, count at `+0x24`, width from low `+0x2C`, generation tags `0x1C` and `0x30` (`workspace: CONTEXT_HANDOFF.md:96-99`).
- The 22 named roots are separate files on disk; a container slot is deeper nesting inside one root, not the same object as a pack root. No size or prefix match against pack roots is expected; finding none is a clean negative (`artifact: unknown_accounting.md:30`).
- Byte sums are sums over rows, not unique physical bytes: nested container ranges contain their descendants (`artifact: docs/coverage.md:8-10`). For this partition specifically both totals match the null-word row to the byte, as verified in Verification.

## Fields

No payload field layout is decoded for this group. The table lists the census CSV columns used to identify and partition it, plus the general resource-record descriptor word at `+0x10` where that word is present; no on-disk field layout is claimed for null slots themselves.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| `type_hash` (CSV column) | n/a | Missing value selects the null group; only token `<null>` occurs, no empty/bare `null` rows | measured | `artifact: type_census.csv:1`; `census_recount/report.md:32,63`; `_evidence/signatures_b/README.md:26-27`; `count_inventory.rs:108,131`; `type_counts.tsv:38` |
| `+0x10` (resource record descriptor word `w4`) | 4-byte word (u32), low byte = code, where present | Engine type enum word: the whole word measures `0x00000059` on 746 script slots. Not applicable to this group, where no `type_hash` value is present; no on-disk null-field width is asserted | measured | `artifact: docs/formats/script-resources.md:7,55`; `workspace: CONTEXT_HANDOFF.md:99,133`; `artifact: docs/coverage.md:123`; `artifact: type_census.csv:1` |
| distinct null marker / null bits | n/a | No such field is established by the source; do not assert an offset or bit layout | unknown | `artifact: type_census.csv:1`; `count_inventory.rs:131` |
| `family`, `stored_bytes`, `logical_bytes` (CSV columns) | n/a | Partition the group into 4,351 / 92,614 / 4,514 and verify byte totals | measured | `nullword_family.tsv:1-9`; `artifact: unknown_accounting.md:13-20` |

## Decode status

- Coverage status: Unknown, no type word or no verified name (`artifact: docs/coverage.md:25,130`). Grade D: identity, count and accounting evidence only (`artifact: docs_complete_work/plan.md:9`).
- The 4,351 nested containers are **container-layer** reads only; the signature row is Full for the container layer, not for leaf payloads (`artifact: docs/coverage.md:176,183`).
- The 92,614 signature-assigned slots carry recognized inner signatures but no type word; several families have only name and count verified, with no field report (`artifact: docs/coverage.md:174-180`; `artifact: unknown_accounting.md:35,47`).
- The 4,514 residual is **accounted, not decoded**. Of it, 615 is a codec-identification gap, not unknown content, and 42 are genuinely unknown; 38 deflate-partial slots may include false positives and are reported as a group, not as decoded formats (`artifact: unknown_accounting.md:69-71,77,88-89`).
- No encoder, round-trip, game-load test or bytecode/field semantics is claimed for any part of this group (`workspace: CONTEXT_HANDOFF.md:201`).

## Verification

Own bounded checks, no bulk archive reads:

```
Import-Csv 'artifact: docs_complete_work/nullword_family.tsv' -Delimiter "`t" | Measure-Object slots,stored_bytes,logical_bytes -Sum
# rows=8 slots_sum=101479 stored_sum=199765610064 logical_sum=200460005055

Import-Csv 'artifact: docs_complete_work/type_counts.tsv' -Delimiter "`t" | Where-Object type_hash -eq '<null>'
# slots=101479 stored=199765610064 logical=200460005055  -> match_slots/stored/logical all True

PowerShell arithmetic (see artifact: docs_complete_work/null_write.md):
# part_slots=101479  part_stored=199765610064  part_logical=200460005055
# sig_slots=92614  sig_stored=52253335840  sig_logical=52636504574
# known_groups=3827  residual_part=4514  codec_part=4514
```

Path aliases used in this document, all resolved with `Test-Path -LiteralPath` on 2026-11-26: `count_inventory.rs`, `nullword_family.tsv`, `type_counts.tsv`, `inventory_log.txt`, `type_inventory.md` and `format_evidence.md` mean `artifact: docs_complete_work/<filename>`; `census_recount/report.md` means `artifact: census_recount/report.md`; `_evidence/signatures_b/README.md` means `artifact: docs_complete/_evidence/signatures_b/README.md`. All other cited paths are written in full.

Source-layer checks already on record: the earlier independent Rust scan read 1,255,039 data rows with 0 malformed rows and matched `artifact: docs/coverage.md:127-181` byte for byte (`artifact: docs_complete_work/type_inventory.md:24-45`, `inventory_log.txt`). An independent Rust re-probe of 1,823 sampled signature-assigned slots reproduced the CSV family in 1,823 of 1,823 cases, 1,021 on the inner path (`artifact: unknown_accounting.md:47`). The residual leaf was still running when that report was written (`artifact: unknown_accounting.md:87`); the consolidated handoff later records the audit as done (`workspace: CONTEXT_HANDOFF.md:21,154`).

## Unknowns

- Stale superseded counts: residual `unknown` was 621 after a deflate-cap fix and is now 615 (`artifact: unknown_accounting.md:88`); 4,375 headers is superseded by 4,373 = 22 + 4,351, and 4,330 is an older correction (`workspace: CONTEXT_HANDOFF.md:101,345,361,366`). The 55 "deflate-partial" hits from an earlier probe were killed as garbage-offset matches; only offset-0 exact matches are real (`artifact: unknown_accounting.md:83`).
- Status snapshot conflict: the older `workspace: coverage_audit/out/tables.md:5-41` marks 25 rows Classified and 9 Partial; the current `artifact: docs/coverage.md:127-163` marks 4 Classified and 30 Partial, with 21 promoted rows. The later file (mtime 19:58Z vs 14:32Z on 2026-11-24) is authoritative. The null-word row remains Unknown in both snapshots (`artifact: docs_complete_work/type_inventory.md:138`).
- RBF0 deeper-promotion caveat, **not applied**: 156 deep-inflate `RBF0` and 1 deep-inflate `PSIN` sit at offset 0 of the inflated payload, not at the bounded-prefix layer (`artifact: unknown_accounting.md:75`). That source sentence says promoting both would give `RBF0` 1,434 and signature-assigned 92,770. The arithmetic is internally inconsistent: 92,614 + 156 = 92,770, but 92,614 + 156 + 1 = 92,771, which would also make `PSIN` 18,641 rather than the published 18,640 (`artifact: unknown_accounting.md:35-47`). The source's 92,770 therefore matches promoting **only** the 156 `RBF0` rows, not both populations. This document records the inconsistency, does **not** reproduce 92,770 as a both-populations result, and keeps the published `RBF0` 1,278, `PSIN` 18,640 and signature-assigned 92,614 unchanged. No promotion is applied.
- The 4,351 container classification and membership come from the same header table, so they are consistent but not independent; the on-disk `9FPR` reads are independent (`artifact: unknown_accounting.md:31`).
- Producer caveat: the CSV column `sig_raw` actually holds the deep-inflated magic while `sig_inner` holds the raw magic; classification must use bytes, not those column names (`artifact: _unknown_audit/section_residual.md:81`; `artifact: docs_complete_work/format_evidence.md:310-312`). Only the nested-container subgroup of the partition is decoded (`artifact: docs_complete_work/format_evidence.md:305-309`).
- 16-byte alignment is an archive-wide property and is not evidence of encryption; the residual's 0.03 to 1.07 stored/logical spread with entropy around 7.9 indicates real compression (`artifact: unknown_accounting.md:77,81-82`).
- Signature verification is unresolved locally: our verifier records 0 verified, 0 failed, 4,373 unknown (`workspace: CONTEXT_HANDOFF.md:104`; `artifact: docs_complete_work/format_evidence.md:262-264`). No external RSA claim is used as a local measurement here.
- No distinct on-disk null marker, null bits, or offset for a null-field is asserted: the source provides only a missing CSV value (`artifact: type_census.csv:1`; `count_inventory.rs:131`).

## Changelog

- 2026-11-26: created this 37th-row type document from `artifact: docs/coverage.md:130`, `artifact: unknown_accounting.md:7-99`, `workspace: CONTEXT_HANDOFF.md:99,133-154,341-371`, `artifact: docs_complete_work/plan.md` and `type_inventory.md`. Grade D, no full-decode implication. All partition counts and byte totals re-verified with bounded PowerShell probes against the independently scanned TSVs; no bulk archive read, no Python, no keys, assets or publication.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/type-null-word.md`. No count was selected by modification time. Reconciliation decisions: 4,375 and/or 4,330 are retained only as historical rejected header totals; the cited current total is 4,373 = 22 roots + 4,351 nested headers (`workspace: CONTEXT_HANDOFF.md:101,345,361,366`).


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
