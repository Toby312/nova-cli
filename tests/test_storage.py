import pytest

from nova.storage import load_data, save_data


def test_save_and_load_data(tmp_path):

    test_file = tmp_path / "test_notes.json"

    sample_notes = [
        {
            "id": 1,
            "title": "Learn Python",
            "content": "Study JSON and file handling"
        }
    ]

    save_data(test_file, sample_notes)

    loaded_notes = load_data(test_file)

    assert loaded_notes == sample_notes