# zft fragments

Status: container layer verified. Body not decoded. No content, asset or name list is published.

## Identity

`zft` is type code `0x03` from the engine's own enum table. The label is not inferred from a file extension.

The measured shape is a **base fragment asset**, not a drawable. Its companion is a BVH fragment store:

- 22,438 of 55,488 `zft` slots share a TOC name hash with a type `0x11` slot.
- 22,438 of 22,440 type `0x11` slots have a `zft` twin, 99.99 percent.
- Zero `zft` slots share a hash with a `zdr` drawable.

## Counts

| Root | Slots |
|---|---:|
| `levels.rpf` | 50,802 |
| `packs.rpf` | 2,865 |
| `data.rpf` | 1,758 |
| `core_restofworld` | 53 |
| `shared_minigame000` | 10 |
| **Total** | **55,488** |

- **5,915,592,480 stored bytes**, **14,211,185,152 logical bytes**.
- All slots are Resource entries; all roots are generation 4.
- Header generations: 5 in 52,603 slots, 4 in 2,865, 8 in 20.
- Name origin: 50,362 dictionary matches and 5,126 unresolved hashes. Names are not reproduced.
- Stored size: minimum 1,456, median 26,288, maximum 9,343,728 bytes.

## Container

The container is verified on the whole population:

- 16 zero bytes at stored `+0x00`.
- zlib header at `+0x10` on all 55,488 slots.
- 2 to 4 streams. Each next stream starts at the next 16-byte-aligned stored offset; observed gaps are 0 to 15 bytes.
- Zero inflate errors.
- The concatenated decoded output equals exactly the declared logical size minus 16 on every slot.

The inflated payload starts with 8 zero bytes, then five 64-bit pointers based at `0x50000000`. All five resolve in 45,390 slots; exactly two resolve in 10,098. A four-`u16` flag block sits at `+0x30`, and the constant block `{-1,-1,-1,+1, 0.7}` sits at `+0xc0`.

The TOC name appears verbatim in the payload in 50,355 of the 50,362 named slots. That is a name check, not a new name source.

Two page-map hypotheses were tested and rejected: only 2 slots have all boundaries on 64 KiB multiples, and 8,594 slots match `ceil(logical / 65536)`.

## Status

**Partial.** The count, roots, container, zlib chain and header prefix are verified across all 55,488 slots. The body, geometry and page map are undecoded. Write status is **W0**; no encoder or round-trip exists.

## Limits

- The body and inline geometry are unresolved.
- The page map and the non-BVH fragment loader are unresolved.
- 5,126 slots have no dictionary name.
- No payload, asset or name list is published.
