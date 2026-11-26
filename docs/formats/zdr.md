# zdr (type 0x02) format record

Local research, 2026-11-26. Scope: RPF9 drawable resources whose Resource descriptor type word is `0x02`. **Actual decode limit:** LOD0 geometry, material bindings and diffuse textures decode on bounded sample slots and export to OBJ/MTL. There is no decode of all 167,897 slots, no all-LOD / skin-weight / shader-state decode, and no writer. Every decode number below is a recorded result from the cited artifact; no decoder was executed for this document. No key material and no game assets appear here.

**Grade: B (partial payload structure)**, conservative: the published `Full` status covers only sampled LOD0 geometry, material bindings and diffuse textures; there is no all-LOD, skin-weight, shader-state or whole-population decode and no writer. Container and page recovery plus the LOD0 object graph are measured on controls; skin streams, shader evaluation and the write path remain open.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

- The little-endian `u32` Resource-word at descriptor `+0x10` is `0x00000002` for `zdr` in the measured slots. The label comes from the game's extension table, whose three rows are `zdr` / `idr` / `#dr`; those rows do not prove three on-disk encodings. Source: `artifact: docs/formats/drawables.md:5-7`.
- The authoritative current table marks `zdr` Full and `zbdr` (`0x0f`) Partial; `zbdr` is a serialized BVH4 store, not a `zdr` mesh, and is excluded from this record. The `Full` label is a published coverage status, not a complete-payload claim for this document: only sampled LOD0 layers are decoded. Sources: `artifact: docs/coverage.md:128,127`; `workspace: coverage_audit/out/tables.md:5-6` (older snapshot); `artifact: docs/formats/drawables.md:9`.
- The type-word join `0x02 = zdr` was established by checking all 47 candidate `0x02` rows from the per-slot census against the full TOC on root, header, slot, offsets, lengths, path and hash. Source: `artifact: district_render.md:11`.
- The enum path is verified; the game's `zdr` factory, object-reader dispatch and per-field runtime accessors are not identified. Source: `artifact: docs/formats/drawables.md:111-123`.
- Store-class name: unknown in the cited registration scan; the core `0x02`-`0x06` registration path was not located. Source: `artifact: docs/formats/zft.md:98`.

## Counts

| Code | Name | Slots | Stored bytes | Logical bytes |
|---|---|---:|---:|---:|
| `0x02` | `zdr` | 167,897 | 46,719,905,568 | 100,362,894,768 |

Denominator: **1,255,039** slots; the exact slot share is **167,897 / 1,255,039**. Exact counts and logical bytes are reported independently in `workspace: coverage_audit/out/tables.md:6`, `artifact: docs/formats/drawables.md:15` and `workspace: CONTEXT_HANDOFF.md:207`; the denominator is in `workspace: CONTEXT_HANDOFF.md:11` and `workspace: coverage_audit/out/tables.md:42`.

- Slots are unique by root, nested-header offset and slot ordinal. Equality with distinct `(root, absolute offset, stored length)` tuples within the code does not prove unique content or non-overlapping physical extents. Logical bytes are declared sizes, not successfully decoded bytes. Source: `artifact: docs/formats/drawables.md:19`.
- The Rust census read 312,661,753 CSV bytes in 1.585 s (197.31 MB/s) and completed the two-pass join in 4.175 s (601,263 input rows/s). This is a metadata scan, not a payload decode benchmark. Source: `artifact: docs/formats/drawables.md:47`.
- Root generation is `4` throughout the census; per-row generation is the high `u16` of the containing header's `+0x18`, not a resource version. Source: `artifact: docs/formats/drawables.md:21`. Per-root, per-generation and name-origin strata are tabulated at `artifact: docs/formats/drawables.md:23-45`.

## Container

- **Prefix.** The measured RPF9 slots start with 16 zero bytes; the first zlib stream begins at `slot + 0x10`. `RSC9` is a family label for the page-resource reader, not required ASCII magic. The file view's synthesized `RSC8` header is a separate layer and does not replace the on-disk zero prefix. Source: `artifact: docs/formats/drawables.md:51`; TOC stored size and offset are in 16-byte units, source `workspace: CONTEXT_HANDOFF.md:99`.
- **Compression.** Concatenated virtual pages hold the object graph; physical pages follow and hold buffers. Streams are zlib. Source: `artifact: docs/formats/drawables.md:51-53`. Alignment evidence: in the 528-byte control the block map is at virtual `0x580`; streams at slot-relative `0x10` and `0x1a0` consume 398 and 100 bytes and expand to 1,616 virtual and 240 physical bytes, summing to the TOC's 1,856 logical bytes; 10 bytes separate the streams and 12 zero bytes follow the last. Source: `artifact: docs/formats/drawables.md:55`.
- **Page-block / chain.** The virtual root begins with a zero qword; root `+0x08` is the block-map link, addressed by subtracting `0x50000000` (accepted range `[0x50000000,0x58000000)`). Physical links use base `0x60000000` (`[0x60000000,0x70000000)`). At the block map, bytes `+0x08` and `+0x09` are virtual and physical page counts; those counts do not prove the pages were recovered. Source: `artifact: docs/formats/drawables.md:53`.
- **Chaining limits.** The core reader searches up to 1 MiB past a stream end for the next zlib signature and caps counts at 1-32 virtual and 1-64 physical pages. A failed physical inflate can return a partially assembled resource; trust an exact slot replay with per-page EOF and summed lengths over CLI page counts alone. Source: `artifact: docs/formats/drawables.md:57`.
- **Unknown honestly.** The other block-map fields are not decoded, and a complete field-driven page reader covering all codecs and padding is open. Source: `artifact: docs/formats/drawables.md:53,57`. The 59-piece district replay did inflate every selected slot to its exact TOC length within slot bounds, but that is a bounded replay, not a whole-type page reader. Source: `artifact: district_render.md:115`.

## Fields

`D`, `M`, `Gm`, `VB`, `MB`, `P`, `T` and `R` are reader-side offset labels defined at `artifact: docs/formats/drawables.md:65`; engine symbol names for these offsets are not available, and none are invented here. Widths and meanings are the local reader's measurements unless marked inferred.

| Offset | Width | Meaning | Confidence | Source |
|---|---|---|---|---|
| descriptor `+0x10` | `u32` | `0x00000002` identifies `zdr` | measured | `artifact: docs/formats/drawables.md:7` |
| `slot+0x00..+0x0f` | 16 bytes | zero prefix before first zlib | measured | `artifact: docs/formats/drawables.md:51` |
| `slot+0x10` | zlib stream | first stream; concatenated virtual pages then physical buffers | measured | `artifact: docs/formats/drawables.md:51-55` |
| virtual root `+0x08` | qword | block-map link; subtract `0x50000000` | measured | `artifact: docs/formats/drawables.md:53` |
| block map `+0x08/+0x09` | `u8`/`u8` | virtual and physical page counts; not proof of recovery | measured | `artifact: docs/formats/drawables.md:53` |
| `D+0x50` | qword link | LOD0 list; list `+0x00` model-pointer array, `+0x08` `u16` count | measured | `artifact: docs/formats/drawables.md:69` |
| `D+0x58/+0x60/+0x68` | qword links | higher-LOD lists; replayed on the largest sample, null in single-LOD controls | measured | `artifact: docs/formats/drawables.md:70` |
| `D+0x70..+0x7c` | 4 floats | candidate LOD thresholds; native rule not traced | inferred | `artifact: docs/formats/drawables.md:71` |
| `D+0xa8` | qword pointer | name reference; not the source of the TOC type code | measured | `artifact: docs/formats/drawables.md:72` |
| `D+0x20..+0x48` | floats | consistent with bound sphere and two AABBs in one control; semantics not established | inferred | `artifact: docs/formats/drawables.md:77` |
| `D+0x10` | pointer | shader-group; group `+0x08` texture-dictionary, `+0x10` material array, `+0x18` `u16` count | measured | `artifact: docs/formats/drawables.md:87` |
| `D+0x18` | pointer | skeleton link; null in no-skeleton control, virtual pointer in skeleton controls | measured | `artifact: docs/formats/drawables.md:101` |
| `M+0x08/+0x10` | pointer / `u16` | geometry-pointer array and its count | measured | `artifact: docs/formats/drawables.md:73` |
| `M+0x20` | pointer | `u16` material index per original geometry ordinal | measured | `artifact: docs/formats/drawables.md:74` |
| `Gm+0x40` | virtual link | qword to a second record; `u32` word count at `+0x08`, physical meshlet pointer at `+0x18` | measured | `artifact: docs/formats/drawables.md:75` |
| `Gm+0x58/+0x60/+0x68` | `u32` / `u64` / pointer | vertex word count (`*4`), geometry marker `0x1601`, physical vertex-buffer pointer | measured | `artifact: docs/formats/drawables.md:76` |
| `VB+0x00..+0x3f` | 16 × `u32` | stream descriptors; nonzero gives offset `2*(word>>8)` and layout tag `word & 0xff` | measured | `artifact: docs/formats/drawables.md:79` |
| `VB+0x60/+0x64/+0x68`, `+0x70/+0x74/+0x78`, `+0x6c` | `f32` / `u32` | position origin, scale, axis selector (`0 → [Z,Y,X]`, `1 → [Z,X,Y]`, else `[X,Y,Z]`) | measured | `artifact: docs/formats/drawables.md:79` |
| `MB+0x00/+0x04/+0x08`, records at `+0x0c` | `u16`/`u32`/16-byte | meshlet count, total triangles, remap entries, meshlet records, then packed triangles and global remap | measured | `artifact: docs/formats/drawables.md:81` |
| Material `+0x00/+0x04/+0x08` | `u32`/bytes/qword | shader-family ID, `atem`, parameter-storage reference | measured | `artifact: docs/formats/drawables.md:88` |
| Material `+0x10/+0x20` | pointers | texture-pointer region and typed-parameter block `P` | measured | `artifact: docs/formats/drawables.md:89` |
| Material `+0x39/+0x3c` | `u8`/`u32` | render bucket and mask, as labeled by the local reader | measured | `artifact: docs/formats/drawables.md:90` |
| `P+0x01/+0x04/+0x08` | `u8`/`u16`/entries | texture count, entry count, 8-byte `(u32 identifier, u32 information)` | measured | `artifact: docs/formats/drawables.md:91` |
| texture ref / `T+0x10`, `T+0x30`, `R+0x10`, `R+0x08` | `u32`/`u64`/pointer | `s=(information>>2)&0xff` when `information&3==0`; `T+0x10` `u64 0x980`; `T+0x30 → R`; `R+0x10` `u32 6` → direct ETPF key at `R+0x08` | measured | `artifact: docs/formats/drawables.md:92` |
| CB parameter kind 3 | bitfields | buffer index bits `2..7`, byte offset `8..19`, byte length `20..31`; shader evaluation not reproduced | inferred | `artifact: docs/formats/drawables.md:93` |
| UV descriptor slots `3,4,14,15` | tags | tag `0x28` two `i16` / 8192, tag `0x42` two `f32`; slot 3 chosen empirically | inferred | `artifact: docs/formats/drawables.md:97` |
| skeleton `+0x6c` | `u16` | bone count (3, 156 in controls); six consecutive duplicates | measured | `artifact: docs/formats/drawables.md:105` |
| skeleton `+0x40` | virtual link | `u16` parent-index array; one root `0xffff`, no cycles in controls | measured | `artifact: docs/formats/drawables.md:106` |
| vertex slot 8 tag `0x25` | `u8` tag | skin-related stream evidence; weights and joint indices not decoded | inferred | `artifact: docs/formats/drawables.md:109` |
| name table `0x1462fcd30 + 0x98*variant + 8*code` | static VA | variant-0 string `zdr` at `0x14677e245` in the examined executable | measured | `artifact: docs/formats/drawables.md:118` |

All positions are little-endian. Source for endianness and reader qualifier: `artifact: docs/formats/drawables.md:65`.

## Decode status

Recorded results, not executed now:

The recorded bounded-reader proof command is below; supply the selected archive, slot start and stored length. It proves only the selected control, with results listed below, rather than a whole-type decode. Source: `artifact: docs/formats/drawables.md:184-196`.

```text
drawable_check <root-archive> <slot-start-hex> <stored-bytes> <private-obj>
```

- Standalone no-skeleton `zdr`, `levels.rpf`, 528 → 1,856 bytes: 1 model, 1 geometry, 1 meshlet, 4 vertices, 2/2 declared triangles, 1 material, 1/1 binding; OBJ verified. Source: `artifact: docs/formats/drawables.md:129`.
- Standalone skeleton `zdr`, `data.rpf`, 1,344 → 4,512 bytes: 3 vertices, 1/1 triangle, 3 bone records counted, 3/3 distinct direct texture IDs matched BC7 ETPF, 0/3 one-bit controls; a binding test, not a pixel or skinning test. Source: `artifact: docs/formats/drawables.md:130`.
- Diffuse textured standalone `zdr`, `levels.rpf`, 5,040 → 10,064 bytes: 186 positions and UVs, 294/294 triangles, 1/1 binding, OBJ and MTL exported, 4/4 IDs matched ETPF, 0/4 controls, 256×256 BC1 sRGB, 186/186 required UVs finite. Source: `artifact: docs/formats/drawables.md:131`; corroborated at `workspace: CONTEXT_HANDOFF.md:207`.
- Textured dictionary member control: 2 geometries, 4,182 positions and UVs, 2,661 faces, 2 bindings, 2/2 diffuse resolved as BC1 sRGB, 9/10 distinct IDs matched ETPF. Source: `artifact: docs/formats/drawables.md:132`.
- Size/root strata: seven bounded Rust probes over 528 to 13,343,136 stored bytes recovered both segments, exact logical sizes and a decoded mesh; 0.999 s wall. Source: `artifact: docs/formats/drawables.md:141-153`.
- Higher LODs on the largest sample: `+0x50` 382,648/382,672 declared triangles, `+0x58` 191,332/191,336, `+0x60` 95,655/95,655, `+0x68` 47,834/47,834, all with in-range model/geometry pointers; not a multi-LOD OBJ export. Source: `artifact: docs/formats/drawables.md:155-162`.
- District replay: 59 `zdr` pieces, 1,026,413 vertices, 1,063,486 triangles, 1,347 LOD0 geometries; textured geometries rose from 113 to 369 of 1,347 with layer-0 terrain binding, an inference for alpha-as-mask on 204 bindings. Source: `artifact: district_render.md:113-115,219`; `workspace: CONTEXT_HANDOFF.md:211-214`.
- Write status: W0 extract-only. OBJ/MTL is a lossy alternate representation; no encoder, parse-back, bit-stable round trip or game-loadable write. Source: `artifact: docs/formats/drawables.md:176-178`; `workspace: CONTEXT_HANDOFF.md:201`.

## Verification

- Exact population: **167,897** slots, **46,719,905,568** stored bytes and **100,362,894,768** logical bytes out of **1,255,039** slots. Sources: `workspace: coverage_audit/out/tables.md:6` and `artifact: docs/formats/drawables.md:15`. These prove census accounting by slot identity, not a decode of every slot.
- Exported OBJ record counts independently checked: standalone textured OBJ 186 `v`, 186 `vt`, 294 `f`, 1 `usemtl`; dictionary-member OBJ 4,182 `v`, 4,182 `vt`, 2,661 `f`, 2 `usemtl`. The bounded control took 1.19 ms through page and material checks before OBJ writing. Source: `artifact: docs/formats/drawables.md:196`. These prove geometry/UV/face and material export on those controls.
- Material path on the earlier textured dictionary walk: 317/317 geometry bindings, 456/507 distinct direct IDs matched ETPF, 0/507 one-bit controls; 0.832 s including raster and export. Source: `artifact: docs/formats/drawables.md:137`. This validates the material path, not the census as a whole.
- District verification re-asserted per-class geometry sums, guard budgets, pixel totals and both seam tables; ground-to-structure tightest 0.00015759468 and worst tile-to-tile 0.00589766277 world units. Source: `artifact: district_render.md:239,246-247`. These prove geometric fit of decoded meshes to placements, not material or animation correctness.
- **EXTERNAL (explicitly marked, unnamed):** `workspace: CONTEXT_HANDOFF.md:11` records an independent implementation agreeing on the 1,255,039 entry count and 4,373 header count. This corroborates only the denominator and header count, not any `zdr` payload decode.
- Decode commands, copied from evidence and **not executed for this document** (recorded results only): `artifact: docs/formats/drawables.md:184-194` lists `cargo build --release --offline --bin drawable_census --bin drawable_check`, `drawable_census <full-toc-db> <descriptor-census-csv> <verified-type-word-join>`, `drawable_check <root-archive> <slot-start-hex> <stored-bytes>`, `drawable_check ... --probe-lods`, `srpf9 model <root-archive> <slot-start-plus-16> --obj <private-obj>`, `srpf9 material ...`, and `cpu_drawable audit|render ...`. The only commands executed in this session were read-only PowerShell file inspection; no decoder, archive scan or GPU job was run.

Recorded replay commands with explicit operand positions, from `artifact: docs/formats/drawables.md:184-194` (not re-run here):

```text
drawable_census <full-toc-db> <descriptor-census-csv> <verified-type-word-join>
drawable_check <root-archive> <slot-start-hex> <stored-bytes> <private-obj>
srpf9 model <root-archive> <slot-start-plus-16> --obj <private-obj>
```

## Unknowns

- Complete field-driven page reader for all codecs and padding: only signature-based recovery on bounded controls is validated. Settling evidence: a slot-bounded reader reproducing declared logical sizes across all slots with per-page EOF and failure accounting (`artifact: docs/formats/drawables.md:57`).
- Skin weights and joint indices for vertex tag `0x25`: tag presence measured on 39 geometries, stream content not decoded. Settling evidence: bounded decode of descriptor slot 8 cross-checked against bone count `+0x6c` and parent array `+0x40` (`artifact: docs/formats/drawables.md:105-109`).
- Native LOD distance rule: four float-like values at `D+0x70..+0x7c` are candidate thresholds only. Settling evidence: trace the native selection code that consumes those offsets (`artifact: docs/formats/drawables.md:71`).
- Bound field semantics at `D+0x20..+0x48`: one-control sphere/AABB reading. Settling evidence: a runtime accessor trace or a multi-variant comparison of stored values against recomputed bounds (`artifact: docs/formats/drawables.md:77`).
- Shader-side evaluation of constant-buffer parameters: extraction only, no identifier-to-semantics table. Settling evidence: bind the parameter identifiers to shader lanes (`artifact: docs/formats/drawables.md:93`; `artifact: district_render.md:206`).
- Texture-reference variant classification and shader UV selection: slot 3 is an empirical choice; other tags are unresolved. Settling evidence: classify all reference tags across slots and trace UV selection (`artifact: docs/formats/drawables.md:92,97`).
- Native `zdr` factory and reader dispatch and the reason `zdr` and `zbdr` take different mesh paths: enum path verified only. Settling evidence: trace the store factory from the extension lookup (`artifact: docs/formats/drawables.md:123`).
- Which header layer the runtime consumes, on-disk zero prefix versus synthesized `RSC8`: both observed. Settling evidence: identify the device-vtable path used for packaged slots (`artifact: docs/formats/drawables.md:51,121`).
- Whole-type decode coverage and writer: only sampled slots decode; no encoder or round trip. Settling evidence: a full-slot bounded decode audit and a parse-back test (`artifact: docs/formats/drawables.md:141,178`).

## Changelog

- 2026-11-26: initial record. Counts taken from `workspace: coverage_audit/out/tables.md:6` and `artifact: docs/formats/drawables.md:15`; container, fields, decode, verification and unknowns taken from `artifact: docs/formats/drawables.md:49-208`, `artifact: district_render.md` and `workspace: CONTEXT_HANDOFF.md`.
- No census scan and no decoder execution were performed by this worker; counts are from the cited artifacts and a separate counting worker. File reads and the patch write used native PowerShell. No Python, no batch archive scan, no key, no asset and no publication.
- 2026-11-26, audit repair: normalized headings to the eight exact names; downgraded the self-assigned grade A to conservative **B (partial payload structure)** because the published `Full` status covers only sampled LOD0 layers with no skin/all-LOD decode or writer; added the authoritative current status citation `artifact: docs/coverage.md:128`. Counts already matched `artifact: docs/coverage.md:128` and `artifact: docs_complete_work/type_counts.tsv`; no decoder was run for this repair.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zdr.md`. No count was selected by modification time.

