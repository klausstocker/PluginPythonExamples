"""Lokale Beispielwerte; LeTTo stellt sein eigenes dataset-Modul bereit."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import DatasetVariable


fuellstand = DatasetVariable("fuellstand", 2.0, "")
ziel = DatasetVariable("ziel", 10.0, "")
zufluss = DatasetVariable("zufluss", 3.0, "")
