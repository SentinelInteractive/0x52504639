# Content inventory

The dump is 108 files and 223.88 GB. It contains 22 RPF archives and 57 TTPF texture databases, plus supporting libraries and manifests. Every number here is an aggregate over that corpus. No path, resource name or extracted value is published in this repository.

## Archive layer

| Quantity | Value |
| --- | --- |
| Valid RPF9 headers | 4,330 |
| Headers inside the 12 top-level archives | 2,536 |
| Headers inside the `pack` containers | 1,794 |
| Declared entries, directories included | about 1,254,994 |
| Carved streams indexed | 2,090,676 |
| Ratio of streams to declared entries | 1.666 |
| Unique streams by content hash | 2,090,498 |
| Duplicate rows | 178, which is 0.0085 percent |
| Expanded bytes for all streams | 334.55 GB |
| Compressed bytes on disk | 97.53 GB |

Streams are indexed first and stored second. Each index row holds the offset, compressed size, uncompressed size, kind and content hash, so any stream can be identified by content and re-extracted from the archive that holds it. The duplication rate is low enough that keying the store by content would not pay for itself.

## Stream kinds

| Kind | Streams | Expanded |
| --- | ---: | ---: |
| Binary | 2,067,172 | 334.12 GiB |
| PSIN | 18,249 | 0.24 GB |
| XML | 3,454 | 0.15 GB |
| RBF0 | 1,264 | 0.01 GB |
| Text | 537 | 0.03 GB |

The binary row is stored now, so extraction is no longer the open problem. Classification is: a drawable-page probe decoded 2 of 13 sampled streams, which puts a per-kind signature set at the top of the queue.

## Bin store

All 2,067,172 binary streams are held in one local store, compressed with zstd. The binary row is no longer a set of offsets that has to be re-extracted before it can be read.

| Quantity | Value |
| --- | --- |
| Streams stored | 2,067,172 |
| Stored size | 102.60 GiB |
| Raw size before compression | 334.12 GiB |
| Compression ratio | 3.26 |
| Segments | 40 |
| Files | 132 |
| Largest file | 4.29 GB |

Storing the streams raw was rejected on disk budget. 334.12 GiB of uncompressed stream data does not fit alongside the corpus it came from, and the compressed form is under a third of it.

Bin-store sizes are binary units: 102.60 GiB stored and 334.12 GiB raw. The exact byte counts are in `data/catalog-summary.json`.

Every row read back clean, with 0 inflate failures, 0 SHA-1 mismatches and 0 overlapping byte ranges. The check ran over 200 random rows, then 2,000, then 200 more read independently of the index.

The writer is Rust and reaches 91 MB/s, or 1,294 streams per second. An earlier Python pass ran at 9.8 MB/s and was stopped at about half, before the writer was ported under the project's language policy.

This is a local store on one machine, not a distributed system, and no part of it is published here. The counts above describe what the store holds.

## Per-archive totals

| Container | Headers | Declared entries | Carved streams |
| --- | ---: | ---: | ---: |
| `levels` | 2,038 | 526,525 | 1,074,852 |
| `pack` story container | 437 | 160,077 | 140,326 |
| `pack` BVH container | 1,261 | 295,223 | 497,090 |
| `anim` | 235 | 84,938 | 129,678 |
| `packs` | 60 | 80,470 | 128,271 |
| `navmeshes` | 29 | 64,779 | 71,338 |
| `data` | 42 | 23,075 | 28,016 |
| `audio` | 104 | 7,283 | 838, plus 7,248 banks found by signature |
| `textures` | 21 | 1,387 | 1,233 |
| `script` | 3 | 1,016 | 914 |
| `common` | 1 | 418 | 954 |
| `shaders` | 1 | 3 | 4,204 |
| Other `pack`, `movies` and `appdata0` | 98 | 9,800 | 12,962 |

The audio row is the worked example of carving without a directory. There are 7,283 declared entries and 7,248 audio banks found by their signature, so 99.5 percent of entries are accounted for with no table.

## Textures

| Quantity | Value |
| --- | --- |
| TTPF databases, files | 57 |
| TTPF databases, distinct | 46 |
| Texture descriptors, files | 357,115 |
| Texture descriptors, distinct | 352,461 |
| Chunks, files | 1,026,947 |
| Chunks, distinct | 1,014,545 |
| Virtual size, files | 151.59 GB |
| Virtual size, distinct | 149.24 GB |
| Chunks extracted | 446,808 |
| Extracted size | 65.12 GB |
| Texel bytes reachable in software | 88.91 percent |
| BCPack texel share, hardware only | 11.09 percent |

## Audio

There are 71,686 signature hits for the audio container magic and 69,679 banks parsed, for 16.57 GB. Of the parsed banks, 65,683 report 48 kHz, 202 report 32 kHz, and 3,781 report no rate. The codec byte is zero for 69,542 banks, with a small tail of other values.

## Video

There are 1,273 container candidates and 797 validated videos, for 13.52 GB. Resolutions are 277 at 1280 by 720, 199 at 1920 by 1080, 168 at 720 by 1280, 36 at 2560 by 1440, plus 1024 by 1024 and 512 by 512 sets. Frame decode is not implemented.

## Serialized metadata

- 18,249 PSIN resources, holding 166,332 unique strings, 1,272 path-like tokens and 81,292 identifier-like strings.
- 3,454 XML documents and 4,443 unique paths, of which 2,295 use a `platform:` prefix, 1,156 a `$(target)` prefix, 815 `$(common)`, 101 `$(root)` and 76 `common:`. About 600 distinct root elements are present.
- 1,264 RBF0 blobs holding 20,651 unique UI names.

These counts are the reason the corpus is close to self-describing. The names a directory would supply are largely already inside the payloads.

## Localisation

15,672 candidate streams carry the localisation container magic, and 6,707 of them hold readable text. All 17,128 section headers found begin with the same magic. The remaining streams are structurally identical but hold a blanked header rather than a table.

The text itself is not published here.

## Models and map

- 447 models exported from a 224 MB sector of the `levels` archive, 446.6 MB of OBJ.
- One static level-of-detail block exported 317 geometries, 877,973 vertices and 506,828 triangles in under half a second.
- A 16 MB slice exported 73 terrain models from one tile. Each tile holds 64 entries at 64 by 64 local extent, and seven tiles give 1,512 entries.
- The 64 entries per tile are meshlet batches, not sub-tiles. Placing them on an 8 by 8 grid creates 64-metre walls; unioning them at a single origin with the scale applied gives a coherent tile.

## World heightmap

The heightmap resource is 2048 by 2048 pixels. Its bounds are x from -13000 to 7000 metres, y from -9000 to 11000 metres and z from -50 to 500 metres, with elevation from -9.0 to 400.8 metres. Land is 9.6 percent of the surface.

Seven per-tile heightmaps at 1024 by 1024 exist alongside it, with matching PNG output.

## Placement

The `levels` archive holds 2,244,675 entity records in 28,518 blocks across 28,516 resources, plus 24,886,645 prop instances and 219,484,361 grass instances in 910,151 batches. `docs/placement-resources.md` describes the layouts.

## What is missing from this picture

Navmesh, animation and shader coverage are counted as carved streams only: 71,338 navmesh, 129,678 animation and 4,204 shader streams. Their formats are not decoded, so no content claim is made beyond the stream count.
