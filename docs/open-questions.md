# Open questions

This page lists what is unresolved, what would settle it, and what cannot be settled from the files we hold. It is kept short on purpose.

## The table key

The cipher is no longer an open question. The tables are enciphered by a 13-round construction of the AES family in CBC mode, with a static initialisation vector on the first stage and per-archive vectors after it, as recorded on the cipher page. Standard AES is 10, 12 or 14 rounds depending on key size and is not this construction.

What remains open is the key. It is not published here, and no key in this repository has been validated against known plaintext. The key schedule comes from material carried by the executable, and none of that material is published.

What would settle it: a correct key that decrypts a table into a plaintext whose first 16 bytes are identical across archives and whose records decode as offsets and sizes. That is a stronger test than any block-level oracle.

## Validating a decryption

A decryption attempt can produce plausible bytes without being correct. Several candidate outputs in this work have done exactly that, and they are recorded as failed rather than used as input. The bar is the four conditions on the cipher page, not a block that looks reasonable.

## The `0x40` region

Whether the format tag at `0x50` is plaintext or ciphertext of a constant descriptor is unresolved. The determinism result makes both readings consistent, and the tag follows the version tuple either way.

What would settle it: a decryption of table 1 that either exposes the tag as a plaintext field, or exposes a constant descriptor whose ciphertext matches.

## The trailer

The trailer is a multiple of 16, has repeated and all-zero blocks, and is not locked to the entry count. Its meaning is unknown, and so is the split offset's role beyond marking the table boundary.

What would settle it: a decrypted table whose last records point into the trailer, or a key that decrypts a trailer block into a recognisable structure.

## Entry layouts

Table 1's record structure is unknown. Table 2 records are 9 or 10 bytes rather than 16, with the width set by the entry count, and their fields are not decoded. Table 1 scales with the name payload and table 2 holds records at the declared count where the container page says the length formula holds, which constrains the layout but does not reveal it.

## Stream classification

Of 2,067,172 binary streams, only a sample has been identified by kind. All of them are now in the bin store, so the kind is the unknown rather than the bytes. A drawable-page probe decoded 2 of 13 sampled streams.

What would settle it: a per-kind signature set built from decoded samples, then a classification pass over the index. This is the highest-yield open item, because everything downstream depends on knowing what each stream is.

## Localisation tables

Grouping is settled. A localisation table is the blob combination `0x10`, `0x101`, `0xA8478889` and `0x99331089` inside a `0DRPz` resource, and `docs/drpz-localisation.md` records the layout, the descriptor rule and the classifier. Three caveats remain.

Continuation pages are not attributed to the page they continue, so their strings are dropped rather than merged. The known page loses 1,908 strings this way. What would settle it: a page-link field, or a rule that binds a continuation by the hash table order rather than by position.

The 32-bit record hash is not a hash of the text. Key names cannot be recovered from it, so readable key names need a wordlist to test candidates against. This is UNVERIFIED and no candidate has been confirmed.

Locale assignment is a heuristic. `roa` and `und` hold 475 pools between them and need a better Latin discriminator. The classifier also excludes 744 weak-pool streams, and an inclusive mode raises recall at the cost of precision.

## Placement assembly

Entity, prop and grass records are readable. Turning them into a continuous world needs two things that are not solved: the 8 by 8 cell order within a tile, and the absolute origin of each tile.

Boundary matching is the working approach for the cell order, since adjacent cells share edge vertices. Heightmap cross-correlation is the working approach for the tile origin. Neither is finished.

## Formats not decoded

- CNavMesh: 71,338 streams carved, polygon decode not implemented.
- Animations and skeletons: 129,678 streams carved, clip dictionaries not decoded.
- Shaders: 4,204 streams carved, partial interpretation only.
- Video: 797 containers validated, frame decode not implemented.
- BCPack textures: hardware-only decode, 11.09 percent of texel bytes.

## What cannot be settled from our files

File names, directory structure and exact extents need the table key. Carving gives offsets and sizes but not names, and the name correlation between carving order and content is 0.993 in `script`, 0.897 in `data` and 0.722 in `levels`, which is far above chance but short of a directory.

The name-to-archive binding is a matching problem with fingerprints on both sides. It can narrow candidates. It cannot confirm one.

## Method notes that remain provisional

- The grass instance quantisation scale is unverified.
- Entity flags at `0x48` are not decoded.
- ETPF field `C` is stored but unexplained.
- The mip chain is counted but not rebuilt deterministically.
- The five ETPF descriptors with a nonzero `u3` are unclassified.

## Corrections

**2026-11-23: the cipher identity is removed from the open list.** This page previously opened with "the exact cipher is unknown" and listed ECB, CBC and XTS as equally possible. The cipher is a 13-round AES-family construction in CBC mode with a staged initialisation vector, as the cipher page records. The open item is the key and a validated decryption, and the section above now says that.

The entry-layout section also previously said both tables hold 16-byte records. Table 2 records are 9 or 10 bytes, and that line is corrected here rather than dropped.
