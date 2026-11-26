# Graded format documentation set

This folder holds 53 Markdown documents: one for each of the 37 rows in the resource-type table (36 named type codes plus the null-word row), one for each of the eight requested inner-signature families, the null-word partition, the shared container layer, retained evidence, this index and the consistency audit. Grades are editorial scope labels, not source-table status labels: **A** means a complete demonstrated decode of an explicitly bounded layer, **B** partial structure or decoding, **C** container, wrapper or signature only, and **D** identity and count only. Field tables in each document carry their own per-field confidence (`measured`, `inferred`, `external` or `unknown`). This set is documentation; it is not a decoder and it is not a writer. No writer, encoder, key, game asset or extracted content is supplied.

The census has 1,255,039 slots, 305,820,985,968 stored bytes and 564,783,265,279 logical bytes. The type table and the signature table are independent partitions of those same slots and must not be added together. Signature `none` (867,780 slots) is not the 101,479 null-word type slots.

## Identity

This index covers all 53 documents in this folder: the 37 type rows, eight signature families, the null-word partition, the shared container layer, the retained evidence, the earlier coverage index and the consistency audit. It defines no binary field and adds no decoder.

## Path-audit summary

The source folder included `PATH_AUDIT.md`, which is deliberately not copied into this folder; its counts are summarised here. It was a path-hygiene pass only: no number, grade, confidence label or claim was changed. It reports 53 Markdown files, 52 files with at least one changed line, 1,641 changed lines and 2,564 rewrites: 2,360 artifact-root rewrites, 195 workspace-root rewrites, four bare game-data-root rewrites, five temporary-workspace rewrites and zero defensive fallbacks. Five URL-scheme or `pack`-scheme lookbehind rejections were left untouched by design. The detector used a negative lookbehind so that `https`, `http` and `pack` scheme tokens are not treated as drive paths: source matches 2,564, destination matches 0. The two-sided token check recorded `https` 3 in both source and destination, `github.com` 0, `http` 0 and `pack` scheme 2, with zero mismatched files. A post-audit rescan of all 54 source-side files, including the audit itself, passed.

## Grouping

The four groups below are by subject and population size: container, signatures and supporting records first; then resource types with at least 10,000 census slots; then types with 1,000 to 9,999 slots; then tail types with fewer than 1,000 slots. Every document appears exactly once. "Not stated" means the document itself gives no editorial grade; the status is the one assigned in `index.md`.

## Container and signatures

| Document | Type or family | Slots | Grade | Covers and does not cover |
| --- | --- | ---: | --- | --- |
| [signatures/container-layer.md](signatures/container-layer.md) | Shared archive container and TOC read layer | 4,351 nested containers | B, supplemental | Covers shared archive-header and TOC evidence plus known exceptions; it does not decode contained leaf formats or verify RSA signatures. |
| [signatures/0drpz.md](signatures/0drpz.md) | 0DRPz inner signature | 290,294 | B | Covers the wrapper and supported text-blob structures; other blob families and type-specific payload-wide decoding remain incomplete. |
| [signatures/9fpr.md](signatures/9fpr.md) | 9FPR nested-container signature | 4,351 | B | Covers nested archive-container structure and its validation; leaf-resource decoding is a separate question. |
| [signatures/adat.md](signatures/adat.md) | ADAT audio signature | 71,676 | C | Covers supported bank/header and audio-pipeline evidence; a complete per-slot payload audit is absent. |
| [signatures/psin.md](signatures/psin.md) | PSIN inner signature | 18,640 | C | Covers supported signature and header observations; no complete local payload decoder is demonstrated. |
| [signatures/rbf0.md](signatures/rbf0.md) | RBF0 inner signature | 1,278 | C | Covers census identity and supported signature evidence; no complete local field decoder is demonstrated. |
| [signatures/kb2.md](signatures/kb2.md) | KB2 video signature | 797 | C | Covers the signature census and explicitly attributed external context; the local payload is not decoded. |
| [signatures/xml.md](signatures/xml.md) | XML text signature | 221 | C | Covers recognized text-signature census and limitations; a verified parser or schema audit is absent. |
| [signatures/sgd5.md](signatures/sgd5.md) | SGD5 shader signature | 2 | C | Covers signature identity and the two-slot census; payload and shader-role decoding remain unresolved. |
| [signatures/null-word.md](signatures/null-word.md) | Signature-oriented null-word accounting | 101,479 | C, supplemental | Retains signature-oriented null-word accounting; it does not imply semantic payload decoding. |
| [null-word-partition.md](null-word-partition.md) | Null-word type row partition | 101,479 | C | Reconciles nested containers, signature assignments and residual subgroups; classification is not a payload decoder. |
| [signatures/README.md](signatures/README.md) | Signature directory guide | not applicable | Not stated (guide) | Lists the signature partition and its evidence; it does not add a decoder. |
| [evidence/census_evidence.md](evidence/census_evidence.md) | Retained census evidence | not applicable | Not stated (retained evidence) | Records source counts and reproduction evidence; it does not measure decoded payload coverage. |
| [evidence/seven_types_index_section.md](evidence/seven_types_index_section.md) | Retained index evidence | not applicable | Not stated (retained evidence) | Preserves seven-type count and scope evidence; it is not a separate resource type. |
| [index.md](index.md) | Coverage index | 1,255,039 | Not stated (index) | Lists every document and its coverage boundary; it is not a binary-format decoder. |
| [CONSISTENCY.md](CONSISTENCY.md) | Consistency audit | not applicable | Not stated (audit) | Reports headings, confidence tokens and path-reference counts for every Markdown file; it does not validate game-load behavior. |

## Large payload types (at least 10,000 slots)

| Document | Type code | Slots | Grade | Covers and does not cover |
| --- | --- | ---: | --- | --- |
| [zbdr.md](zbdr.md) | 0x0f | 250,434 | B | Covers supported page, bounds and leaf-reference structures; internal-node interpretation and writing remain limited. |
| [zdr.md](zdr.md) | 0x02 | 167,897 | B | Covers sampled LOD0 geometry, materials and diffuse-texture export; skin payloads, other LODs and a writer are outside demonstrated coverage. |
| [zmap.md](zmap.md) | 0x49 | 166,072 | C | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. |
| [type-null-word.md](type-null-word.md) | absent | 101,479 | D | Covers the unassigned candidate-type-word row; absence of classification does not imply an entirely unknown or decoded payload. |
| [zbn.md](zbn.md) | 0x06 | 92,199 | B | Covers page and container framing plus supported root-volume fields; shape-body semantics remain incomplete. |
| [zcd.md](zcd.md) | 0x43 | 62,384 | B | Covers the compression prefix and supported inflated header observations; body layout and semantic identity remain unknown. |
| [zft.md](zft.md) | 0x03 | 55,488 | B | Covers page-prefix, stream-chain and size identities; resource-body semantics remain undecoded. |
| [zdd.md](zdd.md) | 0x04 | 48,584 | B | Covers header, name-region and pointer-table observations; the wrapped-object layout remains incomplete. |
| [zsm.md](zsm.md) | 0x58 | 40,019 | B | Covers container and header evidence plus supported array or bounds variants; element semantics and type identity remain incomplete. |
| [zascd.md](zascd.md) | 0x6c | 32,878 | C | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. |
| [zldbmt.md](zldbmt.md) | 0x6f | 30,511 | C | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. |
| [zmt.md](zmt.md) | 0x0b | 28,328 | C | Covers type census and shared wrapper evidence; non-text and type-specific payload semantics remain unverified. |
| [znv.md](znv.md) | 0x4f | 27,644 | B | Covers sampled tile and header evidence plus hierarchy or mesh-array traversal; vertex and node semantics remain incomplete. |
| [zsp.md](zsp.md) | 0x64 | 27,482 | B | Covers container and hash-table structure; token and key semantics remain undecoded. |
| [zad.md](zad.md) | 0x4e | 25,608 | B | Covers container and supported clip-header fields; channel-record arrays remain undecoded. |
| [zbft.md](zbft.md) | 0x11 | 22,440 | B | Covers supported root and header plus leaf-reference structures; node and geometry decoding remain incomplete. |
| [zbdd.md](zbdd.md) | 0x10 | 22,382 | B | Covers header, ascending index and bounded pointer-array structure; index and descriptor meanings remain unresolved. |
| [zas.md](zas.md) | 0x57 | 15,067 | C | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. |

## Mid-size types (1,000 to 9,999 slots)

| Document | Type code | Slots | Grade | Covers and does not cover |
| --- | --- | ---: | --- | --- |
| [zpm.md](zpm.md) | 0x46 | 8,443 | B | Covers header observations including supported count/capacity and twin-identifier relations; key semantics and record stride remain unresolved. |
| [zcov.md](zcov.md) | 0x73 | 8,415 | C | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. |
| [zfid.md](zfid.md) | 0x67 | 6,762 | B | Covers supported header, word-count and padded-body identities; element semantics remain undecoded. |
| [ztyp.md](ztyp.md) | 0x4a | 6,308 | C | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. |
| [zkit.md](zkit.md) | 0x71 | 2,715 | C | Covers type census and shared wrapper evidence; no type-specific payload-wide decoder is established. |
| [ztd.md](ztd.md) | 0x05 | 2,612 | B | Covers container and header evidence plus observed body-size decompositions; pixel format and resource identity remain unresolved. |

## Tail types (fewer than 1,000 slots)

| Document | Type code | Slots | Grade | Covers and does not cover |
| --- | --- | ---: | --- | --- |
| [zscript.md](zscript.md) | 0x59 | 746 | B | Covers resource decoding and structurally verified instruction listing; program semantics and source reconstruction remain outside coverage. |
| [zvert.md](zvert.md) | 0x12 | 611 | C | Covers container and observed pointer/length-class profiles; field roles, count and stride remain unresolved. |
| [zcg.md](zcg.md) | 0x5f | 518 | B | Covers container and supported end-relative relations; the record body remains undecoded. |
| [zcgc.md](zcgc.md) | 0x72 | 518 | B | Covers header and body observations plus twin-identifier relations; full float-body semantics remain unresolved. |
| [zpt.md](zpt.md) | 0x48 | 226 | B | Covers the supported pointer-table partition; segment semantics, counts and record strides remain unresolved. |
| [zmmd.md](zmmd.md) | 0x66 | 142 | C | Covers container and size/stream population profiles; count, stride and payload meaning remain unresolved. |
| [zcps.md](zcps.md) | 0x63 | 98 | B | Covers supported header and duplicated count-pair observations; record semantics remain undecoded. |
| [zfd.md](zfd.md) | 0x56 | 11 | B | Covers the observed path-string count relation and tail extent; the complete record layout remains unresolved. |
| [ztsl.md](ztsl.md) | 0x65 | 5 | B | Covers supported header, count and body-size relations; element semantics remain unresolved. |
| [zsmam.md](zsmam.md) | 0x6e | 5 | C | Covers container and repeating-field observations; no fixed header stream or decoded count is established. |
| [zrd.md](zrd.md) | 0x6d | 4 | B | Covers inner magic and the observed count relation; the record chain remains undecoded. |
| [zjd.md](zjd.md) | 0x4d | 3 | B | Covers the supported duplicated-count and pointer-array relation; element semantics and a payload-wide stride remain unresolved. |
| [zpmd.md](zpmd.md) | 0x45 | 1 | C | Covers the single-slot container and header profile; a payload decoder is not established. |

## Grade index

The grade counts among the 37 type rows are B 24, C 12 and D 1; among the eight signature families, B 2 and C 6. The separate null-word partition is C. The container-layer page is a supplemental B, and the remaining supporting pages are guides, evidence or audits without an editorial grade of their own.
