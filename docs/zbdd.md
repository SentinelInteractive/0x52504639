# zbdd resources

Status: the whole population is decoded down to the index and pointer arrays; the meaning of the indexed values is not. No content, asset or name list is published.

## Identity

`zbdd` is type code `0x10` from the engine's own type-name table. The engine registers it with a store class whose name states a drawable-side BVH, in the same registration batch as the drawable BVH and fragment BVH stores.

The class name says BVH. The payload was tested for a spatial structure and is not one, so the name was not taken as the answer:

- Structural identity, verified: a fixed 64-byte header carrying a `(count, count)` pair, an ascending 32-bit value index of exactly `count` entries, and a `count`-entry pointer array whose targets are 0x20-byte records that begin with two zero words.
- Verified negative: there is no coordinate or bounds data anywhere in the addressed records. Reading this type as a float BVH is ruled out by measurement, not by preference.
- Relation, verified: all 22,382 slots share their name hash with a type `0x04` slot, and the pairing is a strict one-to-one bijection — 22,382 distinct hashes, one twin each, no hash shared by two slots.
- Interpretation, inferred: a per-asset lookup table over the named entries of its twin, keyed by a 32-bit value. 62.753 percent of probed index values appear verbatim in the twin payload.

The open contradiction is recorded rather than hidden: the store class is named after a BVH and the payload holds no BVH. Either the class name covers a wider family than its name suggests, or a second record layout exists on a code path that was not located.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `core_bvh4` | 22,301 | 3,581,296 | 7,996,832 |
| `shared_minigame000_bvh4` | 81 | 10,416 | 22,368 |
| **Total** | **22,382** | **3,591,712** | **8,019,200** |

- Every slot is a resource entry; every root and every containing header has generation 4. The population sits in 132 distinct headers.
- Name origins: 2 dictionary matches, 22,380 unresolved hashes; all name hashes are distinct.
- Size distribution: stored 80 / 96 / 128 / 128 / 368 bytes at min / p25 / p50 / p75 / p95, maximum 3,648; logical 160 / 192 / 272 / 272 / 896, maximum 10,096. Mean 160.5 stored and 358.3 logical bytes.
- 22,382 slots totalling 8.0 MB of logical data: every statement in this page is a whole-population statement, not a sample.

## Container

- Sixteen zero bytes at stored offset 0; a zlib stream head at stored `+0x10` in every slot.
- Exactly one stream per slot, so there is no alignment padding to describe.
- `logical == sum(inflated)` on 22,382 of 22,382 slots, with zero inflate errors. The sixteen stored zero bytes are outside `logical` for this type.

## Fields

Offsets relative to the inflated payload, little-endian, denominator 22,382 slots.

| Offset | Observation | Confidence |
|---|---|---|
| `+0x00`, `+0x04`, `+0x0c`, `+0x10` (8 bytes) | zero in all slots | Measured |
| `+0x08` | virtual pointer, in range in all slots | Measured |
| `+0x18` | the value `1` in all slots | Measured; meaning unknown |
| `+0x20` | virtual pointer to the value index | Measured |
| `+0x28` | `count` as a 16-bit value, repeated at `+0x2a` and again at `+0x38` | Verified: it sizes both arrays in 22,382 of 22,382 slots |
| `+0x30` | virtual pointer to the pointer array | Measured |
| `+0x40` upward | a run of 8-byte values that are either zero or virtual pointers | Measured; target class undecoded |

Count distribution over the population: 4 in 11,982 slots, 1 in 3,904, 2 in 1,979, 16 in 847, 3 in 645, 8 in 354, 5 in 301, 6 in 292, then a tail up to 227.

The smallest 160-byte slot was partitioned byte for byte — header, descriptor, root record, padding and the two arrays — with zero unaccounted bytes.

## Decode

Per layer:

- Container: decoded and verified.
- Header and count: decoded and verified; the count sizes both arrays on every slot.
- Value index: decoded and verified. Exactly `count` 32-bit values, strictly ascending in 22,382 of 22,382 slots, so nothing repeats inside a slot. 130,496 values in total, 105,112 distinct across the population.
- Pointer array: decoded and verified. Exactly `count` entries, every target inside the payload (0 of 130,496 out of range), and the first 32-bit word at every one of the 130,496 targets is zero.
- Element semantics: not decoded. What the 32-bit values denote is unknown.

Twin test: 500 name-paired twins were re-inflated. Every pair has at least one index value found verbatim in the twin payload, 2,170 of 3,458 probed values match (62.753 percent), and in an inspected pair 28 consecutive values appear at twin offsets spaced exactly 0x20 apart in ascending order. That is the basis for the index reading, and it is the limit of the claim.

## Encode

No encoder, no pack-back test and no game-load test exists. The record is small enough that a writer could target it from the field map alone, but the descriptor's semantics, the padding rule and the compressor settings are unresolved. Write status W0.

## Unknowns

- What the 32-bit index values denote. They are found verbatim in the twin payload, but 22,380 of 22,382 slots have no resolvable name, so they cannot be resolved to strings from the index alone.
- The constants at `+0x18` and the zero fields at the start of the header.
- The 0x20-byte descriptor's full layout beyond its size and its leading zero words.
- Whether the pointer-array order follows the ascending index order one to one.
- Why the store class is named after a BVH when no spatial data was measured.

## Method and limits

Rust release binaries, offline, no Python. The whole population was decoded in 0.2 s, so container, count, index and pointer-array results are population statements. The twin test re-inflated 500 pairs. The engine executable is read as a data file and never run. No key material is involved in this type. Private and unpublished: any payload, extracted data, resolved names, per-slot offsets and archive paths.
