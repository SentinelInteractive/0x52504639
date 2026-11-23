# Third-party static census — game executable crypto-relevant material

Brought in from outside as a *fact about the binary side of the same problem*, offered because
`docs/cipher-constraints.md` ends with "what a future key must satisfy" and names H2/H3 as the
surviving shapes. If anyone ever goes looking for *where* such a key could be derived, this is a
starting map of the executable's crypto machinery — measured statically, on the owner's own copy.
Nothing here is a key, key material, or game content; it is a census of code and constants.

AI-assisted (Claude Code); the scanner is the methodology and regenerates everything below.

## How to reproduce

```bash
python3 -I exe_crypto_fingerprint_scanner.py /path/to/game_scarlett_master.exe
```

Stdlib-only, windowed (4 MiB), writes `exe_crypto_census.json` beside itself. Arguments: the
executable path. It touches nothing else.

## Results (plain PE32+ x64, ~115 MiB, 10 sections, machine 0x8664)

| Probe | Result |
|---|---|
| The 32-byte archive anchor (`5f08daab…d8aa6989`), six byte-order forms (raw/reversed/4-byte-swap/8-byte-swap/low-16/high-16) | **0 hits, all forms** — consistent with your determinism result that read this region as plaintext sentinel+tag rather than key material |
| AES forward S-box (full / 64 B / 32 B) | 0 hits |
| AES **inverse** S-box | **exactly 1 occurrence @ raw file offset `0x5fc1267`** (`.rdata`, inside a multi-KB high-entropy band) |
| SHA-256 K-block head, ChaCha `expand 32-byte k` (raw + ASCII) | 0 hits |
| AES-NI opcodes, `.text` vs `.pdata` control | aesenc **126**, aeskeygenassist **31**, aesenclast 9, aesdec 13, aesdeclast 4 — `.pdata` control **all zero**, so the cluster is signal, not scanned-opcode noise |
| ±32 KiB context dig around the inverse S-box | no companion T-table permutation boxes, no zero-flanked 96–320-byte expanded-key islands, no XXTEA delta words |
| fourCC census (ASCII / LE-stored) | PSIN 3/3, RPF 0/4, ETPF 2/0, RBF0 2/0, KB2 1/0, RDS5 1/0 |

Reading, stated narrowly: the executable carries a real AES-capable pipeline
(hardware-accelerated, with a software inverse box suitable for a decrypt-only bootstrap
path), and it does **not** hold a static blob matching the anchor constant in any byte order.
So the key question is not "is it a literal in the binary" but "how is it built at runtime",
and the call sites above are where that would be answered.

## Companion archive-side numbers (our copy, offered as an independent data point)

- Constant-as-key battery (13 candidate keys × ~16 cipher modes incl. AES ECB/CBC/CTR-family,
  RC4, ChaCha, Salsa, XXTEA, Camellia, SM4, Blowfish, IDEA, SEED, 3DES, CAST5; ~2,000 trials):
  null beyond controls — random-key null mean 0.216 / sd 0.021 / max 0.304 (n=400), positive
  control 0.735 (roundtrip-asserted), best real 0.321 at the noise edge. Compatible with your
  39,491-combination matrix finding no hits.
- Independent corroboration of the trailer structure on a separate v1.0.2.1 copy: two containers
  with matching `(w24, w20_hi, w0c)` share exactly the first 32 trailer bytes and diverge from
  byte 32; trailer length `w0c` observed as 64/128/144/240 across six headers. No claim about
  contents, no names included.
- Cross-repo coherence worth knowing (no action requested): sibling repo `JoshRob297/rpf9-research`
  measures the `[w08..w04)` span as 9-or-10 bytes per declared entry, padded to 16. Expressed in
  16-byte cells that is ≈0.56–0.625 cells per entry, whose inverse is ≈1.6 — the same figure your
  `docs/cipher-constraints.md` states as the "directory ratio of about 1.6 for top-level archives"
  in condition 3 of *what a future key must satisfy*. The two projects appear to be measuring the
  same packing in different units; flagging it only in case reconciling the wordings is useful.

If any of this conflicts with what your tooling sees, that mismatch is the interesting part —
please say so and we will chase it.
