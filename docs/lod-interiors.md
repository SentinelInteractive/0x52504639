# LOD links and interior separation

The 1:1 world now resolves LOD parent links and separates interior placements
from the exterior draw pass, so distance no longer quietly drops geometry.

## What is verified

One full archive pass, release build, result cached and reused afterwards:

| Item | Count |
|---|---|
| Map files parsed | 167,492 |
| Placements indexed | 2,234,982 |
| Placements that declare a parent | 1,267,804 |
| LOD links resolved | 1,009,215 |
| Placements classified as interior | 531,072 |
| Drawable interior placements kept out of the exterior pass | 38,684 |
| HD placements that switch to a drawn substitute | 373 |
| Substitute placements streamed | 2,146 |

Link resolution is positional, not nominal. A child declares a parent with an
index and an instance slot; the parent file is found by where the instances
sit, and the pair is accepted only when the instance position matches the child
within 0.5 m in a 256 m grid. Batched instance ranges resolve through the
container's own pool reference and tile the instance block exactly: in a
512 MB probe, 58,357 of 58,357 rows were claimed once with no overlap, and
95 % of batches kept every instance inside their own bounds.

Interiors are classified from resource structure, not from decoded rooms or
portals. A file that carries interior archetypes is treated as interior,
everything else as world. The split is live-toggleable at run time and by
environment variable.

A 6 minute run at the release build completed without a panic: 62 to 68 fps,
9.0 M triangles submitted, 6.5 to 6.8 GB of texture plus geometry residency,
10.5 to 11.1 GB peak dedicated GPU memory.

## What is inferred

- Level 5 placements are drawn as high detail. The stored level is real; the
  meaning "orphan high detail" is inferred from behaviour, not from a
  documented enum.
- Interior membership is per file. A file that mixes world and interior
  content contributes its placements to the world pass.
- Switch distances come from the placement when it declares one, otherwise
  from the archetype. The archetype fallback matches observed behaviour; the
  exact blend curve is not reproduced.

## Limits, stated plainly

An HD placement is only capped at its LOD distance when a substitute with a
real drawable model exists on it, so the far field can never be emptied by the
capping rule. That conservative gate is why only 373 placements switch, and
why the default camera pose, looking out over water, shows no visible
difference yet: no substitute placement falls inside the draw radius there.
The mechanism and its counts are verified; the visible far-field gain at a
populated pose is not yet demonstrated.

Interior separation is the larger measured win: 38,684 drawable interior
placements no longer compete for the geometry and triangle budgets with the
exterior.
