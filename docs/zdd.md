# `zdd` resources

Status: container layer, root header and naming layer verified. Wrapped objects not decoded. No content, asset names, name list or key is published.

## Identity

`zdd` is type code `0x04` from the engine's own type-name table. The label is a three-letter tag and does not establish what the payload represents, so the identity below comes from the payload.

- Structural identity, verified: a small fixed header, a name region, a hash/object region and a pointer array, followed by a payload. Entries are named with a lower-snake-case identifier that ends in a dot plus a two-character type tag.
- Semantic identity, inferred: a container for named sub-resources. Each slot wraps one to sixteen named objects, and the type tag on the name is the same tag the executable uses for a resource type. What the wrapped objects are is not decoded.

A "dictionary" reading is consistent with the measured structure — a name table, an object table and matched count pairs — but this page claims only the structure, not a class name.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 24,423 | 2,683,898,560 | 5,874,261,856 |
| `levels.rpf` | 22,379 | 3,444,182,880 | 8,405,092,080 |
| `story000` | 890 | 152,789,600 | 233,949,472 |
| `core_restofworld` | 796 | 20,692,976 | 46,425,216 |
| `shared_minigame000` | 81 | 6,435,856 | 14,019,056 |
| `data.rpf` | 14 | 1,496,032 | 3,242,432 |
| `story000_restofworld` | 1 | 46,560 | 67,088 |
| **Total** | **48,584** | **6,309,542,464** | **14,577,057,200** |

- Header generation is not uniform: 4 in 23,788 slots, 5 in 19,185, 8 in 5,611. Root generation is 4 in all slots. Every slot is a resource entry.
- Name origin: 41,520 unresolved hashes and 7,064 dictionary matches. The matched names are not reproduced.
- Logical size: minimum 1,808 B, median 65,120, p90 652,624, p99 4,342,352, maximum 30,143,664. Mean 300,036 B.
- Ranges can overlap other indexed resources; distinct physical payloads are not established by these totals.

## Container

Each slot is a 16-byte zero prefix followed by a chain of up to six zlib streams. Measured on all 48,584 slots:

- 16 zero bytes at stored offset 0 and a zlib header `0x78DA` at stored `+0x10`: 48,584 of 48,584.
- `logical == sum(inflated stream lengths)`: 48,582 of 48,584. The 16-byte prefix sits outside `logical`, and the padding between streams is stored-side only.
- This type has the deepest chains measured in this round: two streams in 33,222 slots, three in 13,887, four in 1,464, five in 9, six in 2 — 114,018 streams.
- Inter-stream padding is 0 to 15 bytes to the next 16-byte boundary. Of 65,434 boundaries, 3,942 carry no padding and 61,492 carry 1–15 bytes.
- 45,361 slots end with a zero run between the last stream and the end of the stored range.
- Two slots are short by exactly 48 bytes each and end with a short non-zlib tail. Both are header generation 8. The cause is not established.

Stored accounting is `stored = 16 + sum(compressed extents) + sum(padding) + trailing`.

## Fields

Offsets are relative to the first inflated byte; integers are little-endian.

| Offset | Width | Observation | Confidence |
|---|---|---|---|
| `+0x00` | u64 | 0 in all slots | verified |
| `+0x08` | u32 | relative pointer `0x50000000 + offset`, in range in all slots; target is the name region | verified |
| `+0x0c` | u32 | 0 in all | verified |
| `+0x10` | u64 | 0 in all | verified |
| `+0x18` | u64 | 1 in all | verified |
| `+0x20` | u32 | relative pointer, in range in all slots; target holds 64-bit values and floats | verified pointer, role inferred |
| `+0x28` | u32 | two equal u16 halves in all slots; 108 distinct values; most common 1/1 in 29,141 slots, 4/4 in 12,876, 2/2 in 1,986, 16/16 in 898, 3/3 in 650 | verified values, count/capacity reading inferred |
| `+0x2c` | u32 | 0 in all | verified |
| `+0x30` | u32 | relative pointer, in range in all slots; target is an array of relative pointers | verified |
| `+0x34` | u32 | 0 in all | verified |
| `+0x38` | u32 | identical to `+0x28` in all slots | verified |
| `+0x3c` | u32 | 0 in all | verified |
| `+0x40` | variable | payload; no stable field schema found | verified undecoded |

Name region, from the `+0x08` target: the same paired-u16 shape as the root, then one to four inline NUL-terminated strings of 19–30 printable characters in lower snake case with digits and a final dot plus a two-character tag. In the sample with eight entries the strings are replaced by an array of relative pointers, so names can be indirect. The two-character tag matches the executable's label variant for the drawable type in the sample inspected. A type tag on a name is the expected shape for a container of typed objects.

48,576 of 48,584 slots contain a printable run of eight or more characters; 28,133 contain a run of 32 or more, the threshold at which a run stops being explainable as binary noise. The remaining 20,451 slots are numeric only at that threshold.

Object side: an array of 64-bit relative pointers whose count does not equal the header pair in the samples tested (4 pointers for a count of 1 or 4, 3 for a count of 3, 16 for a count of 8). The population relationship is not established.

An earlier reading of the paired words near `+0x40` as a hash/offset table was tested and rejected: of 32,945 slots with at least two such pairs, only 202 show a monotone second word, and 62,423 distinct first words appear.

## Decode

Verified on all 48,584 slots: the container; the 0x40-byte root header field by field, including three relative pointers that resolve in every slot; and the matched u16 pairs. Verified on fully inflated stratified samples: the name region, including its per-table pair and the inline or indirect name forms.

Explanation stops at byte `0x40`, the start of the payload, and at the object layout behind the pointer array. The header and the naming layer are decoded; the objects are not.

## Encode

None. Write status W0, extract-only.

## Verification

- Whole-census reconciliation in Rust reproduces the slot and byte totals exactly, and the package totals 305,820,985,968 stored and 564,783,265,279 logical.
- Population chain walk: `sum(inflated) == logical` on 48,582 slots; stream histogram as above; 0 unaligned stream starts.
- Population verifier re-inflates every slot and asserts the prefix, the zlib header, `u64@0 == 0` and the `+0x08` pointer range: all pass on 48,584 of 48,584.
- Literal scan over every inflated payload: the nested-archive signature `0DRPz` in 0 slots, `RPF9` in 2 slots, the 8-byte inner schema pair in 0 slots. This type is not a nested archive in general.
- Stratified samples: minimum 1,808 B, median 65,120 B, maximum 30,143,664 B, plus one slot per root. All inflated to exactly the declared logical size.
- Rejected: nested archive wrapper; inner schema pair; a paired-word hash table; a count pair with unit capacity.

## Unknowns

1. The layout of the objects behind the pointer array, and whether the name tag identifies their type.
2. The rule that sets the pointer count against the header pair.
3. The 48-byte shortfall in the two generation-8 exceptions.
4. The proportion of slots with a structurally valid name table, as opposed to printable bytes somewhere.
5. Any handler or vtable on the executable side.

## Limits

No writer exists. No object payload is interpreted. Nothing here is a claim that the population has been decoded, only that the container, header and naming layer have.
