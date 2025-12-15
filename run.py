#!/usr/bin/env python3
"""Convenience runner for the hello world package."""
import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

if __name__ == "__main__":
    # einfache Rechnung
    result = 1 + 2
    print(f"1 + 2 = {result}")

    # bestehendes Modul ausführen
    runpy.run_module("helloworld", run_name="__main__")
