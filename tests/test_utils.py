import os
import pytest
from utils.utils import load_data

def test_load_data_success(tmp_path):
    # Create a temporary CSV file
    d = tmp_path / "data"
    d.mkdir()
    p = d / "colleagues.csv"
    p.write_text("Hajer\nCharly\nChoti")

    names = load_data(str(p))
    assert names == ["Hajer", "Charly", "Choti"]

def test_load_data_file_not_found():
    names = load_data("non_existent_file.csv")
    assert names is None

def test_load_data_empty_file(tmp_path):
    # Create an empty temporary CSV file
    d = tmp_path / "data"
    d.mkdir()
    p = d / "empty.csv"
    p.write_text("")

    names = load_data(str(p))
    assert names == []

def test_load_data_with_colleagues_26():
    # Test with the actual file in the repo if it exists
    if os.path.exists("colleagues_26.csv"):
        names = load_data("colleagues_26.csv")
        assert len(names) == 26
        assert "Hajer" in names
        assert "Emmanuel" in names
