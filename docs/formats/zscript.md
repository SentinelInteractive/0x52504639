# `zscript` (type code `0x59`)

Written 2026-11-26. Decode limit stated first: the container decodes on all 746 slots and a full structural instruction listing is reported on 746 of 746 bodies, but program semantics are **not decoded**: no branch-target model, stack balance, native call targets, import tables, readable source or execution is established (`artifact: script_listing/report.md:145-146,181-192`; `artifact: script_inventory.md:76-81`). Grade **B**, not A, even though the published coverage row is Full (`artifact: docs/coverage.md:151`): byte-level listing is not semantic decoding. Write status W0 (`artifact: docs/formats/script-resources.md:109-113`).


Editorial coverage grade: **B**. This grade describes the demonstrated scope below; source-table status labels and historical grades remain attributed to their original evidence. Evidence: `artifact: docs/coverage.md:127-163` and this document's Verification section.

## Identity

The descriptor's extension index is `0x59`; the executable's extension table maps it to a script extension for variant 0 and a second script extension for variant 1, and the 746 measured descriptors have the whole word `0x00000059` (`artifact: docs/formats/script-resources.md:5-7`). The label `zscript` is the type-list name for code `0x59` (`artifact: script_inventory.md:19`; `artifact: docs/coverage.md:151`). A synthesized container header is not an on-disk magic and its version byte is `0x31` in this set (`artifact: docs/formats/script-resources.md:17`). The decoded object header is not the layout of a different script format: there is no name pointer at `+0x58`, no page/code/string pointer pair at `+0x68/+0x70`, and the pointers are full `0x5xxxxxxx` values rather than masked ones (`artifact: script_inventory.md:41-46`). The `+0x10` hash matches the full-root TOC join on 746 of 746 rows with no duplicate slot hashes and no size disagreements; six private name matches are reported, superseding an earlier all-unresolved note, and no name is reproduced here (`artifact: script_bytecode.md:33-35`).

## Counts

| Measure | Value | Source |
|---|---:|---|
| Slots | 746 | `artifact: docs_complete_work/type_counts.tsv` row `00000059`; `artifact: docs/coverage.md:151` |
| Stored bytes | 50,195,184 | same two sources |
| Logical bytes | 167,734,336 | same two sources |
| Denominator | 1,255,039 slots | `artifact: docs/coverage.md:7,40` |

Exactly two roots carry the type: one slot with 331,744 stored / 1,310,720 logical bytes and 745 slots with 49,863,440 / 166,423,616 bytes (`artifact: script_inventory.md:13-20`; `artifact: docs/formats/script-resources.md:19-25`). Chunk classes are 735 all-zlib slots and 11 zlib-plus-raw slots (`artifact: script_inventory.md:22`). The largest decoded object is 17,072,608 bytes (`artifact: script_inventory.md:50`). Byte sums overlap with nested containers (`artifact: docs/coverage.md:10`).

## Container

Each stored slot starts with sixteen zero bytes that the loader excludes from the cipher extent; the sum of padded TOC chunk sizes equals `stored - 16` in every slot (`artifact: docs/formats/script-resources.md:37-41`). Chunk boundaries are advanced by padded stored lengths while only unpadded bytes enter the inflater, and decoded chunks concatenate to the declared logical size (`artifact: docs/formats/script-resources.md:41`). All 746 slots matched logical size with 998 zlib chunks and 11 raw chunks, and all passed the leading-zero-qword and in-range `+0x08` pointer checks (`artifact: docs/formats/script-resources.md:136-137`). Beyond the container, the decoded object has a bounded primary span (`+0xe8` pointer, `+0xf8` byte length) and a separate auxiliary span (`+0xf0`, `+0xfc`) on 746 of 746 slots; these spans do not overlap and the primary span ends with eight zero bytes on all slots (`artifact: script_bytecode.md:11-19`).

## Fields

Offsets are relative to the named record; the Resource record is 20 bytes and its field records must be resolved through the decrypted TOC column indices (`artifact: docs/formats/script-resources.md:45-47`).

| Offset | Width | Meaning | Confidence | Evidence |
|---|---:|---|---|---|
| Resource `+0x00` | u32 | `w0 & 0x7ffffff0` first logical size component; low nibble contributes synthesized version high nibble | measured | `artifact: docs/formats/script-resources.md:51` |
| Resource `+0x04` | u32 | `w1 & 0xfffffff0` second component; `w1 = 1` here, so second component is zero | measured | `artifact: docs/formats/script-resources.md:52` |
| Resource `+0x08` | u32 | Stored length in 16-byte units, prefix included | measured | `artifact: docs/formats/script-resources.md:53` |
| Resource `+0x0c` | u32 | Slot offset in 16-byte units | measured | `artifact: docs/formats/script-resources.md:54` |
| Resource `+0x10` | u8 | Extension index `0x59`; whole-word value measured on all 746 slots | measured | `artifact: docs/formats/script-resources.md:7,55`; `artifact: script_inventory.md:19` |
| Resource `+0x11` | u8 | Zero in this set; not the stream codec flag | measured | `artifact: docs/formats/script-resources.md:56` |
| Decoded object `+0x00` | qword | Zero | measured | `artifact: script_inventory.md:32`; `artifact: docs/formats/script-resources.md:137` |
| Decoded object `+0x08` | qword | `0x5xxxxxxx` paged pointer, base `0x50000000`, in range | measured | `artifact: script_inventory.md:33,137` |
| Decoded object `+0x10` | u32 | 32-bit TOC name hash; full-root join matched 746/746 rows | measured | `artifact: script_inventory.md:34`; `artifact: script_bytecode.md:35` |
| Decoded object `+0x14` | u32 | `1` in all 746 slots | measured | `artifact: script_inventory.md:35` |
| Decoded object `+0x18` | u32 | `111` in all 746 slots | measured | `artifact: script_inventory.md:36` |
| Decoded object `+0x1c` | 8 bytes | Same constant 8-byte tag in all 746 slots | measured | `artifact: script_inventory.md:37` |
| Decoded object `+0x30..+0x7f` | 16 each | Five descriptor records of `(u64 pointer, u32 count, u32 count)` with equal counts in 746/746 | measured | `artifact: script_inventory.md:39`; `artifact: script_bytecode.md:31` |
| Decoded object `+0xe8` / `+0xf8` | u64 / u32 | Primary-span pointer and byte length, in bounds on 746/746 | measured | `artifact: script_bytecode.md:13` |
| Decoded object `+0xf0` / `+0xfc` | u64 / u32 | Auxiliary-span pointer and byte length, in bounds on 746/746 | measured | `artifact: script_bytecode.md:17` |
| Chunk map `+0x00` / `+0x04` / `+0x07` | u32 / u16 / u8 | Relative offset to entries, entry count, layout byte `2` | measured | `artifact: docs/formats/script-resources.md:58` |
| Chunk entry bits 0..23 / 32..55 / 58..61 / 62..63 | u24 / u24 / u4 / u2 | Logical units of 16, padded stored units of 16, trailing pad, codec class (3 wrapped zlib, 0 raw) | measured | `artifact: docs/formats/script-resources.md:60-66` |
| Cipher descriptor `+0x00` / `+0x04` / `+0x38` | u32 / u16 / u32 | Forward-record selector, algorithm tag `0x11`, flag mask `4` in this set | measured | `artifact: docs/formats/script-resources.md:67` |
| Code word | u16 | `opcode = word * 0x3315 mod 65536`, inverse `0x843D` | external | `artifact: script_listing/report.md:24-25` |
| Operand byte at place `i` | u8 | `plain = (stored ^ key(i)) * 0x6D mod 256`, `key(i) = 0x85 ^ (0x11*i mod 256)` | external | `artifact: script_listing/report.md:26-28` |
| Operand widths | — | U8/S8 1, U16 2, U24 3, U32/S32/F32 4, U64 8; length `2 + sum(widths)` | external | `artifact: script_listing/report.md:29-30` |

The external rules above were extracted as data from a pinned reference table and format-fact file; the local decoder source is original Rust and no external code was vendored (`artifact: script_listing/report.md:11-22`). Opcode-derived facts are labelled external and are not local measurements.

## Decode status

Container: measured on 746 of 746 slots; 998 zlib chunks and 11 raw chunks ended cleanly and matched declared lengths (`artifact: docs/formats/script-resources.md:136`). Structural listing: 530 reference rows parsed with zero rejects, zero duplicates and opcode range 0..529 (`artifact: script_listing/report.md:34-50`); the local walker passed 3/3 smallest, 20/20 stratified and 746/746 all-body tests, consuming 32,703,447 instructions and 117,066,144 code bytes (`artifact: script_listing/report.md:126-146`). The controls show that the `zero`-field invariant, not operand whitening, drives rejection; with that invariant disabled the walk is still 746/746 exact (`artifact: script_listing/report.md:69-72,141-143`). This is a complete byte-level listing of the measured bodies, **not** decoded program semantics: branch targets, stack balance, native RVAs, call/import tables, naming and readable source are unverified (`artifact: script_listing/report.md:183-184`). A PE consumer search found no indexed dispatch match and is a bounded negative, not proof that no VM exists (`artifact: script_bytecode.md:43-49`). Grade B: container and instruction boundaries are measured; semantics are unknown. No encoder or round trip (`artifact: docs/formats/script-resources.md:111`).

## Verification

The retained census-count artifact records these reproduction commands; this documentation pass did not rerun them:

```
rustc -O artifact: docs_complete_work/count_inventory.rs -o artifact: docs_complete_work/count_inventory.exe
& artifact: docs_complete_work/count_inventory.exe artifact: type_census.csv artifact: docs_complete_work
```

Observed: `data_rows: 1255039`, `stored_bytes: 305820985968`, `logical_bytes: 564783265279`, `malformed_or_unparsable_rows: 0` (`artifact: docs_complete_work/inventory_log.txt`); row `00000059` in `artifact: docs_complete_work/type_counts.tsv` is 746 / 50,195,184 / 167,734,336. Source-side commands quoted, not re-run here: `cargo build --release --offline` (2.28 s), `selftest` pass, `parse-table <opcode_table.rs> data\opcodes.tsv` (0.0321 s), `extract20.exe <PE> bodies_all <two script roots>` (4.7552 s for 746 bodies / 167,734,336 bytes) and `decode-list data\opcodes.tsv all_paths.tsv` (3.4012 s, about 32.8 MiB/s) (`artifact: script_listing/report.md:148-175`). The container reference probe recorded 1.942 s and 24.65 stored MiB/s (`artifact: docs/formats/script-resources.md:35,139`). The game executable was read as data and never executed (`artifact: script_listing/report.md:4-7`).

## Unknowns

The older primary-span interpretation is superseded at the structural level by the 746-of-746 instruction-boundary audit, while runtime behavior remains unverified. The public summary's zero-prefix/zlib-chain shorthand omits the TOC-directed storage transformation and 11 raw chunks recorded by the detailed codec source. Sources: `artifact: script_listing/report.md`, sections 3, 6 and 8; `artifact: docs/formats/script-resources.md`, Container and Verification; `artifact: repo-publisher/docs/zscript.md`, Container.

The proprietary block transform's historical name and whether it is standard are unknown (`artifact: docs/formats/script-resources.md:143`); layouts 3 and 4, other cipher tags and flag variants were not exercised (`artifact: docs/formats/script-resources.md:144`); the purpose of the excluded prefix, object/page-chain schema and original compressor parameters are unresolved (`artifact: docs/formats/script-resources.md:145`); whether the primary span is bytecode, a codec or a mix remains an inference (`artifact: script_bytecode.md:37-41`); cross-script table roles such as import, export or relocation are not verified (`artifact: script_bytecode.md:31`). No opcode map was derived from local execution and no operand value is reproduced (`artifact: script_listing/report.md:190-192`).

## Changelog

- 2026-11-26: created this page. No earlier `artifact: docs_complete/zscript.md` existed at the time of writing. Sources: `artifact: docs/coverage.md:151`, `artifact: docs/formats/script-resources.md`, `artifact: script_inventory.md`, `artifact: script_bytecode.md`, `artifact: script_listing/report.md`, `artifact: docs_complete_work/type_inventory.md`, `artifact: docs_complete_work/format_evidence.md:487-543`. No script content, key, asset or publication was produced. Other final documents and source files were not modified.

- 2026-11-26: reconciled to the type/support heading scheme without discarding retained sections; prior text preserved at `artifact: docs_complete_work/reconciliation_original_20261126_1/zscript.md`. No count was selected by modification time.

