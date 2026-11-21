<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sentinel-lockup.png">
  <img src="assets/sentinel-lockup-inverted.png" alt="SentinelInteractive" width="340">
</picture>

# 0x52504639 Research Division

Research documentation, Project 0x52504639.

This repository publishes what we have measured about the RPF9 archive format that GTA VI uses, the TTPF texture database that ships beside it, and the parts of the content that can be read without decrypting the archive directory. It holds notes, catalogues and small tooling, so that the findings can be checked, cited and built on.

We work from a copy of the game we own. We do not distribute game assets, keys, key material or executables, and nothing here is extracted content.

## What we know

The container is understood. A 64-byte header, two 16-byte-record tables and a trailer describe every archive, and the payload behind the header is plain zlib. Content is reachable without the table key, because the streams are found by structure and index rather than by directory lookup.

The archive directory is not solved. Both record tables are enciphered with one global key and a fixed initialisation, and that key has not been recovered. We describe the constraints on the cipher precisely enough that a future key can be tested against them, and we say which readings remain open instead of picking one.

Everything below was measured on a 223.88 GB dump of 108 files, which contains 4,330 RPF9 headers and 57 TTPF databases. Where a number comes from a subset, the document says so.

## Documents

| File | Question it answers |
| --- | --- |
| `docs/rpf9-container.md` | How is an RPF9 archive laid out, and what does each header field do? |
| `docs/ttpf-rds5-etpf.md` | How are RDS5 and ETPF structured, and how are texture chunks addressed? |
| `docs/cipher-constraints.md` | What has been ruled out for the table cipher, and what is still open? |
| `docs/placement-resources.md` | How are world entities, props and grass stored in the `0DRPz` resources? |
| `docs/content-inventory.md` | What content classes exist, and how much of each is reachable? |
| `docs/open-questions.md` | What remains unknown, and what would resolve it? |
| `data/counts.md` | The aggregate numbers, with the status of each. |
| `data/catalog-summary.json` | The same aggregates in machine-readable form. |

`assets/sentinel-lockup.png` is the lockup for a dark background, and `assets/sentinel-lockup-inverted.png` is the same lockup inverted for a light one.

## Headline numbers

- 4,330 valid RPF9 headers: 2,536 inside the 12 top-level archives, including nested ones, and 1,794 inside the `pack` containers.
- About 1,254,994 declared entries, directories included, against 2,090,676 carved streams.
- 57 TTPF databases holding 357,115 texture descriptors across 1,026,947 chunks, for 151.59 GB of virtual texture data.
- 69,679 audio banks, 797 validated videos, and 2,244,675 entity records in the `levels` archive.
- 88.91 percent of texture texel bytes are reachable in software. The remainder is hardware-compressed.

`data/counts.md` carries the full set and marks each number as measured or derived.

## Method

Streams are located by carving on zlib and container signatures at 16-byte seeds, then classified by signature and stored with offset, compressed size, uncompressed size, kind and content hash in an index. Texture chunks are addressed through the RDS5 chunk table and decoded through the ETPF descriptor table. Entity records are read through each resource's own block map, which resolves virtual and physical pages inside the zlib stream.

Nothing in that chain needs the archive directory. That is why the payload layer is complete while the table cipher is not.

## Snapshot check

`.github/workflows/refresh.yml` runs weekly and on demand. It validates `data/catalog-summary.json`, checks that the required documents are present, and writes `data/last-check.json` with the UTC date and the commit it checked. It commits that file only when it changes.

The job cannot re-dump the game. A runner has no game files, so the schedule dates and validates the published snapshot. It does not refresh the numbers. A new number means a local pass, a review, and a commit.

`scripts/publish.ps1` does that local pass from a checkout you name: it copies the sanitized docs in, runs the validator, and prints the git commands. It does not deploy anything.

## Layout

```text
README.md
NOTICE.md
LICENSE
assets/
docs/
data/
scripts/
.github/workflows/refresh.yml
```

## What is not here

- No game assets, no extracted dialogue, no path lists, no model or texture names, no content dumps.
- No keys or key material, and no discussion of recovering an executable.
- No viewer application source and no site source.
- No comparison with other projects, and no ranking of them. This repository states what we know.
- No download sources, and no instructions for obtaining the game.

## Licence and notice

The text and tooling in this repository are released under the MIT licence in `LICENSE`. `NOTICE.md` states the scope of the research and the trademark position.

GTA and Rockstar are trademarks of their respective owners. This work is not affiliated with or endorsed by them.
