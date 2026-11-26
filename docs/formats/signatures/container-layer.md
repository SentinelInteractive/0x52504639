# RPF9 container layer

This page documents only the shared archive container and table-of-contents read layer: it enumerates slots and locates stored payload extents before any leaf-format interpretation. It is **not** a complete decoder for child payloads. Nested containers are archive headers whose contents are enumerated in the same root's flat slot list; nothing here establishes a leaf codec, field semantics, a writer or game-load acceptance. [artifact: docs/coverage.md:10,14; artifact: unknown_accounting.md:24-31; CONTEXT_HANDOFF.md:94-104]

## Identity

The container layer recognises archive headers by `9FPR` magic (`0x52504639`) and reads the header, its two variable tables and the 20-byte resource records. It is a shared read layer, not a signature class: the 4,351 nested-container slots are classified as `container`, and 0 as `signature`, in the local class partition. [CONTEXT_HANDOFF.md:96-99; artifact: docs_complete_work/format_evidence.md:238-243; artifact: docs/coverage.md:14,176]

The complete enumerated tree has 1,255,039 slots and **4,373 headers = 22 standalone root archives + 4,351 nested archive slots**, with 0 reported parse failures. The standalone root headers are not 22 additional census slots: each root is a file on disk and its children, including nested containers, are enumerated within it. The older 4,375 comparison figure is superseded because it contradicts 22 + 4,351. [CONTEXT_HANDOFF.md:101; artifact: docs/coverage.md:7; artifact: docs_complete_work/format_evidence.md:58-60,243; artifact: docs_complete_work/independent_verification.md §4]

The [9FPR family page](9fpr.md) describes the nested-container population in the signature partition. This page describes the shared container read layer. The same nested objects appear in both discussions; the pages do not define additive populations. [artifact: docs/coverage.md:176,183; artifact: unknown_accounting.md:24-31]

## Counts

| Measure | Exact value | Denominator or scope |
|---|---:|---|
| Enumerated slots | 1,255,039 | Entire census |
| Stored bytes | 305,820,985,968 | Entire census, sum of slot metadata |
| Logical bytes | 564,783,265,279 | Entire census, sum of slot metadata |
| Headers | 4,373 | 22 root headers plus 4,351 nested headers |
| Standalone root headers | 22 | Named root files on disk |
| Nested-container slots | 4,351 | 1,255,039 total slots |
| Nested-container stored bytes | 147,279,874,016 | 305,820,985,968 census stored bytes |
| Nested-container logical bytes | 147,279,874,016 | 564,783,265,279 census logical bytes |

All eight values are from the independent CSV re-count and the published tables: `data_rows: 1255039`, `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, 37 distinct type keys and 9 families, with 0 malformed rows. The nested-container byte figures are the `9FPR` signature row and the nested-container population of the null-word partition. [artifact: docs_complete_work/independent_verification.md §1,§3,§4; artifact: docs/coverage.md:7-10,164,176; artifact: unknown_accounting.md:13-18]

These are census slot sums, not unique physical bytes: nested container extents contain their descendants, so summing slot extents double-counts byte ranges. The nested-container report states that their contents are enumerated in the same root's flat slot list. [artifact: docs/coverage.md:10,183; artifact: unknown_accounting.md:30; artifact: docs_complete_work/format_evidence.md:71-72]

## Where it appears

This layer applies to every root archive and every nested archive in the enumerated tree. Nested containers have no resource type word in the census; their type value is `<null>`, and their exact root distribution is on the [9FPR page](9fpr.md). The 4,351 `9FPR` slots are inside the 101,479 type-word Unknown partition and are also the 4,351 `9FPR` signature rows; they are not extra slots in either table. [artifact: docs_complete_work/format_evidence.md:241-243,302-303; artifact: docs/coverage.md:130,176,183; artifact: unknown_accounting.md:7,15]

Header: 64 bytes with `9FPR` at `+0x00`, header length at `+0x04`, table split at `+0x08`, generation tags at `+0x1C` and `+0x30`, entry count at `+0x24`, and the table-2 width input in the low half of `+0x2C`. Table 1 is variable and carries the name/offset payload; Table 2 is the directory index. The header length parses for 4,351 of 4,351 nested slots and is below the stored extent in every case. [CONTEXT_HANDOFF.md:96-98; artifact: docs_complete_work/format_evidence.md:247-254; artifact: unknown_accounting.md:26]

The reported Table-2 stride is `8 + low(+0x2C)`, with extent `ceil(stride * count / 16) * 16`. The handoff reports 9-byte rows for counts 1 through 254 and 10-byte rows for counts 257 upward; it does not establish the missing boundary cases. The formula reproduces 2,383 of 2,616 well-formed generation-4 headers (91.1 percent). The other 233 have high word 2 at `+0x20` and a larger table than the formula predicts, so the rule must not be described as universal. [CONTEXT_HANDOFF.md:98; artifact: docs_complete_work/format_evidence.md:257-259]

A common resource storage form is a 16-zero-byte prefix followed by zlib at stored `+0x10`. That storage convention is separate from an inflated payload's signature. Per-type logical-size conventions differ: `zft` includes the prefix while `zdd` and `zbdd` exclude it. [CONTEXT_HANDOFF.md:100; artifact: docs_complete_work/format_evidence.md:260-262]

## Layer status

**Grade B, conservative.** TOC enumeration is complete at the read layer: 1,255,039 slots and 4,373 headers with 0 reported parse failures, and 4,351 of 4,351 nested header lengths checked. It is not a complete format decode: the Table-2 stride rule leaves 233 generation-4 exceptions unexplained and local RSA verification is 4,373 unknown. This grade applies only to the container layer and never grades child payload decoding. [CONTEXT_HANDOFF.md:98,101,104; artifact: unknown_accounting.md:26; artifact: docs_complete_work/format_evidence.md:14,257-264; artifact: docs_complete_work/independent_verification.md §1]

The published "Full" status for `9FPR` applies to container reading, not to arbitrary leaf content inside a container. No encoder, round-trip or game-load claim is made. [artifact: docs/coverage.md:22,176; artifact: docs_complete_work/format_evidence.md:73-74; CONTEXT_HANDOFF.md:100]

RSA is disclosed separately: `CONTEXT_HANDOFF.md:104` records a claimed external result from an independent implementation whose own header total still reads 4,375. That claim is not a local measurement and is not adopted here. The local verifier is 0 verified, 0 failed and 4,373 unknown. Reading a signed index is not evidence that its signature was verified. [CONTEXT_HANDOFF.md:104; artifact: docs_complete_work/format_evidence.md:262-264]

## Fields if any

Offsets are relative to the archive header unless the row says "resource record". Unnamed fields retain their offset labels; no engine label is invented for an uninterpreted word. Confidence values are one of measured, inferred, external or unknown. [CONTEXT_HANDOFF.md:96-99; artifact: docs_complete_work/format_evidence.md:245-255]

| Offset | Width | Meaning | Confidence | Evidence |
|---|---|---|---|---|
| header extent | 64 bytes | Fixed header extent, not the whole variable header area | inferred | CONTEXT_HANDOFF.md:96; artifact: docs_complete_work/format_evidence.md:247 |
| `+0x00` | 4 bytes | `9FPR` magic `0x52504639`; on-disk prefix reads are independent of the CSV class | measured | CONTEXT_HANDOFF.md:96; artifact: unknown_accounting.md:26,31 |
| `+0x04` | u32 | Header length; parses and stays below stored extent on 4,351 of 4,351 nested slots | measured | CONTEXT_HANDOFF.md:96; artifact: unknown_accounting.md:26 |
| `+0x08` | unknown | Table split between the variable table regions; no further reading reported | inferred | CONTEXT_HANDOFF.md:96; artifact: docs_complete_work/format_evidence.md:250 |
| `+0x1C`, `+0x30` | unknown | Generation tags; no interpretation supplied | inferred | CONTEXT_HANDOFF.md:96; artifact: docs_complete_work/format_evidence.md:251 |
| `+0x20` | unknown | High word equal to 2 in the 233 generation-4 Table-2 exceptions | inferred | CONTEXT_HANDOFF.md:98; artifact: docs_complete_work/format_evidence.md:258 |
| `+0x24` | u32 | Container-local entry count | inferred | CONTEXT_HANDOFF.md:96; artifact: docs_complete_work/format_evidence.md:252 |
| `+0x2C` low half | unknown | Table-2 width input used by the reported stride rule | inferred | CONTEXT_HANDOFF.md:96-98; artifact: docs_complete_work/format_evidence.md:253 |
| Table 1 | variable | Name/offset payload; not a fixed-width record claim | inferred | CONTEXT_HANDOFF.md:97; artifact: docs_complete_work/format_evidence.md:254 |
| Table 2 | variable | Directory index; 233 generation-4 exceptions are unexplained | inferred | CONTEXT_HANDOFF.md:97-98; artifact: docs_complete_work/format_evidence.md:254,257-259 |
| Resource record `+0x00`, `+0x04` | unknown | Logical-size words; masks not specified by the cited read model | inferred | CONTEXT_HANDOFF.md:99; artifact: docs_complete_work/format_evidence.md:255 |
| Resource record `+0x08` | unknown | Stored size in 16-byte units | inferred | CONTEXT_HANDOFF.md:99; artifact: docs_complete_work/format_evidence.md:255 |
| Resource record `+0x0C` | unknown | Offset in 16-byte units | inferred | CONTEXT_HANDOFF.md:99; artifact: docs_complete_work/format_evidence.md:255 |
| Resource record `+0x10` | unknown | Type word at `+0x10` of the 20-byte resource record | inferred | artifact: docs/coverage.md:14; CONTEXT_HANDOFF.md:99 |
| Signed index | unknown | RSA-2048/PKCS#1 v1.5 verification claimed by an independent implementation; external claim only, never a local measurement | external | CONTEXT_HANDOFF.md:104; artifact: docs_complete_work/format_evidence.md:262-263 |
| Local RSA verifier | unknown | 0 verified, 0 failed, 4,373 unknown; signed message representation unresolved | unknown | CONTEXT_HANDOFF.md:104; artifact: docs_complete_work/format_evidence.md:262-263 |

## Verification

The handoff reports complete enumeration of 1,255,039 slots, 4,373 headers and 0 parse failures. The null-word audit independently read on-disk `9FPR` prefixes and checked `headers - 1` against nested slots for every one of the 22 roots; it warns that CSV classification and membership came from the same header table and are not independent evidence, while the on-disk prefix reads are. [CONTEXT_HANDOFF.md:101; artifact: unknown_accounting.md:24-31]

The independent CSV re-count in this documentation task confirms the published aggregates and the null partition: 1,255,039 rows, 305,820,985,968 stored bytes, 564,783,265,279 logical bytes, 0 malformed rows, 37 type rows and 9 family rows all matching `coverage.md`, and the 4,351 / 92,614 / 4,514 null partition summing to 101,479 slots. It re-counts the CSV; it does not rerun archive parsing or cryptographic verification. [artifact: docs_complete_work/independent_verification.md §1,§3,§4,§6; artifact: docs/coverage.md:258-266]

The published page asserts before writing that the census holds exactly 1,255,039 rows, that the 37 type rows and 9 signature rows each sum to 1,255,039 slots, that the four status rows sum to 1,255,039 slots, and that the aggregate stored and logical totals reproduce 305,820,985,968 and 564,783,265,279. [artifact: docs/coverage.md:258-266]

## Unknowns

- The Table-2 rule does not explain the 233 generation-4 exceptions, and it does not establish the 255/256-count boundary cases. [CONTEXT_HANDOFF.md:98; artifact: docs_complete_work/format_evidence.md:257-259]
- The signed message representation remains unresolved for the local RSA verifier; the external RSA claim is not a local measurement and its own total contradicts 4,373. [CONTEXT_HANDOFF.md:104]
- Field widths and meanings at `+0x08`, `+0x1C`, `+0x20`, `+0x24`, `+0x2C` and in the resource record are reported read-model labels, not separately measured widths; uninterpreted words keep their offset labels. [CONTEXT_HANDOFF.md:96-99; artifact: docs_complete_work/format_evidence.md:250-255]
- No local `artifact: docs/formats/rpf9-container.md` exists at audit time (`Test-Path` returned `False` for both `artifact: docs/formats/rpf9-container.md` and `artifact: docs/rpf9-container.md`), although `coverage.md:176` links that name. Container claims here cite the handoff, the null-word audit and the evidence manifests instead. [artifact: docs/coverage.md:176; artifact: docs_complete_work/container_supplement_write.md §Checks]
- Container success does not establish leaf codecs, field semantics, writers or game acceptance. [artifact: docs/coverage.md:183,193-196; artifact: unknown_accounting.md:87-89]

## Changelog

- 2026-11-26 (initial): Separated container-layer evidence from leaf-signature interpretation. Used the corrected 4,373-header total; the earlier 4,375 figure is superseded because it contradicts 22 roots plus 4,351 children. [CONTEXT_HANDOFF.md:101; artifact: docs_complete_work/format_evidence.md:243]
- 2026-11-26 (audit repair): Kept all supported detail and added the scope disclosure, the exact eight-heading structure, a five-column field table with strictly measured/inferred/external/unknown confidence, explicit local path-and-line citations, the conservative grade B boundary, the 4,373 = 22 + 4,351 arithmetic, the 233 Table-2 exceptions and the external-only RSA attribution. No count was changed and no source or sibling document was modified. [artifact: docs_complete_work/container_supplement_write.md §Checks]

**Source register (local paths):** `workspace: CONTEXT_HANDOFF.md` §5 lines 94-104; `artifact: docs/coverage.md` lines 7-16, 121-183, 258-266; `artifact: unknown_accounting.md` lines 7-31, 87-89; `artifact: docs_complete_work/format_evidence.md` lines 58-72, 238-264; `artifact: docs_complete_work/independent_verification.md` sections 1, 3, 4 and 6. Commands used for bounded checks are recorded in `artifact: docs_complete_work/container_supplement_write.md`.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/container-layer.md`. No count was selected by modification time. Reconciliation decisions: 4,375 and/or 4,330 are retained only as historical rejected header totals; the cited current total is 4,373 = 22 roots + 4,351 nested headers (`workspace: CONTEXT_HANDOFF.md:101,345,361,366`).

