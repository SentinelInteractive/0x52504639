# `zsp` resources

Status: container and hash-table structure decoded. Token and key semantics not decoded. No content, asset names, name list or key is published.

## Identity

`zsp` is type code `0x64` from the engine's own type-name table.

- Structural identity, verified: a hash table. A 32-bit key maps to a dense `0..N−1` index, stored in a power-of-two bucket array of 0x110-byte buckets, sixteen key/value pairs per bucket, with a 16-byte token field at the head of each bucket and one 32-bit flag word per entry.
- Semantic identity, inferred: a per-resource index structure attached to navigation content. Every slot lives in `navmeshes.rpf`, the header declares its own entry count, and no coordinates, polygons or material records appear anywhere in the decoded regions.

A "shader" reading of the tag is unsupported: the archive holds navigation content and the payload has no shader-shaped structure.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `navmeshes.rpf` | 27,482 | 376,513,072 | 2,325,782,256 |
| **Total** | **27,482** | **376,513,072** | **2,325,782,256** |

- Header generation 4 and root generation 4 in all slots. Every slot is a resource entry.
- Name origin: all 27,482 slots are unresolved hashes. This type has no resolved name anywhere in the index, so no name-level cross-check is possible for it.
- Logical size: minimum 2,656 B, median 41,904, p75 131,072, p90 196,608, p99 327,680, maximum 649,440. Mean 84,629 B.
- The mean is twice the median; the 84 KiB figure that circulated early in this study is the mean, not the median. The distribution concentrates at a few exact sizes, which matches a table whose size is driven by entry and bucket counts rather than by content volume.
- Eleven archive headers hold these slots, and none is shared with the `0x4f` tiles in the same archive.

## Container

Each slot is a 16-byte zero prefix followed by one zlib stream, or rarely two. Measured on all 27,482 slots:

- 16 zero bytes at stored offset 0 and `0x78DA` at stored `+0x10`: all slots.
- `logical == sum(inflated stream lengths)`: all slots, no exceptions.
- One stream in 27,476 slots, two in 6. There is almost no chaining: the payload is one continuous buffer.
- All six stream-to-stream boundaries carry padding, each to the next 16-byte boundary.
- 26,597 slots end with a zero run between the last stream and the end of the stored range.

## Fields

Offsets are relative to the first inflated byte.

| Offset | Width | Observation | Confidence |
|---|---|---|---|
| `+0x00` | u64 | 0 in all slots | verified |
| `+0x08` | u32 | relative pointer to a 16-byte tail header, in range in all slots | verified |
| `+0x0c` | u32 | 0 in all | verified |
| `+0x10` | u32 | bucket count, a power of two: 8 in 12,778 slots, 256 in 7,131, 512 in 6,263; nine distinct values from 8 to 2,048 | verified |
| `+0x14` | u32 | entry count N; equals `+0x50` in 300 of 300 sampled slots | verified |
| `+0x18` | u32 | one constant: the bucket array always starts at offset 0x60 | verified |
| `+0x1c` | u32 | 0 in all | verified |
| `+0x20` | u32 | relative pointer to the flag array, which follows the bucket array | verified |
| `+0x24` | u32 | 0 in all | verified |
| `+0x28`, `+0x2c`, `+0x30` | 3 × u32 | the same power-of-two value in every slot: 128, 256, 512 or 1,024 | verified values, meaning unknown |
| `+0x34` | u32 | 24,480 distinct values in a narrow band; never a valid in-buffer pointer | verified value, meaning unknown |
| `+0x38`, `+0x3c` | 2 × u32 | 0 in all | verified |
| `+0x40`, `+0x44` | 2 × f32 | fixed-point extents | verified values, meaning unknown |
| `+0x48` | u32 | 0 in 16,826 slots, otherwise one of seven values | verified value, meaning unknown |
| `+0x50` | u32 | duplicate of the entry count N | verified |
| `+0x54`–`+0x5c` | 3 × u32 | 0 in all | verified |
| `0x60` | — | start of the bucket array, `bucket_count × 0x110` bytes | verified |
| after buckets | — | flag array, one 32-bit word per entry, rounded up to four | verified |
| after flags | — | tail; its first 16 bytes are a tail header, the rest is mostly zero | inferred |

Bucket layout, verified on complete payloads and a 300-slot sample:

- 0x110 bytes = a 16-byte token field plus sixteen `(64-bit key, 64-bit value)` pairs.
- `(flag_offset − 0x60) / 0x110` is an exact integer in every parsed sample, which fixes the stride.
- Keys are 32-bit-wide values stored in eight bytes; values are a dense `0..N−1` index. Keys and values are distinct within a slot.
- The token field is a byte array terminated by the first byte with the high bit set, normally `0x80`, with the remainder of the 16 bytes also `0x80`. There is no NUL terminator and no length prefix. Token lengths run 4 to 16 bytes.
- The token array length equals the number of populated pairs in the same bucket, with zero mismatches on 300 sampled slots. Total token bytes equal the pair count and the header's entry count.

Smallest-slot accounting, complete: 2,656 bytes = 96-byte header + 8 buckets × 0x110 + 88 flag words + 32-byte tail. The same identity reproduces a 41,904-byte slot and a 649,440-byte slot.

There is no text in this type: no payload contains a printable run of 32 bytes or more, and the longest run in any slot is under 32. An earlier "ASCII-bearing" count was a weak test that counted printable bytes rather than words.

## Decode

Verified on all slots for the container, and on complete payloads plus a 300-slot sample for the structure: the 0x60-byte header including bucket count, entry count, bucket-array offset, flag-array pointer and the duplicate count; the bucket array at its declared stride; the key/value pairs; the token fields; and the flag array. The smallest slot is accounted for byte for byte.

Explanation stops at the meaning of the token byte, the meaning of the three power-of-two words and the trailing payload beyond its 16-byte header. The layout is decoded; the semantics are not.

## Encode

None. Write status W0. A writer would need the key namespace and the token semantics.

## Verification

- Whole-census reconciliation reproduces 27,482 slots, 376,513,072 stored and 2,325,782,256 logical exactly.
- Population chain walk: prefix and zlib header on all slots; `sum(inflated) == logical` on all slots; stream histogram as above; 0 unterminated streams.
- Independent population verifier re-inflates every slot and asserts the prefix, the zlib header, `u64@0 == 0` and the first pointer range: all slots pass.
- Printable-run scan over every inflated payload: zero slots with a run of 32 bytes or more. This is the cleanest negative text result in the round.
- Structural parse: 300 of 300 sampled slots agree on token bytes = pair count = header entry count, and per-bucket pair length = bucket token count with zero mismatches.
- Samples: 2,656 B (smallest and modal floor), 41,904 B (median), 131,072 B, 649,440 B (largest). All inflated to exactly the declared logical size.
- Rejected: a chain with many streams; readable names in the token field (about 29 percent of token bytes are in `[a-z0-9_]` and about 25 percent are control bytes); a shader or material table; a shared header with the `0x4f` tiles; coordinates or polygon records in the decoded regions.

## Unknowns

1. The semantics of the token byte and the flag word per entry.
2. Whether the keys are name hashes, object IDs or another namespace. The type has no resolved names, so this cannot be tested from the index.
3. The meaning of the power-of-two triple and the distinct counter word.
4. The tail payload beyond its 16-byte header.
5. Any handler or vtable on the executable side.

## Limits

No writer exists. The keys do not resolve to names. Nothing here claims the population has been decoded, only the header, bucket array, tokens and flags.
