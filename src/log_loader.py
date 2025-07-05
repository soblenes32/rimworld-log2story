"""Utilities for loading RimWorld log files."""
from pathlib import Path
from typing import Union


def load_log(path: Union[str, Path]) -> str:
    """Load a log file and return its contents as a string.

    Parameters
    ----------
    path : Union[str, Path]
        Path to the log file.

    Returns
    -------
    str
        Contents of the log file.
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Log file not found: {p}")
    return p.read_text(encoding="utf-8", errors="ignore")

def load_output_log(root: Union[str, Path]) -> str:
    """Load ``output_log.txt`` from the given directory."""
    return load_log(Path(root) / "output_log.txt")


def load_player_log(root: Union[str, Path]) -> str:
    """Load ``Player.log`` from the given directory."""
    return load_log(Path(root) / "Player.log")
