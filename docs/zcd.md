# zcd resources

Status: container layer verified. Object identity and body not decoded. No content, asset or name list is published.

## Identity

`zcd` is type code `0x43` from the engine's own enum table. The label does not establish what the payload represents. The bounded-prefix census records these slots under the unknown signature family, not under a recognised inner magic.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `anim.rpf` | 52,923 | 3,751,548,832 | 6,845,846,464 |
| `story000` | 9,189 | 2,964,030,128 | 4,300,227,408 |
| `levels.rpf` | 170 | 30,729,312 | 37,614,640 |
| `story000_restofworld` | 77 | 47,344,672 | 77,594,880 |
| `core_restofworld001` | 22 | 733,648 | 1,571,824 |
| `shared_minigame000` | 2 | 16,016 | 42,400 |
| `core_restofworld` | 1 | 464 | 1,504 |
| **Total** | **62,384** | **6,794,403,072** | **11,262,899,120** |

- All slots are Resource entries.
- Root generation is 4. Header generations: 4 in 62,211 slots, 5 in 81, 8 in 92.
- Name origin: 1,525 dictionary matches and 60,859 unresolved hashes. The paths themselves are not reproduced.
- Ranges can overlap other indexed resources. Distinct physical payloads are not established by these totals.

## Container

- All 62,384 slots have a valid zlib header at stored offset `+0x10`.
- Every first stream yields at least `0xA0` inflated bytes.
- In 304 directly probed samples, the preceding 16 bytes are zero. That prefix result is sampled, not population-wide.
- A chain walk reached the declared logical size minus 16 in all 62,384 slots. It found one stream in 32,072 slots, two in 30,310, and three in two. It permits up to 128 bytes between streams and stops at the cap, so it does not prove the full block layout.
- Many first-block output lengths are multiples of 64 KiB or 16 bytes less. This is an observation, not a complete block rule.

## Fields

Offsets are relative to the inflated data, little-endian.

| Offset | Width | Observation | Confidence |
|---|---|---|---|
| `+0x00` | 8 | Zero in all 62,384 headers | measured, meaning unknown |
| `+0x08` | 8 | Upper 32 bits zero; 62,371 low words begin with byte `0x50` | measured, pointer interpretation sampled |
| `+0x18` | 8 | Zero in all headers | measured |
| `+0x2c` | 4 | Zero in all headers | measured |
| `+0x4c` | 4 | Zero in all headers | measured |
| `+0x90` | 4 | Nonzero in all headers; value 3 occurs 31,154 times | measured, meaning unknown |
| `+0x94` | 4 | `0x01000000` in all headers | measured, meaning unknown |
| `+0x98`, `+0x9c` | 4 each | Zero in all headers | measured |

In 304 sampled resources, the pointer-like word at `+0x08` minus `0x50000000` resolves to a 16-byte record near the inflated buffer end. Its first eight and last six bytes are zero, with two one-byte values between them; the second byte is zero in all 304 samples. Treating it as a page map is a hypothesis, not a decoded structure.

## Status

**Partial.** The inventory and container layer are verified across the whole family. The object identity, page-map semantics, block structure, fields and body remain open. Write status is **W0**; no encoder or round-trip exists.

## Limits

- A collision dictionary and a drawable dictionary cannot be distinguished from the type label alone.
- The full chain scan without an output cap and a static trace from type dispatch to the object loader are the next checks.
- No payload, asset or name list is published.
