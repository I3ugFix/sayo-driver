#!/bin/bash
# Run SayoDriver (activate venv and start knob_drag.py).
cd "$(dirname "$0")"
source venv/bin/activate
python3 knob_drag.py
