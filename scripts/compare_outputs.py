#!/usr/bin/env python3
"""Compare selected OpenTrack text outputs produced by rerunning the same scenario."""

import argparse
import difflib
from pathlib import Path
import sys


def read_rows(root: Path, relative_name: str, encoding: str) -> list[str]:
    relative_path = Path(relative_name)
    if relative_path.is_absolute() or relative_path.drive or ".." in relative_path.parts:
        raise ValueError(f"Expected a path relative to the output directory: {relative_name}")
    path = (root / relative_path).resolve(strict=True)
    if not path.is_relative_to(root):
        raise ValueError(f"Output resolves outside {root}: {relative_name}")
    lines = path.read_text(encoding=encoding).splitlines()
    return [line.rstrip() for line in lines if line.strip() and not line.lstrip().startswith("//")]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=Path)
    parser.add_argument("rerun", type=Path)
    parser.add_argument("files", nargs="+", help="Output files relative to both directories")
    parser.add_argument("--encoding", default="utf-8-sig", help="Text encoding (default: UTF-8 with optional BOM)")
    args = parser.parse_args()

    baseline, rerun = args.baseline.resolve(), args.rerun.resolve()
    result = 0
    for name in dict.fromkeys(args.files):
        try:
            original = read_rows(baseline, name, args.encoding)
            repeated = read_rows(rerun, name, args.encoding)
        except (OSError, UnicodeError, LookupError, ValueError) as error:
            print(f"ERROR {name}: {error}", file=sys.stderr)
            result = 2
            continue

        if not original or not repeated:
            print(f"ERROR {name}: expected data rows in both outputs", file=sys.stderr)
            result = 2
            continue
        if original == repeated:
            print(f"MATCH {name} ({len(original)} data rows)")
            continue
        result = max(result, 1)
        print(f"DIFF {name} ({len(original)} vs {len(repeated)} data rows)")
        for line in difflib.unified_diff(original, repeated, f"baseline/{name}", f"rerun/{name}", lineterm=""):
            print(line)
    return result


if __name__ == "__main__":
    sys.exit(main())
