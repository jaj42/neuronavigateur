#!/usr/bin/env python3
"""Regenerate every matplotlib figure: runs figures/src/*.py (helpers start with "_")."""

import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"

failed = []
for script in sorted(SRC.glob("[!_]*.py")):
    r = subprocess.run([sys.executable, script.name], cwd=SRC)
    if r.returncode:
        failed.append(script.name)
if failed:
    sys.exit(f"échec : {', '.join(failed)}")
