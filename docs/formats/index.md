# RPF9 documentation coverage index

## Identity

This index covers the 37 type-table rows (36 named codes and the null-word row), eight requested signature families, and the separate null-word partition. Documentation coverage does not imply complete payload decoding. Source: `artifact: docs/coverage.md:121-183` and the individually linked documents.

## Counts

The census contains exactly **1,255,039 slots**, **305,820,985,968 stored bytes**, and **564,783,265,279 logical bytes**. Type and signature tables independently partition the same slots; overlapping nested-container byte ranges are not unique physical storage. Sources: `artifact: docs/coverage.md:7-16,164,181`; `artifact: docs_complete_work/independent_counts/compare_stdout.txt:7-31`.

The required deliverables are 46 subject documents plus this index. Supplemental evidence, guides and the consistency report are listed separately below; the current exact Markdown-file total is audited in [CONSISTENCY.md](CONSISTENCY.md).

## Container

### Resource-type rows


| Document | Type code | Census slots | Grade | Coverage status | Coverage boundary |
|---|---|---:|---|---|---|
 | [zbdr](zbdr.md) | `0x0f` | 250,434 | B | Partial structure/decoding | Covers supported page, bounds and leaf-reference structures; internal-node interpretation and writing remain limited. | 
 | [zdr](zdr.md) | `0x02` | 167,897 | B | Partial structure/decoding | Covers sampled LOD0 geometry, materials and diffuse-texture export; skin payloads, other LODs and a writer are outside demonstrated coverage. | 
 | [zmap](zmap.md) | `0x49` | 166,072 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. | 
 | [Null-word type row](type-null-word.md) | absent | 101,479 | D | Identity/count only | Covers the unassigned candidate-type-word row; absence of classification does not imply an entirely unknown or decoded payload. | 
 | [zbn](zbn.md) | `0x06` | 92,199 | B | Partial structure/decoding | Covers page/container framing and supported root-volume fields; shape-body semantics remain incomplete. | 
 | [zcd](zcd.md) | `0x43` | 62,384 | B | Partial structure/decoding | Covers the compression prefix and supported inflated header observations; body layout and semantic identity remain unknown. | 
 | [zft](zft.md) | `0x03` | 55,488 | B | Partial structure/decoding | Covers page-prefix, stream-chain and size identities; resource-body semantics remain undecoded. | 
 | [zdd](zdd.md) | `0x04` | 48,584 | B | Partial structure/decoding | Covers header, name-region and pointer-table observations; the wrapped-object layout remains incomplete. | 
 | [zsm](zsm.md) | `0x58` | 40,019 | B | Partial structure/decoding | Covers container/header evidence and supported array or bounds variants; element semantics and type identity remain incomplete. | 
 | [zascd](zascd.md) | `0x6c` | 32,878 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. | 
 | [zldbmt](zldbmt.md) | `0x6f` | 30,511 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. | 
 | [zmt](zmt.md) | `0x0b` | 28,328 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; non-text and type-specific payload semantics remain unverified. | 
 | [znv](znv.md) | `0x4f` | 27,644 | B | Partial structure/decoding | Covers sampled tile/header and hierarchy or mesh-array traversal; vertex and node semantics remain incomplete. | 
 | [zsp](zsp.md) | `0x64` | 27,482 | B | Partial structure/decoding | Covers container and hash-table structure; token and key semantics remain undecoded. | 
 | [zad](zad.md) | `0x4e` | 25,608 | B | Partial structure/decoding | Covers container and supported clip-header fields; channel-record arrays remain undecoded. | 
 | [zbft](zbft.md) | `0x11` | 22,440 | B | Partial structure/decoding | Covers supported root/header and leaf-reference structures; node and geometry decoding remain incomplete. | 
 | [zbdd](zbdd.md) | `0x10` | 22,382 | B | Partial structure/decoding | Covers header, ascending index and bounded pointer-array structure; index and descriptor meanings remain unresolved. | 
 | [zas](zas.md) | `0x57` | 15,067 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. | 
 | [zpm](zpm.md) | `0x46` | 8,443 | B | Partial structure/decoding | Covers header observations including supported count/capacity and twin-identifier relations; key semantics and record stride remain unresolved. | 
 | [zcov](zcov.md) | `0x73` | 8,415 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. | 
 | [zfid](zfid.md) | `0x67` | 6,762 | B | Partial structure/decoding | Covers supported header, word-count and padded-body identities; element semantics remain undecoded. | 
 | [ztyp](ztyp.md) | `0x4a` | 6,308 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. | 
 | [zkit](zkit.md) | `0x71` | 2,715 | C | Container/wrapper/signature only | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. | 
 | [ztd](ztd.md) | `0x05` | 2,612 | B | Partial structure/decoding | Covers container/header evidence and observed body-size decompositions; pixel format and resource identity remain unresolved. | 
 | [zscript](zscript.md) | `0x59` | 746 | B | Partial structure/decoding | Covers resource decoding and structurally verified instruction listing; program semantics and source reconstruction remain outside coverage. | 
 | [zvert](zvert.md) | `0x12` | 611 | C | Container/wrapper/signature only | Covers container and observed pointer/length-class profiles; field roles, count and stride remain unresolved. | 
 | [zcg](zcg.md) | `0x5f` | 518 | B | Partial structure/decoding | Covers container and supported end-relative relations; the record body remains undecoded. | 
 | [zcgc](zcgc.md) | `0x72` | 518 | B | Partial structure/decoding | Covers header/body observations and twin-identifier relations; full float-body semantics remain unresolved. | 
 | [zpt](zpt.md) | `0x48` | 226 | B | Partial structure/decoding | Covers the supported pointer-table partition; segment semantics, counts and record strides remain unresolved. | 
 | [zmmd](zmmd.md) | `0x66` | 142 | C | Container/wrapper/signature only | Covers container and size/stream population profiles; count, stride and payload meaning remain unresolved. | 
 | [zcps](zcps.md) | `0x63` | 98 | B | Partial structure/decoding | Covers supported header and duplicated count-pair observations; record semantics remain undecoded. | 
 | [zfd](zfd.md) | `0x56` | 11 | B | Partial structure/decoding | Covers the observed path-string count relation and tail extent; the complete record layout remains unresolved. | 
 | [ztsl](ztsl.md) | `0x65` | 5 | B | Partial structure/decoding | Covers supported header, count and body-size relations; element semantics remain unresolved. | 
 | [zsmam](zsmam.md) | `0x6e` | 5 | C | Container/wrapper/signature only | Covers container and repeating-field observations; no fixed header stream or decoded count is established. | 
 | [zrd](zrd.md) | `0x6d` | 4 | B | Partial structure/decoding | Covers inner magic and the observed count relation; the record chain remains undecoded. | 
 | [zjd](zjd.md) | `0x4d` | 3 | B | Partial structure/decoding | Covers the supported duplicated-count and pointer-array relation; element semantics and a payload-wide stride remain unresolved. | 
 | [zpmd](zpmd.md) | `0x45` | 1 | C | Container/wrapper/signature only | Covers the single-slot container and header profile; a payload decoder is not established. | 

Row counts and source coverage notes: `artifact: docs/coverage.md:127-163`; independently recounted totals: `artifact: docs_complete_work/type_counts.tsv`. The linked documents supply field-specific evidence.

### Inner-signature families

| Document | Census slots | Grade | Coverage status | Coverage boundary |
|---|---:|---|---|---|
 | [0DRPz](signatures/0drpz.md) | 290,294 | B | Partial structure/decoding | Covers wrapper and supported text-blob structures; other blob families and type-specific payload-wide decoding remain incomplete. | 
 | [ADAT](signatures/adat.md) | 71,676 | C | Container/wrapper/signature only | Covers supported bank/header and audio-pipeline evidence; a complete per-slot payload audit is absent. | 
 | [PSIN](signatures/psin.md) | 18,640 | C | Container/wrapper/signature only | Covers supported signature/header observations; no complete local payload decoder is demonstrated. | 
 | [9FPR](signatures/9fpr.md) | 4,351 | B | Partial structure/decoding | Covers nested archive-container structure and its validation; leaf-resource decoding is a separate question. | 
 | [RBF0](signatures/rbf0.md) | 1,278 | C | Container/wrapper/signature only | Covers census identity and supported signature evidence; no complete local field decoder is demonstrated. | 
 | [KB2](signatures/kb2.md) | 797 | C | Container/wrapper/signature only | Covers signature census and explicitly attributed external context; the local payload is not decoded. | 
 | [XML](signatures/xml.md) | 221 | C | Container/wrapper/signature only | Covers recognized text-signature census and limitations; a verified parser/schema audit is absent. | 
 | [SGD5](signatures/sgd5.md) | 2 | C | Container/wrapper/signature only | Covers signature identity and the two-slot census; payload and shader-role decoding remain unresolved. | 

These counts use the published bounded-probe partition. The additional 867,780 slots with no recognized signature are not a ninth requested signature-family document and are distinct from the 101,479 null-word slots. Sources: `artifact: docs/coverage.md:168-183`; `artifact: docs_complete_work/family_counts.tsv`.

### Null-word partition

| Document | Census slots | Grade | Coverage status | Coverage boundary |
|---|---:|---|---|---|
 | [Null-word partition](null-word-partition.md) | 101,479 | C | Container/wrapper/signature only | Reconciles nested containers, signature assignments and residual subgroups; classification is not a payload decoder. | 

The published partition is 4,351 nested containers + 92,614 signature-assigned slots + 4,514 residual slots = 101,479. The residual contains 3,827 recognizable slots, 30 placeholders, 615 slots with a codec-identification gap and 42 genuinely unknown slots. Sources: `artifact: unknown_accounting.md:7-18,49-75`; `artifact: docs_complete/null-word-partition.md`.

The source's hypothetical total of 92,770 includes 156 additional RBF0 hits; also promoting its one additional PSIN hit would give 92,771. Neither promotion is applied to the published tables here. Source: `artifact: unknown_accounting.md:75`; arithmetic: `92614 + 156 = 92770`, `92614 + 156 + 1 = 92771`.


### Supplemental evidence and administration

| Document | Coverage status | What it does and does not cover |
|---|---|---|
| [signatures/container-layer.md](signatures/container-layer.md) | B, supplemental container structure | Covers shared archive-header/TOC evidence and known exceptions; it does not decode contained leaf formats or verify RSA signatures. |
| [signatures/null-word.md](signatures/null-word.md) | C, supplemental signature accounting | Retains signature-oriented null-word accounting; it does not imply semantic payload decoding. |
| [signatures/README.md](signatures/README.md) | Guide | Lists the signature partition and its evidence; it does not add a decoder. |
| [evidence/census_evidence.md](evidence/census_evidence.md) | Retained census evidence | Records source counts and reproduction evidence; it does not measure decoded payload coverage. |
| [evidence/seven_types_index_section.md](evidence/seven_types_index_section.md) | Retained index evidence | Preserves seven-type count and scope evidence; it is not a separate resource type. |
| [_evidence/signatures_b/README.md](_evidence/signatures_b/README.md) | Retained census evidence | Documents the signature aggregation and definitions; it does not decode signature-family payloads. |
| [_evidence/signatures_index_section.md](_evidence/signatures_index_section.md) | Retained index evidence | Preserves the signature index contribution; it does not introduce a ninth requested signature family. |
| [_evidence/tail_reconciliation.md](_evidence/tail_reconciliation.md) | Retained reconciliation evidence | Records tail-type sourcing and coverage decisions; it does not remove the cited decode limitations. |
| [index.md](index.md) | Index | Lists every Markdown document and its coverage boundary; it is not a binary-format decoder. |
| [CONSISTENCY.md](CONSISTENCY.md) | Audit | Reports headings, confidence tokens and path-reference counts for every Markdown file; it does not validate game-load behavior. |

## Fields

This index does not define binary fields. Field layouts and per-field confidence belong to the linked subject documents.

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| not applicable | not applicable | No binary field is asserted by this index | unknown | Linked subject documents' Fields or Fields if any sections |

## Decode status

Grades are editorial scope labels: A requires a complete demonstrated decode of an explicitly bounded layer, B denotes partial structure/decoding, C denotes container/wrapper/signature coverage only, and D denotes identity/count evidence only. No source-table Full status upgrades the sampled drawable or structural script result to complete semantic decoding. Each table row states the supported boundary and links its evidence. Field confidence remains separate: measured, inferred, external or unknown.

## Verification

Two release Rust census runs produced byte-identical type, family, null-family and cross-tab TSVs; all 37 type rows and nine census family rows agree with the source table on slots, stored bytes and logical bytes, with zero substantive mismatches. Evidence: `artifact: docs_complete_work/independent_counts/compare_stdout.txt`; commands and scanner limitations: `artifact: docs_complete_work/independent_verification.md`.

Earlier accurate subset evidence is retained rather than replaced by modification time: seven named types account for 235,446 slots / 18,437,133,488 stored / 69,980,587,296 logical bytes (`evidence/seven_types_census.parent_verified.txt`); six other indexed types account for 794,474 slots / 82,629,088,992 stored / 275,215,441,440 logical bytes (`evidence/census_counts.json`). These are subset totals, not extra slots. Original assembled index: `artifact: docs_complete_work/reconciliation_original_20261126_1/index.md`.

The exact per-file heading and confidence audit, counting rules, command and remaining drive-letter path references are recorded in [CONSISTENCY.md](CONSISTENCY.md).

## Unknowns

Every type-table row has a document, including the null row; none is omitted for lack of a payload decoder. Container-only, wrapper-only and semantically incomplete types remain explicitly limited in their documents. Signature none (867,780 slots) is not a ninth requested family and is distinct from the 101,479 null-word slots (`artifact: docs/coverage.md:172,183`). No external format layout is promoted to a local measurement by this index.

## Changelog

- 2026-11-26: replaced fragmented index assembly with a complete subject and supplemental-document register, preserving the prior index in the cited snapshot. Rejected the earlier estimate of 245,000 slots for the seven-type subset in favor of the artifact-backed 235,446 (`evidence/seven_types_census.parent_verified.txt`).
- 2026-11-26: retained the published null-word partition. The source's hypothetical 92,770 count includes only 156 additional RBF0 hits; including its one additional PSIN hit would give 92,771. Neither promotion is applied (`artifact: unknown_accounting.md:75`). Source-table Full labels remain attributed; conservative document grades and actual decode limits control this index.
