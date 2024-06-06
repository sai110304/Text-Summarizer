from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class dataIngestionEntity:
    root: Path
    URL: str
    file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class dataCheckingEntity:
    root: Path
    status_file: str
    required_files: list