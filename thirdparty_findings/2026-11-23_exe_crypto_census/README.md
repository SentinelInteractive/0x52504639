# Third-party measurement note — executable crypto material (external copy)

Reviewed 2026-11-23; **revised after maintainer review** (thanks, maminka19482). The original
version of this folder carried a scanner; it is **withdrawn from this PR** — this is a
doc-only note, as requested. The scanner's single wrong value is stated below with its cause,
because the correction is the useful part.

## Results (measurements on an external v1.0.2.1 copy; no game content included)

| Probe | Result |
|---|---|
| The 32-byte archive anchor (`5f08daab…d8aa6989`), six byte-order forms | 0 hits in all forms |
| AES forward S-box (full / 64 B / 32 B) | 0 hits |
| **AES inverse S-box** | **exactly one occurrence at file offset `0x5FC2950`** (in `.rdata`, inside a high-entropy band); head `52 09 6a d5 …` |
| SHA-256 K block | 2 occurrences (`0x5F446B0`, `0x5FC3CE0`); the second is adjacent to the inverse S-box — consistent with a crypto-library data region |
| ChaCha `expand 32-byte k` (raw + ASCII) | 0 hits |
| AES-NI opcodes in `.text` vs `.pdata` control | aesenc 126, aeskeygenassist 31, aesenclast 9, aesdec 13, aesdeclast 4; control all zero |
| ±32 KiB around the inverse S-box | no companion T-table permutations, no zero-flanked 96–320 B key-like islands |

Reading, narrowly: the binary contains real AES-capable machinery (hardware-accelerated
sites plus one software inverse box) and does not contain the anchor constant as a literal.

## The correction (kept visible on purpose)

The first submission reported the inverse S-box at `0x5FC1267`. That was a **scanner
artifact**: its windowed loop advanced the read base by `window − 255` while the file
handle advanced a full `window`, so any offset past the first 4 MiB was short by
255 bytes × 23 windows = `0x16E9`. `0x5FC1267 + 0x16E9 = 0x5FC2950`, and a byte-exact
check at `0x5FC2950` matches the inverse S-box on all 256 bytes. A corrected full-file
scan (fixed advance, deterministic, twin-run identical) finds exactly one occurrence.
Two further defects the reviewer caught — a malformed hand-typed SHA-256 constant
(now derived from the published words) and a ChaCha constant typo — changed results:
with correct constants the SHA-256 table appears twice, as tabled above.

## Scope and provenance

Static reads only, on an owner-controlled copy; single target binary; fourCC census and
import/export material deliberately not included here (out of this repository's scope).
The withdrawn scanner and its corrected successor stay in the originating project; this
note records only the measured values and the correction.
