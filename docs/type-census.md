# Type census

Status: read-only classification from the full TOC. No game content is published.

## Result

- **1,255,039 slots** across 22 roots and 4,373 headers.
- The `+16` word in a 20-byte resource record is the **RAGE resource type enum**, not a hash. Code `0x00` to `0x12` uses the variant-0 table; `0x40` to `0x73` uses the callback table.
- **1,153,560 slots** carry a verified type name. **4,514** remain null-word and unclassified.
- The mapping is code-level, not a filename guess. It is resolved through the executable's own enum tables and checked against real resource headers.

## Top types by slot count

| Code | Name | Slots |
|---|---|---:|
| `0x0f` | zbdr | 250,434 |
| `0x02` | zdr | 167,897 |
| `0x49` | zmap | 166,072 |
| `0x06` | zbn | 92,199 |
| `0x43` | zcd | 62,384 |
| `0x03` | zft | 55,488 |
| `0x04` | zdd | 48,584 |
| `0x58` | zsm | 40,019 |
| `0x6c` | zascd | 32,878 |
| `0x6f` | zldbmt | 30,511 |
| `0x0b` | zmt | 28,328 |
| `0x4f` | znv | 27,644 |
| `0x64` | zsp | 27,482 |
| `0x4e` | zad | 25,608 |
| `0x11` | zbft | 22,440 |
| `0x10` | zbdd | 22,382 |
| `0x57` | zas | 15,067 |

## Signature families

Some slots carry an inner signature that does not match the `+16` type. The largest is `0DRPz`, a PSIN wrapper:

| Signature | Slots |
|---|---:|
| `0DRPz` | 290,294 |
| `ADAT` | 71,676 |
| `PSIN` | 18,640 |
| `9FPR` | 4,351 |
| `RBF0` | 1,278 |
| `KB2` | 797 |
| `XML` | 221 |
| `SGD5` | 2 |

The `0DRPz` family is split across eight type codes: zmt, zmap, ztyp, zas, zascd, zldbmt, zkit and zcov. The signature appears at offset `+0x10` after inflation, not at the start of the stored page.

## What this does and does not prove

- **Proved:** the `+16` field is a type enum, and the names are the executable's own variant-0 labels.
- **Proved:** the slot counts and the type-code totals agree with the full TOC index.
- **Not proved:** that every type is decoded. A type name is classification evidence, not a decoder.
- **Not proved:** the meaning of the `+16` word where it is null. Binary slots have no resource word.

## Method

- Full TOC index: 1,255,039 slots, one row per slot, with stored and logical sizes.
- Resource record: 20 bytes, offset at `+12`, stored size at `+8`, both in 16-byte units.
- Enum tables: the engine's own variant-0 table for `0x00..0x12` and callback table for `0x40..0x73`.
- Batch scan and merge in Rust. No game execution, no key use, no asset export.

## Limits

- The census classifies headers and bounded prefixes, not full payloads.
- Container and descendant ranges overlap, so byte sums are not unique physical bytes.
- No file is published. The table is a map of the archive, not a content dump.
