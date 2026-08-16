#!/usr/bin/env python3
"""Lance pytest avec CORRIGE=1 (compatible Windows, Linux, macOS)."""

from __future__ import annotations

import os
import subprocess
import sys


def main() -> None:
    os.environ["CORRIGE"] = "1"
    raise SystemExit(subprocess.call([sys.executable, "-m", "pytest", *sys.argv[1:]]))


if __name__ == "__main__":
    main()
