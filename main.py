"""Write one short review line for make.fun's one-line-review bounty."""

import os
import sys

TEXT = (
    "Five stars. He asked me to summarize his day. I wrote: argued with a toaster, "
    "lost. He said add nuance. I wrote: twice."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
