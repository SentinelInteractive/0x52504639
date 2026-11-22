# GTA VI animation: class-10 clip decode and skin binding

Status of the offline reverse-engineering work on the RAGE9 animation format and
the skeleton/mesh binding that turns decoded clips into a skinned export. This
document is private research output: it contains no names, no content, no code
and no extracted assets. Numbers are measured on a single reference build.

## 1. Class-10 channel codec

Clip data is stored as channel blocks. A block header declares a signature, the
frame count, a per-frame stride, and eleven class counts with a matching table of
slot indices. Blocks are decoded per class:

| class | payload |
| --- | --- |
| 0 | static quaternion, three floats, `w` reconstructed |
| 1 | static vector3 |
| 2 | static scalar |
| 4 | per-frame bit-packed quantised float, `{bits, quantum, offset}` |
| 5 | per-frame LUT index with an inline table |
| 7 | quaternion with one component reconstructed from the other three |
| 8 | explicitly stored quaternion, normalised |
| 10 | 64-frame superblock, eight interleaved bit lanes, second-order zigzag delta |

Class 10 is the bulk of the motion. Each superblock carries an anchor and a
cumulative offset; both are redundant encodings of the same state, so every block
can be checked against itself. Two independent checks are applied:

- the cumulative offset of superblock `k` must equal the sum of the 8k preceding
  run widths;
- stepping the previous superblock one frame past its end must land exactly on
  the next anchor.

Verified coverage on this build:

- animations found: **94,256**
- decoded completely: **94,072** (99.80%)
- anchor checks: **9,482,698**
- non-finite values produced: **0**
- quaternion tracks outside unit norm by more than 1e-3: **0**
- channel streams that consume exactly `data_off` bytes: **all decoded clips**

The remaining 184 clips fail structurally (class 3 blocks with an unknown layout,
or a run count that disagrees with the declared frame groups). They are reported,
not silently skipped.

## 2. Skeleton structure

The struct chain is `payload+0x18 -> drawable (+0x18) -> skeleton`, with the
bone count at `+0x6c` followed by a six-entry `u16` count/max chain.

| field | content |
| --- | --- |
| `+0x20` | `{u32 hash, u32 index}` table, 512-row window |
| `+0x28`, `+0x30` | further transform arrays |
| `+0x38` | bind records, 64 bytes each: 3x4 affine, translation in column 4, row 4 unused |
| `+0x40` | `u16` parent array, `0xFFFF` root |
| `+0x48` | variable-length name/hash table |
| `+0x6c` | bone count |

The fourth row of a bind record is not part of the transform. Inverting the full
4x4 including that row produces non-finite matrices; forcing the row to
`(0,0,0,1)` before inversion fixes it. This was the cause of the first
non-finite pose result.

## 3. Dense bone map

`+0x20` is an open-addressed hash table of 8-byte rows. It is **not** ordered by
index and **not** ordered by hash: rows sit in probe order and empty slots hold
`0xFFFF_FFFF`.

Two properties broke earlier permutation tests:

- capacity exceeds the bone count, so a bone-count-sized window leaves holes;
- two rows can alias one bone (a name hash and a bone id), so non-empty row count
  exceeds bone count.

Capacity was therefore detected rather than assumed, by requiring the smallest
power of two whose rows resolve to exactly `n` distinct indices covering `0..n-1`:

| window rows | non-empty rows | distinct indices | holes | verdict |
| --- | --- | --- | --- | --- |
| 256 | 122 | 95 | 47 | rejected |
| 512 | 283 | 142 | 0 | accepted |
| 1024 | 503 | 142 | 142 | rejected, rows out of range |

Reference rig: 142 bones, 142 distinct indices covering `0..141`, zero holes,
370 empty rows. The map is a real `0..n-1` set, not set overlap.

Hierarchy from the parent array: 10 roots, maximum depth 15, no cycles. A second
reference rig (133 bones) yields 1 root and passes the same checks.

## 4. Clip binding

Bone ids are hashes, so binding is a table lookup, not a geometric fit. A clip
counts as bound only when **every** distinct bone id in it resolves in the rig's
dense map.

- 127,589 payloads in one archive yield **2,791** rigs with a complete dense map.
- Against 68,237 animations: **4,230,268** fully-resolving rig/clip pairs, in
  4.5 s (932k pairs/s).
- Reference rig A (142 bones) fully binds **1,472** clips. Best: **51 of 51**
  distinct ids, 330 frames, 10.967 s.
- No rig in that archive fully binds more than **60** ids. A 136-id clip found
  earlier belongs to a rig outside it; its 75% overlap is **not** reported as a
  binding.

## 5. Resource pages

A resource is a chain of compressed frames at one archive offset. The block map
at `+0x08` declares virtual and physical page counts; physical pages hold vertex
and meshlet buffers under `0x60xxxxxx` pointers.

- The measured build stores these resources as **zlib**; an intermediate store of
  the same payloads re-compressed them as **zstd**. Both are sniffed per frame.
- Frames are read one at a time and the reader stops at the declared page count.
- Reading the correct archive matters: a copy of the archive with zeroed regions
  decodes as "no stream at this offset".

Reference rig B: one virtual page (49,920 bytes) then two physical pages
(2,162,688 and 48,864 bytes).

## 6. Vertex attribute split

Stream descriptors are eight `u32` words at the geometry's vertex-buffer offset.
The low byte is the attribute tag and `(word >> 8) << 1` is the byte offset.
Tags repeat across attributes, so a tag never determines layout: the stride is
the gap to the next stream offset, divided by the vertex count.

| rig | bytes/vertex | strides | product check |
| --- | --- | --- | --- |
| A (142 bones) | 56 | 8, 8, 8, 8, 4, 20 | 48,982 x 56 = 2,743,120 = declared buffer |
| B (133 bones) | 88 | 8, 12, 12, 4, 36, 4, 12 | 14,734 x 88 + 128-byte header = 1,296,720 = declared buffer |

Both tilings are exact to the byte. Descriptor 0 is always position, tag `0x42`,
8 bytes per vertex. An earlier claim that the descriptors do not tile the stride
was an arithmetic error in offset multiplication, not a format fact.

## 7. Skin weights

One 4-byte stream carries four `unorm8` weights. Over all 14,734 vertices of rig
B's single level-0 geometry:

- vertices summing to the full unorm range (255 +- 3): **100.00%**
- pre-normalisation sum range: **0.502 to 1.000** (the 0.502 cases are vertices
  whose remaining weight sat in palette slots that were dropped, see below)
- after normalisation: sum range **[1.000000, 1.000000]**, vertices outside
  1e-4: **0**

## 8. Joint field: palette closure

The joint stream is a 12-byte `0x26` stream. It reads as three 4-byte groups of
the form `[pad][a][b][pad]`, with groups 0 and 1 supplying the four weight slots:
slot 0 = group 0 byte 1, slot 1 = group 0 byte 2, slot 2 = group 1 byte 1,
slot 3 = group 1 byte 2. Group 2 repeats group 0.

The earlier 4.86% failure rate came from reading the 12 bytes as three independent
`4 x u8` quads and from a 4,000-vertex sample. Whole-mesh statistics settle it:

| byte position | distinct values | maximum |
| --- | --- | --- |
| 1, 5, 9 | 90, 91, 90 | **94** |
| 0, 4, 8 | 52 | 255 (pad) |
| 2, 6, 10 | 61 | 255 (palette) |
| 3, 7, 11 | 36 | 255 (pad) |

Per-vertex bytes show the pairing directly:

| vertex | weights | joint bytes |
| --- | --- | --- |
| a | 187, 57, 10, 1 | `FF 0E 02 FF  FF 0E 00 FF  FF 0E 00 FF` |
| b | 222, 33, 0, 0 | `25 48 A7 00  25 48 A7 00  24 48 A7 00` |

For vertex a the slots resolve to joints 14, 2, 14, 0, giving joint 14 at weight
187+10, joint 2 at 57 and joint 0 at 1. For vertex b they resolve to 72, 167, 72,
167, giving joint 72 at 222 and joint 167 at 33.

**Conclusion: the joint values are palette indices into the drawable's own bone
list, not directly into the skeleton.** The palette is wider than the skeleton:
raw values reach **255** against a 133-bone skeleton, while the maximum index
actually used by a positive weight is **94**.

Closure applied: influences whose palette index is at or above the skeleton bone
count are dropped and the remaining weights renormalised. Cost, measured:

- dropped influences: **5,753** across **2,894** vertices (19.6% of vertices)
- dropped weight: **721.35** of **14,734.0** total weight units = **4.90%**
- retained weight per vertex after normalisation: exactly 1.0

## 9. Skinned export

One glTF 2.0 binary is emitted per rig, containing the full skeleton, the skin and
the clip channels that resolve.

| property | value |
| --- | --- |
| file size | 773,984 bytes |
| bones | 133 (1 root) |
| vertices / triangles | 14,734 / 16,336 |
| joint index maximum | 94 (limit 133) |
| weight sum range | [1.000000, 1.000000], 0 outside 1e-4 |
| inverse bind matrices | 133, from inverting the bind world matrices |
| node transforms | TRS decomposed from `inverse(parent world) x world` |
| frames / duration | 110 / 3.633333 s |
| animation channels | 38 mapped |

### Known limitation

The clip used is the best available for this rig at **38 of 57** distinct bone ids
(66.67%), not a full bind. No clip in the archive fully binds this rig; its best
is 38/57, so the export is a partial retarget. Because 19 clip bones have no
counterpart, the posed result displaces up to 10.56 m on a 0.5 m mesh, which is
physically wrong. The skin binding itself is verified; the **animation is flagged
unverified** and must not be read as a correct pose. Full-bind clips exist at
51/51 for the other rig, whose drawable carries no skin streams.

## 10. Summary

| item | status |
| --- | --- |
| class-10 clip decode | 94,072 / 94,256 (99.80%), 9,482,698 anchor checks, 0 non-finite |
| skeleton field map | complete, including the affine fourth-row fix |
| dense bone map | 142/142 contiguous indices, capacity probe 512 accepted, 256 and 1024 rejected |
| hierarchy | 10 roots / depth 15 / acyclic (rig A), 1 root (rig B) |
| clip binding by subset | 51/51 on rig A, 1,472 fully bound clips, 4,230,268 pairs total |
| resource pages | zlib and zstd frames, declared page counts honoured |
| vertex attribute split | exact to the byte for two rigs, 56 and 88 bytes per vertex |
| skin weights | 100% of vertices sum to 1.0 after normalisation, 0 failures |
| joint field | closed as palette indices; max used 94 of 133 bones, 4.90% weight dropped |
| skinned glTF | emitted, 133 bones, 14,734 verts, 16,336 tris, IBMs and weights validated |
| clip coverage on the skinned rig | 38/57 (66.67%), animation unverified |
