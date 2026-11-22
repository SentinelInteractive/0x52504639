# Reconstructed directory and name index

## What was built

A reconstructed directory and name index over carved payload streams from a shipping Xbox build that uses the RPF9 archive format. The index associates an inferred folder path and name with individual payload streams, and attributes each stream to the archive header that contains it. It is emitted as a plaintext index for research use.

## Limit of this output

The retail archive record tables are encrypted, and the table key is not held. This output is therefore not a game-valid table of contents. Every name carries a confidence level and is inferred from payload bytes; no name is read from an archived table.

## Aggregate counts

- 2,067,172 carved payload streams indexed
- 538,772 streams given a name - 26.06 percent
- 421,605 distinct inferred names
- 21,239 distinct inferred folders
- 4,325 containing archive headers catalogued, 4,095 of which hold at least one carved stream
- 133,337-token name pool
- 17,038 paths claimed by more than one stream

## Method

- Payload streams were carved from the archives and stored compressed. Each stream was decompressed and examined.
- A name pool was built from metadata sources and filtered to identifiers and path-shaped tokens. Anything containing a space was discarded, so that neither dialogue nor prose could enter the pool.
- Each stream's own payload was scanned for path-shaped and extension-bearing tokens. The highest-ranked candidate was kept and given a confidence level.
- Containing archive headers were attributed to streams by offset.
- A plaintext index is emitted for research and is marked as not game valid.

## Confidence levels

A stream receives at most one of these. `exact`, `path prefix` and `identifier` mean a name was inferred; `weak` means none was.

- **Exact** - the payload contained a path with a known file extension, or a path carrying the archive's own path prefix together with a known extension. This is the strongest evidence the format offers without the table key.
- **Path prefix** - the payload contained a path-shaped string without a known extension. The folder structure is supported; the file name is not.
- **Identifier** - the payload contained a single token and no path: an extension-bearing filename, a resource-type suffix such as a drawable or fragment marker, or an underscore-bearing identifier.
- **Weak** - no name evidence at all. Only a payload type was recorded.

The four counts are exhaustive across the corpus.

## Confidence split

- 21 exact
- 123,262 path prefix
- 415,489 identifier
- 1,528,400 weak

## Repeated names

A stream is a block, not a whole file. A large asset split across many blocks yields the same dominant name many times, once per block. The 17,038 repeated paths are therefore block splitting - one logical file distributed over many blocks - and not two different files competing for one path.

## What this is not

- Not a decryption result.
- Not a key.
- Not extracted game content.
- No assets.
- No dialogue.
- No strings published.
- Not a claim about nested archives: no carved stream begins at a nested archive header, so containment between nested archives is not represented. Nested headers are archive framing, not payload.
