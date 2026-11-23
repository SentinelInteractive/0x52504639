# Full TOC index

Status: read path complete. Write path not started.

Scope: Xbox Series build 1.0.2.1, own copy. The executable is read as data only. No key, asset or executable is published.

## Counts

- **1,255,039 slots** across 22 roots.
- **4,373 headers**: 22 roots and 4,351 children.
- **0 header parse failures.**
- 564,783,265,279 logical bytes and 305,820,985,968 stored bytes. Container and descendant ranges overlap, so neither number is unique disk usage.
- **381,096 slots dictionary-matched (30.37%)**, 227,869 distinct strings. 873,943 slots keep an unresolved hash. No original full paths are claimed.

A comparison target reports the same entry and child counts, and 4,375 headers. Our 4,373 is exactly 22 roots plus 4,351 children. The two-header difference is unresolved and is not papered over.

## Resource record

The resource record is **20 bytes**, not 18:

| Offset | Meaning |
|---|---|
| `+0` | u32 size and flags. Logical size is `(u32 & 0x7ffffff0) + (u32 at +4 & 0xfffffff0)`. |
| `+8` | u32 stored size in 16-byte units. |
| `+12` | u32 payload offset in 16-byte units. |
| `+16` | u32 candidate type word. Unverified. |

The 16-byte prefix before a zlib stream is outside the compressed data. 14,757 of 14,762 sampled resources start with 16 zero bytes and then `78 DA`. The 746 script resources use a different codec and are covered separately.

## Name hashes

- `hash32` is Jenkins one-at-a-time, seed 0.
- `hash64` is lane 1 of MurmurHash3 x64_128, seed 0, with the executable's low-byte length quirk.
- 656 slots match both widths and 1,984 match the 64-bit hash. Four anchors were independently decompressed and contain the exact hashed identifier.
- The confirmed inputs are leaf or stem names, not full paths. The join is a dictionary match, not a recovered original path.

## Script resources

- 746 slots, all decoded to their declared logical sizes.
- The codec is a selective big-endian CTR with a per-chunk zlib or raw dispatch. Key material and initialisation values are not published.
- Write status: extract-only. Re-encryption is feasible but no encoder or round-trip is verified.

## Type census

- 387,259 slots have a recognised prefix magic. 867,780 are unknown.
- `0DRPz` 290,294; `ADAT` 71,676; `PSIN` 18,640; `9FPR` 4,351; `RBF0` 1,278; `KB2` 797; `XML` 221; `SGD5` 2.
- The `+16` word is a candidate type identifier, not a verified hash. Binary slots have no resource word. Magic matches are classification evidence, not proof that a type is decoded.

## Signature status

- The signature blob location and the PKCS#1 v1.5 envelope are known for `common.rpf`.
- The signed message representation has not been reproduced. Counts: **0 verified, 0 failed, 4,373 unknown.**
- A digest mismatch on an unproven representation is not a failed archive signature. No key or signature bytes are published.

## Why this matters

The read index is the base for the tool and the per-type work. It gives exact slots, offsets, stored and logical sizes, name hashes and dictionary matches without relying on a reconstructed catalogue. It does not decrypt, extract or publish game content.

## Reproduce

The index is produced by the local reader from a user-supplied executable and a user-owned package. The reader is not published with the key or decoder path. Counts in this page can be checked against the public container facts and the per-root summary.
