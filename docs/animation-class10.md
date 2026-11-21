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
