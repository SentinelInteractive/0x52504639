# ztd resources

Status: container verified on every slot, header partly decoded, pixels not decoded, identity inferred. No content, texture, pixel data or name is published.

## Identity

`ztd` is type code `0x05` from the engine's own type-name table. This is the only type in its round with **no** store registration carrying its word: the small core codes are registered by a path that has not been located, and the texture-store string that exists in the image is referenced from a site that does not carry this word. **No class name is claimed.** The label is a three-letter tag and does not establish what the payload is.

Structural identity, verified:

- A serialised header stream followed by one or more body streams inside the same slot. The body length is `logical − header` and is non-zero in 2,603 of 2,612 slots.
- The header is a relocation graph: 32-bit words of the form `0x50000000 | offset` whose target is an offset inside the header, not inside the logical size. A pointer at header `+8` is present in every slot; four more pointer slots are present in 2,603.
- The slot's own 64-bit name hash does not appear in the first 512 header bytes (0 of 2,612).

Semantic identity, inferred, not verified: a texture resource whose pixel data is stored in the same slot. Three measurements support it and none proves it.

1. For 8 of the 9 slots that have a resolvable name, that exact name string occurs verbatim inside the inflated header. The ninth carries three other texture-style runs instead of its own name.
2. All 75 binary slots that share a name hash with this type decompress to the package's own texture-container signature at byte 0, and 57 of those 75 embed a name string that also occurs verbatim in a header of this type. Cross-references by stored hash are 0 of 75, so the association is by name.
3. Bodies are large, high-entropy and 16-byte aligned, and their lengths decompose exactly into power-of-two footprints plus a small header.

What would promote this to verified: locating the reader for this type, or decoding one body stream with an independent block-compression decoder into a coherent image. Neither was done, and no pixel was decoded.

## Counts

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `textures.rpf` | 1,365 | 188,005,904 | 487,062,816 |
| `levels.rpf` | 1,009 | 123,688,608 | 468,845,648 |
| `core_restofworld` | 145 | 10,430,784 | 27,220,512 |
| `data.rpf` | 75 | 102,402,640 | 309,526,688 |
| `shared_minigame000` | 18 | 989,184 | 15,898,096 |
| **Total** | **2,612** | **425,517,120** | **1,308,553,760** |

- Every slot is a resource entry; every root and every containing header has generation 4. The population sits in 32 distinct headers, the largest carrying 1,315 slots.
- Name origins: 9 dictionary matches, 2,603 unresolved hashes; all name hashes are distinct.
- Size distribution: stored 48 / 3,392 / 26,208 / 109,296 / 284,704 bytes at min / p25 / p50 / p75 / p95, maximum 27,998,560; logical 96 / 33,168 / 33,168 / 524,544 / 524,544, maximum 39,866,560.
- The logical size is quantised and decomposes exactly into header plus a power-of-two body:

| Logical | Header | Body | Slots | Body |
|---:|---:|---:|---:|---|
| 33,168 | 400 | 32,768 | 1,314 | 2^15 |
| 524,544 | 256 | 524,288 | 748 | 2^19 |
| 262,416 | 272 | 262,144 | 270 | 2^18 |
| 8,624 | 432 | 8,192 | 23 | 2^13 |
| 4,384 | 288 | 4,096 | 12 | 2^12 |
| 96 | 96 | 0 | 9 | header only |

The largest slot is 39,866,560 logical bytes: a 3,296-byte header and a 33,226,752-byte body.

## Container

- Sixteen zero bytes at stored offset 0; a zlib stream head at stored `+0x10` in every slot.
- Streams per slot: two in 2,530, three in 70, one in 9, four in 3. Later streams start at the next 16-byte-aligned stored offset with a gap of 0 to 15 bytes.
- `logical == sum(inflated)` on 2,612 of 2,612 slots, with zero inflate errors. The sixteen stored zero bytes are outside `logical`.
- The first stream is the header (96 to 3,296 bytes) and the last is the body. Whether extra streams split the body into mip levels or into separate payloads was not established.
- Body lengths are 16-byte aligned in every slot and 4,096-byte aligned in 2,611 of 2,612.

## Fields

Offsets relative to the inflated header, little-endian, denominator 2,612 slots.

| Offset | Observation | Confidence |
|---|---|---|
| `+0` | 8 zero bytes | Verified |
| `+24` | the value `1` in every slot | Verified |
| `+8`; `+32`, `+48`, `+104`, `+112` | relocation-style pointers inside the header, present in 2,612 and 2,603 slots respectively | Verified |
| `+40`, `+56` | packed pairs of equal 16-bit halves: (2,2) in 1,391 slots, (1,1) in 1,101 | Verified |
| `+72` | power-of-two magnitude: 1,024 in 1,315 slots, 262,144 in 748, 65,536 in 272, 512 in 59 | Verified magnitude; a pixel-count reading is inferred |
| `+76` | a tagged word whose low 16 bits take the values 2, 4, 8, 16 | Measured; a format-tag reading is inferred |
| `+80` | 2,432 in 2,560 slots | Measured |
| `+88` | `0x60000000` in 2,551 slots — a tagged word, not a pointer | Measured |
| `+120` | two equal 16-bit halves: 0x800080 in 1,324 slots, 0x2000200 in 759, 0x1000100 in 326 | Measured |
| `+128` | `0x00010005` in 2,423 slots | Measured |
| `+132` | `0x00010000` in 2,508 slots | Measured |
| `+160` | `0xffff0241` in 2,562 slots | Measured |
| `+164` | `0xffffffff` in 2,567 slots | Measured |
| `+184` | a small integer in most slots, or the first four bytes of the name string in 272 | Measured |

Two arithmetic relations: for two of the three dominant families the body length is the magnitude field times 2 or 4, and for the third the multiplier is 32 and is unexplained. There is no meaningful float field in the first 512 header bytes — the apparent ones are packed 16-bit pairs and integer magnitudes.

## Decode

Per layer:

- Container: decoded and verified on every slot.
- Header: partly decoded — the pointer graph, the size pair, the magnitude field and the constant block are measured; no field was resolved to an unambiguous width, height, format and mip-count tuple.
- Body: not decoded. No pixel block was decoded into an image and no texture was exported.

Body statistics over 119.9 million sampled bytes: Shannon entropy minimum 0.000, p25 3.106, median 4.948, p75 6.548, maximum 7.950 bits per byte; 4,261,360 distinct 16-byte blocks; 128,264 all-zero blocks; the longest zero run is 65,536 bytes, so at least one body is entirely zero.

Block-compression test, reported as a measurement and not as a decode: in the high-entropy family 149,931 of 181,504 blocks (82.6 percent) begin with a byte shape consistent with a modern block-compression mode, while in a raw family 30,885 of 35,072 blocks (88 percent) begin with a zero byte. No block was decoded, so block compression is a hypothesis for about 1,317 slots, not a finding.

Hypotheses tested against the payload:

| Hypothesis | Verdict |
|---|---|
| Pixels live in a separate resource and the header holds only names | rejected: the body is inside the slot in 2,603 of 2,612 |
| The slot's own name hash is stored in the header | rejected: 0 of 2,612 |
| Companion texture slots are referenced by stored hash | rejected: 0 of 75 |
| A standard width/height/format/mip header sits in the first 512 bytes | not verified: the sliding-window detector also fires on pointer and name bytes |
| The body is entirely block-compressed | rejected as a universal claim: low-entropy families dominate the small sizes |

## Encode

No encoder, no pack-back test and no game-load test exists. The container rule is known and reproducible, and the observed header and body pairs reproduce the recurring logical sizes exactly, but the relocation graph and the format fields are not decoded, so no slot can be synthesised. Write status W0.

## Unknowns

- The class name and the reader: no registration and no dispatch site for this word was located.
- The exact meaning of the magnitude field, the tag word and the four constant fields; in particular whether the magnitude is a pixel count.
- True width, height, format and mip layout for any slot.
- Whether the three- and four-stream slots are mip chains.
- Whether the high-entropy family is a block format at all: no block was decoded.
- Why one body is entirely zero, and why one header carries three other texture-style runs instead of its own name.

## Method and limits

Rust release binaries, offline, over all 2,612 slots; one read-only shell aggregation of already-written output was used for the companion summary and every number it produced was re-checked against the Rust output. The engine executable is read as a data file and never run. No key material is involved in this type. Private and unpublished: any payload, any pixel data, every name string and name list, per-slot offsets and archive paths.
