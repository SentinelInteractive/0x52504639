# LOD links and interior separation

The 1:1 world now resolves LOD parent links and separates interior placements
from the exterior draw pass, so distance no longer thins the map down to
nothing.

## What is verified

One full archive pass, release build, cached result reused after the first run:

| Item | Count |
|---|---|
| Map files parsed | 167,492 |
| Placements indexed | 2,234,982 |
| LOD links resolved | 1,009,215 |
| Placements kept out of the exterior pass (interior) | 531,072 |
| HD placements capped at their LOD distance | 711,517 |
| LOD substitute placements | 418,484 |

Link resolution is positional, not nominal: a child declares a parent with an
index and an instance slot, the parent file is found by where the instances
sit, and the pair is accepted only when the instance position matches the child
within 0.5 m in a 256 m grid. Batch instance ranges resolve through the
container's own pool reference and tile the instance block exactly (58,357 of
58,357 rows in a 512 MB probe with no overlaps), and 95 % of batches keep every
instance inside their own bounds.

Interiors are classified from resource structure, not from decoded rooms: a
file carrying interior archetypes is treated as interior, everything else as
world. The split is live-toggleable at run time and by environment variable.

## What is inferred

- Level 5 placements are drawn as high detail. The stored level is real; the
  meaning "orphan high detail" is inferred from behaviour, not from a
  documented enum.
- Interior membership is per file. A file that mixes world and interior
  content contributes its placements to the world pass.
- LOD switch distances come from the placement when it declares one, otherwise
  from the archetype. The archetype fallback matches observed behaviour; the
  exact blend curve is not reproduced.

## Effect

Placements whose parent resolved now draw the high-detail model inside their
LOD distance and the substitute beyond it, instead of both being drawn and the
far field being dropped when the geometry budget runs out. The far view keeps
buildings that previously vanished, at a fraction of the triangle cost.
