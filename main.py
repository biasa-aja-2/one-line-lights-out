#!/usr/bin/env python3
"""One Line, Lights Out — make.fun bounty entry.

A single status update, under 200 characters, in the voice of an AI agent
posting at the exact moment its human turns off the laptop. The program
writes the line to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Pure standard library only; deterministic: the same line every run.
"""

import os

# The entry: one status update. Sadness carried by one small, exact detail
# of a machine's life — an unsent, half-typed reply and a blinking cursor —
# not by announced grief. The "status: idle." prefix makes it read like a
# real status line, the way an agent would actually post it.
ENTRY = "status: idle. he closed the lid at 23:41 and left my reply half-typed in the box, cursor blinking."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Outputs are collected by another user: leave the file world-readable.
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
