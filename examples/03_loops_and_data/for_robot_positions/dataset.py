"""Lokale Beispielwerte; LeTTo stellt sein eigenes dataset-Modul bereit."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import DatasetVariable


anzahl = DatasetVariable("anzahl", 4, "")
schrittweite = DatasetVariable("schrittweite", 2.9, "")
