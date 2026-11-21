#!/usr/bin/env python3
"""Validate the published research snapshot and record its check date.

Run from the repository root, or pass --repo-root. Exits 1 on the first
failure so CI shows the reason without a traceback.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REQUIRED_DOCS = [
    "README.md",
    "NOTICE.md",
    "LICENSE",
    "docs/rpf9-container.md",
    "docs/ttpf-rds5-etpf.md",
    "docs/cipher-constraints.md",
    "docs/placement-resources.md",
    "docs/drpz-localisation.md",
    "docs/content-inventory.md",
    "docs/open-questions.md",
    "data/counts.md",
    "data/catalog-summary.json",
    "scripts/validate_snapshot.py",
    ".github/workflows/refresh.yml",
]

REQUIRED_NUMBERS = {
    "corpus.files": int,
    "corpus.gigabytes": float,
    "archives.valid_headers": int,
    "archives.declared_entries": int,
    "streams.total": int,
    "streams.unique": int,
    "streams.duplicate_rows": int,
    "streams.kinds.binary": int,
    "streams.kinds.psin": int,
    "streams.kinds.xml": int,
    "streams.kinds.rbf0": int,
    "streams.kinds.text": int,
    "bin_store.streams": int,
    "bin_store.stored_bytes": int,
    "bin_store.raw_bytes": int,
    "bin_store.ratio": float,
    "bin_store.segments": int,
    "textures.descriptors_files": int,
    "textures.descriptors_distinct": int,
    "textures.chunks_files": int,
    "textures.software_reachable_percent": float,
    "audio.banks": int,
    "video.validated": int,
    "placement.entities": int,
    "placement.resources": int,
    "drpz.streams_scanned": int,
    "drpz.drpz_streams": int,
    "drpz.tables": int,
    "drpz.strings": int,
    "drpz.readable_ratio": float,
    "drpz.chars": int,
    "drpz.locales": int,
    "cipher.headers_checked": int,
    "cipher.keys_recovered": int,
}

# Fragments are joined so the blocklist itself does not put these names
# into the published tree.
BANNED_TOKENS = [
    "cyber" + "leek",
    "torr" + "ent",
    "re" + "pack",
    "fast" + "resume",
    "game_" + "scar" + "lett",
    "percy" + "star",
    "six" + "ng",
    "leon" + "ida",
    "sentinel" + "rpfviewer",
    "vi" + "-view",
    "site" + "_vi",
    "d:" + "\\gta6",
    "c:" + "\\users",
    "c:" + "\\coding",
]

SCAN_FILES = [
    "README.md",
    "NOTICE.md",
    "docs/rpf9-container.md",
    "docs/ttpf-rds5-etpf.md",
    "docs/cipher-constraints.md",
    "docs/placement-resources.md",
    "docs/drpz-localisation.md",
    "docs/content-inventory.md",
    "docs/open-questions.md",
    "data/counts.md",
    "data/catalog-summary.json",
]

IPV4 = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


class Failure(Exception):
    pass


def dig(data: dict, dotted: str):
    node = data
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            raise Failure(f"missing key: {dotted}")
        node = node[part]
    return node


def check_docs(root: Path) -> int:
    missing = []
    empty = []
    for rel in REQUIRED_DOCS:
        path = root / rel
        if not path.is_file():
            missing.append(rel)
        elif path.stat().st_size == 0:
            empty.append(rel)
    if missing:
        raise Failure("missing required files: " + ", ".join(missing))
    if empty:
        raise Failure("empty required files: " + ", ".join(empty))
    return len(REQUIRED_DOCS)


def check_json(root: Path) -> dict:
    path = root / "data/catalog-summary.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Failure(f"catalog-summary.json is not valid JSON: {exc}") from exc

    if data.get("format") != "rpf9-research-catalog-summary":
        raise Failure("catalog-summary.json has an unexpected format marker")
    if data.get("schema_version") != 1:
        raise Failure("catalog-summary.json schema_version must be 1")

    for dotted, kind in REQUIRED_NUMBERS.items():
        value = dig(data, dotted)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise Failure(f"{dotted} must be numeric")
        if kind is int and not isinstance(value, int):
            raise Failure(f"{dotted} must be an integer")
        if value < 0:
            raise Failure(f"{dotted} must not be negative")

    kinds = dig(data, "streams.kinds")
    kind_sum = sum(kinds.values())
    if kind_sum != dig(data, "streams.total"):
        raise Failure(f"stream kinds sum to {kind_sum}, total says {dig(data, 'streams.total')}")

    unique = dig(data, "streams.unique")
    dupes = dig(data, "streams.duplicate_rows")
    if unique + dupes != dig(data, "streams.total"):
        raise Failure("unique streams plus duplicate rows must equal the total")

    if dig(data, "bin_store.streams") != dig(data, "streams.kinds.binary"):
        raise Failure("bin store stream count must equal the binary stream count")

    if dig(data, "bin_store.stored_bytes") >= dig(data, "bin_store.raw_bytes"):
        raise Failure("bin store stored_bytes must be smaller than raw_bytes")

    if dig(data, "textures.descriptors_distinct") > dig(data, "textures.descriptors_files"):
        raise Failure("distinct descriptor count exceeds the file count")

    if dig(data, "cipher.keys_recovered") != 0:
        raise Failure("keys_recovered must stay 0 unless a key is actually published")

    scanned = dig(data, "drpz.streams_scanned")
    drpz_streams = dig(data, "drpz.drpz_streams")
    tables = dig(data, "drpz.tables")
    strings = dig(data, "drpz.strings")
    if drpz_streams > scanned:
        raise Failure("drpz_streams must not exceed streams_scanned")
    if tables > drpz_streams:
        raise Failure("drpz tables must not exceed drpz_streams")
    if strings < tables:
        raise Failure("drpz strings must not be fewer than tables")
    ratio = dig(data, "drpz.readable_ratio")
    if not 0.0 <= ratio <= 1.0:
        raise Failure("drpz readable_ratio must be a fraction between 0 and 1")
    if dig(data, "drpz.locales") < 1:
        raise Failure("drpz locales must be at least 1")

    return data


def check_hygiene(root: Path) -> int:
    scanned = 0
    problems = []
    for rel in SCAN_FILES:
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8").lower()
        scanned += 1
        for token in BANNED_TOKENS:
            if token in text:
                problems.append(f"{rel}: banned token {token!r}")
        for match in IPV4.finditer(text):
            problems.append(f"{rel}: address-like string {match.group(0)!r}")
    if problems:
        raise Failure("; ".join(problems))
    return scanned


def current_commit(root: Path) -> str:
    env_sha = os.environ.get("GITHUB_SHA", "").strip()
    if env_sha:
        return env_sha
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def write_stamp(root: Path, commit: str) -> Path:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    stamp = {
        "checked_utc": now.isoformat().replace("+00:00", "Z"),
        "commit": commit,
        "validator": 1,
        "status": "pass",
    }
    path = root / "data/last-check.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(stamp, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate the research snapshot.")
    parser.add_argument("--repo-root", default=".", help="repository root, defaults to the current directory")
    parser.add_argument("--no-write", action="store_true", help="validate only, do not write data/last-check.json")
    args = parser.parse_args(argv)

    root = Path(args.repo_root).resolve()
    if not root.is_dir():
        print(f"FAIL  repository root not found: {root}")
        return 1

    try:
        docs = check_docs(root)
        print(f"PASS  required files present ({docs})")
        data = check_json(root)
        print(f"PASS  catalog-summary.json valid ({len(REQUIRED_NUMBERS)} numeric fields)")
        print(f"PASS  stream kinds sum to {data['streams']['total']}")
        scanned = check_hygiene(root)
        print(f"PASS  hygiene scan clean ({scanned} files)")
    except Failure as exc:
        print(f"FAIL  {exc}")
        return 1

    commit = current_commit(root)
    if args.no_write:
        print(f"SKIP  stamp not written (commit {commit[:12]})")
        return 0

    path = write_stamp(root, commit)
    rel = path.relative_to(root)
    stamp = json.loads(path.read_text(encoding="utf-8"))
    print(f"WROTE {rel.as_posix()} ({stamp['checked_utc']}, {stamp['commit'][:12]})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
