"""Lokale Beispielwerte; LeTTo stellt sein eigenes dataset-Modul bereit."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common import DatasetVariable


spannung = DatasetVariable("spannung", 12, "")
start = DatasetVariable("start", 2, "")
stopp = DatasetVariable("stopp", 10, "")
schrittweite = DatasetVariable("schrittweite", 2, "")
