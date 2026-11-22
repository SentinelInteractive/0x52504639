# Animation clips

The clip layer is no longer opaque. The block header, the channel classes and the
64-frame codec validate on real archive data, and one full clip decodes.

## Block header

A `crAnimSequence` block starts with a class table. The header validates exactly:

- 11 channel classes at `+0x1e`
- per-class index tables, 4-aligned, ending precisely at the first data offset
- frame count and stride consistent with the animation header
- `findtag 0DRPz` on the same reader reproduces the census count exactly, which
  confirms the resource walk

Archive-wide on `anim.rpf`, from 128,922 payloads and 11.58 GB uncompressed:

| Measure | Value |
| --- | ---: |
| Valid block headers | 211,888 |
| Streams carrying them | 71,721 |
| Blocks with class-10 channels | 133,309 |
| Class-10 channels | 6,830,891 |

## Class 10

Class 10 is the compressed per-frame codec:

- 64-frame superblocks
- 8 interleaved lanes
- second-order zigzag delta: `vel += acc`, `pos += vel`
- cumulative offsets reset by anchor values at each superblock boundary
- anchors validated by continuity across the boundary

The duration relation is `(frames - 1) / fps`, not `frames / fps`. That resolves an
older discrepancy in the notes.

Other classes mapped from slot-index geometry: static quaternion, static vector3,
static float, per-frame bit-packed quantised, per-frame lookup index, one missing
quaternion component, normalise directive. Class 3 is rare and still undecoded.

## One clip

A 350-frame clip decoded end to end:

| Check | Result |
| --- | --- |
| Frames, header versus block | 350 = 350 |
| Duration | 23.266666 s = 349 / 15 |
| Tracks | 139 |
| Class-10 channels | 334 |
| Anchor checks | 1,670, 0 failures |
| Channel stream end | exact |
| Non-finite values | 0 |
| Quaternion norms | 1.000000 |

Six 64-frame superblocks, 8 lanes, anchor continuity. A local plot of summed
per-frame angular change shows a burst, decay, activity and settle, and the three
sampled frames differ. Bones move.

## Archive-wide decode

| Measure | Value |
| --- | ---: |
| Animations found | 94,256 |
| Decoded completely | 94,072 |
| Success | 99.80 percent |
| Frames | 15,625,840 |
| Tracks | 5,489,352 |
| Anchor checks | 9,482,698, 0 non-finite |

The 184 failures are resource truncation from the extraction window, not format
errors. They need re-extraction, not a decoder change.

## Skeleton link, partial

Clip bone ids are real hashes shared with rig payloads. One rig matched 126 of 136
clip bone ids, 92.6 percent. The dense index mapping is not proven yet, so no
skinned export has been produced. A skeleton struct and a hash-to-index table are
present in the rig payloads and are the next target.

## Status

- Clip decode: working, 99.80 percent of the archive
- Skinning: id-level join only, index mapping open
- Class 3: open
- No animation content, character names or scene names are published


## Skin binding status

This section appends to the class-10 animation work. It records what the skeleton
and vertex layout now prove, and what remains open. It contains no names, no
content, no code and no extracted assets.

### Dense bone map: solved

The skeleton's `+0x20` field points at an open-addressed hash table of 8-byte
rows `{u32 hash, u32 index}`. The table is **not** ordered by index and **not**
ordered by hash; rows sit in probe order and empty slots hold `0xFFFF_FFFF`.

The earlier permutation test failed for two reasons, both now fixed:

- the table's capacity is larger than the bone count, so a bone-count-sized
  window leaves holes;
- two rows can alias one bone (a name hash and a bone id), so the non-empty row
  count exceeds the bone count.

Capacity was detected rather than assumed, by requiring the smallest power of
two whose rows resolve to exactly `n` distinct indices covering `0..n-1`:

| window rows | non-empty rows | distinct indices | holes | verdict |
| --- | --- | --- | --- | --- |
| 256 | 122 | 95 | 47 | rejected |
| 512 | 283 | 142 | 0 | accepted |
| 1024 | 503 | 142 | 142 | rejected (rows out of range) |

Result on the reference rig: 142 bones, 142 distinct indices covering `0..141`
with zero holes, 370 empty rows in a 512-row window. The dense map is a real
`0..n-1` set, not just set overlap.

Skeleton field map derived from bytes, all confirmed on the reference rig:

| field | content |
| --- | --- |
| `+0x20` | `{hash, index}` table, 512-row window |
| `+0x38` | bind records, 64 bytes each, 3x4 affine with translation in column 4 |
| `+0x40` | `u16` parent array, `0xFFFF` root; 10 roots, maximum depth 15, no cycles |
| `+0x48` | variable-length name/hash table |
| `+0x6c` | bone count, followed by a six-entry `u16` count/max chain |

### Clip binding: solved

Bone ids are hashes, so binding is a table lookup, not a geometric fit. Matching
was scored by subset: a clip binds to a rig only when **every** distinct bone id
in that clip resolves in the rig's dense map.

- One archive of 127,589 payloads yields 2,791 rigs with a complete dense map.
- Against 68,237 animations, 4,230,268 fully-resolving rig/clip pairs were found
  in 4.5 s (932k pairs/s).
- The reference rig (142 bones) binds 1,472 clips completely. Its best clip
  resolves **51 of 51** distinct bone ids over 330 frames and 10.967 s.
- No rig in that archive fully binds more than 60 ids. A 136-id clip therefore
  belongs to a rig outside it; it was not forced and its 75% overlap is not
  reported as a binding.

### Resource pages: solved

A resource is a chain of compressed frames at one archive offset. The block map
at `+0x08` declares the virtual and physical page counts, and the physical page
holds vertex and meshlet buffers under `0x60xxxxxx` physical pointers. The frame
codec must be sniffed per frame: the measured build stores these resources as
zlib, while an intermediate store re-compressed the same payloads as zstd. Both
paths are implemented, read frame by frame, and stop at the declared page count.

For the reference rig the chain is one virtual page (63,088 bytes) followed by
one physical page; decoding the pair reproduces the drawable's geometry.

### Vertex attribute split: solved

The earlier claim that six descriptors do not tile the stride was an arithmetic
error. Offsets follow the form `(word >> 8) << 1` and, measured against the
vertex count, every stream tiles exactly:

| rig | bytes/vertex | strides | product check |
| --- | --- | --- | --- |
| A (142 bones) | 56 | 8, 8, 8, 8, 4, 20 | 48,982 x 56 = 2,743,120 = declared buffer |
| B (133 bones) | 88 | 8, 12, 12, 4, 36, 4, 12 | 14,734 x 88 plus 128-byte header = declared buffer |

Descriptor 0 is always position, tag `0x42`, 8 bytes per vertex. Tags repeat
across attributes, so a tag alone never determines layout; stride comes from the
gap to the next stream offset.

### Skin weights: validated

On rig B, one 4-byte stream carries four `unorm8` weights. Over all 14,734
vertices of its single level-0 geometry:

- every vertex sums to the full unorm range (255 +- 3): pass fraction **1.0000**
- weight sum minimum and maximum both **1.0000**
- vertices failing the sum test: **0**

### Joint indices: partially resolved

The joint field is not yet proven, and no joint claim is published.

On rig B the 12-byte `0x26` stream reads as three 4-byte groups of the form
`[0xFF][index][second][0xFF]`. Treated as `4 x u8` with `0xFF` meaning unused,
95.14% of vertices satisfy "every non-`0xFF` byte is below the bone count". That
is far above chance, so the field really does hold joint indices, but 4.86% of
vertices are not explained by a single reading.

Byte-position statistics narrow it down: the first index position in each group
has only 7 distinct values, all at or below 30, in 100% of vertices. The second
position reaches values up to 158 against a 133-bone skeleton, which indicates an
index into a wider palette rather than directly into the skeleton, or a different
sub-field. Resolving that is the remaining work.

### Skinned export: pending

A skinned glTF has not been emitted, because emitting one requires joint indices
that pass, and they currently pass at 95.14% as a stream. Publishing an export
built on a partially decoded influence field would misrepresent it.

### Summary

| item | status |
| --- | --- |
| dense bone map | yes, 142/142 contiguous indices |
| capacity probe | yes, 512 accepted, 256 and 1024 rejected |
| parent array and hierarchy | yes, 10 roots, depth 15, acyclic |
| clip binding by subset | yes, 51/51 ids on the reference rig |
| resource page chain | yes, zlib and zstd frames, declared page count honoured |
| vertex attribute split | yes, exact per-stream strides for two rigs |
| skin weights | yes, 100% of vertices sum to 1.0 |
| joint indices | partial, 95.14% stream-level |
| skinned export | pending the joint field |
