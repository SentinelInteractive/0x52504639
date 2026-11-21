# BCPack: entropy layer and measured coverage

BCPack is the entropy codec that sits in front of the block-compressed texture formats in the RDS5 texture databases. Of the texture formats in this corpus it is the one this project does not decode. This document records what has been measured about it, and what is still open.

Nothing here is a decoder, a format specification, a probability table or a decoded surface. None of those is published. The figures are measurements over the corpus this project holds.

## Where BCPack sits

A texture database carries a codec per chunk in its chunk table. The BCPack values select a block-compressed family rather than a deflate stream. A decoded BCPack chunk has a length fixed by its codec and its block count: 8 bytes per block for BC1 and BC4, 16 bytes per block for BC3, BC5, BC6H and BC7. Compressed size never changes the decoded size, which is what makes the virtual byte count a stable denominator.

The entropy layer is rANS over a fragment stream:

- The coding tables are static. There are 16 probability models, selected per fragment, with no per-chunk frequency header.
- A fragment carries a 2-byte or 3-byte header. The header selects the model, narrows the symbol width, carries a state-reset flag and gives the payload length.
- The payload is an rANS state machine with 8-bit renormalisation and a hard lower state limit, so a fragment boundary is a state-machine boundary rather than a byte-alignment convention.

## Coverage

Across the 46 distinct texture databases there are 1,014,499 texture chunks. That is 46 fewer than the 1,014,545 chunk rows on disk, and the difference is one leading ETPF descriptor chunk per database. 105,845 of the texture chunks are BCPack.

| Measure | Value |
| --- | ---: |
| BCPack chunks | 105,845 |
| Compressed bytes | 12,152,348,416 |
| Decoded (virtual) bytes | 16,356,958,208 |
| Share of decoded texture bytes | 10.9599 percent |
| Compressed to virtual ratio | 0.743 |

By codec the chunk counts are BC1 100,020, BC3 35, BC4 77, BC5 325, BC6H 268 and BC7 5,120. BC2 does not appear in this corpus.

An earlier figure of 11.09 percent was a virtual-byte share that counted a trailing all-zero table sentinel the parser now drops. The measure was corrected down by 0.13 percentage points. The sentinel was a parsing artefact, so this is a correction of a number, not a retraction of the method.

A descriptor-based cross-check attributes 8.6954 percent of mip 0 surface bytes to BCPack. That is a lower bound only, because 281,074 descriptors span more than one chunk, so the virtual length ratio above is the exact measure.

0.646 percent of BCPack payload bytes are zero. No BCPack chunk is entirely zero. The entirely-zero chunks that appear elsewhere in the chunk set are confined to the graphics database.

## Framing status

The container framing is partly recovered:

- Fragments are interleaved across lanes per round, rather than stored contiguous.
- Each chunk opens with a 4-byte big-endian initial state.
- The 2-byte and 3-byte header forms are mapped at field level, including both payload length encodings.
- The 16 probability models are static across the corpus.
- One byte is prefetched ahead of the first fragment.

The first fragment of a chunk closes exactly in 119 of 146 sampled chunks. What is not recovered is the renormalisation path that carries state across fragment boundaries, so a chunk cannot be run to its end.

No BCPack surface has been decoded end to end. No block-level, visual or fidelity claim is made here, and none should be inferred from the figures above.

## What is established

- The rANS arithmetic. The platform vendor publishes a reference implementation, and the decoding arithmetic, the state limits and the acceptance rules for a legal terminal state were reproduced against it on isolated fragments, with round-trip checks in both directions.
- The fragment header grammar at field level, and the two payload length encodings.
- The chunk census above, and the codec field mapping in the chunk table.
- That the chunk corpus has to come from the RDS5 chunk table. Chunk sets extracted by other means earlier in this work did not match the table, and measurements taken from those sets are void.

## What is open

- The renormalisation path across fragment boundaries. This is the blocker.
- Whether the partial framing holds across the whole corpus rather than the 146 sampled chunks.
- Decoded texel counts, per-codec fidelity and any surface equality check. Each of these needs a full decode.

## Redistribution

No decoder is distributed. No probability table set, no lookup table, no extracted or decoded texture and no reproduction of the codec tables is published in this repository.
