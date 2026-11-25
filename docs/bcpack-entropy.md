# BCPack texture compression: measured format facts

Scope: format research on a single lawfully obtained copy of the software.
Nothing here is a decoder, a format specification, or a recipe for one. No game
asset, no probability table, no lookup table and no decoded texture is published
or shipped.

## What BCPack is

BCPack is the Xbox Series X|S Media Decompression Unit (MDU) entropy codec in
front of block-compressed GPU textures (BC1 to BC7). In the chunk table the
codec id is the block format number times four, so BC1 is 0x04, BC3 0x0C, BC5
0x14, BC7 0x1C. The entropy layer is rANS over a fragment stream: the coding
tables are static, sixteen probability models are selected per fragment with no
per-chunk frequency header, a 2-byte or 3-byte fragment header selects the model,
narrows the symbol width, carries a state-reset flag and gives the payload
length, and the payload is a 32-bit rANS state machine with 8-bit
renormalisation and a hard lower state limit. A fragment boundary is a
state-machine boundary, not a byte-alignment convention. A decoded chunk of N
blocks has a fixed length per codec (N times 8 bytes for BC1 and BC4, N times 16
for BC3, BC5, BC6H and BC7), independent of compressed size.

## Measured coverage

Across the 57 texture databases held, there are over a million texture chunks.
108,605 are BCPack, carrying 16,795,893,760 bytes of decoded (virtual) texture:
BC1 102,725 chunks, BC3 35, BC4 77, BC5 333, BC6H 268, BC7 5,167. BC2 has none.
Only 0.646% of BCPack payload bytes are zero and no chunk is entirely zero.

An earlier census covered 46 of those databases: 105,845 BCPack chunks,
12,152,348,416 compressed bytes on disk, 16,356,958,208 bytes decoded, a share
of 10.9599% of the decoded texture byte stream by virtual size at 0.743
compressed/virtual. That share is left as measured over those 46 databases; the
counts above are current. An earlier 11.09% included a trailing all-zero table
sentinel the parser now drops, and was corrected downward by 0.13 percentage
points rather than retracted: the sentinel was a parser artefact.

## The container layout, now settled

A chunk is one byte stream shared by a fixed number of lanes: 12 for BC1, BC3,
BC4 and BC5, and 16 for BC6H and BC7. Every lane emits one symbol per 8 virtual
bytes, so a lane's symbol count is the decoded length divided by 8. Five rules
describe the stream completely.

1. Each lane has a constant symbol width per block format, and a 2-bit field in
   each fragment header narrows it. The width is per-lane and per-codec, not one
   global value: for BC1 the twelve widths are 8, 8, 5, 6, 5, 5, 6, 5, 8, 8, 8,
   8. The probability model follows from the narrowed width and a 4-bit model
   index in the same header byte.
2. A lane requests one byte whenever its 1-byte input buffer is empty and it
   still has payload to read. Requests are served from the shared stream in lane
   index order, at most 8 bytes per clock; a lane not served does nothing for
   that clock.
3. Output is in lockstep. Each lane holds one symbol in a slot, and all slots
   are released together once every lane still active holds one.
4. A fragment with the reset flag ends when its payload is exhausted and its
   state is back at the lower limit; the next byte in that lane is a new header.
   A fragment without the flag instead drains symbols from its residual state,
   with no further input, until the state reaches the limit.
5. A payload may end with the state trimmed to the limit shifted right by one or
   two bytes, because the encoder may drop up to two trailing zero bytes. That
   boundary must be accepted, not treated as an error.

The layout looks like a fixed eight-lane interleave for the first 48 bytes of a
chunk and nothing like it afterwards. While every lane is filling its header and
4-byte initial state, the lower-numbered lanes win the 8-byte budget on every
clock, so the first 48 bytes are lanes 0 to 7 in stride. Once those lanes are
decoding they request a byte only when they need one, and the remaining lanes
take the budget. Reading a whole chunk as a fixed stride assigns every byte after
the first 48 to the wrong lane, which is what earlier revisions were doing.## Evidence

* 108,605 of 108,605 chunks decode with every lane present, every lane at
  exactly its symbol count, and the stream consumed to a zero pad. Zero
  failures, 46 distinct databases across 57 files, all six codecs in use.
* For a sample spanning both lane counts and four codecs, the decoded symbol
  streams are byte-identical to an independent public implementation's. That is
  agreement between implementations, not ground truth against hardware.
* For BC1, BC3, BC4 and BC5 the public block layouts require one specific lane
  to be zero, and for BC7 they do not. The decode gives zero in 119 of 119
  chunks of the first group and non-zero in all 27 chunks of the second.

## The block layer

Blocks come out in stream order, which is the surface's native tiled order, so a
decoded chunk is de-tiled with the standard Gfx10 layout before display. Only BC1
is assembled. Lane 0 carries a back-reference distance of at most 255 blocks;
lanes 2 to 7 carry zigzag corrections to the six 5/6/5/5/6/5-bit endpoint
components modulo their widths; lanes 8 to 11 carry one 2x2 index quadrant each.
A reference pointing before block 0 reads a fixed 256-entry predictor window, and
the 256 quadrant patterns are selected through a fixed permutation. Both are
fitted constants, fitted by other projects, not published by us and not
reproduced here.

One 128 by 1024 BC1 surface was decoded end to end as a check on the pipeline:
4,894 distinct colours and a mean adjacent-pixel delta of 7.50, against 26,594
colours and 52.80 for 64 KiB of uniform noise on the same metric. That validates
the entropy layer and the block assembly, not the fitted tables. BC3, BC4, BC5,
BC6H and BC7 block layers remain open; BC3 and BC5 are an endpoint or colour half
plus 3-bit index rows and need their own fitted index tables.

## Corrections to earlier revisions

1. That a BC5 block needs at least 16 lanes. It needs 12, two elements per block.
   The 16-lane count belongs to BC6H and BC7.
2. That a mode-bit distribution of 0.698 was a BC1 noise baseline. That value is
   a unit-normal test for BC5 surfaces; the BC1 three-colour share for uniform
   noise is 0.4989.
3. That the byte scheduler was the remaining mismatch once the arithmetic
   closed. It was not; the lane count and the demand-driven feeder had been read
   as a fixed stride.

## What is not claimed

The probability tables, the fitted block-layer tables and every decoded texture
stay private, and no decoder is distributed. No fidelity figure is offered for
BC3, BC4, BC5, BC6H or BC7, and no comparison with any community or commercial
tool is made. No licence is granted or implied: the codec is patent encumbered
and nothing here describes the scope of any claim.
