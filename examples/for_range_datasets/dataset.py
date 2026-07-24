from dataclasses import asdict, dataclass
from typing import Any, Optional

@dataclass(frozen=True)
class DatasetVariable:
    name: str
    value: Any = None
    unit: Optional[str] = None

a = DatasetVariable('a', 4)
n = DatasetVariable('n', 3)