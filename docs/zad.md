# `zad` resources

Status: container and clip header verified. Channel record array not decoded. No content, asset names, name list or key is published.

## Identity

`zad` is type code `0x4e` from the engine's own type-name table.

- Structural identity, verified: one resource record per slot, carrying a single NUL-terminated name, a literal `.anim` token, and long runs of numeric track data. It is a single-object record, not a table of many objects.
- Semantic identity, inferred: an animation-clip payload — one named clip per slot with float track data and monotone counters. The alternative readings tested (metadata table, placement dictionary, localisation blob) are inconsistent with the measured content.

The word "dictionary" in the working note is not supported by the payload: there is one clip object per slot, not a keyed set.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `story000` | 25,341 | 1,263,722,656 | 1,700,950,704 |
| `story000_restofworld` | 267 | 11,582,112 | 16,147,584 |
| **Total** | **25,608** | **1,275,304,768** | **1,717,098,288** |

- Header generation 4 and root generation 4 in all slots. Every slot is a resource entry.
- Name origin: 25,483 unresolved hashes and 125 dictionary matches. The 125 matched names are one per slot; they are not reproduced.
- Logical size: minimum 688 B, median 10,928, p75 56,672, p90 196,608, p99 654,048, maximum 1,860,256. Mean 67,053 B.
- No slot has stored bytes greater than or equal to logical bytes.
- Four slots resolve to names ending in the executable's variant label for the drawable type. They are ordinary members of the population by size and layout.

## Container

Each slot is a 16-byte zero prefix followed by a chain of zlib streams. Measured on all 25,608 slots:

- 16 zero bytes at stored offset 0 and `0x78DA` at stored `+0x10`: all slots.
- `logical == sum(inflated stream lengths)`: 25,606 of 25,608. The 16-byte prefix and the padding between streams are outside `logical`.
- One stream in 21,876 slots, two in 3,732. No slot has three.
- Of the 3,732 stream-to-stream boundaries, 253 carry no padding and 3,479 carry 1–15 bytes to the next 16-byte boundary. Every stream start is 16-byte aligned.
- 24,009 slots end with a zero run between the last stream and the end of the stored range.
- Two slots are short by exactly 16 bytes against the declared logical size. Both are ordinary by every other measure. The shortfall is unexplained; a page-boundary or footer accounting artefact is a hypothesis, not a finding.

Stored accounting is `stored = 16 + sum(compressed extents) + sum(padding) + trailing`.

## Fields

Offsets are relative to the first inflated byte.

| Offset | Width | Observation | Confidence |
|---|---|---|---|
| `+0x00` | u64 | 0 in all slots | verified |
| `+0x08` | u32 | relative pointer, resolves inside the buffer in all slots; target is a named record | verified |
| `+0x10`–`+0x30` | 8 × u32 | zero in all slots | verified |
| `+0x38` | u32 | relative pointer; its target begins with a NUL-terminated printable string in all slots | verified |
| `+0x40` | u16 | count 24–64, 41 distinct values | verified value, meaning unknown |
| `+0x42` | u16 | equals `+0x40` plus one in all slots | verified |
| `+0x44` | u32 | 1 in all slots | verified |
| `+0x48` | u32 | relative pointer, resolves in all slots | verified |
| `+0x50` | u32 | one of two values: 11 in 25,567 slots, 29 in 41 | verified value, meaning unknown |
| `+0x54` | u32 | 0 in all | verified |
| `+0x58` | u32 | small count 1–21; 1 in 18,999 slots, 2 in 3,874, 3 in 1,342 | verified value, meaning unknown |
| `+0x5c` | u32 | one constant in all slots | verified |
| `+0x60` | u64 | 0 in all | verified |
| `+0x68` | u32 | one distinct value per slot | verified value, hash role inferred |
| `+0x6c` | u32 | 0 in all | verified |
| `+0x70` | u32 | high entropy, 288 zeros, otherwise long tail | verified value, role unknown |
| `+0x74`–`+0x8c` | u32 ×7 | mixed small offsets and hash-like words | verified values, meaning unknown |
| `≥0x90` | floats / u16 | 113,943 words equal 1.0 population-wide; quaternion-like constants such as 0.707107 appear; repeated records of about 0x48 bytes begin near 0x148 in the median sample | verified values, record layout inferred |

The frame-count, duration and frame-rate triple that an animation format normally carries was searched for and not found at any population-stable offset: no fixed 32-bit word among the header fields holds 24, 30 or 60. Frame-rate tokens in the strings occur 0, 1 and 0 times across the population.

## Decode

Verified on all slots by one walk: the container; the 0xC0-byte root header including the three relative pointers, the count/capacity pair with capacity equal to count plus one, the version word and two constants; and the name string at the third pointer, at least one printable NUL-terminated string per slot.

Explanation stops at 0xC0, where the per-channel record array begins. No record stride has been established, so no clip can be walked to its end. This is a partial decode: the container and the root record, not the animation data.

## Encode

None. Write status W0, extract-only. The obstacle is not the container, which is ordinary zlib, but the clip record layout.

## Verification

- Whole-census reconciliation in Rust reproduces 25,608 slots, 1,275,304,768 stored and 1,717,098,288 logical exactly.
- Population chain walk: `sum(inflated) == logical` on 25,606 slots; stream histogram 1→21,876 and 2→3,732; zero unaligned stream starts.
- Independent population verifier re-inflates every slot and asserts the prefix, the zlib header, `u64@0 == 0` and the first pointer range: all slots pass.
- Literal scan over every inflated payload: the animation token present in all 25,608 slots with 38,184 occurrences, and the clip-name token exactly once per slot.
- Root-record walk: all 25,608 slots pass the full assertion set, including three resolving pointers, capacity equal to count plus one, two constant words, at least one name string, and every 8-byte-aligned relative pointer in the header in range.
- Stratified samples: 880 B, 10,928 B, 1,860,256 B, one per root and one drawable-labelled slot. All inflated to exactly the declared logical size.
- Rejected: metadata table (113,943 1.0 words and 917,147 monotone counters are inconsistent); placement dictionary (one clip name per slot, no instance data); localisation blob (strings are confined to one region, the interior is numeric).
- The formula `16 + sum(streams) + padding == logical` was tested and rejected for this type.

## Unknowns

1. The record stride and channel layout beyond 0xC0.
2. Whether the two small count fields are channel and track counts.
3. The meaning of the two per-slot words that look like hashes.
4. The 16-byte shortfall in the two exception slots.
5. Any handler or vtable on the executable side.

## Limits

No writer exists. No clip name is published. Nothing here claims the population has been decoded, only the container and the clip header.
