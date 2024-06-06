from dataclasses import dataclass
from pathlib import Path

@dataclass
class dataIngestionEntity:
    root: Path
    URL: str
    file: Path
    unzip_dir: Path