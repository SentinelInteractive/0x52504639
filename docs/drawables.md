# Drawable and BVH resources

Status: read and extract path verified. No game content is published.

## Types

The `+16` word in a 20-byte resource record is the RAGE resource type enum. Two large geometry types:

| Code | Name | Slots | Stored bytes | Logical bytes |
|---|---|---:|---:|---:|
| `0x02` | zdr | 167,897 | 46,719,905,568 | 100,362,894,768 |
| `0x0f` | zbdr | 250,434 | 7,335,183,152 | 124,157,781,744 |

## zdr

`zdr` is the drawable. The verified path covers:

- the page-resource container and block map;
- the drawable model and LOD list;
- packed vertices and meshlet indices;
- the shader group, material array and texture IDs;
- skeleton and skin references where present.

A single-LOD drawable exported to OBJ. A textured sample exported to OBJ/MTL with 186 vertices, 294 triangles, one material and 4 of 4 texture IDs matched; its diffuse surface decoded.

## zbdr

`zbdr` is **not a mesh**. It is a serialized Xbox raytracing **BVH4**, registered by the game as `BvhDrawableStore`.

- It stores bounds and triangle references into a companion `zdr`.
- Eight sampled payloads decoded. One BVH referenced two triangles; its fingerprint-matched `zdr` companion decoded to four vertices and two triangles with exactly matching bounds.
- Four of five same-name fingerprint pairs passed.
- 128,160 `zbdr` slots share a TOC name hash with a `zdr`, including all 126,746 dictionary-resolved slots; none match top-level `zdd`.

The remaining gap is the runtime ordering of the build descriptor's geometry array. The consumer path is traced; the producer is not.

## District render

A coastal district block was assembled from placements and drawables: 59 pieces, 1,026,413 vertices, 1,063,486 triangles. Seams: ground to structure 0.000158 world units; tile to tile 0.005898. See the map-render note for the full numbers.

## Write status

Both types are **W0 extract-only**. No resource encoder or round-trip is verified. The BVH is read-only.

## Limits

- The drawable writer, the shader variant matrix and the skin-binding completeness remain open.
- The type census classifies headers and bounded prefixes, not full payloads.
- No asset, image or name list is published.
