# `0DRPz` localisation tables

`0DRPz` is not a text format. It is the generic resource wrapper that most PSIN payloads use, and localisation is one blob combination inside it. The wrapper holds a 0x50-byte root struct plus typed blobs addressed by relative virtual pointers.

This page covers the wrapper, the descriptor table, the blob set that carries text, the classifier that separates a localisation table from any other string pool, and the counts from a run over four archives.

No strings are published here or anywhere else in this repository. Every value below is a count, an offset or a ratio.

## Wrapper layout

Offsets are from the start of the resource stream.

| Offset | Field |
| --- | --- |
| `+0x00` | u64 zero |
| `+0x08` | u64 reference pointer, virtual |
| `+0x10` | root struct, 0x50 bytes |

Root struct:

| Offset | Field |
| --- | --- |
| `+0x00` | magic `0DRPz` |
| `+0x10` | u32 variant word |
| `+0x18` | u64 pointer |
| `+0x28` | u64 pointer to the blob descriptor table |
| `+0x30` | u64 pointer |
| `+0x38` | u32 descriptor count |
| `+0x3C` | u32 descriptor count, a repeat of `+0x38` |

The descriptor count is the low u16 of `root+0x3C`. The upper half of that word carries other bits and is not part of the count.

The virtual base is per resource, not global: `0x50000000` in `data.rpf` and `0x60000000` in `levels.rpf`. A pointer resolves as `ptr - base = offset inside the same resource`.

Pointer guards must not reject a resource for a zero or unusual value. Zero-length blobs and stub resources are normal, and a guard that is too strict loses the whole resource rather than one field.

## Blob descriptor table

One 12-byte record per blob, at the pointer held in `root+0x28`:

| Offset | Field |
| --- | --- |
| `+0x00` | u32 id |
| `+0x04` | u32 len |
| `+0x08` | u64 ptr, virtual |

The id is a type tag. Four ids carry text:

| Id | Contents |
| --- | --- |
| `0x10` | NUL-separated UTF-8 string pool |
| `0x101` | hash table, 0x10-byte records |
| `0xA8478889` | per-string offset blob |
| `0x99331089` | schema blob |

The four together are a localisation table. The `0x10` pool also appears on its own in resources that hold names rather than text, so the presence of a pool alone does not make a table.

Text sits in `data.rpf` and in `story000`, not in `data.rpf` alone.

## Classifier

A pool is accepted as a localisation table when all three tests pass:

| Test | Threshold |
| --- | --- |
| String count | at least 10 |
| Mean string length | at least 8 characters |
| Valid UTF-8 share | at least 0.90 of strings |

Each resource then gets one label:

- `table` when at least one pool passes all three tests.
- `weak` when pools exist and none passes.
- `binary` when no pool is found.
- `stub` when the blob descriptor table is empty.

When no blob declares `0x10`, the scanner falls back to content: at least 10 segments, 85 percent of segments valid graphic UTF-8 of 2 bytes or more, and a mean of 6 bytes or more.

Measured against labelled samples, the classifier scored precision 0.9355 and recall 1.0000 on 60 samples, and precision 0.9649 and recall 1.0000 on 2,000. The mean-8 rule produced no false positives on that set.

## Counts

The run covered four archives: `data`, `story000`, `story000_restofworld` and `packs`.

| Quantity | Value |
| --- | ---: |
| Streams scanned | 287,361 |
| `0DRPz` resources | 68,412 |
| Localisation tables | 25,834 |
| Strings | 7,289,933 |
| Strings readable | 99.91 percent |
| Invalid UTF-8 strings | 0 |
| Characters | 231,374,054 |
| Locale buckets | 13 |
| Throughput, data | 2,072 MB/s |
| Throughput, streams | 25,764 streams/s |

The `streams.kinds.psin` row in `data/counts.md` counts streams matched by signature in the full index. This run matches the `0DRPz` root magic inside four archives, so the two figures are separate measures and are not directly comparable.

## Locale assignment

Script ranges are tested first: Latin, Cyrillic, Greek, CJK, kana, Hangul, Arabic, Thai and Hebrew. A pool with enough non-ASCII text in one script is assigned that script's language directly.

Everything else is ASCII-folded and scored against stopword tables for seven Latin-script languages. The best score wins if it clears a 4 percent hit rate and at least two hits. `roa` labels Latin-script text that no stopword table claims, and `und` labels text with too little signal to call. The run produced 13 buckets.

## Determinism

Two runs over the same input produced an identical `tables.csv` SHA-1. The scan reads the bin store by content hash, so row order does not depend on filesystem order.

## Control case

One known localisation page inside `data.rpf` decodes to 471 strings with locale `en` and a readable ratio of 1.0. It is used as a decode check, not as a published sample.

## Limits

- The 32-bit record hash is not a hash of the text, so key names cannot be recovered from the hash alone and need a wordlist. UNVERIFIED.
- Continuation pages are not attributed. The known page drops 1,908 strings that continue onto a second page.
- 744 weak-pool streams were excluded. An inclusive mode raises recall and lowers precision.
- `roa` and `und` cover 475 pools and need a better Latin discriminator.
- Archives outside the four swept are unswept. They likely hold little text. UNVERIFIED.
