# zbft fragments

Status: container, virtual root and body header verified on every slot. Leaf references partly decoded. Node records and geometry not decoded. No content, asset or name list is published.

## Identity

`zbft` is type code `0x11` from the engine's own type-name table. The label is a three-letter tag and does not establish what the payload is, so the identity below comes from the payload and from the engine's own store registration.

- Store registration, verified: the engine registers this type word with a store whose class name states a fragment-level BVH, in the same registration batch as the drawable BVH store and the smaller drawable-index store. The literal type word is confirmed by 27 sibling registrations.
- Structural identity, verified: two compressed streams, a small virtual-root stream and a body whose entries are addressed by `0x50000000`-relative virtual pointers. A 32-bit tag appears exactly once in every payload, the node region has a declared extent whose record layout is undecoded, and the root reference's low three bits select box versus triangle.
- Format identity, inferred: the tag, the 64-byte stride and the box/triangle discriminator match the drawable BVH layout measured earlier in this project. Reading this as a serialised bottom-level acceleration structure is an inference from that structural match, not a vendor-specification lookup.

Companion relation, verified as a population statement: 22,438 of 22,440 slots share their name hash with a type `0x03` fragment slot, 99.99 percent, the same base-versus-companion pattern the drawable and its BVH follow. No numeric field correlates between the two sides, so the build derivation is unproven.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `core_bvh4` | 22,430 | 414,695,840 | 6,731,696,832 |
| `shared_minigame000_bvh4` | 10 | 76,928 | 1,646,368 |
| **Total** | **22,440** | **414,772,768** | **6,733,343,200** |

- Every slot is a resource entry; every root and every containing header has generation 4. The population sits in 263 distinct headers.
- Name origins: 21,356 dictionary matches and 1,084 unresolved hashes; all 22,440 name hashes are distinct.
- Size distribution: stored 160 / 560 / 2,448 / 7,120 / 50,336 bytes at min / p25 / p50 / p75 / p95, maximum 1,686,432; logical 720 / 5,840 / 32,976 / 131,280 / 786,688, maximum 26,870,112.
- The logical-to-stored ratio runs 3.812 to 38.682 with a median of 14.428, the highest in this project.

## Container

Verified on all 22,440 slots.

- Sixteen zero bytes at stored offset 0; a zlib stream head at stored `+0x10` in every slot.
- Exactly two streams per slot. The second begins at the next 16-byte-aligned stored offset; the gap is 0 to 15 bytes, never more.
- `logical == sum(inflated)` on 22,440 of 22,440 slots, with zero inflate errors. The sixteen stored zero bytes are outside `logical` for this type, unlike the older fragment type which counts them inside.
- The first stream is not a fixed size: 208 bytes in 20,552 slots, 256 in 1,395, 352 in 244, 544 in 245, 400 in 2, then two singletons. A reader that assumes a constant 208-byte header is wrong for 1,888 slots.

## Fields

Offsets relative to the inflated payload, little-endian.

| Field | Observation | Confidence |
|---|---|---|
| virtual root `+0x20` | `0x60000000` in all 22,440 slots — a tagged word, not a pointer | Measured |
| virtual root `+0x28` | virtual pointer with seven values whose frequencies equal the seven first-stream length classes | Measured; it locates the block map |
| virtual root `+0x38` | `0x50000050` in all slots | Measured |
| body tag | one 32-bit tag per payload, at a position fixed by the virtual-root field | Verified |
| body extent | equals the root pointer plus `0x100` in all 22,440 slots | Verified |
| node region extent | declared node-region extent: `64 * (count + 1)` bytes on all 22,440 slots. The inflated body is larger than this on all slots, so it is a region bound, not the body size. The record layout inside the region is undecoded; four pre-declared layout tests were refuted. | Measured; layout undecoded |
| root reference | low three bits are box-shaped in 22,439 slots and triangle-shaped in the single smallest slot | Measured; discriminator reading inferred |
| leaf table | columnar entries with a 2,048-entry group size and a 0x20000 group stride; the largest slot decodes 15,970 leaves | Measured |

## Decode

Per layer:

- Container: decoded and verified on all slots.
- Virtual root and body header: decoded and verified, including three identities that hold on 100 percent of the population.
- Leaf references: partly decoded, 20,576 of 22,440 slots under a bounded read; the other 1,864 are not claimed.
- 64-byte node records: not decoded. The array size and stride are verified; a box or parent node's contents are not.
- Geometry: not decoded. No vertex, index or triangle was read out.

Negative results, measured: a constant 208-byte header (false for 1,888 slots); the `0x60000000` word read as a pointer (no in-range target); a numeric correspondence with the base fragment type over 22,438 pairs (match rates 0.01 to 7.39 percent, consistent with chance).

## Encode

No encoder, no pack-back test and no game-load test exists. Write status W0, and the weakest one in this project: with the node records and leaf columns unresolved, even a re-emitter of the measured fields would not produce a loadable structure.

## Unknowns

- The contents of the 64-byte node records and the parent table.
- The rule that decides the first-stream length across its seven classes.
- The 1,864 slots whose leaf decode failed.
- How the structure is derived from its base fragment twin, given that no field correlates.
- The builder path. A builder library sits beside the archives but was not analysed.

## Method and limits

Rust release binaries, offline, no Python. Container checks and field profiles run over the whole population; the leaf-decode figure is the success rate of a bounded read and is reported as such. The engine executable is read as a data file and never run. No key material is involved in this type. Private and unpublished: any payload, any extracted data, resolved names, per-slot offsets and archive paths.
