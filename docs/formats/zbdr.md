# `zbdr` resources (type code `0x0f`)

2026-11-26, revised after the same-day BVH4 adoption pass. Grade **B (partial payload structure)**, conservative: no complete `zbdr`-population payload decode exists; the BVH4 structural layer is checked on retained `zbft`-derived bodies and `zbdr`-specific body evidence is sampled. Decode limits: the node layer is structurally decoded on 141 retained bodies **drawn from the `zbft` population**, using an externally sourced layout checked against local bytes; it is not a `zbdr`-population measurement. `zbdr`-specific body evidence remains eight sampled slots. Byte-exact rehydration, child-box recomputation, the parent array's values, runtime ordering, the writer, a standalone OBJ and any round trip are not established. The 2026-11-24 limitation "internal box/parent tables remain to be decoded" (`artifact: docs/formats/drawables.md:258`) is superseded for the shared layout by `artifact: bvh_nodes/adopt.md:243-266` (2026-11-26), with the artifact-scope caveat just stated.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The little-endian resource descriptor word at `+0x10` is `0x0000000f` in the measured `zbdr` slots; `0x00000002` is `zdr`. These labels come from the game's extension table, not guessed filenames. Variant-0 strings are `zbdr` / `ibdr` / `#bdr`; the three rows do not prove three on-disk encodings (`artifact: docs/formats/drawables.md:7`).

Structural identity, **inferred from static code plus payload replay**: `zbdr` is a serialized Xbox raytracing bottom-level acceleration structure (BVH4), registered at runtime as `BvhDrawableStore`. It stores a BVH and numbered triangle references into separate input geometry, not a drawable's model/LOD/shader graph and not a standalone mesh. The ordinary `zdr` mesh decoder returns `NoGeometry` on `zbdr` by design (`artifact: docs/formats/drawables.md:210-216`, `:244`, `:252-258`).

Static dispatch evidence: `0x145ba61f0` passes `BvhDrawableStore` and literal `0x0f` to store initializer `0x1419ca0b0`, which writes the enum at store `+0x30` and installs vtable `0x1461d1af0`; sibling codes are `0x10` `BvhDwdStore` and `0x11` `BvhFragmentStore` (`artifact: docs/formats/drawables.md:244`). The extension-string accessor at `0x14056ee50` branches at `0x14056efae` to the `0x0f` result at `0x14056f079` (`artifact: docs/formats/drawables.md:243`). Neither path was executed; the executable was read as a PE/COFF file only.

Node-layer identity, **external, adopted mechanically and checked on local bytes** (`artifact: bvh_nodes/adopt.md:1-84`): the structure is `body[0x100 .. 0x100 + 64*(size_units+1))`, with the 64-byte `XboxBvh4Header` at structure offset 0. Node pointers encode `kind = ptr & 7`, `unit = ptr >> 3`, `address = structure_start + unit * 64`; kinds 0-3 are TRI0-TRI3, 4 BOX16, 5 BOX32, 6 INSTANCE, 7 AABB_GEOMETRY, and `0xffffffff` is invalid; BOX32 consumes two units (`:46-48`). The layout came from raw third-party files at commit `bd6ba97` read on 2026-11-26 (`:8-19`). No code was copied; the local scanner is an independent std-only Rust implementation (`:18-19`, `:129-131`). **External label, external claim.**

Grade scope: **B (partial payload structure)** covers the serialized BVH4 structural clauses checked on the retained bodies (header, level table, group headers, child pointers, traversal) plus `zbdr`-specific companion/geometry validation on eight slots. No grade A is claimed: the structural decode is on `zbft`-derived bodies, not all 250,434 `zbdr` slots, and byte-exact rehydration, the `H+0x38` parent-array values and a writer remain open. `artifact: docs/formats/drawables.md:258` and `workspace: coverage_audit/out/tables.md:5` recorded Partial before the adoption pass; the current authoritative status is `Partial` at `artifact: docs/coverage.md:127`. That is a date/scope difference, not a silent retraction.

Companion relation: **inferred, not a general pair proof**. Four of five same-name `zdr`/`zbdr` controls matched the game's 64-bit geometry-fingerprint check exactly at LOD0; the largest same-name pair failed despite agreeing on 93 geometry ordinals (`artifact: docs/formats/drawables.md:218`). A metadata join found a shared 64-bit TOC name hash for 128,160 of 250,434 `zbdr` slots against the `zdr` set, including all 126,746 dictionary-resolved slots plus 1,414 unresolved slots, and zero matches against the top-level `zdd` hash set (child names inside dictionaries were not tested) (`artifact: docs/formats/drawables.md:220`, `workspace: CONTEXT_HANDOFF.md:208`). A bounded text search found **zero** genuinely new own-derived `zbdr` numeric header pairs beyond the eight burned slots; the only new pair is one isolated external-document value, not for publication (`artifact: bvh_heldout/leaf2_zbdr.md:74-84`, `:88-99`, `:135-140`). The Brickell district render uses terrain height-patch `zdr`, explicitly **not** `zbdr` (`artifact: district_render.md:91`).

## Counts

| Scope | Slots | Stored bytes | Logical bytes | Source |
|---|---:|---:|---:|---|
| `zbdr`, all resource slots | 250,434 | 7,335,183,152 | 124,157,781,744 | `workspace: coverage_audit/out/tables.md:5`; `workspace: CONTEXT_HANDOFF.md:208`; `artifact: docs/formats/drawables.md:16` |
| Denominator, all census slots (Resource and Binary) | 1,255,039 | not used | not used | `artifact: docs_complete/evidence/census_counts.json`, `total_rows`; `workspace: coverage_audit/out/tables.md:42` |

The exact share of all resource slots is `250,434 / 1,255,039` (`artifact: docs/coverage.md:127`, cross-checked against `artifact: docs_complete_work/type_counts.tsv`). Counts are TOC slots, unique by root, nested-header offset and slot ordinal. They also equal the distinct `(root, absolute offset, stored length)` tuples within the code, which does not establish unique content or non-overlapping physical extents. Logical bytes are declared sizes, not successfully decoded bytes (`artifact: docs/formats/drawables.md:19`).

Per-root split, captured from `artifact: docs/formats/drawables.md:42-45`:

| Root | Name origin | Slots | Stored bytes | Logical bytes |
|---|---|---:|---:|---:|
| `core_bvh4.rpf` | DictionaryMatch | 125,835 | 6,303,001,328 | 106,424,221,520 |
| `core_bvh4.rpf` | UnresolvedHash | 123,372 | 973,088,256 | 16,765,190,128 |
| `shared_minigame000_bvh4.rpf` | DictionaryMatch | 911 | 57,298,384 | 938,415,088 |
| `shared_minigame000_bvh4.rpf` | UnresolvedHash | 316 | 1,795,184 | 29,955,008 |

Root generation is `4` throughout; header generation is the high 16 bits of the containing header's `+0x18` word, not a resource version. No row uses `Original` (`artifact: docs/formats/drawables.md:21`). The full census scan read all 1,255,039 rows in both the descriptor census and the SQLite index (4,373 headers), with no missing or duplicate join keys (`artifact: docs/formats/drawables.md:47`).

Separate artifact, not a `zbdr` count: `artifact: bvh_population/rows.tsv` holds **22,440** rows, all `status=ok`, matching the `zbft` (`0x11`) population, with 22,430 rows on `core_bvh4.rpf` and 10 on `shared_minigame000_bvh4.rpf` (`artifact: bvh_population/summary.md:6-16`; fresh targeted scan recorded in section 6). The 141 adoption bodies come from this `zbft`-derived set (`artifact: bvh_nodes/manifest.tsv:1-5`; `artifact: bvh_nodes/report.md:18-20`).

## Container

`RSC9` is a family label for the RAGE9 page-resource reader, not required ASCII magic. In bounded examples the slot starts with 16 zero bytes and the first zlib stream starts at slot `+0x10`; concatenated virtual pages hold the object graph and physical pages follow them (`artifact: docs/formats/drawables.md:51`).

Compression and prefix: stored `+0x00..+0x0f` are zero; `+0x10` begins a zlib stream. The 176-byte stored control inflated to 208 virtual plus 768 physical bytes, 976 logical bytes in total (`artifact: docs/formats/drawables.md:51`, `:61`, `:254`). Eight deduplicated slots from both roots inflated to their exact declared sizes (`artifact: docs/formats/drawables.md:254`). A prefix-only census on `shared_minigame000_bvh4.rpf` reproduced all 1,227 `zbdr` rows there (1,331 slots total in 0.466 s internal, 2,858 slots/s); its `bounded-inflate` status describes the prefix probe only (`artifact: docs/formats/drawables.md:174`).

Pages and blocks: the virtual root begins with a zero qword; `+0x08` is the block-map link, decoded by subtracting `0x50000000` (reader accepts `[0x50000000, 0x58000000)`). Physical links use base `0x60000000` over `[0x60000000, 0x70000000)`. At the block map, bytes `+0x08` and `+0x09` are virtual and physical page counts; they do not by themselves prove page recovery, and the remaining map fields are not decoded (`artifact: docs/formats/drawables.md:53`). In five size/root controls the block map sat at virtual `0x80` with one page per segment and a physical buffer from 512 to 31,457,280 bytes (`artifact: docs/formats/drawables.md:61`). The physical buffer `P` carries the header at `P+0x100` (`artifact: docs/formats/drawables.md:224`; `artifact: bvh_nodes/adopt.md:23-24`).

Alignment and chain status: the serialized outer size in the auxiliary record at `V+0x18` is rounded to 256 bytes (`artifact: docs/formats/drawables.md:228`). Nodes are 64-byte units; BOX32 consumes two units. Group storage is 4 KiB for BOX16 and 8 KiB for BOX32, holding at most `GROUP = 64` nodes each (`artifact: bvh_nodes/adopt.md:48`, `:59-68`). The scanner checks pre-header words `u32(P+0x20) = 0x140 + 64*size_units` and `u32(P+0x28) = u32(P+0x20) - 0x100`; the level table sits at `structure_end - 4 - 8*C` with the final u32 holding `C` (`artifact: bvh_nodes/adopt_scan.rs:258-263`; `artifact: bvh_nodes/adopt.md:50-57,158`). Coordinate discrepancy: the parenthetical body offsets `0x120`/`0x128` in `adopt.md:43-44` disagree with its scanner, which reads `0x20`/`0x28`; this document uses the scanner-checked offsets. The `4 mod 8` level-table start is a placement consequence, not a separate record-boundary finding (`adopt.md:227-231`). The core reader searches up to 1 MiB past a stream end for the next zlib signature and caps counts at 1-32 virtual and 1-64 physical pages. Its CLI can probe beyond a declared slot, and a failed physical inflate can still return a partially assembled resource; exact slot replay with per-page EOF and summed lengths is the trusted chain (`artifact: docs/formats/drawables.md:57`). A complete field-driven page reader for all codecs and padding remains open.

## Fields

All scalars and pointers are little-endian. `V` is the virtual resource root, `P` the physical buffer linked by `V+0x20`, `H = P+0x100` the compressed acceleration-structure header, `S` the structure start (`= H`), and `n` the leaf index within a group of up to 2,048 records. "Measured" means an observed value or a static-code comparison captured in the cited source; "inferred" means an interpretation; "external" means a name or rule sourced from the adopted outside layout, with local verification noted in the Meaning cell; "unknown" means no interpretation is established. Offset labels are used where no engine label was located.

| Offset | Width | Meaning | Confidence | Source |
|---|---:|---|---|---|
| `V+0x00` | 8 | Zero qword at virtual root | measured | `artifact: docs/formats/drawables.md:53` |
| `V+0x08` | 8 | Block-map link; subtract `0x50000000` | measured | `artifact: docs/formats/drawables.md:53` |
| `V+0x10` | 8 | `u64 1` in five wrapper controls; role unknown | measured | `artifact: docs/formats/drawables.md:61` |
| `V+0x18` | 8 | Virtual link to aux record at `V+0xa0`; its first `u32` is outer serialized size rounded to 256, byte `+0x05` equals densely referenced geometry-ordinal count, qword bits `54..55` select validation LOD (all eight controls LOD 0) | measured | `artifact: docs/formats/drawables.md:61`, `:228` |
| `V+0x20` | 8 | Physical pointer `0x60000000`, start of `P`; runtime converts to GPU-address alias when in mapped physical range | measured | `artifact: docs/formats/drawables.md:229`, `:245` |
| `V+0x28/+0x30/+0x38` | 8 each | Virtual links; first two targets read zero, third links to identity-basis bytes at `V+0x50` | measured | `artifact: docs/formats/drawables.md:61`, `:230` |
| `V+0x40` | 8 | Native validation compares this qword with selected drawable LOD geometry-derived fingerprint plus six; not the builder's `H+0x08` CRC32 | measured | `artifact: docs/formats/drawables.md:231`, `:246` |
| `V+0x50..` | 12+ | Three padded vectors read as an identity basis; transform reading is inferred. Ordinary `zdr` reader expects an LOD0 virtual pointer here, sees `f32 1.0` bit pattern and fails tag fallback | inferred | `artifact: docs/formats/drawables.md:61`, `:230` |
| `P+0x20/+0x28/+0x30` | 8 each | Serialized byte extent, deserialized byte extent, trailing BLAS-pointer count (DXR serialized-header naming is external); count zero in controls; `P+0x20 = P+0x28 + 0x100` | external | `artifact: docs/formats/drawables.md:232` |
| `P+0x20/+0x28` (low words) | 4 each | Declared end words: `0x140 + 64*size_units` and that value minus `0x100`; matched 141 of 141 retained bodies; use scanner coordinates rather than the conflicting prose parenthesis | measured | `artifact: bvh_nodes/adopt_scan.rs:258-263`; `artifact: bvh_nodes/adopt.md:158` |
| `H+0x00` | 4 | `flags`, observed `0x81020006` in 141 of 141 bodies | measured | `artifact: bvh_nodes/adopt.md:30`, `:157`; `artifact: docs/formats/drawables.md:233` |
| `H+0x04` | 4 | `size_units`, count of 64-byte nodes excluding the header; `64*(size_units+1)` is structure extent | measured | `artifact: bvh_nodes/adopt.md:31`, `:91-93`, `:159` |
| `H+0x08` | 4 | `crc32`; native validation export compares it with a checksum over geometry descriptors; builder diagnostic label | measured | `artifact: bvh_nodes/adopt.md:32`, `:249-250`; `artifact: docs/formats/drawables.md:234` |
| `H+0x0c` | 4 | `numElements`; CPU rehydrator leaf-record loop count | measured | `artifact: bvh_nodes/adopt.md:33`, `:234`; `artifact: docs/formats/drawables.md:234` |
| `H+0x10..+0x24` | 4 each | Six `f32` scene bounds, min XYZ then max XYZ; all eight controls finite and ordered; rounding relation to input vertex bounds open | measured | `artifact: docs/formats/drawables.md:235`, `:249`; `artifact: bvh_nodes/adopt.md:34-35` |
| `H+0x28/+0x2c` | 4 each | `offsetToNodes` / `offsetToPrimRemap` (signed in the external doc); group regions derived from the level table lie inside the structure | external | `artifact: bvh_nodes/adopt.md:36-37`, `:160` |
| `H+0x30` | 4 | `rootNodePtr`; `kind = ptr & 7`, `unit = ptr >> 3`. Observed 140 BOX16 and 1 TRI0 root on retained bodies; earlier probe called it packed root reference | external | `artifact: bvh_nodes/adopt.md:38`, `:46-48`, `:161`, `:205-206`; `artifact: docs/formats/drawables.md:236` |
| `H+0x34` | 4 | `offsetToElements`; earlier probe called it relative leaf-table offset | external | `artifact: bvh_nodes/adopt.md:39`, `:250`; `artifact: docs/formats/drawables.md:236` |
| `H+0x38` | 4 | `offsetToParents`; older diagnostic used the same label. The target array's own values are still not decoded; parent relation is reconstructed from child pointers | external | `artifact: bvh_nodes/adopt.md:40`, `:253`; `artifact: docs/formats/drawables.md:237` |
| `H+0x3c` | 4 | `compressionParams`; older diagnostic read low three bytes as `f32 byte << 23` scale. `no_xform = 0` in 141 of 141, so override values are in a transformed leaf frame | external | `artifact: bvh_nodes/adopt.md:41`, `:173`; `artifact: docs/formats/drawables.md:237` |
| Level table, `structure_end - 4 - 8*C` | 4 + 8*C | Final u32 is `C`; preceding `C` pairs are `(BOX32_end, BOX16_end)` byte offsets from `offsetToNodes`, bottom-up. Ordered and divisible by 128/64 on 141 of 141 bodies | external | `artifact: bvh_nodes/adopt.md:50-57`, `:160`, `:217-220` |
| Group word, `S + offsetToNodes + level offset + t*64` | 4 | `count = word >> 24`, `mask = word & 0xffffff`; 1 to 4 children, no bit past `6*count`. 195,341 of 195,341 parsed nodes valid | external | `artifact: bvh_nodes/adopt.md:59-65`, `:164-165`, `:249` |
| Child-pointer words | 4 each | Packed 3-bit type plus 29-bit 64-byte unit, written after the group header words; 499,178 TRI0 pointers, 0 invalid, 0 out of structure, 0 wrong-level box or non-TRI leaf pointers | external | `artifact: bvh_nodes/adopt.md:62-64`, `:166-169`, `:250` |
| Override words | 2 (BOX16) / 4 (BOX32) | One value per mask bit at `6*slot + component`, min xyz then max xyz. BOX16 masks all zero; 2,260 BOX32 nodes carry 11,775 f32 overrides, all finite, all 5,058 paired min/max ordered; containment in scene bounds not testable | external | `artifact: bvh_nodes/adopt.md:64-77`, `:170-174`, `:251-252` |
| Leaf `+0`, `+4*n`, `+7*n` | 3 each | `u24` geometry ordinals, first primitive ordinals, second primitive ordinals; `0xffffff` means no second primitive. Groups of 2,048 with `0x20000` source stride | measured | `artifact: docs/formats/drawables.md:239` |
| Leaf `+3*n`, `+10*n` | 1 each | Per-record bytes read by native code; not used to reconstruct winding or pairing | unknown | `artifact: docs/formats/drawables.md:239` |

The "external" rows are the only claims named from outside conventions; each carries a local verification note where one was measured. No specification URL was verified in this pass for the DXR naming; the BVH4 layout URLs are listed in `artifact: bvh_nodes/adopt.md:14-16` and were read by that artifact, not re-fetched here.

## Decode status

Layer status, with scope stated honestly:

Recorded `zbdr`-sample proof command, not executed in this revision (`artifact: docs/formats/drawables.md:256`):

```text
zbdr_probe <root-archive> <slot-start-hex> <stored-bytes> <logical-bytes> [<companion-archive> <companion-slot-start-hex> <companion-stored-bytes>]
```

The shared node-layout proof is the recorded `adopt_scan` command in section 6 on retained `zbft` bodies, not an additional `zbdr` sample run (`artifact: bvh_nodes/adopt.md:127-138`; `artifact: bvh_nodes/report.md:18-20`).

- Container, prefix, page recovery: **decoded** on sampled slots. Exact declared sizes reached on eight deduplicated slots from both roots; five size/root strata each recovered both pages (`artifact: docs/formats/drawables.md:164-174`, `:254`).
- Compressed header, bounds, leaf-reference tables: **decoded** on 8 of 8 deduplicated slots, including the 2,085,328-byte stored maximum with 269,957 leaf records, 491,856 unique primitive references and 93 geometry ordinals. All eight tables had duplicate-free, gap-free primitive ordinal sets per referenced geometry (`artifact: docs/formats/drawables.md:254`).
- Internal node layer: **structurally decoded** on 141 retained bodies (140 BOX16 roots, 1 TRI0) using the adopted external layout: 141/141 flags and declared end words, 141/141 valid level tables, 4,190 groups (1,218 BOX16 plus 2,972 BOX32) and 195,341 nodes (29,234 BOX16 plus 166,107 BOX32). Child counts were 2 in 28,900 nodes, 3 in 29,185, 4 in 137,256; none 0, 1 or above 4. `bad_count = 0`, `bad_mask = 0`, and all five pointer-error columns zero. Traversal from the declared root closed on 140/140 box samples with no cycle, dangling pointer, orphan or multi-parent node, and leaves reached equalled `L` in 140/140 (`artifact: bvh_nodes/adopt.md:153-174`, `:243-266`). This supersedes the older "internal box tables open" line for the family layout; it does not replace the `H+0x38` target-array value decode, which remains open.
- Overrides: **partially decoded**. BOX16 masks are zero on every parsed node, so half-precision `half_down`/`half_up`/`±inf` rules are unexercised. BOX32 overrides were decoded on 2,260 nodes across 73 samples: 11,775 stored f32 values, 0 NaN, 0 infinity, 5,058 ordered min/max pairs and 0 reversed pairs. Scene-bounds containment is not testable because `compressionParams != 0x007f7f7f` in 141 of 141 (`artifact: bvh_nodes/adopt.md:170-174`, `:251-252`, `:273-283`).
- Wrong-offset and triangle-root controls: the +1-byte shift gave 385,578 invalid count/mask words and 195,320 of 195,341 nodes failing; +4 bytes gave 8,380 and 4,190 of 195,341; the true offset had 0 failures. The single triangle-root sample separated as expected: root type TRI0, `nc=0`, no level table, and its leaf slot produced a plausible header word but an out-of-range child pointer (`artifact: bvh_nodes/adopt.md:191-212`, `:249`).
- Companion validation: **partial**. The 176-byte sample's box root held two leaf records referencing triangle ordinals 0 and 1 of geometry 0; its fingerprint-matched `zdr` companion decoded to four vertices and two triangles with bounds approximately `(-0.16797, -0.21484, 0)` to `(0.16797, 0.21484, 0)`. The singleton BLAS matched a separate three-vertex, one-triangle drawable's bounds. Four of five same-name controls passed the fingerprint check; the largest did not (`artifact: docs/formats/drawables.md:218`, `:254`).
- Artifact-scope reconciliation: the 141 bodies were retained from the `zbft` (`0x11`) population via `artifact: bvh_population/rows.tsv` and `zbft_slots.tsv` (`artifact: bvh_nodes/report.md:18-20`; `artifact: bvh_population/summary.md:6-9`). `zbdr` uses the same serialized header at `P+0x100` (`artifact: docs/formats/drawables.md:224`), so the node-layer result is a family-level structural decode applied to `zbdr`, not a measured decode of 250,434 `zbdr` bodies. That is why the grade is B, not A: the structural layer is checked on borrowed `zbft` bodies and `zbdr`-specific coverage is sampled. The older four trailing-word refutations are explained by the adopted level-table reading, not silently dropped (`artifact: bvh_nodes/adopt.md:214-241`, `:255`).
- No standalone mesh or OBJ: the type has no drawable mesh; leaf references require the separate input geometry's index and position buffers (`artifact: docs/formats/drawables.md:216`, `:250`).
- Population-level `zbdr` body decode: **not achieved**. The census and the 1,227-row prefix probe are metadata or bounded-prefix checks only (`artifact: docs/formats/drawables.md:47`, `:174`). No new held-out own-derived `zbdr` numeric pair was found in bounded text artifacts (`artifact: bvh_heldout/leaf2_zbdr.md:97`, `:135-140`).
- Write status: **W0, extract-only**. No encoder, game-format parse-back, bit-stable round trip, game-loadable write, byte-exact rehydration or runtime adoption proof exists (`artifact: docs/formats/drawables.md:178`, `:258`; `artifact: bvh_nodes/adopt.md:265-266`, `:284`; `workspace: CONTEXT_HANDOFF.md:201`).

Captured page strata, from `artifact: docs/formats/drawables.md:166-174` (not re-run here): 144 to 720 bytes, 208 virtual / 512 physical; 4,400 and 4,512 to 65,744, 208 / 65,536; 2,085,328 to 31,457,488, 208 / 31,457,280; and a 4,688 to 65,744 control in the smaller root. All five returned `NoGeometry` from the mesh reader, which is expected. Five runs took 0.625 s wall including launches and failed mesh probes; eight BVH probe runs took 0.896 s (3.50 stored MB/s, 53.96 logical MB/s) including process launches, inflate, checks and private log writes (`artifact: docs/formats/drawables.md:174`, `:256`). The adoption scan took 1,053 ms for 141 bodies / 60,013,056 bytes read in one `rustc -O` run (`artifact: bvh_nodes/adopt.md:129-134`).

## Verification

Commands below are copied from existing evidence and were **not executed in this session** unless marked fresh. Tool binaries are local Rust builds, not the game; the executable and packaged builder DLL were read as PE/COFF files and never loaded or run (`artifact: docs/formats/drawables.md:182-194`, `:256`, `:258`).

```text
cargo build --release --offline --bin drawable_census --bin drawable_check
cargo build --release --offline --bin zbdr_probe
drawable_check <root-archive> <slot-start-hex> <stored-bytes> [<private-obj>]
zbdr_probe <root-archive> <slot-start-hex> <stored-bytes> <logical-bytes> [<companion-archive> <companion-slot-start-hex> <companion-stored-bytes>]
llvm-objdump -d --start-address=0x144ebbc30 --stop-address=0x144ebbd36 <game-exe>
cd artifact: bvh_nodes; rustc -O adopt_scan.rs -o adopt_scan.exe; ./adopt_scan.exe
cargo run --release --offline --bin bvh_pop_probe -- artifact: bvh_population
```

Sources for those captured runs: `artifact: docs/formats/drawables.md:182-194`, `:256`; `artifact: bvh_nodes/adopt.md:127-138`; `artifact: bvh_population/summary.md:8-9`. Additional captured checks: the Rust xref scanner covered 99,875,328 executable bytes in 0.544 s (~184 MB/s including input read), followed by `llvm-objdump` confirmation at matching VAs (`artifact: docs/formats/drawables.md:256`). Fingerprint controls used `u64(Gm+0x30) >> 9` folded over models selected by `M+0x34 & 0x20` and `u16(M+0x36)` geometries with shader mask at material `+0x3c` (`0x2001` or `0x2008` fully set), plus six (`artifact: docs/formats/drawables.md:218`).

Commands **actually run in this session** were read-only PowerShell text reads plus one narrow Rust batch over the 2.9 MB TSV. No decoder, archive payload scan, executable, GPU job or Python was used:

```powershell
Get-ChildItem 'artifact: docs/formats' -Filter '*.md' | Select-Object -ExpandProperty Name
Select-String -Path 'workspace: CONTEXT_HANDOFF.md' -Pattern 'zbdr|0x0f|0f' -CaseSensitive:$false
Get-Content 'workspace: CONTEXT_HANDOFF.md' | Select-Object -Index (0..376)
Get-Content 'artifact: docs/formats/drawables.md'
Get-Content 'workspace: coverage_audit/out/tables.md'
Get-Content 'artifact: bvh_nodes/adopt.md'
Get-Content 'artifact: bvh_population/summary.md'
Get-Content 'artifact: bvh_population/verify_report.md'
Get-Content 'artifact: bvh_heldout/leaf2_zbdr.md'
Select-String -Path 'artifact: district_render.md' -Pattern 'zbdr|BVH|bvh|0x0f|acceleration'
rustc -O workspace: temp/rows_probe.rs -o workspace: temp/rows_probe.exe
& workspace: temp/rows_probe.exe
```

Fresh TSV result (`rows_probe.rs`, std only): 21 columns in the order `idx, status, N, L, rootref, rootref_slot, rootref_low3, leaf_off, h38_signed, P20, P28, body_len, hdr_len, T1, T2, T3, T4, mg_group, mg_extent, root, name`; 22,440 data rows, all `ok`; `N` in [3, 285,375], `L` in [1, 155,308]; roots 22,430 `core_bvh4.rpf` and 10 `shared_minigame000_bvh4.rpf`; `rootref_low3` histogram `4:22,439`, `0:1`; T1 pass 21,971 / fail 469, T2/T3/T4 pass 22,440 each. Sample rows: idx 0 `N=369 L=231 leaf_off=640 rootref_low3=4 hdr_len=208`; idx 7,763 `N=3 L=1 leaf_off=128 rootref_low3=0`; idx 22,439 `N=40 L=24 leaf_off=256 rootref_low3=4`. These reproduce `artifact: bvh_population/summary.md:13-25`, `:43-46`, `:91` and `artifact: bvh_population/verify_report.md:9-24`, `:43-49` without a PowerShell TSV pipeline. They describe `zbft`, not `zbdr`. Language used here: PowerShell/native reads and a std-only Rust batch; no Python, no decoder run, no archive scan. No keys, assets or local selection records are reproduced; nothing was published.

## Unknowns

- Byte-exact rehydration: the external artifact claimed byte-identical output against `XboxBvhBuilder.dll!RehydrateRaytracingAccelerationStructureX` on eight samples with private geometry and the DLL; this was not reproduced locally (`artifact: bvh_nodes/adopt.md:81-84`, `:269-272`). Settling evidence: a legally sourced geometry-plus-DLL replay, which is unavailable under the current posture.
- BOX16 half overrides: masks are zero on all 141 bodies, so `half_down`/`half_up`/`±inf` and `0x7c00`/`0xfc00` rules are unexercised (`artifact: bvh_nodes/adopt.md:170`, `:252`, `:273-276`). Settling evidence: a body with a non-zero BOX16 mask plus recomputed child boxes.
- BOX32 override containment: `no_xform = 0` in 141 of 141, so stored values live in a transformed leaf frame; without source geometry the transform cannot be inverted (`artifact: bvh_nodes/adopt.md:173`, `:280-283`). Settling evidence: one fingerprint-matched companion whose geometry permits child-box recomputation.
- `H+0x38` target array values: labelled `offsetToParents` externally and reconstructed parent relation comes from child pointers; the array itself is still not decoded (`artifact: bvh_nodes/adopt.md:40`, `:253`; `artifact: docs/formats/drawables.md:237`). Settling evidence: decode the array at the adopted offset and cross-check against traversal-derived parents.
- Runtime ordering and the build-descriptor `+0x18` geometry-array producer upstream of game submission functions `0x140ea6c60` and `0x142490a20` (`artifact: docs/formats/drawables.md:247`, `:258`). The external doc marks the game's runtime call path Open (`artifact: bvh_nodes/adopt.md:284`). Settling evidence: static trace of that producer plus a paired runtime-order comparison, which cannot be done by executing the game.
- Why the largest same-name pair failed the fingerprint check despite 93 agreeing geometry ordinals; name hash is not a sufficient pair proof (`artifact: docs/formats/drawables.md:218`, `:220`). Settling evidence: reproduce the seven-step fingerprint on that pair and trace where its selected geometry set diverges.
- `zbdr`-specific node-layer measurement: the 141 bodies are `zbft`-derived; no `zbdr` population pass over all 250,434 slots has been run, and the bounded text search found zero new own-derived `zbdr` numeric pairs beyond eight known slots (`artifact: bvh_nodes/report.md:18-20`; `artifact: bvh_heldout/leaf2_zbdr.md:97`, `:135-140`). Settling evidence: a bounded slot-exact Rust pass over both `zbdr` roots with per-page EOF, summed-length assertions and the adopted group decode.
- Meaning of `V+0x10` (`u64 1`), `V+0x40` beyond its comparison role, the two zero virtual links at `V+0x28/+0x30`, and whether the identity-basis reading at `V+0x50` generalises (`artifact: docs/formats/drawables.md:61`, `:228-231`). Settling evidence: trace native accessors and compare their reads on controls with different wrapper values.
- Block-map fields beyond the two page-count bytes, padding and alignment rules beyond the observed 208-byte virtual wrapper and 256-byte outer size, and a field-driven page reader covering all codecs (`artifact: docs/formats/drawables.md:53`, `:57`, `:61`). Settling evidence: trace the native block-map consumer and verify its page boundaries against complete slot-bounded inflations.
- Family-level caveat: the pre-registered T1 rule on `H+0x38` was refuted with 469 counterexamples out of 22,440 `zbft` slots, while T2-T4 survived with none (`artifact: bvh_population/summary.md:22-25`, `:36-39`). That is a `zbft` population result and does not transfer to `zbdr` without a `zbdr` pass. Settling evidence: freeze the same rules on a bounded `zbdr` sample before judging them there.
- Child names inside `zdd` dictionaries were not tested against `zbdr` hashes; the join result is limited to top-level `zdd` (`artifact: docs/formats/drawables.md:220`). Settling evidence: a child-name hash join followed by the existing geometry-fingerprint check.
- Write path: no encoder, parse-back or round trip for any extract-only type (`workspace: CONTEXT_HANDOFF.md:201`). Settling evidence: an encoder whose output reparses with identical structural values, followed by the separately claimed game-load test.

## Changelog

- 2026-11-26, supervising review: corrected the declared-end coordinates to the scanner's `P+0x20/P+0x28`, documented the conflicting prose offsets, added explicit settling evidence to the remaining open questions and clarified that the denominator includes Resource and Binary census rows. Sources: `artifact: bvh_nodes/adopt_scan.rs:258-263`; `artifact: bvh_nodes/adopt.md:43-44`; `artifact: docs_complete/evidence/census_counts.json`.
- 2026-11-26: initial graded document. Grade B assigned from `workspace: coverage_audit/out/tables.md:5` and `workspace: CONTEXT_HANDOFF.md:164`. Counts, container, fields, decode status and verification compiled from `artifact: docs/formats/drawables.md:7-258`, with companion context from `artifact: district_render.md:91`. No new measurement or decoder run was performed; no published number was changed by this document.
- 2026-11-26, revision: grade split into A for the serialized BVH4 structural layer and B for `zbdr`-specific scope, after `artifact: bvh_nodes/adopt.md:1-336` added the externally sourced, locally checked level-table/group/pointer/traversal decode on 141 retained bodies and `workspace: docs/bvh-node-checkpoint.md:159-181` recorded the same result. Added the `H+0x00..+0x3c` external field names, structure extent and alignment, override results, wrong-offset controls, the artifact-scope reconciliation with the older `drawables.md` (2026-11-24) limitation, the `artifact: bvh_heldout/leaf2_zbdr.md` held-out finding, and a fresh narrow Rust TSV schema/sample check. Census placeholders unchanged; nothing published.
- 2026-11-26, audit repair: resolved the three count placeholders to 250,434 / 7,335,183,152 / 124,157,781,744 from `artifact: docs/coverage.md:127` and `artifact: docs_complete_work/type_counts.tsv`; normalized headings to the eight exact names; downgraded the earlier A/B split to a single conservative grade **B (partial payload structure)** because the structural decode is on `zbft`-derived bodies and no whole-`zbdr` payload decode exists. No decoder was run for this repair.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zbdr.md`. No count was selected by modification time.

