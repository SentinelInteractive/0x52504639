# `zsm` resources

Status: container and header verified. Array elements and type identity not decoded. No content, asset names, name list or key is published.

## Identity

`zsm` is type code `0x58` from the engine's own type-name table.

- Structural identity, verified: a compact numeric record with a short header, a local bounding box in one header variant, and a set of arrays described by repeated `{pointer, 0, count, capacity}` descriptors.
- Semantic identity, unknown, with a leading hypothesis: an auxiliary per-object shape or simulation record that belongs to a drawable-class asset. That reading is inferred from the asset class of the few matched names, the local-scale coordinates and the array graph. The specific class is not established.

This is the weakest identification in this round and is reported as such. The type name is a tag, not a description.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 39,947 | 659,442,176 | 1,530,627,024 |
| `core_restofworld` | 36 | 140,272 | 246,320 |
| `shared_minigame000` | 36 | 139,152 | 625,984 |
| **Total** | **40,019** | **659,721,600** | **1,531,499,328** |

- Header generation 4 and root generation 4 in all slots. Every slot is a resource entry.
- Name origin: 40,008 unresolved hashes and 11 dictionary matches. The 11 matched slots resolve to drawable-class assets — apparel, a weapon attachment, a prop and a vehicle-side record. The names themselves are not reproduced.
- Logical size: minimum 112 B, median 23,584, p90 131,568, p99 204,880, maximum 1,245,824. Mean 38,269 B.
- Ranges can overlap other indexed resources.

## Container

Each slot is a 16-byte zero prefix followed by a chain of one or two zlib streams. Measured on all 40,019 slots:

- 16 zero bytes at stored offset 0 and `0x78DA` at stored `+0x10`: all slots.
- `logical == sum(inflated stream lengths)`: all slots, no exceptions.
- One stream in 18,888 slots, two in 21,131. No slot has three. 61,150 streams total.
- Of the 21,131 stream-to-stream boundaries, 1,363 carry no padding and 19,768 carry 1–15 bytes to the next 16-byte boundary. Every stream start is 16-byte aligned.
- 37,542 slots end with a zero run between the last stream and the end of the stored range.
- In two-stream slots the first stream is small, about 560–640 bytes, and carries the header; the second carries the bulk. A first stream of about 560 bytes next to a much larger logical size is that split, not truncation.

## Fields

Offsets are relative to the first inflated byte.

| Offset | Width | Observation | Confidence |
|---|---|---|---|
| `+0x00` | u64 | 0 in all slots | verified |
| `+0x08` | u32 | relative pointer, in range in 39,217 of 40,000 scanned slots; most common targets 0x140, 0x1d0, 0x200 | verified |
| `+0x0c` | u32 | 0 in all | verified |
| `+0x10` | u32 | 0 in 38,432 slots; non-zero values are mostly pointer-shaped — a header variant discriminator | verified count, meaning inferred |
| `+0x18` | u32 | 311 distinct values, largest groups around `0x00020000`, `0x00030000`, `0x00038000` | verified value, meaning unknown |
| `+0x1c` | u32 | one constant in 26,662 slots, 0 in 13,198 | verified |
| `+0x20` | u32 | 251 distinct values; largest group 6,841 slots | verified value, meaning unknown |
| `+0x24` | u32 | small integers | verified value, meaning unknown |
| `+0x30`, `+0x34`, `+0x38` | 3 × f32 | min corner of a bounding box in the 8,741-slot variant carrying the box initialisers; min ≤ max on all three axes in that variant | verified for the variant |
| `+0x40`, `+0x44`, `+0x48` | 3 × f32 | max corner of the same box | verified for the variant |
| `+0x50`–`+0x5c` | 4 × f32 | +FLT_MAX in the same 8,741 slots | verified |
| `+0x60`–`+0x6c` | 4 × f32 | −FLT_MAX in the same 8,741 slots | verified |
| `+0x70` | u32 | relative pointer in 23,641 of 40,000 | verified |
| `+0x90`/`+0x94` | u32 | 0 in 40,003 of 40,005 | verified |
| `+0x98`/`+0x9c` | two u32 | count/capacity pair, equal in every observed slot: (0,0) 19,579, (1,1) 3,964, (9,9) 871, (22,22) 746, (20,20) 695 | verified |
| `+0xa0`, `+0xb0` | u32 | relative pointers in 20,046 of 40,005 | verified |
| `+0xa8`/`+0xac` | two u32 | second count pair, mostly 1 | verified |
| `+0xb8`–`+0xcc` | 6 × u32 | hash-like 64-bit words; none matched a name hash in the index | verified values, hash role inferred |
| `+0xe4` | u32 | one constant in 20,046 of 40,005 | verified |
| `+0xec`, `+0xf0`, `+0xf4` | 3 × f32 | 1e−6, 1e6 and 1.0 in about 13,575 slots | verified values, quantisation reading inferred |

Array descriptors are a repeated 16-byte `{pointer, 0, count, capacity}` with count equal to capacity in every observed case; one sample exposes seven of them. The elements behind the pointers are not decoded.

The bounding-box reading is variant-local: unconditioned, min ≤ max holds on only 36,299 of 40,000 slots on the first axis, because other header variants reuse those offsets for pointers. Conditioned on the 8,741 slots that carry the ±FLT_MAX initialiser pair, the box is exact on all three axes.

## Decode

Verified: the container on all slots; header fields through `+0x10c`, with the bounding box fully explained in one variant and the array descriptors decoded. The smallest slot, 112 logical bytes, is accounted for byte for byte — every byte is zero, a relative pointer or a counted field. The meaning of three header words remains unknown even there.

Explanation stops at the first pointed-to array, at a variable offset. This is header plus descriptors, not a semantic payload decode.

## Encode

None. Write status W0.

## Verification

- Whole-census reconciliation reproduces 40,019 slots, 659,721,600 stored and 1,531,499,328 logical exactly.
- Population chain walk: prefix and zlib header on all slots; `sum(inflated) == logical` on all slots; 0 unterminated streams.
- Independent population verifier re-inflates every slot and asserts the prefix, the zlib header, `u64@0 == 0` and the first pointer range: all slots pass.
- Bounding box: the +FLT_MAX group and the −FLT_MAX group are the same 8,741 slots, and min ≤ max on all axes in 8,741 of 8,741.
- Stratified samples from 112 B to 1,245,824 B; every one inflated to exactly the declared logical size.
- Rejected: a scene or placement record; a streaming-map cell; an audio or minigame config table; a text or name table; a collision volume alone.
- Caveat: 8,321 of 40,019 slots contain a printable run of 32 bytes or more, so a text-like region exists in about 21 percent of the population. It does not change the numeric reading of the header, but "no strings anywhere" is not proven.

## Unknowns

1. Element layout behind the array descriptors.
2. The meaning of three header words and three float constants.
3. Whether the hash-like words are name hashes from a table not held locally.
4. The printable region in 21 percent of slots.
5. Any handler or vtable on the executable side.

## Limits

No writer exists. The type identity is inferred, not proven. Nothing here claims the population has been decoded, only the container and the header.
