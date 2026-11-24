# `znv` resources

Status: container, tile header, node hierarchy and mesh arrays located. Vertex semantics not decoded. No content, asset names, name list or key is published.

## Identity

`znv` is type code `0x4f` from the engine's own type-name table. It is one of a navigation family of codes in the same labelling block.

- Structural identity, verified: a tile record with an identity transform, a tile scale, a node hierarchy of 0x60-byte nodes carrying box corners in whole metres, and a footer that declares a vertex array and a 16-bit index array.
- Semantic identity, inferred: a navigation-mesh tile. The node corners are integer metre coordinates spaced 256 m apart with a constant height term, and the index array's maximum equals the vertex count minus one, which describes a closed mesh, tiled.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `navmeshes.rpf` | 27,644 | 5,398,485,440 | 15,420,757,856 |
| **Total** | **27,644** | **5,398,485,440** | **15,420,757,856** |

- Header generation 4 and root generation 4 in all slots. Every slot is a resource entry.
- Name origin: 27,585 unresolved hashes and 59 dictionary matches. The matched names are not reproduced.
- Logical size: minimum 1,136 B, median 132,912, p75 720,896, p90 1,769,472, p99 3,485,456, maximum 7,733,248. Mean 557,834 B.
- This is the heaviest type in this round: 15.4 GB logical from 27,644 slots, and a quarter of the population above 720 KiB. The modal size class, 132,912 B, covers more than half the population.
- Twelve archive headers hold these slots: ten with 2,448 slots each, one with 3,002 and one with 162.

## Container

Each slot is a 16-byte zero prefix followed by one or two zlib streams. Measured on all 27,644 slots:

- 16 zero bytes at stored offset 0 and `0x78DA` at stored `+0x10`: all slots.
- `logical == sum(inflated stream lengths)`: all slots, no exceptions.
- One stream in 4,598 slots, two in 23,046. 50,690 streams total.
- Of the 23,046 stream-to-stream boundaries, 1,512 carry no padding and 21,534 carry 1–15 bytes to the next 16-byte boundary. Every stream start is 16-byte aligned.
- 26,907 slots end with a zero run between the last stream and the end of the stored range.
- Stream count does not track size: the largest slot is a single stream while a modal slot is two. In two-stream slots the first stream ends on a 64 KiB multiple of output, so the split follows virtual page boundaries rather than a fixed byte budget.

## Fields

Offsets are relative to the first inflated byte.

| Offset | Width | Observation | Confidence |
|---|---|---|---|
| `+0x00` | u64 | 0 in all slots | verified |
| `+0x08` | u32 | relative pointer `0x50000000 + offset`, in range in full payloads | verified |
| `+0x10` | u32 | variant discriminator: 9 in 18,791 slots, 11 in 5,507, 3 in 3,149, 7 in 161, 1 in 35 | verified value, meaning unknown |
| `+0x14` | u32 | one constant in all 27,644 slots | verified |
| `+0x18` | u64 | 0 in all | verified |
| `+0x20`–`+0x4c` | 12 × f32 | identity 3 × 4 matrix; the 1.0 word present in every slot and the rest zero | verified bytes, transform reading inferred |
| `+0x60`, `+0x64` | 2 × f32 | 128.0 in 27,482 slots; the 162 slots of the smallest header carry other values | verified |
| `+0x68` | f32/u32 | 0 in about two thirds of sampled slots, otherwise small values | verified value, meaning unknown |
| `+0x6c` | u32 | 0 in all | verified |
| `+0x70` | u32 | relative pointer to the footer descriptor table, in range in 200 of 200 full payloads | verified |
| `+0x80`, `+0x88`, `+0x98` | u32 | further descriptor pointers, all in range in 200 of 200 | verified |
| `+0x90` | u32 | array count, modal value 4,352 in 15,461 slots | verified |
| `+0xa0` | u32 | pointer to a 0x60-byte-stride node array | verified |
| `+0xa8`, `+0xb0`, `+0xb8` | u32 | zero in about two thirds of sampled slots, otherwise valid pointers | verified |
| `+0xc0`, `+0xc4` | two u32 | counts, modal 1,089 and 1,152 in the same 15,461-slot family | verified values, meaning inferred |
| `+0xc8`, `+0xcc` | two u32 | counts or sizes, modal 148,128 and 118,150 in that family | verified values, meaning unknown |
| `+0xe8` | u32 | one constant in 24,474 slots | verified |
| other words | u32 | `+0x04`, `+0x0c`, `+0x1c`, `+0x24`–`+0x5c`, `+0x74`–`+0x7c`, `+0x84`–`+0x8c` are 0 in sampled full payloads | verified |

Declared structure, from a modal-size slot:

- The footer declares two arrays at 16-byte stride: a vertex array with 1,089 elements of 12 bytes, and an index array with 4,352 `u16` values.
- The index array's maximum is 1,088 and it holds 1,089 unique values — exactly the vertex count range, so the pair closes as a mesh. 1,089 = 33 × 33.
- The 12-byte vertex element has a strong 12-byte periodicity and six 16-bit slots, including `0xffff` sentinels. It is not a float triple; float triples live in the 0x60-byte node records instead.
- Node records are 0x60 bytes: two float pairs plus a constant 0.35, with corner pairs in integer metre magnitudes 256 apart, the tile granularity.
- Footer mask words follow the array descriptors. Their meaning is unknown.

## Decode

Verified: the container on all slots; the root header through `+0x10c`, including the footer pointer, the discriminator, the identity matrix, the tile scale and five descriptor pointers, byte-checked on a 200-slot stratified sample. A mesh walk enumerates the footer `(pointer, count)` entries and accepts a pair when the vertex span `pointer + count × 12` and the index span `pointer + count × 2` fit the buffer and every `u16` index is below the vertex count. It succeeds on 138 of 200 sampled slots.

Explanation stops at the footer mask words, at the interior of the node records, and at the six 16-bit fields of each vertex element. The 62 walk failures are concentrated in the largest slots, whose footers expose fewer aligned pairs — a gap in the walker, not evidence about the format.

## Encode

None. Write status W0.

## Verification

- Whole-census reconciliation reproduces 27,644 slots, 5,398,485,440 stored and 15,420,757,856 logical exactly.
- Population chain walk: `sum(inflated) == logical` on all slots; stream histogram as above; 0 unterminated streams; 0 unaligned stream starts.
- Independent population verifier re-inflates every slot and asserts the prefix, the zlib header, `u64@0 == 0` and the first pointer range: all slots pass.
- Field population histograms over all slots confirm the constant words and the tile-scale group.
- Stratified samples from 1,136 B to 7,733,248 B; every one inflated to exactly the declared logical size.
- Rejected: that this type is the sibling `0x64` in the same archive at another level of detail (different header shape, zero shared header offsets, different size distribution, different arrays); that the big array is a float triple array; that the index count is a multiple of four.
- An early chain-walking tool capped its output at the declared logical size minus 16 and produced a spurious "inflates to logical minus 16" reading. It has been fixed and the claim withdrawn.

## Unknowns

1. The semantics of the six 16-bit fields per vertex element and the quantisation scale to metres.
2. The footer mask words and the 1–15 trailing stored bytes.
3. The node-record fields beyond the corners and the four child pointers. Resolve by walking parent to child inside one tile.
4. The footer layout for large slots, where the current walker fails on 62 of 200 samples.
5. Any handler or vtable on the executable side.

## Limits

No writer exists. No rendered navigation imagery is included, by policy. Nothing here claims the population has been decoded, only the tile header, node hierarchy and mesh arrays.
