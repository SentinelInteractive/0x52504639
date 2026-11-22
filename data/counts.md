# Counts

Quick reference for the aggregate numbers. Measured means counted directly on the corpus; derived means computed from a measured value.

## Corpus

| Quantity | Value | Status |
| --- | ---: | --- |
| Files in the dump | 108 | measured |
| Size | 223.88 GB | measured |
| RPF archives | 22 | measured |
| TTPF databases | 57 | measured |

## Archives

| Quantity | Value | Status |
| --- | ---: | --- |
| Valid RPF9 headers | 4,330 | measured |
| Headers in top-level archives | 2,536 | measured |
| Headers in `pack` containers | 1,794 | measured |
| Declared entries | about 1,254,994 | measured |
| Carved streams | 2,090,676 | measured |
| Streams to entries ratio | 1.666 | derived |
| Unique streams | 2,090,498 | measured |
| Duplicate rows | 178 (0.0085 percent) | measured |

## Streams

| Kind | Count | Expanded |
| --- | ---: | ---: |
| Binary | 2,067,172 | 334.12 GiB |
| PSIN | 18,249 | 0.24 GB |
| XML | 3,454 | 0.15 GB |
| RBF0 | 1,264 | 0.01 GB |
| Text | 537 | 0.03 GB |
| Total | 2,090,676 | 334.55 GB |

Compressed on disk the same streams occupy 97.53 GB.

## Bin store

| Quantity | Value | Status |
| --- | ---: | --- |
| Bin streams stored | 2,067,172 | measured |
| Stored size, zstd | 102.60 GiB | measured |
| Raw size before compression | 334.12 GiB | measured |
| Compression ratio | 3.26 | derived |
| Segments | 40 | measured |
| Files | 132 | measured |
| Largest file | 4.29 GB | measured |
| Writer throughput | 91 MB/s | measured |
| Writer stream rate | 1,294 streams/s | measured |

Bin-store sizes are binary units: 102.60 GiB stored and 334.12 GiB raw. The exact byte counts are in `data/catalog-summary.json`.

Readback covered 200 random rows, then 2,000, then 200 more read independently of the index, with 0 inflate failures, 0 SHA-1 mismatches and 0 overlapping ranges. The store is local to one machine and is not distributed. An earlier Python writer ran at 9.8 MB/s and was stopped at about half.

## Textures

| Quantity | Files | Distinct | Status |
| --- | ---: | ---: | --- |
| Databases | 57 | 46 | measured |
| Descriptors | 357,115 | 352,461 | measured |
| Chunks | 1,026,947 | 1,014,545 | measured |
| Virtual size | 151.59 GB | 149.24 GB | derived |
| BC7 descriptors | 77,838 | | measured |
| BC6H descriptors | 1,025 | | measured |
| BC7 and BC6H size, mip 0 | 43.7 GB | | measured |
| BC7 and BC6H size, mip chains | 45.9 GB | | measured |
| BC7 and BC6H share of chain bytes | 35.76 percent | | derived |
| Software reachable | 88.91 percent | | measured |
| BCPack share | 10.96 percent | | measured |

## BCPack

The entropy layer is identified and the framing is partly recovered. No surface has been decoded end to end, and no decoder, table or texture is published. See `docs/bcpack-entropy.md`.

| Quantity | Value | Status |
| --- | ---: | --- |
| BCPack chunks | 105,845 | measured |
| Compressed bytes | 12,152,348,416 | measured |
| Decoded (virtual) bytes | 16,356,958,208 | measured |
| Share of decoded texture bytes | 0.109599 | derived |

The share is against the distinct-corpus virtual total. An earlier 11.09 percent included a trailing all-zero table sentinel that the parser now drops, so the figure moved down by 0.13 percentage points. Chunk counts here exclude the leading ETPF descriptor chunk of each database.

## Media

| Quantity | Value | Status |
| --- | ---: | --- |
| Audio banks parsed | 69,679 | measured |
| Audio size | 16.57 GB | derived |
| Banks at 48 kHz | 65,683 | measured |
| Banks at 32 kHz | 202 | measured |
| Video containers validated | 797 | measured |
| Video size | 13.52 GB | derived |

## Placement

| Quantity | Value | Status |
| --- | ---: | --- |
| Archives scanned | 22 | measured |
| Resources scanned | 290,294 | measured |
| Entity resources | 31,141 | measured |
| Entity blocks | 31,144 | measured |
| Entity records, de-duplicated | 2,281,720 | measured |
| Entity records, raw sum over blocks | 2,281,852 | measured |
| Prop instances | 24,886,645 | measured |
| Grass instances | 219,484,361 | measured |
| Batches, prop plus grass | 910,151 | measured |

## Localisation

Tables are `0DRPz` resources, and the layout is in `docs/drpz-localisation.md`. The run covered `data`, `story000`, `story000_restofworld` and `packs`.

| Quantity | Value | Status |
| --- | ---: | --- |
| Streams scanned | 287,361 | measured |
| `0DRPz` resources | 68,412 | measured |
| Localisation tables | 25,834 | measured |
| Strings | 7,289,933 | measured |
| Readable strings | 99.91 percent | derived |
| Invalid UTF-8 strings | 0 | measured |
| Characters | 231,374,054 | measured |
| Locale buckets | 13 | measured |
| Weak-pool streams excluded | 744 | measured |

No string from any table is stored in this repository.

## Cipher work

| Quantity | Value | Status |
| --- | ---: | --- |
| Headers checked | 4,330 | measured |
| Table-1 blocks examined | 1,227,740 | measured |
| Table-2 blocks examined | 538,176 | measured |
| Cipher and key combinations tested | 39,491 | measured |
| Attempts | 318,564 | measured |
| Compression decode attempts | 8,850,000 | measured |
| Keys in the zero-block oracle | 656,828 | measured |
| GTA V NG keys expanded | 101 | measured |
| GTA V NG construction variants | 64 | measured |
| GTA V NG evaluations | 25,856 | measured |
| GTA V NG hits | 0 | measured |
| Keys recovered | 0 | measured |

The last row is the state of the work. The container and the payloads are open. The directory is not.
