# Localisation coverage

Every shipped archive in the package was decompressed and classified, then every accepted
string table was hashed and matched against the 32-bit identifiers used by the audio config.
The counts below come from that single pass; no sampling and no extrapolation.

## Corpus

| measurement | value |
|---|---|
| archives scanned | 18 |
| streams decompressed | 2,067,172 |
| localisation-pool resources | 287,427 |
| accepted string tables | 25,913 |
| strings extracted | 7,312,731 |
| characters | 232,572,599 |
| strings hashed | 55,910,167 |
| hash-table records | 7,137,384 |
| printable strings | 99.9% |
| invalid UTF-8 strings | 0 |
| read errors | 0 |
| inflate throughput | 679 MB/s |
| wall time | 504 s |

## Locale buckets

Buckets are assigned by script and vocabulary, not by a declared field, so the boundaries
between the closely related languages are soft. The counts are what the classifier produced.

| bucket | strings |
|---|---|
| Spanish | 1,134,127 |
| Chinese | 1,089,126 |
| Portuguese | 572,453 |
| Russian | 571,369 |
| French | 566,754 |
| Korean | 564,175 |
| Italian | 561,828 |
| Polish | 558,361 |
| English | 557,821 |
| German | 554,441 |
| Japanese | 548,405 |
| Romance, other | 23,297 |
| undetermined | 10,574 |
| **total** | **7,312,731** |

Twelve full localisations plus a partial thirteenth. No bucket is dominant: the largest is
15.5% of the corpus, which is what a same-day, same-build translation set looks like.

## Audio naming

| measurement | value |
|---|---|
| music records in the audio config | 1,589 |
| resolved to a bank by id | 1,589 (100%) |
| duration-validated against the bank | 1,589 (100%), max error 1 ms |
| resolved to a name from shipped tables | 772 (48.6%) |

Naming is the weak axis. The 817 unnamed records are the short entries and the licensed
tracks: their mean duration is 114.6 s against 231.6 s for the named set, and the shipped
tables contain no spelling of their identifiers. A full sweep of every archive, including
pools that the table filter normally rejects, adds only 7 of them, so the missing titles are
not stored anywhere in the package's string data.

## Method notes

- Identifiers are matched on the full 32 bits of a Jenkins-style one-at-a-time hash over the
  normalised name (lowercased, non-alphanumeric runs collapsed to one underscore).
- A name is only reported when a candidate string hashes to the record's identifier. All 772
  were re-hashed by a second, independent implementation; 772 of 772 agree.
- Three records carry a second string with the same hash. Where one candidate reads as a
  sentence and another as a title, the title is reported and the collision is recorded
  rather than resolved.
- Duration is checked as half the bank's sample count divided by its rate, against the config
  duration, with a 10 ms tolerance; the observed maximum error is 1 ms.
