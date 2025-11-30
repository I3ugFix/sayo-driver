#!/bin/bash
# Script para ejecutar knob_drag.py con el entorno virtual activado

cd "$(dirname "$0")"
source venv/bin/activate
python3 knob_drag.py

