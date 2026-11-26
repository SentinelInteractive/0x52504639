# `zscript` resources

Status: container, header and instruction boundaries verified on all 746 slots. No opcode semantics beyond a published opcode table, no control flow, no writer. No script contents, strings or names published.

## Identity

`zscript` is type code `0x59` from the engine's own type-name table.

- Structural identity, verified: a script payload whose inflated body is a stream of fixed-format instructions. Every instruction boundary and every operand extent follows from the opcode table alone, with no reading of script contents.
- Semantic identity, not claimed. The mnemonics are those of a published opcode table. No meaning beyond those mnemonics is asserted here.

## Counts

| Code | Slots | Stored bytes | Logical bytes |
|---|---:|---:|---:|
| `0x59` | 746 | 50,195,184 | 167,734,336 |

- All 746 slots decode to their declared logical sizes. No slot is truncated and no slot leaves bytes unaccounted for.
- These are the same 746 slots counted in the type census and in the full index.

## Container

Each slot is a 16-byte zero prefix followed by a chain of zlib streams. Measured on all 746 slots:

- 16 zero bytes at stored offset 0.
- A zlib chain after the prefix. Each stream is inflated in order.
- `logical == sum(inflated stream lengths)`: all 746 slots, no exceptions.

Header facts, offsets relative to the first inflated byte:

| Observation | Slots |
|---|---:|
| Header length field equals the value at `+0x24` | 746 of 746 |
| `+0x28` equals `+0x2C` | 746 of 746 |
| Body is at least `0x180` bytes | 746 of 746 |
| Code begins at `0x180` | 731 of 746 |

In the remaining 15 slots the code does not begin at `0x180`. The listing still consumes the body exactly in those slots.

## Listing

The listing decoder is built from a published opcode table. It maps each opcode to an instruction length and a set of operand fields. It does not interpret the operands.

| Measure | Value |
|---|---:|
| Opcode rows in the table | 530 |
| Operand fields | 439 |
| Instructions decoded | 32,703,447 |
| Code bytes consumed | 117,066,144 |
| Undecodable bytes | 0 |
| Slots whose boundaries consume the body exactly | 746 of 746 |

Instruction boundaries land on the end of the body in every slot. There is no leftover tail and no read past the declared length.

## Verification

- Container reconciliation reproduces 746 slots, 50,195,184 stored bytes and 167,734,336 logical bytes exactly.
- Whole-population header check reproduces the four observations in the table above, each on 746 of 746 slots.
- Whole-population listing check decodes 32,703,447 instructions over 117,066,144 code bytes, with 0 undecodable bytes and exact body consumption on 746 of 746 slots.
- Control: setting the opcode multiplier to 1 fails 745 of 746 slots. Boundaries no longer reach the end of the body.
- Control: disabling whitening fails 745 of 746 slots. The one specimen that still passes is an 8-byte all-zero stub.
- Caveat on the whitening control: whitening changes operand values, not instruction lengths. The whitening-off control therefore fails through a reserved-field invariant, not through boundary realignment. It is evidence that whitening is applied, not evidence that boundaries depend on it.

## Limits

- The decode covers boundaries and operand extents only.
- No opcode semantics beyond the published mnemonics. No control flow reconstruction, no basic blocks and no call graph.
- No writer. No round-trip, no re-encryption and no encoder is verified.
- No script contents, strings or names are printed or published.
