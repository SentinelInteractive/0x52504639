# Constraints on the table cipher

Both RPF9 record tables are enciphered. This page records what the ciphertext proves, what it rules out, and what a future key would have to satisfy. It does not contain a key, and it does not describe how to obtain one.

The aim is narrow. If a key is ever lawfully available, it should be testable in one pass against facts already measured, rather than re-deriving the model from scratch.

## Corpus

All claims here are checked against 4,330 headers unless marked otherwise. An earlier pass used a 663-header subset, which was 15 percent of the corpus and missed ten `pack` containers. Three statements from that pass are corrected and used in no conclusion below:

- The `0x40` to `0x60` region is not one 32-byte constant. It is a fixed 16-byte sentinel followed by a 16-byte format tag with four values.
- The generation word at `0x18` is `(gen << 16) | 0x7A00` with gen from 4 to 8, not the single constant `0x47A00`.
- The trailer is not locked to the entry count.

Extracted table bytes: 19,643,840 from table 1 and 8,610,816 from table 2 for the 663-header subset. The extended corpus holds 1,227,740 table-1 blocks and 538,176 table-2 blocks.

## The cipher is global and position-relative

The first 16 bytes of table 1 are byte-identical in all 4,330 headers. They are identical across 12 top-level archives, 10 `pack` containers, nested archives, a 76 GiB archive and a 6.6 MB one, and 19 version values spanning generations 4 through 8.

They do not vary with the archive id, the `0x28` field, the version, the flags, the entry count, the container, the nesting depth, or the absolute file offset.

Any per-archive nonce, salt, initialisation vector or key makes that probability zero. So there is one global key, one global initialisation or tweak base, and no dependence on absolute file offset. This is the strongest structural fact in the format. It also means one recovered key decrypts every table in the game.

Ciphertext is a function of the table-relative offset and the plaintext block. Identical plaintext at the same table-relative offset always yields identical ciphertext.

## Block size and padding

The block size is 16 bytes.

- Table lengths are multiples of 16 in 4,330 of 4,330 headers, and the trailer length is too.
- A one-record table 2 is 16 bytes, not 32. There is no PKCS#7 padding and no length leak from padding.
- Table 1 has a 512-byte minimum, which is 32 records.
- Every byte position inside a 16-byte table-2 record is uniform across the corpus, with chi-square values between 230 and 294 against a 255 plus or minus 23 expectation. A plaintext entry table cannot do that, because an offset or size field would leave small values and zero high bytes in fixed columns. Every byte of every record passes through the cipher.

A 64-bit block cipher would show independent 8-byte halves. The two halves of the format-tag block carry the same partition, so 16-byte blocks are supported over 8-byte ones.

## Entropy

Table 1 measures 8.0000 bits per byte with a chi-square of 358 on 255 degrees of freedom. Table 2 measures 8.0000 with a chi-square of 244. Both are uniform, and both are uniform in every byte column.

## Repetition stops at byte 48

| Measurement | Result |
| --- | --- |
| Repeated 16-byte table-1 blocks, 1,227,740 blocks | 39 values, all at offsets 0, 16 and 32 |
| Repeated blocks in table 1 from byte 48, 1,225,751 blocks | 0 |
| Repeated 16-byte blocks in table 2, 538,176 blocks | 0 |
| Repeated 8-byte slots in table 2, 1,076,352 slots | 0 |
| Accidental 16-byte collisions expected | about 2 in 10 to the 27 |
| Table 1 bytes 0 to 16 | 1 value in 4,330 |
| Table 1 bytes 16 to 32 | 4 values |
| Table 1 bytes 32 to 48 | 3,522 distinct |
| Table 1 bytes 48 and beyond | unique per archive |

So two and a half blocks behave like a fixed preamble, and past byte 48 no two archives in the game share any 8 bytes at a common offset.

Repeat statistics on their own do not discriminate ECB from a chained mode, and it is important to say why. A synthetic entry table built from a hash, an offset and a size has 0.0000 percent duplicate 16-byte blocks, while a synthetic table of 16-byte names has 99.96 percent. Unique records make ECB silent. Zero duplicates therefore only rule out ECB over a plaintext full of repeated records, such as a name table of 16-byte cells. The mode is settled by the same-file crib in the corrections section, not by this measurement.

## Stream modes are falsified

If a stream mode reused a keystream, the XOR of two ciphertexts at equal offsets would equal the XOR of two plaintexts, and that would be structurally non-uniform.

| Stream | Zero fraction of pairwise XOR | Expected by chance |
| --- | --- | --- |
| Table 1, whole | 0.02180 | 0.003906, dominated by the 48-byte preamble |
| Table 1 from byte 48 | 0.00390 | 0.003906 |
| Table 2 | 0.00391 | 0.003906 |

The measurement covers 5.0 million bytes and 159 same-length pairs. Control tables of exactly the observed size give 19.20 percent and 13.38 percent zero fractions for an entry table and a name table. The real streams are 35 to 50 times too clean, and the determinism result already forces a reused keystream for any stream cipher. ChaCha20, AES-CTR and Salsa20 with a fixed nonce are out.

## Compression is falsified

A compression reading was tested and rejected. The largest test ran 8.85 million decoder attempts, and none produced a valid decode at a table start. `t1[0]` is `0x5f` in every table from 512 bytes to 950 KB, which no zlib or dictionary stream would do.

## Hypotheses and their falsifiers

| Id | Hypothesis | Key form | Status |
| --- | --- | --- | --- |
| H1 | AES-256-ECB, raw 16-byte blocks, one global key | 32 bytes | Falsified by the same-file crib (retracted 2026-11-22) |
| H2 | AES-256-CBC, fixed initialisation vector, one global key per table | 32 bytes plus 16 | Alive, chained-mode candidate |
| H3 | AES-256-XTS, tweak from the table-relative data-unit index | 64 bytes | Alive, chained-mode candidate |
| H4 | AES-128 variants of H1 to H3 | 16 bytes | Falsified for the H1 variant; alive for H2 and H3 |
| H5 | Custom 128-bit block cipher in the earlier-title lineage | S-box tables plus key schedule | NG variant falsified; other variants untested without the key |
| H6 | ChaCha20, AES-CTR or Salsa20 with a fixed nonce | 32 bytes plus 16 | Falsified by the XOR test |
| H7 | Per-record ECB with no chaining | as H1 | Falsified by the same-file crib (retracted 2026-11-22) |
| H8 | Compression rather than encryption | not applicable | Falsified |
| H9 | Key derived from a header field | hash or repetition of header values | Falsified for every tested derivation |

Chained mode. ECB is falsified by a same-file crib across nested archives. Corpus repeats occur only at block index 0 to 2, and 457 same-length pairs share two leading blocks then never another.

The two surviving shape candidates are H2 and H3. Every derivation from the archive id, the `0x28` field or the `0x40` sentinel failed, and the determinism result excludes any per-archive derivation in principle.

## What has been tried and failed

The full matrix covered 39,491 cipher, key and initialisation-vector combinations over 318,564 attempts, plus a zero-block oracle over 656,828 keys. It covered AES-128, AES-192 and AES-256 in ECB, CBC, CFB, OFB, CTR and XTS, ChaCha20, TEA, XTEA and XXTEA, and the publicly documented key set from the earlier title.

None reproduced a known block. The `0x40` region was fed to several of those passes as key material before it was understood to be a plaintext-shaped constant, which explains why those passes scored as random.

## GTA V NG is ruled out

The RPF7 lineage carries two distinct schemes. One is AES-256 in ECB with a single global 32-byte key. The other is NG: a 17-round table cipher with 68 subkeys, 17 tables of 16 by 256 entries, and a per-file key derived from the file name and size. NG is the documented custom cipher in this lineage, so it is the one that can be run against the tables directly.

The real NG construction was ported to Rust and run against RPF9 material. The run covered 101 expanded keys, applied in both directions, over 64 construction variants, for 25,856 evaluations. It produced 0 hits.

A negative result only counts if the same code can produce a positive, so the port was checked against retail GTA V NG material. It decrypted the retail `common.rpf` archive, flag `0x0FEFFFFF`, with that archive's documented NG key, and produced structured entries with ASCII names and near-monotone offsets. The port and the key derivation were therefore working at the moment the RPF9 run found nothing.

So the RPF9 tables are not GTA V NG under the material that is known. An AES-256 global-key reading in a chained mode remains the best-supported inference, and the exact cipher and key are still open. A custom cipher that is not NG remains possible, and it would look identical to AES in every structural test so far.

## What a future key must satisfy

A candidate key is correct when all of the following hold:

1. Decrypting table 1 at offset 0 with the global key yields the same 16-byte plaintext for every archive.
2. The plaintext from byte 48 is a plausible record: an offset and size, or a name, in a fixed stride.
3. Table 2 decrypts to declared-entry records whose count matches the header count within the known directory ratio of about 1.6 for top-level archives and 1.0 elsewhere.
4. Concatenated table-1 plaintext contains the path or name payload whose length the table already implies.

A block-level oracle is weaker than this. A key that decrypts one block plausibly can still be wrong, which is why the roadmap calls for a scoring oracle rather than a pass or fail check.

## What is not proven

- The exact cipher and mode.
- Whether the `0x40` to `0x60` region is plaintext tagging or ciphertext of a constant.
- The meaning of the trailer, the split offset, and the four format tags.
- The exact entry layout of both tables.

These are stated as open. Nothing in this repository claims otherwise.

## Corrections

**2026-11-22: ECB is falsified, H1 and H7 move from Alive to Falsified.** The previous text of this page said that ECB, CBC and XTS could not be told apart from ciphertext alone, and listed AES-256-ECB with one global key as Alive. That was correct for the evidence then cited, which compared different archives at equal offsets. It is wrong as a general claim, and the retraction is recorded here rather than by overwriting the old statement without trace.

The decisive measurement is a same-file crib. One payload, 24,626 bytes compressed and 41,824 bytes uncompressed with SHA-1 `a2f4d2b7`, is indexed by two nested archives, `rpf2` at data offset `0x1000` and `rpf3` at data offset `0x6000`. Both tables therefore carry a record for the same file. The XOR of the two ciphertext blocks is non-zero in all 16 bytes at all three alignments tested. Under ECB with one global key that XOR would be zero, because identical plaintext blocks at any position encrypt to identical ciphertext. The mode is chained.

What survives unchanged: the 16-byte block size, the global key with no per-archive derivation, the 48-byte repeat boundary, the stream-mode falsification and the compression falsification. Those measurements never discriminated the modes on their own and are not affected.

What changes: H1 and the H1 half of H4 are out. H2 (CBC with a fixed initialisation vector) and H3 (XTS with a position tweak) are the remaining shape candidates. Both produce the same ciphertext for equal plaintext at equal positions, so the older same-position statistics are consistent with either. A future key still has to satisfy the four conditions above; only the mode list has shortened.
