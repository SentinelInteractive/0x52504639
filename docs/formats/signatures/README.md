# Payload signatures and the container layer

This directory documents eight recognized payload-signature families, the shared container layer and the null-word type partition. A signature describes bytes observed at a particular payload layer. It is not the resource type enum stored in a resource record. Several signatures are seen only after inflation; ADAT, KB2, SGD5 and the nested 9FPR containers are identified directly from stored bytes. [H, §8–9; U, “Nested containers” and “Signature-assigned”]

**The type-word table and the signature table are two independent partitions of the same 1,255,039 slots. They must never be added together.** Each table independently sums to 1,255,039 slots, 305,820,985,968 stored bytes and 564,783,265,279 logical bytes. A null-word slot with an ADAT signature is one slot viewed in two ways, not two slots. [T, both total rows; C-A, `all_families`; C-B, null-word family table]

## Identity

This retained document is supporting material; it introduces no independently decoded resource type. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/README.md`.

## Counts

No additional population count is asserted in this section. Any recorded counts retain their original evidence in Verification. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/README.md`.

## Where it appears

No additional storage-layer claim is introduced by this section. Original placement or container observations, if any, remain in Verification. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/README.md`.

## Layer status

This section adds no decode capability beyond the explicitly scoped evidence retained in the document. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/README.md`.

## Fields if any

This support section asserts no additional binary field layout.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| not applicable | not applicable | No additional binary field is asserted | unknown | `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/README.md` |

## Verification

### Pages and exact census partition

All rows below come from the signature partition. The denominator is 1,255,039 slots, 305,820,985,968 stored bytes and 564,783,265,279 logical bytes. `none` is the published signature-table label for the CSV's literal `Unknown` family; it does not mean that all such payloads lack recognizable structure after deeper inspection. [T, signature table; C-A, `all_families`; U, “Residual”]

| Signature | Slots | Stored bytes | Logical bytes | Recognition layer | Reported status |
|---|---:|---:|---:|---|---|
| [0DRPz](0drpz.md) | 290,294 | 12,137,708,928 | 51,368,850,240 | Inflated `+0x10` | Partial: wrapper and selected text blobs |
| [ADAT](adat.md) | 71,676 | 38,297,906,160 | 38,297,508,464 | Stored `+0x00` | Partial: reported audio-to-Opus path, no per-slot audit |
| [PSIN](psin.md) | 18,640 | 154,829,776 | 487,573,772 | Inflated `+0x00` | Partial: some header records |
| [9FPR](9fpr.md) | 4,351 | 147,279,874,016 | 147,279,874,016 | Stored `+0x00` | Full for container reading only |
| [RBF0](rbf0.md) | 1,278 | 2,129,984 | 16,004,417 | Inflated `+0x00` | Classified, no verified field decoder |
| [KB2](kb2.md) | 797 | 13,520,694,880 | 13,520,690,172 | Stored `+0x00` | Classified, payload not decoded |
| [XML](xml.md) | 221 | 3,639,664 | 40,592,391 | Inflated prefix (`XML@0` detector label) | Classified, text readable, parser unverified |
| [SGD5](sgd5.md) | 2 | 274,135,376 | 274,135,358 | Stored `+0x00` | Classified, shader mapping open |
| none | 867,780 | 94,150,067,184 | 313,498,036,449 | No recognized signature in the bounded census probe | Recognition result, not one semantic format |
| **Total** | **1,255,039** | **305,820,985,968** | **564,783,265,279** | | |

Counts: [C-A; C-B; T]. Positions: [F, “Identity”; U, “Signature-assigned”; C-A/C-B, family magic/status tables]. Decode status: [T, signature rows]. These are retained source status labels with their actual layer limits, not newly claimed decoders.

- [Container layer](container-layer.md) documents the shared header, TOC/resource record, table-width exceptions and cryptographic-verification limit. [H, §5]
- [Null-word partition](null-word.md) reconciles 101,479 slots into 4,351 nested containers, 92,614 signature-assigned slots and 4,514 residual. The residual is exactly 3,827 known/recognizable shapes, 30 placeholders, 615 codec gaps and 42 unknown. **Accounting is not decoding.** [U, primary reconciliation and residual tables]


### Wrapper type codes

0DRPz is shared by `0x0B zmt`, `0x49 zmap`, `0x4A ztyp`, `0x57 zas`, `0x6C zascd`, `0x6F zldbmt`, `0x71 zkit` and `0x73 zcov`. All 290,294 members belong to those eight codes. Every member of the other seven recognized signature rows has type `<null>` in this census; no numeric type code is manufactured from its magic. [C-A, family type breakdowns; C-B, family type and null-word family tables; F, “Identity”]

The 0DRPz source says its root is parsed via a PSIN wrapper path. That implementation relationship does not merge the two signature rows. Likewise, 9FPR nested-container extents and their child entries coexist in the same flat census; the metadata byte sum is not unique physical occupancy. [F, “Exe path”; U, “Nested containers”]


### Counting and evidence limits

“Slots” means CSV data rows in this fixed census. Family/root/type subtotals retain that unit; they are not distinct names or `(root, slot)` pairs. The CSV retains `header_offset` as a separate field, and nested containers can reuse local slot numbers. The second aggregation's distinct-pair diagnostics are not substituted for the census denominator. Stored and logical byte totals sum their respective CSV fields; neither is a count of successfully decoded output bytes. [C, CSV schema; C-B, summary definitions and distinct-slot diagnostics; U, “Nested containers”]

The bounded census probe is not a complete codec or semantic audit. The earlier raw-byte accounting report independently re-probed 1,823 signature-assigned samples with 1,823 agreements, including 1,021 inner-path recognitions. It also checked every nested 9FPR header length. Those reported checks remain separate from this task's fresh CSV aggregation. No new raw archive decode was run for these pages. [U, “Nested containers,” “Signature-assigned” and “Limit”; C-A; C-B]

The deeper 156 RBF0, one PSIN and 128 BOM-prefixed XML shapes remain in the 4,514 residual. This preserves the supplied signature-table version and exact reconciliation. A future promotion must revise both affected partitions explicitly. The residual's primary table, not its approximate proposed prose, controls the exact 3,827/30/615/42 split. [U, “Residual,” “Limit” and “Proposed coverage wording”]

No encoder, round-trip or game-load test is reported by the supplied format coverage. `9FPR` “Full” is limited to container reading, and the local RSA verifier is still zero verified, zero failed, 4,373 unknown. [H, §5, §8–9]


### Source register

The following identifiers are used locally in each page. They identify the requested source files and precise sections without importing unrelated material from those files.

| ID | Source and location | Use |
|---|---|---|
| C | [type_census.csv](../../type_census.csv), 21-column header and all data rows | Exact fixed census: family, type, root, magic, status and declared sizes |
| C-A | [census_aggregates.json](../_evidence/signatures_a/census_aggregates.json), `families`, `all_families`, `overall` | Rust aggregation for 0DRPz, ADAT, PSIN and 9FPR; all-family cross-check |
| C-B | [summary.json](../_evidence/signatures_b/summary.json) and sibling TSV tables | Separate Rust aggregation for RBF0, KB2, XML, SGD5 and the null-word partition |
| T | `coverage_audit/out/tables.md`, lines 1–42 (type partition), 44–57 (signature partition) | Exact published totals and signature-specific status notes |
| H | `CONTEXT_HANDOFF.md`, §5 (lines 94–104), §8 (131–154), §9 (158–201) | Corrected container geometry, type/signature distinction, current layer limits |
| U | [unknown_accounting.md](../../unknown_accounting.md), reconciliation (13–18), nested containers (22–31), signature-assigned (33–47), residual (49–77), limit (85–89) | Exact null-word/residual accounting and prior raw-byte verification |
| F | [docs/formats/0drpz.md](../../docs/formats/0drpz.md), “Identity,” “Container,” “Decode,” “Encode,” “Verification,” “Unknowns” | Eight-code wrapper, fields and bounded text-decoding claims |

All requested `docs/formats/*.md` files were searched for the eight signatures; the dedicated 0DRPz report supplies the family field map. The other family pages retain the input audit's explicit field/decoder gaps rather than importing structures from other formats. [T, signature notes; F]

### Reproducible census evidence

Both independent Rust aggregation tools read the same census SHA-256:

```text
f5e7729f1fd706a5b93fc71ad9f7acbf42ba5758a477bcbfa66b4ebcd0e5275d
```

Each reports 1,255,039 data rows. Their all-family slot/stored/logical totals agree with each other and the two published total rows. Retained source code is in [aggregation A](../_evidence/signatures_a/census_family_agg.rs) and [aggregation B](../_evidence/signatures_b/census_agg/src/main.rs); B's [run log](../_evidence/signatures_b/run_log.txt) and [evidence README](../_evidence/signatures_b/README.md) record its command and diagnostics. This task used **two fast-workers for counting**. [C-A; C-B]

## Unknowns

This heading does not resolve any unknown field or decoding limit. Consult the retained evidence and its source limitations. Preserved source: `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/README.md`.

## Changelog

- 2026-11-26: Created the eight signature pages, shared container-layer page and null-word partition page. Reconciled exact census totals with two Rust counting workers. Kept the two partitions independent, preserved deeper residual classifications, and separated recognition, decompression, structural reads and semantic decoding. [C-A; C-B; T; U; H; F]

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/README.md`. No count was selected by modification time.

