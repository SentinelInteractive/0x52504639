# Real geometry district render

Status: local text-only proof. No images, assets, path lists or model names are published.

## Result

A coastal district block was assembled from placements and decoded drawables, then rendered on the CPU.

- **59 pieces**: 29 structural, 20 ground, 10 building shells.
- **1,026,413 vertices, 1,063,486 triangles, 1,347 geometries.**
- Ground is a terrain height-patch resource family on a 64-unit lattice, with **244 of 244** dual-key placement matches.
- **33 distinct BC1/BC7 diffuse surfaces**, 109.6 MB RGBA, 954 of 1,033 catalog hits.
- Seams: ground to structure **0.000158 world units**; tile to tile **0.005898**; two shipped off-lattice patches reach 3.475.
- CPU render at 1280x720, 16.5 s wall, 2.73M input triangles per second.
- 113 of 1,347 geometries are textured. The layered terrain blend (render bucket 2) is not implemented.

## Method

- Placements join to drawables by archetype hash and TOC name hash.
- World transforms come from the placement records, not hand placement.
- Seam test: boundary edges are binned on a 0.001-unit grid to find duplicate topology, then original unrounded positions are compared.

## Limits

- No images or game assets are published.
- The layered terrain blend, the `0x80` ground-versus-structure flag and the two off-lattice patches remain open.
- This is a local render of decoded geometry, not a game-loadable scene.
- The counts are from one district block, not an install-wide map census.
