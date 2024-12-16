import os
from pathlib import Path


class FilePath:

    __ROOT_DIR: Path = Path(__file__).parent.parent.parent
    DATA_DIR: str = os.path.join(__ROOT_DIR, "data")
