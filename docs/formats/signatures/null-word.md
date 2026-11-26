# Null-word partition

## Identity

The null-word population is a partition of the resource type-word table, not a ninth payload signature or one opaque format. Its 101,479 slots have no resource type word in the census. They include nested containers, six recognized signature families and a residual. A missing type word does not mean the stored payload is unrecognizable. [T, null-word row; U, “Verdict” and “Signature-assigned”]

**The type-word table and the signature table are two independent partitions of the same 1,255,039 slots. They must never be added together.** Every null-word slot is already counted once in the signature partition, whether as `9FPR`, one of the six signature-assigned families, or signature `none` (literal CSV family `Unknown`). The 0DRPz family is a separate, typed population. [T, both tables; C-A, `all_families`; C-B, null-word family table]

## Counts

| Measure | Null-word total | Census denominator |
|---|---:|---:|
| Slots | 101,479 | 1,255,039 slots |
| Stored bytes | 199,765,610,064 | 305,820,985,968 stored bytes |
| Logical bytes | 200,460,005,055 | 564,783,265,279 logical bytes |

The exact three-way partition is below. Its slot denominator is 101,479; its byte denominators are the null-word totals immediately above. These are sums of census metadata, not unique physical disk occupancy. Nested container extents contain children also listed in the flat slot enumeration. [U, reconciliation and “Nested containers”; C-B, null-word family table]

| Population | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| Nested containers (`9FPR`) | 4,351 | 147,279,874,016 | 147,279,874,016 |
| Signature-assigned, six leaf families | 92,614 | 52,253,335,840 | 52,636,504,574 |
| No-signature residual | 4,514 | 232,400,208 | 543,626,465 |
| **Total** | **101,479** | **199,765,610,064** | **200,460,005,055** |

The signature-assigned subtotal is itself exactly partitioned as follows, with denominator 92,614 slots. [U, “Signature-assigned”; C-B, null-word family table]

| Family | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| [ADAT](adat.md) | 71,676 | 38,297,906,160 | 38,297,508,464 |
| [PSIN](psin.md) | 18,640 | 154,829,776 | 487,573,772 |
| [RBF0](rbf0.md) | 1,278 | 2,129,984 | 16,004,417 |
| [KB2](kb2.md) | 797 | 13,520,694,880 | 13,520,690,172 |
| [XML](xml.md) | 221 | 3,639,664 | 40,592,391 |
| [SGD5](sgd5.md) | 2 | 274,135,376 | 274,135,358 |
| **Total** | **92,614** | **52,253,335,840** | **52,636,504,574** |

### Residual partition

The 4,514-slot residual is fully accounted for by four groups. The denominator here is 4,514 residual slots, 232,400,208 stored bytes and 543,626,465 logical bytes, not the entire null-word population. [U, residual table]

| Residual group | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| Known or recognizable shapes | 3,827 | 195,216,032 | 405,428,345 |
| Placeholders | 30 | 480 | 450 |
| Codec-identification gaps | 615 | 33,926,464 | 126,978,572 |
| Genuinely unknown | 42 | 3,257,232 | 11,219,098 |
| **Total** | **4,514** | **232,400,208** | **543,626,465** |

The 42 unknown slots comprise 38 partial-deflate candidates and four unmatched compressed binaries. The source warns that the 38 partial hits may include false positives. The 615 are a codec-identification gap; they must not be relabelled as decoded content or as proven encryption. [U, “Verdict,” “Residual,” “False leads killed” and “Limit”]

The 3,827 known/recognizable shapes break down as follows. This table counts recognition categories, not fully decoded files. [U, residual table]

| Shape | Slots |
|---|---:|
| `PAMH` texture page-map headers | 1,477 |
| Texture page records (`01 00 01 02 80 00 80 00`) | 1,476 |
| `MoVE`, version `0x13`, movie chunk index | 443 |
| RBF0 reached by deeper raw-DEFLATE inflation | 156 |
| XML with BOM (`EF BB BF` before `<?xml`) | 128 |
| `GFX*` Scaleform shapes | 87 |
| `EA885A04` small-magic family | 34 |
| Plain-text manifests | 16 |
| `EDUP` | 5 |
| `MHIU` | 2 |
| `SPS1` | 1 |
| PSIN reached by deeper raw-DEFLATE inflation | 1 |
| `PS\0` shader table | 1 |
| **Total** | **3,827** |

The 30 placeholders carry `FORCE_EMPTY_RPF\0`. They are outside the 3,827 known-shape subtotal. Deeper RBF0, PSIN and BOM-prefixed XML remain residual sub-shapes in this frozen partition; promoting them would require an explicit census revision, not an unannounced change to this documentation's totals. [U, residual table and “Residual” discussion]

## Where it appears

The only type value in this partition is `<null>`; it is not a numeric resource enum assignment. All 22 roots are represented below. The denominator is 101,479 null-word slots. [C-B, null-word token/root tables; U, “Verdict”]

| Root | Slots |
|---|---:|
| `anim.rpf` | 593 |
| `appdata0.rpf` | 2 |
| `audio.rpf` | 7,283 |
| `common.rpf` | 418 |
| `data.rpf` | 4,164 |
| `levels.rpf` | 12,000 |
| `movies.rpf` | 515 |
| `navmeshes.rpf` | 50 |
| `pack/core_bvh4/core_bvh4.rpf` | 1,306 |
| `pack/core_licenses/core_licenses_data.rpf` | 6 |
| `pack/core_restofworld/core_restofworld.rpf` | 43 |
| `pack/core_restofworld001/core_restofworld001.rpf` | 6 |
| `pack/shared_minigame000/shared_minigame000.rpf` | 788 |
| `pack/shared_minigame000_bvh4/shared_minigame000_bvh4.rpf` | 13 |
| `pack/story000/story000.rpf` | 70,204 |
| `pack/story000/story000_script.rpf` | 2,327 |
| `pack/story000_bvh4/story000_bvh4.rpf` | 4 |
| `pack/story000_restofworld/story000_restofworld.rpf` | 60 |
| `packs.rpf` | 657 |
| `script.rpf` | 1,015 |
| `shaders.rpf` | 3 |
| `textures.rpf` | 22 |
| **Total** | **101,479** |

## Layer status

**Accounting is not decoding.** The exact slot and byte reconciliation does not change the type-word coverage label “Unknown” into “Full.” The 4,351 nested containers have a verified container read layer; the 92,614 signature-assigned slots have differing family-specific decode status; and residual recognition ranges from known shapes to placeholders, codec gaps and unknowns. None of these accounting steps establishes a universal payload decoder. [T, null-word and signature rows; U, “Verdict” and final warning; H, §8]

Magic positions are layer-specific: ADAT, KB2 and SGD5 have stored magic at zero; PSIN, RBF0 and XML are recognized through bounded zlib inflation; 9FPR is a raw nested archive. The residual raw-DEFLATE population contains 157 exact declared-size inflations, but exact decompression does not itself decode an RBF0 or PSIN structure. [U, “Nested containers,” “Signature-assigned” and “Residual”]

## Fields if any

There is no shared null-word field layout. Family-specific layouts and limits belong on the linked family pages. The partition key is the census type value `<null>`, and the residual key is census family `Unknown`, corresponding to signature-table `none`. The residual byte prefixes above are recognition evidence, not complete field schemas. [C-B, null-word family/token tables; T, signature `none` row; U, residual table]

## Verification

- This pass re-aggregated the census in Rust: 101,479 null-word slots and both byte totals match the source reconciliation exactly. All family and root subtotals also reconcile. [C-B]
- The earlier raw-byte audit independently read every nested-container prefix/header length and reconciled `headers - 1` for all 22 roots. [U, “Nested containers”]
- The earlier signature re-probe matched 1,823 of 1,823 samples across the six signature-assigned families, with 1,021 using an inner path. This is a sample audit, not a 92,614-slot semantic decode audit. [U, “Signature-assigned”]
- The residual report records 157 of 157 raw-DEFLATE inflations matching the declared logical size, agreed by two implementations. It also separates 3,671 zlib, 38 partial-deflate and 648 none classifications, totalling 4,514. This is reported prior evidence, not a new archive scan by this documentation task. [U, “Residual”]

The source's final “Proposed coverage wording” uses an approximate 3,899 recognizable figure. This page uses the exact primary residual table instead: 3,827 known/recognizable, 30 placeholders, 615 codec gaps and 42 unknown. The earlier codec-gap value 621 is superseded by 615. [U, residual table, “Limit” and “Proposed coverage wording”]


### Sources

- **C-A:** [All-family census totals](../_evidence/signatures_a/census_aggregates.json), `all_families`.
- **C-B:** [Null-word families](../_evidence/signatures_b/nullword_family.tsv), [roots](../_evidence/signatures_b/nullword_root.tsv), [tokens](../_evidence/signatures_b/nullword_token.tsv), [residual family](../_evidence/signatures_b/nullword_unknown_family.tsv) and [summary](../_evidence/signatures_b/summary.json); input `type_census.csv`.
- **T:** `coverage_audit/out/tables.md`, null-word row and signature table.
- **U:** [Unknown accounting](../../unknown_accounting.md), especially the primary reconciliation/residual tables and “Limit.”
- **H:** `CONTEXT_HANDOFF.md`, §8–9. See the [source register](README.md#source-register).

## Unknowns

- Codec identification remains open for 615 slots. The source supplies compression-like measurements but does not verify a codec or establish encryption. [U, “Residual” and “False leads killed”]
- The 42 genuinely unknown entries remain unresolved, including the false-positive caveat for 38 partial-deflate candidates. [U, “Verdict” and “Limit”]
- Known shape recognition is not equivalent to field or semantic decoding, and writers/round-trip/game-load tests remain unverified. [U, final warning; H, §9]

## Changelog

- 2026-11-26: Documented the exact three-way null-word partition and four-way residual partition. Preserved the fixed census family boundaries, corrected the approximate proposed wording by using the primary table, and made the accounting/decoding distinction explicit. [C-B; U]


- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/null-word.md`. No count was selected by modification time.

