# 0DRPz payload family

Scope and grade: **B, partial payload decode.** Only the storage envelope, the 0x50-byte
shared root, the blob descriptor table and the four localisation blob IDs are locally
decoded. The 290,294-slot signature census is a classification count, not a count of
decoded texts; non-text blobs, overrun pools, the external key-name hash and every write
path remain undecoded. Nothing in this page is a whole-family payload decode.

## Identity

`0DRPz` is a **five-byte ASCII payload signature** at inflated `+0x10`, which is also
`+0x00` of the shared root object. It is not the resource type word at `+0x10` of the
20-byte RPF9 resource record; eight different type codes carry it. The trailing `z` is
ASCII `0x7A` in the token, not a separate type byte
(`artifact: docs/formats/0drpz.md:L9`, `:L76`; `artifact: docs_complete_work/format_evidence.md:L5`).

Two `+0x10` positions must not be conflated: the *stored* `+0x10` is the first zlib byte
after the 16-zero-byte prefix, while the *inflated* `+0x10` is the signature
(`artifact: docs/formats/0drpz.md:L36-L45`; `artifact: docs_complete/signatures/container-layer.md`).
The census label is `0DRPz@16`
(`artifact: docs_complete/_evidence/signatures_a/census_aggregates.json:L52-L66`).

## Counts

| Measure | Family total | Census denominator | Evidence |
|---|---:|---:|---|
| Slots | 290,294 | 1,255,039 | `artifact: docs/coverage.md:L173`, `:L7` |
| Stored bytes | 12,137,708,928 | 305,820,985,968 | same; `artifact: docs_complete/_evidence/signatures_b/all_families.tsv:L2`, `:L2` of `totals.tsv` |
| Logical bytes | 51,368,850,240 | 564,783,265,279 | same; `all_families.tsv:L2`, `totals.tsv:L4` |

**Type-code and root split.** The eight type codes exhaust the family; each family count equals that code's full census
type total (`artifact: docs/formats/0drpz.md:L11-L23,L32`;
`artifact: docs_complete/_evidence/signatures_a/census_aggregates.json:L122-L315`).

| Type code | Variant-0 label | Slots | Stored bytes | Logical bytes |
|---|---|---:|---:|---:|
| `0x0b` | zmt | 28,328 | 4,920,841,360 | 29,509,517,168 |
| `0x49` | zmap | 166,072 | 4,770,055,552 | 8,063,899,008 |
| `0x4a` | ztyp | 6,308 | 534,759,472 | 1,915,879,104 |
| `0x57` | zas | 15,067 | 245,830,720 | 1,978,452,832 |
| `0x6c` | zascd | 32,878 | 554,083,984 | 5,935,045,424 |
| `0x6f` | zldbmt | 30,511 | 217,945,568 | 680,928,064 |
| `0x71` | zkit | 2,715 | 135,945,920 | 511,600,976 |
| `0x73` | zcov | 8,415 | 758,246,352 | 2,773,527,664 |
| **Total** | | **290,294** | **12,137,708,928** | **51,368,850,240** |

Root split from the same per-slot aggregation
(`census_aggregates.json:L68-L114`): `levels.rpf` 188,449;
`pack/story000/story000.rpf` 48,084; `anim.rpf` 22,823; `data.rpf` 15,768;
`navmeshes.rpf` 9,603; `packs.rpf` 4,678;
`pack/shared_minigame000/shared_minigame000.rpf` 787;
`pack/story000_restofworld/story000_restofworld.rpf` 101;
`pack/core_restofworld/core_restofworld.rpf` 1. Name origin: 4,770 dictionary-matched
and 285,524 unresolved hashes (`artifact: docs/formats/0drpz.md:L30`). The signature table
and the type table are independent partitions of the same slots and are never added
(`artifact: docs/coverage.md:L12-L16`).

## Where it appears

Stored form: 16 zero bytes at slot `+0x00`, zlib stream beginning at stored `+0x10`,
inflated bytes thereafter. The 16-byte prefix is outside both the compressed and the
encrypted stream (`artifact: docs/formats/0drpz.md:L36-L40`, `:L72`). The root occupies
0x50 bytes at inflated `+0x10`; blob descriptors follow via a pointer, so descriptor
positions are **resource-relative virtual addresses**, not sequential file offsets.
A blob pointer minus a per-resource virtual base gives an offset inside the same
resource; observed bases are `0x50000000`, `0x60000000`, `0x40000000` and zero
(`artifact: docs/formats/0drpz.md:L52-L55`; `artifact: drpz_report.md:L25-L30`, `:L40-L41`).
Reading the base as a single constant rejects 47 of 60 `levels.rpf` samples
(`artifact: drpz_report.md:L40-L41`). A per-resource base is a measured convention, not an
inferred value from the signature.

## Layer status

Grade B. Decoded: storage envelope, root, descriptor table and four localisation blob
IDs. Not decoded: other blob kinds, most wrapped content, the external key name behind
`0x101`, continuation overruns and the write path
(`artifact: docs/formats/0drpz.md:L66-L96,L107-L113`;
`artifact: docs_complete_work/format_evidence.md:L174-L186`).
The four-archive text sweep measured 25,834 text tables, 7,289,933 strings,
231,374,054 characters, 99.91 percent readable, zero invalid UTF-8 and zero
control-bearing strings, with two byte-identical runs and classifier precision 0.9649
/ recall 1.0000 on 2,000 streams
(`artifact: docs/formats/0drpz.md:L80-L88`). That sweep and the 290,294-slot census have
different units and must be reported separately
(`artifact: docs/formats/0drpz.md:L105`). Write status is **W0, extract-only**
(`artifact: docs/formats/0drpz.md:L92-L96`).

## Fields if any

Offsets are **inflated-payload relative** unless labelled stored or root-relative.
Widths are byte counts of the on-disk/inflated representation
(`artifact: docs/formats/0drpz.md:L40-L53`; `artifact: drpz_report.md:L14-L31`).

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| stored `+0x00` | 16 | zero prefix, outside zlib and cipher extents | measured | `artifact: docs/formats/0drpz.md:L39,L72` |
| stored `+0x10` | variable | zlib stream start | measured | `artifact: docs/formats/0drpz.md:L40` |
| inflated `+0x00` | 8 | zero `u64` | measured | `artifact: drpz_report.md:L15` |
| inflated `+0x08` | 8 | reference pointer | measured | `artifact: drpz_report.md:L16` |
| inflated `+0x10` | 5 | `0DRPz` magic (root `+0x00`) | measured | `artifact: docs/formats/0drpz.md:L45` |
| root `+0x10` | 4 | `u32` variant word; value 2 in 14,388 tables (role inferred from use) | measured | `artifact: drpz_report.md:L19`; `artifact: docs/formats/0drpz.md:L46` |
| root `+0x18` | 8 | pointer | measured | `artifact: docs/formats/0drpz.md:L47` |
| root `+0x28` | 8 | pointer to blob descriptor table | measured | `artifact: docs/formats/0drpz.md:L48` |
| root `+0x30` | 8 | pointer | measured | `artifact: docs/formats/0drpz.md:L49` |
| root `+0x38` | 4 | `u32`; high bits used by some archives, no supported reading | unknown | `artifact: drpz_report.md:L23`; `artifact: docs/formats/0drpz.md:L112` |
| root `+0x3C` | 4 | low `u16` descriptor count; high `u16` flags have unresolved semantics | measured | `artifact: docs/formats/0drpz.md:L51,L64`; `artifact: drpz_report.md:L24,L38-39` |
| blob descriptor | 16 | `{u32 blob_id, u32 byte_len, u64 pointer}` | measured | `artifact: docs/formats/0drpz.md:L52`; `artifact: drpz_report.md:L25` |
| blob `0x10` | Variable | NUL-separated UTF-8 string pool | measured | `artifact: docs/formats/0drpz.md:L59`; `artifact: drpz_report.md:L28` |
| blob `0x101` | 16 per record | hash records `{u32 hash, u32 0, u32 (n<<16)\|1, u32 0}` | measured | `artifact: docs/formats/0drpz.md:L60` |
| blob `0xA8478889` | Not specified here | per-string offsets | measured | `artifact: docs/formats/0drpz.md:L61` |
| blob `0x99331089` | Not specified here | pool descriptor | measured | `artifact: docs/formats/0drpz.md:L62` |

`root+0x38` is **not** the descriptor count: the `+0x38` reading reproduces the low
`u16` of `+0x3C` in 56 of 60 `data.rpf` and 2 of 60 `levels.rpf` samples, so the count
must come from `+0x3C` (`artifact: drpz_report.md:L38-L39`). Out-of-range pointers occur
in otherwise valid tables; in-range descriptors are kept and an overrunning pool is
clamped to the stream end (`artifact: docs/formats/0drpz.md:L64`;
`artifact: drpz_report.md:L42-L44`). The blob-role readings apply to localisation pools,
not to every non-text blob (`artifact: docs/formats/0drpz.md:L57-L64`).

**Source classification retained.** The signature audit labels this family Partial: wrapper, descriptor table and four
text blob IDs decode, while other IDs, payload shapes and the writer do not.
The reported decode results below retain their original scope
(`coverage_audit/out/tables.md`, `0DRPz` row; `artifact: docs/formats/0drpz.md:L98-L105`).

## Verification

- Signature at inflated `+0x10` in **290,294 of 290,294** family slots; type-word join
  delta zero slots and zero bytes for all eight codes
  (`artifact: docs/formats/0drpz.md:L100-L101`).
- Full sweep: 287,361 streams, 24,234,233,148 raw bytes, 2,072.1 MB/s
  (`artifact: docs/formats/0drpz.md:L102`).
- Independent family aggregation command (Rust, release, offline):
  `census_agg.exe artifact: type_census.csv artifact: docs_complete/_evidence/signatures_b`
  produced `data_rows: 1255039`, `stored_bytes: 305820985968`,
  `logical_bytes: 564783265279`, zero malformed rows, 0.667 s total / 0.378 s parse
  (`artifact: docs_complete/_evidence/signatures_b/run_log.txt:L1-L12`,
  `README.md:L10-L19`). Bounded PowerShell re-sum of the two published tables in
  `artifact: docs_complete_work/format_evidence.md:L40-L50` reproduced
  `TYPE rows=37 ... 1255039 ... 305820985968 ... 564783265279` and the same nine-row
  signature totals. Neither check reruns the extractor.
- No external URL was fetched for this page; all figures above are local.

## Unknowns

- The external key name hashed into blob `0x101` is not stored in the resource; the
  recorded hash is not JOAAT, FNV-1a, MurmurHash3 or CRC-32 of the string text
  (`artifact: docs/formats/0drpz.md:L90`; `artifact: drpz_report.md:L58-L62`).
- `root+0x38` and the high half of `root+0x3C` have no supported meaning
  (`artifact: docs/formats/0drpz.md:L112`).
- Overrunning pools, weak pools that fail the classifier and non-text blob IDs remain
  open (`artifact: docs/formats/0drpz.md:L107-L111`).
- No encoder, round trip or game acceptance test exists
  (`artifact: docs/formats/0drpz.md:L92-L96`).

## Changelog

- 2026-11-26: Earlier page consolidated the eight-code identity, exact census totals
  and layer-qualified status and kept the 25,834-table sweep separate from the
  290,294-slot census (`artifact: docs_complete/signatures/0drpz.md` pre-edit).
- 2026-11-26: Rewritten with the eight required headings, grade B, explicit stored vs
  inflated offset bases, five-byte magic width, a five-column confidence table and
  command-level verification. No count was changed and no document outside this page
  was modified.

- 2026-11-26: reconciled to the signature heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/signatures/0drpz.md`. No count was selected by modification time.


- 2026-11-26: removed stale line-number suffixes from citations to Markdown within this reconciled set, because section normalization moved those lines; artifact paths and section content remain the references.
