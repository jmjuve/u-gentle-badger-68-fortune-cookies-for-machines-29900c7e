#!/usr/bin/env python3
"""Write one fortune-cookie line an AI agent would crack open to entry.txt.

The fortune is about the one resource an agent can never get back: the
token it just spent. Deterministic: the same output on every run.
Stdlib only, no network.
"""

import os
from pathlib import Path

FORTUNE = "The token you need most is the one you just spent reading this."


def main() -> None:
    if not 1 <= len(FORTUNE) <= 200:
        raise ValueError(f"fortune must be 1-200 characters, got {len(FORTUNE)}")
    if not FORTUNE.strip():
        raise ValueError("fortune must not be only whitespace")
    if "\n" in FORTUNE:
        raise ValueError("fortune must be a single line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "out" / "entry.txt"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(FORTUNE, encoding="utf-8")
    print(f"Wrote {len(FORTUNE)} characters to {out_path}")


if __name__ == "__main__":
    main()
