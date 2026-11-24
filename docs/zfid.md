# zfid resources

Status: container, header, word count and padded body verified on every slot. Element semantics not decoded. No content, asset or name list is published.

## Identity

`zfid` is type code `0x67` from the engine's own type-name table. The engine registers the word with a store class named for facial identity, in the same registration batch as the drawable, fragment-BVH, clip and animation stores.

- Structural identity, verified: two compressed streams. The first is a fixed 240-byte header in all 6,762 slots; the second is a body of little-endian 32-bit words. A 32-bit word count at header `+0x78` sizes the used part of the body, and the largest body class is a fixed 128 KiB block padded with zeros after the count.
- Semantic identity, inferred: the store class names a facial identity and the body statistics fit a dense float array, with no index runs, no quaternion blocks and no fixed period. Which float belongs to which blend shape, bone or corrective target is not established.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 6,758 | 138,238,544 | 316,261,712 |
| `core_restofworld` | 4 | 84,464 | 174,032 |
| **Total** | **6,762** | **138,323,008** | **316,435,744** |

- Every slot is a resource entry; every root has generation 4. The containing header generation is 4 in 6,229 slots and 5 in 533.
- Name origins: 1,282 dictionary matches, 5,480 unresolved hashes; all name hashes are distinct.
- Size distribution: stored 112 / 5,760 / 12,176 / 39,904 / 56,864 bytes at min / p25 / p50 / p75 / p95, maximum 59,152; logical 5,072 / 13,712 / 23,936 / 131,312 / 131,312, maximum 131,312.
- The logical size takes exactly five values, all of the form header plus body: 5,072, 13,712, 23,936, 63,744 and 131,312.

## Container

- Sixteen zero bytes at stored offset 0; a zlib stream head at stored `+0x10` in every slot.
- Exactly two streams per slot. The first decodes to exactly 240 bytes in 6,762 of 6,762 slots. The second begins at the next 16-byte-aligned stored offset with a gap of 0 to 15 bytes.
- `logical == sum(inflated)` on 6,762 of 6,762 slots, with zero inflate errors. The sixteen stored zero bytes are outside `logical` for this type, unlike the older fragment and dictionary types that count them inside.

## Fields

Offsets relative to the inflated payload, little-endian, denominator 6,762 slots.

Constant on every slot: zero blocks through most of the header; three pointer-shaped constants at `+0x08`, `+0x10` and `+0x98`; a `0x00090004` word at `+0x7c`; `0x00001601` at `+0x80`; `0x60000000` at `+0x88`; `0xffff0214` at `+0xc0`; `0xffffffff` at `+0xc4`; `0x00000101` at `+0xd8`.

| Offset | Distinct | Observation | Confidence |
|---|---:|---|---|
| `+0x78` | 6 | the count: 1,206 in 1,627 slots, 3,368 in 1,627, 5,924 in 1,627, 15,876 in 1, 17,974 in 1,597, 17,984 in 283; never zero | Verified by the length identity below |
| `+0x58` | 33 | exactly eight values per body-length class; not the slot's name hash in either half | Measured; meaning unknown |
| `+0x5c` | 45 | zero in 6,603 slots, 8 in 56, 7 in 15 | Measured; meaning unknown |
| `+0x60` | 87 | zero in 6,611 slots, one pointer-shaped value | Measured; meaning unknown |
| `+0x64` | 53 | zero in 6,611 slots, 8 in 54 | Measured; meaning unknown |

The count predicts the body length. With `body = logical − 240`:

| body | Slots | count | `body − 4·count` |
|---:|---:|---:|---:|
| 4,832 | 1,627 | 1,206 | 8 |
| 13,472 | 1,627 | 3,368 | 0 |
| 23,696 | 1,627 | 5,924 | 0 |
| 63,504 | 1 | 15,876 | 0 |
| 131,072 | 1,597 | 17,974 | 59,176 |
| 131,072 | 283 | 17,984 | 59,136 |

The residual over the whole population is `0` in 3,255 slots, `8` in 1,627, `59,176` in 1,597 and `59,136` in 283. Two consequences:

- No single offset-and-stride pair over the header makes the relation exact for all 6,762 slots; an exhaustive 2/4/8-byte scan finds none. The per-class table is the correct statement.
- The residual is a zero-padded tail, not a second array: in the 128 KiB class the tail is exactly `32,768 − count` words for 1,862 of the 1,880 slots; 14 slots are entirely zero after the leading word and 4 carry two extra bytes.

The body begins with the 32-bit value `1` at absolute offset 240 in all 6,762 slots. Header generation does not change the layout: generation 4 holds all six counts and generation 5 holds four of them, never the largest.

## Decode

Per layer:

- Container: decoded and verified on all slots.
- Header: decoded and verified for the constants and the count.
- Body: decoded and verified as a word array with a count and a padded tail; the values are not interpreted.
- Element semantics: not decoded.

Body statistics per class: exact-zero words are 0.87, 0.65, 0.63, 99.99 and 45.56 percent; the longest zero run equals the word count minus one for the empty records. The words are floats, not indices — the longest increasing 16-bit run in range is 4 to 5 words and the longest increasing 32-bit run is 2, in every class. They are not quaternions: only 7 to 29 four-word windows per class, of up to 962,560 tested, have a squared norm within 0.01 of 1. They have no rigid period: equality at lags 4 to 48 over an 8 KiB prefix stays between 1.8 and 5.2 percent.

Twin test: 1,647 slots share their name hash with a type `0x04` dictionary slot, 24.4 percent of the population. Re-inflating both sides of all 1,647 pairs finds no numeric relation: the count, the logical size and either half of the name hash appear in the twin 0 times, and the stored size twice (0.12 percent). The pairing is name identity, not an embedded reference. All 1,647 pairs fall in the 128 KiB class.

## Encode

No encoder, no pack-back test and no game-load test exists. The layout and the count identity would make a writer feasible in principle — sixteen zeros, a stream of the 240-byte header with the count set, alignment padding, then `1` followed by the float words and the zero tail — but the compressor settings, the fill bytes and the fields at `+0x58` are unresolved, so no round trip was attempted. Write status W0.

## Unknowns

- The meaning of the header fields at `+0x58` (33 values, eight per size class), `+0x5c`, `+0x60` and `+0x64`.
- Which float index maps to which blend shape, bone or corrective, and whether the array is per-vertex, per-bone or per-morph-target.
- Why the smallest class carries a two-word tail while two others end exactly at the count.
- Why one 63,504-byte slot is 99.99 percent zero.
- Why all dictionary twins fall in the largest class, and what the twin holds relative to this type.
- The four constant pointer-shaped words: in this container they are constants, not relocations.

## Method and limits

Rust release binaries, offline, no Python, over all 6,762 slots; the key numbers were re-derived by a second checker that does not read the first one's output. The engine executable is read as a data file and never run. No key material is involved in this type. Private and unpublished: any payload, extracted data, resolved names, per-slot offsets and archive paths.
