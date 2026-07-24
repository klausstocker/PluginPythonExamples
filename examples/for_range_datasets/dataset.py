import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import DatasetVariable


a = DatasetVariable('a', 4)
n = DatasetVariable('n', 3)
