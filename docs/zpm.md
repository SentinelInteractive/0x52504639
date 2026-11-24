# zpm resources

Status: container and header field inventory verified on every slot. No record stride and no key semantics. No content, asset or name list is published.

## Identity

`zpm` is type code `0x46` from the engine's own type-name table, registered by the engine with a store class named for motion. The label is not treated as proof: the payload was searched for the three signatures a motion clip would carry and none was found.

- Structural identity, verified: a fixed header of at least 0x120 bytes followed by variable-length data. The header carries a `(count, capacity)` pair of 16-bit values with `capacity == count + 1` on every slot, six virtual pointers that resolve inside the payload on every slot, and a high-entropy 32-bit identifier that is distinct in all 8,443 slots.
- Discriminator, verified: every payload contains the literal path-scheme token `pack:/` and none contains the animation-clip token `.anim`. The clip type in this package is the exact reverse.
- Companion, verified: exactly one other type shares this population's name hashes — the clip store `0x43` — 729 slots by name hash, and the 32-bit identifier is equal on both sides in 729 of 729 pairs with 729 distinct values. A per-slot identifier is shared between a motion record and its clip; the equality is measured, the role is inferred.
- Semantic identity, inferred: a motion record that references assets by path and carries numeric parameters, paired with a clip of the same name.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `anim.rpf` | 8,440 | 38,471,568 | 204,184,160 |
| `story000` | 3 | 29,328 | 81,824 |
| **Total** | **8,443** | **38,500,896** | **204,265,984** |

- Every slot is a resource entry; every root and every containing header has generation 4. The population sits in 67 distinct headers.
- Name origins: 725 dictionary matches, 7,718 unresolved hashes; all name hashes are distinct.
- Size distribution: stored 400 / 896 / 1,328 / 2,880 / 15,584 bytes at min / p25 / p50 / p75 / p95, maximum 1,334,288; logical 1,536 / 3,920 / 7,264 / 15,856 / 82,432, maximum 8,589,696.
- The logical-to-stored ratio runs 2.112 to 18.410 with a median of 4.818.

## Container

- Sixteen zero bytes at stored offset 0; a zlib stream head at stored `+0x10` in every slot.
- One stream in 8,017 slots, two in 426. Where two, the second starts at the next 16-byte-aligned stored offset with a gap of 0 to 15 bytes.
- `logical == sum(inflated)` on 8,443 of 8,443 slots, with zero inflate errors.
- No rule was found for the 426 two-stream splits.

## Fields

Offsets relative to the inflated payload, little-endian, denominator 8,443 slots.

| Offset | Observation | Confidence |
|---|---|---|
| 27 scattered offsets in the first 0xb0 bytes | zero in every slot | Verified |
| `+0x08`, `+0x38`, `+0x48`, `+0x70`, `+0x80`, `+0xa0`, `+0x100`, `+0x108` | virtual pointers, in range in every slot | Verified shape; targets undecoded |
| `+0x40` / `+0x42` | `count` / `capacity`, range 20–114, median 74, `capacity == count + 1` on every slot | Verified |
| `+0x44` | `1` in every slot | Verified |
| `+0x50` | small enum: one value in 8,255 slots, a second in 186, then two singletons | Measured |
| `+0x58` | small counter 1..6 | Measured |
| `+0x5c`, `+0x94` | `0x01000000` in every slot | Verified |
| `+0x68` | high-entropy 32-bit identifier, distinct in all 8,443 slots, equal to the clip twin's value in 729 of 729 pairs | Verified |
| `+0x78` / `+0x90` | packed pairs of equal 16-bit halves (2,2) in 4,466 slots, (1,1) in 1,597, then 3..6 | Measured |
| `+0x88` | small enum, one value in 7,830 slots | Measured |
| `+0xa8` | small counts up to 1,084 | Measured |
| `+0xc8`, `+0xd0`, `+0xf8`, `+0x120` | small integer fields with one dominant value each | Measured |
| `+0x110` | a sentinel pair in 5,026 slots, zero in 2,355 | Measured |
| `+0x160` | high-entropy word, one value in 4,198 slots | Measured; meaning unknown |

The count/capacity idiom is the same one the animation-clip report documents, with a different range (20–114 here, 24–64 there). That is a header-family resemblance, inferred; the objects counted are not identified.

## Decode

Per layer:

- Container: decoded and verified on every slot.
- Header field inventory: decoded and verified — constants, the count/capacity pair, the pointer set and the identifier are measured on 100 percent of the population.
- Header semantics: partly inferred. The count is a count; what it counts is unknown.
- Record array: not decoded. There is no global record stride: the greatest common divisor of all logical sizes is 16, and only 4, 8 and 16 divide every slot. A residual test with a plausible header boundary and a 12-byte stride divides only 2,826 slots, and its three residual classes are simply the lengths modulo 16 — not evidence of a 12-byte record.
- Key semantics: not decoded.

Float tests over the whole population beyond the header:

- 50.5 million words; 98.353 percent finite; 73.172 percent finite, non-zero and small; 1.142 percent within 1e-6 of 1.0.
- 355,883 contiguous float runs of length 4 or more. Only 1.36 percent are strictly increasing, and inside runs the adjacent pairs are increasing 15.3 million times and decreasing 15.1 million times — there is no monotone time axis.
- 0.306 percent of four-word windows have a squared norm within 0.01 of 1 — no quaternion array.

Together these rule out keyframes, quaternion channels and radian angles as the array's content. What remains plausible is normalised parameter data, stated as an inference.

## Encode

No encoder, no pack-back test and no game-load test exists. The container could be re-emitted, but the array stride, the count's referent and the pointer targets are unresolved. Write status W0.

## Unknowns

- The header boundary and the meaning of the six pointer targets.
- What the count/capacity pair counts.
- Any population-wide record stride.
- Why the identifier is shared with the clip twin; a common clip identifier is the working hypothesis.
- What causes 426 slots to carry a second stream.
- What the path token addresses, and whether those references are internal or external to the package.

## Method and limits

Rust release binaries, offline, no Python, over the whole population; the twin test re-inflated all 729 pairs and compared the identifier on both sides. The engine executable is read as a data file and never run. No key material is involved in this type. Private and unpublished: any payload, extracted data, resolved names, per-slot offsets and archive paths.
