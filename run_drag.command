#!/bin/bash
# Double-click to run SayoDriver (opens Terminal and runs the driver).
cd "$(dirname "$0")"
source venv/bin/activate
python3 knob_drag.py
echo ""
echo "Press Enter to close this window..."
read
