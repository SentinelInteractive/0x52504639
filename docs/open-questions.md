# Open questions

This page lists what is unresolved, what would settle it, and what cannot be settled from the files we hold. It is kept short on purpose.

## The table cipher

The exact cipher is unknown. ECB, CBC and XTS remain possible, and no test distinguishes them from ciphertext alone because no two archives share table plaintext past byte 48.

What would settle it: a correct key, applied to a table, producing a plaintext whose first 16 bytes are identical across archives and whose records decode as offsets and sizes. That is a stronger test than any block-level oracle.

A custom block cipher in the earlier-title lineage is also possible. It would look identical to AES in every structural test run so far, because the tests measure geometry, entropy and repetition rather than round constants.

## The `0x40` region

Whether the format tag at `0x50` is plaintext or ciphertext of a constant descriptor is unresolved. The determinism result makes both readings consistent, and the tag follows the version tuple either way.

What would settle it: a decryption of table 1 that either exposes the tag as a plaintext field, or exposes a constant descriptor whose ciphertext matches.

## The trailer

The trailer is a multiple of 16, has repeated and all-zero blocks, and is not locked to the entry count. Its meaning is unknown, and so is the split offset's role beyond marking the table boundary.

What would settle it: a decrypted table whose last records point into the trailer, or a key that decrypts a trailer block into a recognisable structure.

## Entry layouts

Both tables hold 16-byte records, and the record structure inside them is unknown. Table 1 scales with the name payload and table 2 holds roughly one record per entry, which constrains the layout but does not reveal it.

## Stream classification

Of 2,067,172 binary streams, only a sample has been identified by kind. A drawable-page probe decoded 2 of 13 sampled streams.

What would settle it: a per-kind signature set built from decoded samples, then a classification pass over the index. This is the highest-yield open item, because everything downstream depends on knowing what each stream is.

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
