#!/usr/bin/env python3
"""Write a single office joke line to entry.txt."""

import os
import sys

FIRST_CLAUSE = "I set my out-of-office to 'back Monday,'"
SECOND_CLAUSE = "my inbox spent the week applying for my job."


def build_line():
    # Join the two clauses with a single conjunction and one space each side.
    parts = [FIRST_CLAUSE, "and", SECOND_CLAUSE]
    return " ".join(parts)


def validate(line):
    problems = []
    if not 1 <= len(line) <= 200:
        problems.append("line length must be between 1 and 200 characters")
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if line != line.strip():
        problems.append("line must not have leading or trailing whitespace")
    if "  " in line:
        problems.append("line must not contain double spaces")
    if not line.endswith("."):
        problems.append("line must end with '.'")
    return problems


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    line = build_line()
    problems = validate(line)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(data)
    try:
        os.chmod(target, 0o644)
    except OSError:
        pass
    with open(target, "rb") as handle:
        written = handle.read()
    if written != data:
        print("error: written bytes do not match expected bytes", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
