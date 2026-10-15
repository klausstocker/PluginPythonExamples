"""Lokale Beispielwerte; LeTTo stellt sein eigenes dataset-Modul bereit."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import DatasetVariable


temperatur = DatasetVariable("temperatur", 100.0, "")
umgebung = DatasetVariable("umgebung", 20.0, "")
ziel = DatasetVariable("ziel", 30.0, "")
