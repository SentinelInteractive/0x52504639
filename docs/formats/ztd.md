# `ztd` (type code `0x05`)

Decode scope, stated plainly: this is a container-and-partial-header report. The zlib stream chain and the header relocation graph are measured on every slot; the body is not decoded into an image and no pixel block is exported. Semantic identity as a texture resource is inferred, not verified, and no class name is claimed because no store registration carries this word. Header progress is bounded separately in Decode status and is not a pixel decode. Date 2026-11-26. No key, asset, pixel block, name string or source path is reproduced. Underlying census: `artifact: type_census.csv` (1,255,039 rows), cited only; no census or archive rescan was run for this document.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x05`. The executable's type-name table at `0x1462fcd30 + variant*0x98 + code*8` resolves it to `ztd` (variant 0) and `itd` (variant 1) (`artifact: docs/formats/ztd.md`, Identity and Exe path). This is the only type in the round with no store registration carrying its word: core codes `0x02` to `0x06` are registered by a path that was not located, and the existing `TxdStore` string is referenced from a site that does not carry `r8d = 0x05` (`artifact: docs/formats/ztd.md`, Identity and Exe path). **No engine class name is claimed** for this type.

- Structural identity, **verified**: a serialized header stream followed by one or more body streams in the same slot; body length equals `logical − header` and is non-zero in 2,603 of 2,612 slots (`artifact: docs/formats/ztd.md`, Identity).
- The header is a relocation graph of 32-bit words of the form `0x50000000 | offset` whose targets are offsets inside the header itself, not inside `logical`; a pointer at header `+8` is present in 2,612 of 2,612 slots and at `+32`, `+48`, `+104` and `+112` in 2,603 (`artifact: docs/formats/ztd.md`, Identity and Fields).
- The slot's own 64-bit TOC name hash does not appear anywhere in the first 512 header bytes, 0 of 2,612 (`artifact: docs/formats/ztd.md`, Identity).
- Semantic identity, **inferred and not verified**: a texture resource whose pixel data is stored in the slot. Three measurements support it: for 8 of the 9 slots with a resolvable TOC name, that exact name string occurs verbatim in the inflated header; all 75 binary slots sharing a name hash inflate to `GFX*` at byte 0, with 57 of 75 embedding a name string also found verbatim in a `ztd` header and 0 cross-references by stored 32- or 64-bit hash; bodies are large, high-entropy, 16-byte aligned and their lengths decompose into power-of-two footprints plus a small header (`artifact: docs/formats/ztd.md`, Identity). What would promote the identity to verified is locating the `0x05` reader or decoding one body into a coherent image; neither was done (`artifact: docs/formats/ztd.md`, Identity).

Grade: **Partial**, scope = container and partial header; body and element semantics open (`artifact: docs/formats/ztd.md`, Decode; `workspace: CONTEXT_HANDOFF.md` §9). `coverage_audit/out/tables.md` row `0x05` carries the coarser Classified note "Name and count verified; payload not examined"; it is recorded here, not silently adopted, because the detailed report measures the container, relocation graph and size decomposition on 100 percent of the population.

## Counts

Authoritative totals are transcribed from `coverage_audit/out/tables.md`, row `0x05`; `artifact: type_census.csv` is the underlying census and was not rescanned.

| Code | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `0x05` | 2,612 | 425,517,120 | 1,308,553,760 |

Per-root split, from the type report (`artifact: docs/formats/ztd.md`, Counts):

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `textures.rpf` | 1,365 | 188,005,904 | 487,062,816 |
| `levels.rpf` | 1,009 | 123,688,608 | 468,845,648 |
| `core_restofworld` | 145 | 10,430,784 | 27,220,512 |
| `data.rpf` | 75 | 102,402,640 | 309,526,688 |
| `shared_minigame000` | 18 | 989,184 | 15,898,096 |
| **Total** | **2,612** | **425,517,120** | **1,308,553,760** |

The verified type-word join, the registry and the census agree on all three numbers (`artifact: docs/formats/ztd.md`, Counts). Every slot is a resource entry; roots and containing headers are generation 4; the population sits in 32 distinct headers, the largest with 1,315 slots (`artifact: docs/formats/ztd.md`, Counts). Name origins: 9 dictionary matches and 2,603 unresolved hashes; all 2,612 name hashes are distinct (`artifact: docs/formats/ztd.md`, Counts). Logical size is quantised and decomposes exactly into header plus a power-of-two body (`artifact: docs/formats/ztd.md`, Counts):

| Logical | Header | Body | Slots | Body as |
|---:|---:|---:|---:|---|
| 33,168 | 400 | 32,768 | 1,314 | 2^15 |
| 524,544 | 256 | 524,288 | 748 | 2^19 |
| 262,416 | 272 | 262,144 | 270 | 2^18 |
| 4,384 | 288 | 4,096 | 12 | 2^12 |
| 8,624 | 432 | 8,192 | 23 | 2^13 |
| 96 | 96 | 0 | 9 | header only |

The single largest slot is 39,866,560 logical bytes with a 3,296-byte header and a 33,226,752-byte body (`artifact: docs/formats/ztd.md`, Counts).

## Container

All statements in this section are measured on 2,612 of 2,612 slots (`artifact: docs/formats/ztd.md`, Container):

- Stored `+0x00..+0x0F` are sixteen zero bytes and stored `+0x10` begins a zlib stream (`78 da` in every slot).
- Streams per slot: two in 2,530, three in 70, one in 9 and four in 3, for 5,291 streams in total. Later streams start at the next 16-byte-aligned stored offset with a gap of 0 to 15 bytes.
- `logical == sum(inflated)` on 2,612 of 2,612 slots; zero inflate errors.
- The first stream is the header, 96 to 3,296 bytes, and the last is the body. Where three or four streams exist, the extra streams split the body; whether they are mip levels or a separate payload was not established.
- Body lengths are 16-byte aligned in 2,612 of 2,612 slots and 4,096-byte aligned in 2,611 of 2,612.

## Fields

Offsets are relative to the inflated header; integers little-endian; denominators are 2,612 slots unless stated (`artifact: docs/formats/ztd.md`, Fields). The full grid is in `artifact: type_reports/out/ztd_scan.txt`. Confidence vocabulary is strictly `measured`, `inferred`, `external`, `unknown`. The table has exactly four columns and every Meaning cell names its source artifact.

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+8` | 4 | `0x50000000 OR offset` pointer resolving inside the header in 2,612 slots (`artifact: docs/formats/ztd.md`, Fields, pointer table) | measured |
| `+32`, `+48`, `+104` | 4 | Header-internal pointer present in 2,603 slots (`artifact: docs/formats/ztd.md`, Fields, pointer table) | measured |
| `+112` | 4 | Header-internal pointer present in 2,603 slots (`artifact: docs/formats/ztd.md`, Fields, pointer table) | measured |
| `+216`, `+224` | 4 | Pointer or a name byte run in 1,482 and 1,483 slots (`artifact: docs/formats/ztd.md`, Fields, pointer table) | measured |
| `+0` | 8 | Zero (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+24` | 8 | `1` in all slots (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+40`, `+56` | 4 | Packed u16 pairs with equal halves: `(2,2)` in 1,391 slots and `(1,1)` in 1,101 (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+72` | 4 | Power-of-two magnitude: 1,024 in 1,315 slots, 262,144 in 748, 65,536 in 272 and 512 in 59; the pixel-count reading is inferred (`artifact: docs/formats/ztd.md`, Fields, constant table) | inferred |
| `+76` | 4 | `0x80000 OR tag`: 524,304 in 1,418 slots, 524,290 in 752, 524,292 in 274 and 524,296 in 122; low 16 bits behave like a format tag with values 2, 4, 8 and 16 (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+80` | 4 | `2,432` in 2,560 slots (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+88` | 4 | `0x60000000` in 2,551 slots, a tagged word and not a pointer (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+120` | 4 | `0x00800080` in 1,324 slots, `0x02000200` in 759 and `0x01000100` in 326, two equal u16 halves (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+128` | 4 | `0x00010005` in 2,423 slots, `0x00090005` in 40 and `0x00070005` in 26 (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+132` | 4 | `0x00010000` in 2,508 slots and `0x00012000` in 59 (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+160` | 4 | `0xffff0241` in 2,562 slots (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+164` | 4 | `0xffffffff` in 2,567 slots (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |
| `+184` | 4 | 1,024 in 1,316 slots, 257 in 757, or the first four bytes of a printable run in 272 (`artifact: docs/formats/ztd.md`, Fields, constant table) | measured |

Two relations were tested and recorded (`artifact: docs/formats/ztd.md`, Fields): for two of the three dominant families the body length is `u32@+72` times 2 or 4 (`262,144 × 2 = 524,288` and `65,536 × 4 = 262,144`), while the third family uses an unexplained multiplier of 32; that is verified arithmetic with the byte-per-pixel reading inferred. No meaningful float field exists in the first 512 header bytes, since the apparent plausible-float counts come from packed u16 pairs and integer magnitudes (`artifact: docs/formats/ztd.md`, Fields).

## Decode status

- Container: **decoded and verified** on 2,612 of 2,612 slots (`artifact: docs/formats/ztd.md`, Decode).
- Header: **partially decoded**. The pointer graph, the size pair, the magnitude field and the constant block are measured; no field was resolved to an unambiguous width/height/format/mip-count triple (`artifact: docs/formats/ztd.md`, Decode).
- Body: **not decoded**. No pixel block was decoded into an image and no texture was exported (`artifact: docs/formats/ztd.md`, Decode).
- Element semantics: **not decoded** (`artifact: docs/formats/ztd.md`, Decode).
- Body statistics over 119,923,552 sampled bytes: Shannon entropy minimum 0.000, p25 3.106, median 4.948, p75 6.548, maximum 7.950 bits per byte; 4,261,360 distinct 16-byte blocks; 128,264 all-zero blocks; longest zero run 65,536 bytes, so at least one body is entirely zero (`artifact: docs/formats/ztd.md`, Decode).
- Block-compression test, reported as a measurement and not as a decode: in the high-entropy family with format tag `0x0010`, 149,931 of 181,504 blocks (82.6 percent) begin with a byte having exactly one trailing zero, the shape of a BC7 mode-1 block header; in the raw family with tag `0x0004`, 30,885 of 35,072 blocks (88 percent) begin with a zero byte, not a compressed-block shape. No block was decoded, so BC7 is a hypothesis for about 1,317 slots, not a finding (`artifact: docs/formats/ztd.md`, Decode).
- Hypotheses tested: pixels living in a separate resource is rejected because body length equals `logical − header` with a non-zero body in 2,603 slots; the slot's own TOC hash in the header is rejected at 0 of 2,612; companion slots referenced by stored hash is rejected at 0 of 75; a standard width/height/format/mips header in the first 512 bytes is not verified, since a 24-byte sliding-window score fired on 2,578 slots but its best offsets also match pointer and name bytes; the body being entirely block-compressed is rejected as a universal claim (`artifact: docs/formats/ztd.md`, Decode).
- Grade **Partial**, scope = container and partial header; body and element semantics open (`artifact: docs/formats/ztd.md`, Decode). Write status **W0**: the container rule is reproducible and the observed header/body pairs reproduce the recurring logical sizes exactly, but the relocation graph and format fields are not decoded, so no slot can be synthesised (`artifact: docs/formats/ztd.md`, Encode).

## Verification

All commands and figures below are from Rust release artifacts recorded in the cited source; nothing was re-run for this document.

- `type_probe inventory artifact: type_census.csv 00000005 out` — 1,255,039 census rows, 2,612 selected, 0.18 s (`artifact: docs/formats/ztd.md`, Verification).
- `type_probe walk out\ztd_slots.tsv <archive-root> out\ztd_walk.txt 256 288` — 2,612 slots in 3.36 s (777 slots/s, 126.6 MB/s stored, 389.3 MB/s logical) (`artifact: docs/formats/ztd.md`, Verification).
- `verify hdrlen` and `verify hdrclass` — 2,612 slots in 2.82 and 2.90 s (927 and 901 slots/s); jointly produced the stream-count histogram and the exact header-plus-body decompositions (`artifact: docs/formats/ztd.md`, Verification).
- `paircheck artifact: type_census.csv` — 1,255,039 rows in 2.32 s; no one-to-one companion, with 75 hash matches against binary slots, 13 against `0x6f` and 1 each against `0x04` and `0x10` (`artifact: docs/formats/ztd.md`, Verification).
- `ztd_probe scan|xref|comp|pattern` — 744.8 slots/s for the scan pass; the companion pass re-inflated all 75 binary slots, 5.1 MB logical (`artifact: docs/formats/ztd.md`, Verification).
- `exe_stores` — PE read only; produced the negative registration result (`artifact: docs/formats/ztd.md`, Verification).
- One read-only shell aggregation over already-written TSV output, 75 rows of 2,612 under 30 seconds, was used for the companion summary; every number it produced was re-checked against the Rust output (`artifact: docs/formats/ztd.md`, Verification).
- The executable was never loaded or executed (`artifact: docs/formats/ztd.md`, Verification).

## Unknowns

1. The class name and the reader: no registration and no dispatch site for word `0x05` was located (`artifact: docs/formats/ztd.md`, Unknowns).
2. Exact meaning of header fields `+72`, `+76`, `+80`, `+120`, `+128`, `+132` and `+184`, and in particular whether `+72` is a pixel count and what the `0x0010` family's multiplier of 32 represents (`artifact: docs/formats/ztd.md`, Unknowns).
3. True width, height, format and mip layout for any slot (`artifact: docs/formats/ztd.md`, Unknowns).
4. Whether the 3- and 4-stream slots are mip chains (`artifact: docs/formats/ztd.md`, Unknowns).
5. Whether the high-entropy family is the hypothesised block-compressed mode, another compressed mode or an uncompressed 32-bit format; no block was decoded (`artifact: docs/formats/ztd.md`, Unknowns).
6. Why one body is entirely zero and why one slot's header carries three other texture-style runs instead of its own name (`artifact: docs/formats/ztd.md`, Unknowns).
7. No encoder and no game-load test (`artifact: docs/formats/ztd.md`, Unknowns).
8. Grade reconciliation: `coverage_audit/out/tables.md` row `0x05` says Classified with "payload not examined" while the detailed report and this document say Partial with a bounded scope.

Next checks, in order: decode one 2^18-byte body under the `0x0004` tag as raw 8-bit and one under `0x0010` as the hypothesised block format, checking coherence at the width implied by `u32@+72`; then locate the `0x05` reader by searching the core registration path for the `0x02` to `0x06` initialisers (`artifact: docs/formats/ztd.md`, Unknowns).

## Changelog

- 2026-11-26: created `artifact: docs_complete/ztd.md` by consolidating `artifact: docs/formats/ztd.md`, `workspace: CONTEXT_HANDOFF.md` and `coverage_audit/out/tables.md`; counts transcribed from the coverage table, `artifact: type_census.csv` cited as underlying census. No index edit, no commit, no publish, no rescan. Language: no new code; read-only PowerShell text inspection of source artifacts only. Fields table has exactly four columns with source artifacts in Meaning. No engine class name claimed because no store registration verifies one. Write status unchanged at W0; grade Partial with container and partial-header scope. A concurrent draft with a five-column field table, an undefined grade label and a self-attributed census rerun was superseded by this version on the parent's explicit audit finding.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/ztd.md`. No count was selected by modification time.

