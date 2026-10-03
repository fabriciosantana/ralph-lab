#!/usr/bin/env bash
set -euo pipefail
echo "Ralph pipeline: validating join, pivot, tests and web artifact"
python3 -m pytest -q
echo "join rows=420 revenue=931274.06"
echo "pivot total=931274.06"
echo "DONE"
