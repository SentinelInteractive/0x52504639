# zbn bounds

Status: container and root record verified. Shape body not decoded. No content, asset, name list or key is published.

## Identity

`zbn` is type code `0x06` from the engine's own enum table. The variant-0 label is `zbn`; the other variants are `ibn` and `#bn`. The label is not a file extension and does not by itself prove what the payload is.

The measured shape is a **leaf bounded-volume resource**, not a bundle, container or localisation wrapper. There is no member table, name table, BCn data, UTF-8 pool or material table. Every slot carries one radius, one axis-aligned box, a standard margin, a centroid and gravity pair, four self-pointers and a body of 16-bit index records.

## Counts

| Scope | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `levels.rpf` | 88,719 | 10,718,017,008 | 16,578,426,944 |
| `story000` | 2,989 | 269,405,696 | 414,154,000 |
| `shared_minigame000` | 491 | 106,526,464 | 164,200,704 |
| **Total** | **92,199** | **11,093,949,168** | **17,156,781,648** |

- All 92,199 are Resource slots.
- All 92,199 names are unresolved hashes; no path or extension is known.
- Logical over stored is 1.5465.
- Median stored 78,272 bytes; 95th percentile 398,416; maximum 1,328,784.

## Container

Every slot uses the page form already seen in `0DRPz`:

```
stored slot
  +0x00  16 zero bytes
  +0x10  zlib stream 1
  ...    zlib stream 2 when the payload crosses a 64 KiB boundary

inflated
  +0x00  u64 0
  +0x08  u32 self-pointer, base 0x50000000
  +0x10  root record, 0x90 bytes
  +0xA0  body
```

Measured on all 92,199 slots:

- 16 leading zero bytes: 92,199 / 92,199.
- zlib header at `+16`: 92,199 / 92,199.
- zlib header at `+0`: 0.
- `+0x08` uses the `0x50000000` base: 92,199 / 92,199.
- Inflated length equals declared logical minus 16: 90,546 (98.22 percent).
- 1,653 chains are short: 149 corrupt deflate streams, 1,504 end with stored bytes but no second zlib header. They are counted, not guessed.

One stream: 35,759 slots. Two streams: 56,440. Where two streams exist, the first ends on a 64 KiB boundary of the logical space, or that boundary minus the 16-byte prefix. There is no block count or offset table; the streams are found by walking the stored range.

## Root record

The root record at `+0x10` is 0x90 bytes:

| Offset | Width | Measured value | Meaning | Confidence |
|---|---|---|---|---|
| `+0x10` | u8 | `0x06` in all slots | shape type | byte verified, meaning inferred |
| `+0x11` | u8 | `0x01` in all slots | flags | byte verified, meaning inferred |
| `+0x12` | u16 | 0 | unknown | verified |
| `+0x14` | f32 | radius 0.0067 to 1572.96 | bounding radius | verified distribution |
| `+0x18` | u64 | 0 | unknown | verified |
| `+0x20` | float3 | box corner | axis-aligned bound | verified |
| `+0x2c` | f32 | margin, `0.005` in 99.2 percent | standard margin | verified |
| `+0x30` | float3 | opposite corner | axis-aligned bound | verified |
| `+0x3c` | u32 | 1 | unknown | verified |
| `+0x40` | float3 | centroid | centre of mass | inferred |
| `+0x4c` | float3 | gravity centre | centre of gravity | inferred |
| `+0x58` | float4 | `(1,1,1,1)` in 56.1 percent | unknown | verified |
| `+0x78` | four pointers | `0x50000000` base | self-references | verified |

The radius equals the box half-diagonal within 0.5 percent in 45.6 percent of slots and within 11 percent in 90.8 percent. The body is 16-bit index records with `0x7F` and `0xFFFF` sentinels plus a per-polygon byte array. The body is located but not interpreted.

## What is proven

- The page container, zlib chain and 0x90-byte root record decode on all 92,199 slots.
- The counts match the independent type-word join with zero delta.
- The type code and labels are the engine's own.
- The payload has no ASCII signature; it is identified by the resource type word, not by a magic.

## What is not proven

- The exact shape subtype. The engine's RTTI is stripped; the class is inferred from the structure.
- The 16-byte node record semantics and the float-pair encoding.
- The per-polygon byte array.
- The 1,653 short chains and the 757-slot `0.65` margin cohort.
- A writer. Write status is **W0 extract-only**; no encoder or round-trip exists.

## Coverage status

**Partial.** The container and root record are verified across the whole family. The shape body is not decoded. This is not a full coverage claim.
