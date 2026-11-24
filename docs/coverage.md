# Coverage by file type

Status: read-only classification of the resource index. No content, asset, name list or key is published here.

Every resource slot in the package carries a type word. This page lists every type the game's own enum table defines, how many slots carry it, how many bytes it accounts for, and how much of it is actually decoded. It is a checklist of what is proven, not a claim that the package is understood.

- 1,255,039 slots, 4,373 archive headers, 22 roots.
- 305,820,985,968 stored bytes and 564,783,265,279 logical bytes, aggregated from the same index.
- 37 type rows: 36 named codes plus the null group.
- Byte sums are not unique physical bytes. Nested container ranges contain their descendants, so a byte can be counted in more than one row.

## Two tables, two questions

The type word at `+0x10` of the 20-byte resource record answers "what did the engine dispatch this as". An inner signature in the inflated payload answers "what shape is the data". They are different questions about the same slot, and the two tables below are two independent partitions of the same 1,255,039 slots.

Neither table may be added to the other. A slot appears once in each.

## Coverage legend

| Status | Meaning |
|---|---|
| **Full** | A decoder exists, its output was checked against independent evidence on real slots from the package, and a written report records the scope. |
| **Partial** | A container, a record set or a subset of payload shapes is verified, but the decoder or writer is incomplete for the type as a whole. |
| **Classified** | The name and the slot and byte counts are verified from the enum table and the index. There is no decoder. |
| **Unknown** | No type word, or no verified name for it. |

Two rules matter more than the labels.

1. A name is not coverage. A type is Classified because the enum table names it, not because its payload is understood.
2. A count is not coverage either. Counting slots and bytes proves the index, not the format.

## Summary

| Status | Slots | Share |
|---|---:|---:|
| Full | 168,643 | 13.44 percent |
| Partial | 540,728 | 43.08 percent |
| Classified | 444,189 | 35.39 percent |
| Unknown | 101,479 | 8.09 percent |
| **Total** | **1,255,039** | **100 percent** |

Only two payload types reach Full: the drawable `0x02` and the script `0x59`. Nine reach Partial, and all nine decode one layer of a larger type. Twenty-five of the thirty-six named codes have no decoder at all.

### The five largest types that are still Classified

| Code | Name | Slots | Share of index |
|---|---|---:|---:|
| `0x06` | zbn | 92,199 | 7.35 percent |
| `0x43` | zcd | 62,384 | 4.97 percent |
| `0x03` | zft | 55,488 | 4.42 percent |
| `0x04` | zdd | 48,584 | 3.87 percent |
| `0x58` | zsm | 40,019 | 3.19 percent |
| | **Total** | **298,674** | **23.80 percent** |

### The five largest types with no report

The same five types, in the same order. This is not a copy of the previous list by accident: every type that has a report is either Full or Partial, so the largest types without a report are by construction the largest Classified types. If a decoder is built for any of them, the list changes.

One type is Full without a report in this repository. The script row therefore says `none published`, not `none written`. The internal record exists; it is not public, and this page does not link it.

## Every type code

Sorted by slot count. Codes `0x00` to `0x12` come from the static enum table, codes `0x40` to `0x73` from the callback table. The null group is the rows with no `+0x10` word.

| Code | Name | Slots | Stored bytes | Logical bytes | Coverage | Report | Note |
|---|---|---:|---:|---:|---|---|---|
| `0x0f` | zbdr | 250,434 | 7,335,183,152 | 124,157,781,744 | Partial | [drawables](drawables.md) | Pages, header, bounds and leaf-reference tables decode on 8 of 8 samples; internal nodes and writer undecoded. |
| `0x02` | zdr | 167,897 | 46,719,905,568 | 100,362,894,768 | Full | [drawables](drawables.md) | LOD0 geometry, materials and diffuse textures decode and export to OBJ/MTL on sampled slots; single LOD, no skin payload, no writer. |
| `0x49` | zmap | 166,072 | 4,770,055,552 | 8,063,899,008 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and text blob ids decode; the rest of the payload does not. |
| none | null word | 101,479 | 199,765,610,064 | 200,460,005,055 | Unknown | none | No `+0x10` resource word: binary slots, plus the nested archive headers counted under the `9FPR` signature. |
| `0x06` | zbn | 92,199 | 11,093,949,168 | 17,156,781,648 | Classified | none | Largest type without a decoder; name and count only. |
| `0x43` | zcd | 62,384 | 6,794,403,072 | 11,262,899,120 | Classified | none | Name and count verified; no payload decoder. |
| `0x03` | zft | 55,488 | 5,915,592,480 | 14,211,185,152 | Classified | none | Name and count verified from the executable enum table; no payload decoder. |
| `0x04` | zdd | 48,584 | 6,309,542,464 | 14,577,057,200 | Classified | none | Dictionary container; one member was located in a control, but no dictionary decoder exists. |
| `0x58` | zsm | 40,019 | 659,721,600 | 1,531,499,328 | Classified | none | Name and count verified; no payload decoder. |
| `0x6c` | zascd | 32,878 | 554,083,984 | 5,935,045,424 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and text blob ids decode; the rest of the payload does not. |
| `0x6f` | zldbmt | 30,511 | 217,945,568 | 680,928,064 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and text blob ids decode; the rest of the payload does not. |
| `0x0b` | zmt | 28,328 | 4,920,841,360 | 29,509,517,168 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and the text blob ids decode; other blob ids and non-text content do not. |
| `0x4f` | znv | 27,644 | 5,398,485,440 | 15,420,757,856 | Classified | none | Name and count verified; navigation payload not decoded. |
| `0x64` | zsp | 27,482 | 376,513,072 | 2,325,782,256 | Classified | none | Name and count verified; shader payload not decoded. |
| `0x4e` | zad | 25,608 | 1,275,304,768 | 1,717,098,288 | Classified | none | Name and count verified; no payload decoder. |
| `0x11` | zbft | 22,440 | 414,772,768 | 6,733,343,200 | Classified | none | Name and count verified; no payload decoder. |
| `0x10` | zbdd | 22,382 | 3,591,712 | 8,019,200 | Classified | none | Name and count verified; no payload decoder. |
| `0x57` | zas | 15,067 | 245,830,720 | 1,978,452,832 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and text blob ids decode; the rest of the payload does not. |
| `0x46` | zpm | 8,443 | 38,500,896 | 204,265,984 | Classified | none | Name and count verified; no payload decoder. |
| `0x73` | zcov | 8,415 | 758,246,352 | 2,773,527,664 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and text blob ids decode; the rest of the payload does not. |
| `0x67` | zfid | 6,762 | 138,323,008 | 316,435,744 | Classified | none | Name and count verified; no payload decoder. |
| `0x4a` | ztyp | 6,308 | 534,759,472 | 1,915,879,104 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and text blob ids decode; the rest of the payload does not. |
| `0x71` | zkit | 2,715 | 135,945,920 | 511,600,976 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and text blob ids decode; the rest of the payload does not. |
| `0x05` | ztd | 2,612 | 425,517,120 | 1,308,553,760 | Classified | none | Name and count verified; payload not examined. |
| `0x59` | zscript | 746 | 50,195,184 | 167,734,336 | Full | none published | End-to-end decode of all 746 script slots with exact declared sizes; no encoder and no bytecode semantics. |
| `0x12` | zvert | 611 | 25,514,416 | 70,874,224 | Classified | none | Name and count verified; no payload decoder. |
| `0x5f` | zcg | 518 | 685,024 | 5,228,768 | Classified | none | Name and count verified; no payload decoder. |
| `0x72` | zcgc | 518 | 919,033,488 | 1,276,056,736 | Classified | none | Name and count verified; no payload decoder. |
| `0x48` | zpt | 226 | 8,472,768 | 110,748,448 | Classified | none | Name and count verified; no payload decoder. |
| `0x66` | zmmd | 142 | 7,096,224 | 10,378,208 | Classified | none | Name and count verified; no payload decoder. |
| `0x63` | zcps | 98 | 107,312 | 214,160 | Classified | none | Name and count verified; no payload decoder. |
| `0x56` | zfd | 11 | 51,312 | 827,344 | Classified | none | Eleven slots; name and count verified, nothing decoded. |
| `0x65` | ztsl | 5 | 182,736 | 228,416 | Classified | none | Five slots; name and count verified, nothing decoded. |
| `0x6e` | zsmam | 5 | 370,720 | 792,464 | Classified | none | Five slots; name and count verified, nothing decoded. |
| `0x6d` | zrd | 4 | 6,641,616 | 16,922,688 | Classified | none | Four slots; name and count verified, nothing decoded. |
| `0x4d` | zjd | 3 | 2,880 | 28,240 | Classified | none | Three slots; name and count verified, nothing decoded. |
| `0x45` | zpmd | 1 | 7,008 | 20,704 | Classified | none | One slot; name and count verified, nothing decoded. |
| | **Total** | **1,255,039** | **305,820,985,968** | **564,783,265,279** | | | |

## Inner signature families

A signature in the inflated payload, grouped by slot count. `0DRPz` sits at `+0x10` of the inflated resource and is a wrapper, not a type. Its eight type codes are the eight `0DRPz` rows above.

| Signature | Slots | Stored bytes | Logical bytes | Coverage | Report | Note |
|---|---:|---:|---:|---|---|---|
| none | 867,780 | 94,150,067,184 | 313,498,036,449 | Unknown | none | No recognized signature in the bounded prefix probe. |
| `0DRPz` | 290,294 | 12,137,708,928 | 51,368,850,240 | Partial | [drpz-localisation](drpz-localisation.md) | Wrapper, descriptor table and the four text blob ids decode; other blob ids, other payload shapes and the writer do not. |
| `ADAT` | 71,676 | 38,297,906,160 | 38,297,508,464 | Partial | none | The audio pipeline reads these banks through to Opus; no per-slot decode audit and no format report. |
| `PSIN` | 18,640 | 154,829,776 | 487,573,772 | Partial | none | Several header records are partly mapped; no complete decoder and no format report. |
| `9FPR` | 4,351 | 147,279,874,016 | 147,279,874,016 | Full | [rpf9-container](rpf9-container.md) | These slots are nested containers, not leaf payloads; the container header, table split, trailer and signed index are read for every header. |
| `RBF0` | 1,278 | 2,129,984 | 16,004,417 | Classified | none | Blob counts and a name set are recorded locally; no field report and no decoder. |
| `KB2` | 797 | 13,520,694,880 | 13,520,690,172 | Classified | none | Name and count verified; payload not decoded. |
| `XML` | 221 | 3,639,664 | 40,592,391 | Classified | none | Name and count verified; documents are readable text but no parser is verified. |
| `SGD5` | 2 | 274,135,376 | 274,135,358 | Classified | none | Two slots; the shader mapping is an open question. |
| **Total** | **1,255,039** | **305,820,985,968** | **564,783,265,279** | | | |

Read this table as a statement about the signature layer only. A slot in the `none` row is not therefore unexamined: both Full drawable types sit there, because neither carries an inner signature this probe recognizes. The 4,351 `9FPR` slots are counted here as containers and appear nowhere else as leaf payloads.

## What full coverage means

Full is deliberately narrow.

- The decoder runs on real slots taken from the shipped package, not on a synthetic fixture.
- The output is checked against something independent: declared sizes, declared counts, mesh bounds against a companion resource, structural invariants, or a written artifact that can be counted.
- A report records what was checked and what was not.

Full does not mean complete, and it does not mean writable.

- No type in this package has a writer. Every type with a decoder is extract-only. No bit-stable round trip and no game-loadable write has been demonstrated for any format here.
- Full is per layer. The drawable type is Full for LOD0 geometry, material bindings and diffuse surfaces, and not Full for skin weights, higher LODs or every render bucket. The script type is Full for the container and the codec, and not Full for bytecode semantics or a script writer.
- Full is about the format, not the population. One decoder proven on a stratified sample is Full; the share of the population it has been exercised on is a separate number, and the responsible reading of either Full row is "the format is decoded", not "every slot has been decoded".

The honest headline: two payload types are decoded end to end, a container layer and three wrappers are partly decoded, and most of the index by slot count is named and counted but not read.

## What is missing

Ordered by how much of the index it would unlock.

1. The five largest Classified types, 298,674 slots and 23.80 percent of the index, have no decoder. `zbn`, `zcd`, `zft`, `zdd` and `zsm` are the whole of that gap.
2. The eight `0DRPz` codes are Partial for one blob combination. The text blob ids decode; every other blob id in the wrapper does not, and the 32-bit record hash over that text is not a hash of the text itself, so record keys are not recoverable from the payload alone.
3. The `zbdr` BVH has verified pages, header, bounds and leaf-reference tables. Its internal box and parent nodes are undecoded, the runtime ordering of the build-descriptor geometry array is unresolved, and there is no writer.
4. The `zdr` decoder covers LOD0. Skin weights and joint indices, normals and tangents, higher-LOD export, two render buckets and the shader variant matrix remain open.
5. `ADAT` and `PSIN` have pipeline use but no per-slot audit and no format report. Both are Partial on the strength of a working path, not a measured census.
6. `RBF0`, `KB2`, `XML` and `SGD5` are counts only: 2,298 slots with nothing decoded.
7. The null-word group breaks down as 4,514 slots with no type word and no signature, 4,351 nested containers, and 92,614 slots inside the six other signature families. Only the container third of that group is decoded.
8. There is no encoder, packer or TOC rewriter for any type. Every write status in this project is W0.

## Method and checks

The batch join is a single Rust release binary, offline, with no dependencies. It reads the per-slot census once, aggregates by type word and by signature family, joins the result to the verified type-word table and to a written status record per row, and emits the two tables above.

- 298.2 MiB read in 7.10 s, 42.01 MiB/s, 176,809 rows/s, 1,255,039 rows.
- No Python is used anywhere in the join or the reconciliation.

Checks the run asserts before it writes a row:

- The census holds exactly 1,255,039 rows.
- The 37 type rows sum to 1,255,039 slots, and each row's slots, stored bytes and logical bytes equal the verified type-word join for that code.
- The 9 signature rows sum to 1,255,039 slots.
- The four status rows sum to 1,255,039 slots.
- The aggregate stored and logical totals reproduce the independent sums, 305,820,985,968 and 564,783,265,279.

The published page is re-parsed and both tables are re-summed from the rendered markdown. If either total does not land on 1,255,039, this page is wrong and should not be trusted.

## Limits

- The census classifies headers and bounded prefixes. It does not prove that a slot's payload was read.
- Stored and logical byte sums overlap across nested containers and are not unique physical bytes.
- Type names are the executable's own variant-0 labels. They are not file extensions and they do not prove three on-disk encodings.
- Samples behind every Partial and Full row are described in the linked report, not here.
