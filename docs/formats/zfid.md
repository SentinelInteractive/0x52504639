# `zfid` (type code `0x67`)

Decode scope, stated plainly: this is a container-and-header report with a decoded body word array. The zlib container, the 240-byte header and the count identity are verified on every slot; the body is decoded only as a little-endian word array with a count and a padded tail. No element is interpreted. Header progress is bounded separately in Decode status and is not a claim about body meaning. Date 2026-11-26. No key, asset, payload content, matched name or source path is reproduced. Underlying census: `artifact: type_census.csv` (1,255,039 rows), cited only; no census or archive rescan was run for this document.


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor type word is `0x67`. The executable's type-name table at `0x1462fcd30 + variant*0x98 + code*8` resolves it to `zfid` (variant 0, cell `0x14618db18`, string `0x146784645`) and `ifid` (variant 1); a variant-2 label was not located and none is claimed (`artifact: docs/formats/zfid.md`, Identity and Exe path). The word is registered by a verified PE read: `lea rdx,["FacialIdentityStore"]` at `0x145ba699c`, `mov r8d,0x67` at `0x145ba69a3`, `call 0x1419ca0b0` (`artifact: docs/formats/zfid.md`, Identity and Exe path). `FacialIdentityStore` is the only engine label claimed here, and it is verified by image bytes.

- Structural identity, **verified**: a resource of two zlib streams; the first decodes to a 240-byte fixed header, the second is a body of little-endian 32-bit words; a 32-bit word count at header `+0x78` sizes the used part of the body, and the largest body class is a fixed 128 KiB block padded with zeros after the count (`artifact: docs/formats/zfid.md`, Identity).
- Semantic identity, **inferred**: the store class names a facial identity and the body statistics fit a dense float array, with no index runs, quaternion blocks or fixed period. Which float belongs to which blend shape, bone or corrective target is not established (`artifact: docs/formats/zfid.md`, Identity).
- Companion test, **verified as a name statement**: 1,647 `zfid` slots share their 64-bit name hash with a `0x04` `zdd` slot, which is 24.4 percent of this population. Re-inflating both sides of all 1,647 pairs finds no numeric relation: the `zfid` count appears in its twin 0 times, logical size 0 times, stored size 2 times (0.12 percent), and neither half of the name hash 0 times. The pairing is name identity, not an embedded reference (`artifact: docs/formats/zfid.md`, Decode).

Grade: **Partial**, scope = container, header, count identity and body word-array structure; element semantics open (`artifact: docs/formats/zfid.md`, Decode; `workspace: CONTEXT_HANDOFF.md` §9). `coverage_audit/out/tables.md` row `0x67` carries the coarser Classified note "Name and count verified; no payload decoder"; it is recorded here, not silently adopted, because the detailed report measures the container, header and array on 100 percent of the population.

## Counts

Authoritative totals are transcribed from `coverage_audit/out/tables.md`, row `0x67`; `artifact: type_census.csv` is the underlying census and was not rescanned.

| Code | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `0x67` | 6,762 | 138,323,008 | 316,435,744 |

Per-root split, from the type report (`artifact: docs/formats/zfid.md`, Counts):

| Root | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `packs.rpf` | 6,758 | 138,238,544 | 316,261,712 |
| `core_restofworld` | 4 | 84,464 | 174,032 |
| **Total** | **6,762** | **138,323,008** | **316,435,744** |

The verified type-word join, the independently maintained registry and the census agree on all three numbers, each equal to the sum of the per-root rows (`artifact: docs/formats/zfid.md`, Counts). Every slot is a resource entry and every root has generation 4; containing headers are generation 4 in 6,229 slots and generation 5 in 533 (`artifact: docs/formats/zfid.md`, Counts). Name origins: 1,282 dictionary matches and 5,480 unresolved hashes; all 6,762 name hashes are distinct and names are not reproduced (`artifact: docs/formats/zfid.md`, Counts). The slots sit in 17 distinct archive headers, the largest with 2,439 (`artifact: docs/formats/zfid.md`, Counts). Logical size takes exactly five values, all of the form `240 + body`: 5,072, 13,712, 23,936, 63,744 and 131,312 (`artifact: docs/formats/zfid.md`, Counts).

## Container

All statements in this section are measured on 6,762 of 6,762 slots (`artifact: docs/formats/zfid.md`, Container):

- Stored `+0x00..+0x0F` are sixteen zero bytes and stored `+0x10` begins a zlib stream (`78 da` in every slot).
- Every slot holds exactly two zlib streams. The first decodes to exactly 240 bytes in 6,762 of 6,762; the second is the body.
- The second stream begins at the next 16-byte-aligned stored offset. Measured padding is 8 bytes in 5,889 boundaries, 0 in 6,831, 7 in 712 and 1 to 15 in the remainder; no boundary exceeds 15.
- Zero inflate errors across the population.
- `logical == sum(inflated stream lengths)` on 6,762 of 6,762. This is the `zft`/`zdd` container identity without the 16-byte prefix term: `zft` measured `logical == sum + 16` and `zfid` measures `logical == sum`; both carry the sixteen stored zero bytes (`artifact: docs/formats/zfid.md`, Container).

## Fields

Offsets are relative to the concatenated inflated payload (the 240-byte header occupies `+0x00..+0xEF`); integers little-endian; "all" means all 6,762 slots (`artifact: docs/formats/zfid.md`, Fields). Confidence vocabulary is strictly `measured`, `inferred`, `external`, `unknown`. The table has exactly four columns and every Meaning cell names its source artifact.

| Offset | Width | Meaning | Confidence |
|---|---|---|---|
| `+0x00`, `+0x04`, `+0x0c`, `+0x14..+0x54`, `+0x68..+0x74`, `+0x84`, `+0x8c..+0x94`, `+0x9c..+0xbc`, `+0xc8..+0xd4`, `+0xdc..+0xec` | 4 | Zero blocks in all slots (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0x08` | 8 | `0x500000d0`, pointer-shaped constant (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0x10` | 8 | `0x50000070`, pointer-shaped constant (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0x7c` | 4 | `0x00090004`, two u16 with values 9 and 4 (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0x80` | 4 | `0x00001601` (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0x88` | 4 | `0x60000000` (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0x98` | 8 | `0x500000b0`, pointer-shaped constant (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0xc0` | 4 | `0xffff0214` (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0xc4` | 4 | `0xffffffff` (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0xd8` | 4 | `0x00000101`, two u16 with values 1 and 1 (`artifact: docs/formats/zfid.md`, Fields, constant table) | measured |
| `+0x78` | 4 | Word count with six distinct values: 1,206 in 1,627 slots, 3,368 in 1,627, 5,924 in 1,627, 15,876 in 1, 17,974 in 1,597 and 17,984 in 283; never zero, and the word-count reading is verified by the length identity (`artifact: docs/formats/zfid.md`, Fields, varying table) | measured |
| `+0x58` | 4 | 33 distinct values, exactly eight per body-length class; not the slot's name hash in either half; meaning unknown (`artifact: docs/formats/zfid.md`, Fields, varying table) | unknown |
| `+0x5c` | 4 | 45 distinct values, zero in 6,603 slots, 8 in 56 and 7 in 15; meaning unknown (`artifact: docs/formats/zfid.md`, Fields, varying table) | unknown |
| `+0x60` | 4 | 87 distinct values, zero in 6,611 slots, one pointer-shaped value, rest scattered; meaning unknown (`artifact: docs/formats/zfid.md`, Fields, varying table) | unknown |
| `+0x64` | 4 | 53 distinct values, zero in 6,611 slots and 8 in 54; meaning unknown (`artifact: docs/formats/zfid.md`, Fields, varying table) | unknown |
| body at absolute `0xf0` | 4 | Leading u32 value `1` in all 6,762 slots (`artifact: docs/formats/zfid.md`, Fields, body note) | measured |

With `body = logical − 240`, the measured class table is: body 4,832 with 1,627 slots at count 1,206 and residual 8; body 13,472 with 1,627 slots at count 3,368 and residual 0; body 23,696 with 1,627 slots at count 5,924 and residual 0; body 63,504 with 1 slot at count 15,876 and residual 0; body 131,072 with 1,597 slots at count 17,974 and residual 59,176; and body 131,072 with 283 slots at count 17,984 and residual 59,136 (`artifact: docs/formats/zfid.md`, Fields, length identity). Header generation does not change the layout: generation 4 holds all six counts and generation 5 holds four and never 17,984 (`artifact: docs/formats/zfid.md`, Fields).

## Decode status

- Container: **decoded and verified** on 6,762 of 6,762 slots (`artifact: docs/formats/zfid.md`, Decode).
- Header: **decoded and verified** for the constant blocks and the count field (`artifact: docs/formats/zfid.md`, Decode).
- Body: **decoded and verified as a word array with a count and a padded tail**; the array values are not interpreted (`artifact: docs/formats/zfid.md`, Decode).
- Element semantics: **not decoded** (`artifact: docs/formats/zfid.md`, Decode).
- No single `(offset, stride)` pair over header bytes 0 to 240 makes `body = stride·count + c` exact for all 6,762 slots; an exhaustive 2/4/8-byte scan finds none. The residual is a zero-padded tail, not a second array: in the 131,072 class the tail is exactly `32,768 − count` words for 1,862 of 1,880 slots, 14 slots are entirely zero after the leading word and 4 carry two extra bytes (`artifact: docs/formats/zfid.md`, Fields).
- Body measurements: the words are floats, not indices, with longest increasing u16 run 4 to 5 words and longest increasing u32 run 2 in every class; not quaternion blocks, with only 7 to 29 four-word windows per class of 833,024 to 962,560 tested having squared norm within 0.01 of 1; no rigid 4-float period; float exponents span the full biased range 0 to 255 in every class (`artifact: docs/formats/zfid.md`, Decode).
- Grade **Partial**, scope = container, header and body word-array structure; element semantics open (`artifact: docs/formats/zfid.md`, Decode). Write status **W0**: the layout and count identity make a writer feasible in principle, but zlib parameters, alignment fill bytes and the fields at `+0x58..+0x64` are unestablished and no byte-stable round trip was attempted (`artifact: docs/formats/zfid.md`, Encode).

## Verification

All commands and figures below are from Rust release artifacts recorded in the cited source; nothing was re-run for this document.

- `type_probe inventory artifact: type_census.csv 00000067 out` — 1,255,039 census rows in 0.20 s, 6,762 selected (`artifact: docs/formats/zfid.md`, Verification).
- `type_probe walk out\zfid_slots.tsv <archive-root> out\zfid_walk.txt 256 288` — 6,762 slots in 0.84 s (8,013 slots/s, 164 MB/s stored, 375 MB/s logical) (`artifact: docs/formats/zfid.md`, Verification).
- `type_probe join artifact: type_census.csv 00000067 out\join_00000067.txt` — 1,255,039 rows in 2.26 s, 554,465 rows/s (`artifact: docs/formats/zfid.md`, Verification).
- `paircheck artifact: type_census.csv` — 1,255,039 rows in 2.32 s, 540,157 rows/s; the 1,647 `zdd` pairings are unambiguous (`artifact: docs/formats/zfid.md`, Verification).
- `verify hdrlen`, `verify u32 ... 120 88`, `verify resid ... 120 4`, `verify xtab ... 120` — 6,762 slots each, 0.79 to 0.83 s per pass at 8,190 to 8,596 slots/s; re-derived the 240-byte first stream, the six-value count histogram, residual set `{0, 8, 59,136, 59,176}` and class cross-tab (`artifact: docs/formats/zfid.md`, Verification).
- `zfid_probe headers|stride|body|tail|zdd|ids` — 0.68 to 2.96 s per pass, 6,931 to 9,944 slots/s; outputs `out\zfid_fields.txt`, `zfid_stride.txt`, `zfid_body.txt`, `zfid_tail.txt`, `zfid_zdd.txt`, `zfid_ids.txt` (`artifact: docs/formats/zfid.md`, Verification).
- `exe_stores` — 120,181,760 bytes scanned as a PE file; produced the registration row and the class string (`artifact: docs/formats/zfid.md`, Verification).
- The executable was never loaded or executed (`artifact: docs/formats/zfid.md`, Verification).

## Unknowns

1. Meaning of header fields `+0x58` (33 values, eight per size class), `+0x5c`, `+0x60` and `+0x64`; the `+0x58` tag is not the name hash and does not resolve a name (`artifact: docs/formats/zfid.md`, Unknowns).
2. Element semantics: which float index maps to which blend shape, bone or corrective, and whether the array is per-vertex, per-bone or per-morph-target (`artifact: docs/formats/zfid.md`, Unknowns).
3. Why the 4,832 class carries a two-word tail while the 13,472 and 23,696 classes end exactly at `4·count` (`artifact: docs/formats/zfid.md`, Unknowns).
4. Why one 63,504-byte slot is 99.987 percent zero and why 14 slots of the 131,072 class are empty after the leading word (`artifact: docs/formats/zfid.md`, Unknowns).
5. Why all 1,647 `zdd` companions fall in the 131,072 class and what the twin holds relative to this type (`artifact: docs/formats/zfid.md`, Unknowns).
6. The four constant `0x5xxxxxxx` pointer-shaped words: in this container they are constants, not relocations, so whatever they address is not inside the resource (`artifact: docs/formats/zfid.md`, Unknowns).
7. The `zfid` loader: the store registration is located, but the reader consuming the 240-byte header is not (`artifact: docs/formats/zfid.md`, Unknowns).
8. Grade reconciliation: `coverage_audit/out/tables.md` row `0x67` says Classified while the detailed report and this document say Partial with a bounded scope.

Next checks, in order: find the reader called from the `FacialIdentityStore` registration and read its field order; then test whether the `+0x58` tag selects a float layout by grouping the 131,072 class on the tag (`artifact: docs/formats/zfid.md`, Unknowns).

## Changelog

- 2026-11-26: created `artifact: docs_complete/zfid.md` by consolidating `artifact: docs/formats/zfid.md`, `workspace: CONTEXT_HANDOFF.md` and `coverage_audit/out/tables.md`; counts transcribed from the coverage table, `artifact: type_census.csv` cited as underlying census. No index edit, no commit, no publish, no rescan. Language: no new code; read-only PowerShell text inspection of source artifacts only. Fields table has exactly four columns with source artifacts in Meaning. Write status unchanged at W0; grade Partial with header and body-word-array scope. A concurrent draft with a five-column field table, an undefined grade label and a self-attributed census rerun was superseded by this version on the parent's explicit audit finding.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zfid.md`. No count was selected by modification time.

