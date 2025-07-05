from pathlib import Path

import pytest

from src import log_loader


def test_load_output_log(tmp_path: Path):
    # Setup: copy sample log to temporary directory
    log_path = tmp_path / "output_log.txt"
    log_path.write_text("example output log")

    content = log_loader.load_output_log(tmp_path)
    assert content == "example output log"


def test_load_player_log(tmp_path: Path):
    log_path = tmp_path / "Player.log"
    log_path.write_text("player log text")

    content = log_loader.load_player_log(tmp_path)
    assert content == "player log text"


def test_missing_file(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        log_loader.load_output_log(tmp_path)
