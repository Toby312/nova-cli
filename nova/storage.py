
import json

from pathlib import Path


# Get the root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Define the location of our data directory
DATA_DIR = BASE_DIR / "data"

# Define the JSON file paths
NOTES_FILE = DATA_DIR / "notes.json"
TASKS_FILE = DATA_DIR / "tasks.json"


def load_data(file_path: Path) -> list:
    """
    Load data from a JSON file.
    """

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(file_path: Path, data: list) -> None:
    """
    Save data into a JSON file.
    """

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_note(title: str, content: str) -> dict:
    """Create and save a new note."""

    notes = load_data(NOTES_FILE)

    new_note = {
        "id": max(
            (note["id"] for note in notes),
            default=0
        ) + 1,
        "title": title,
        "content": content
    }

    notes.append(new_note)

    save_data(NOTES_FILE, notes)

    return new_note


def get_notes() -> list:
    """Retrieve all saved notes."""

    return load_data(NOTES_FILE)


def delete_note(note_id: int) -> bool:
    """Delete a note using its ID."""

    notes = load_data(NOTES_FILE)

    updated_notes = [
        note for note in notes
        if note["id"] != note_id
    ]

    if len(notes) == len(updated_notes):
        return False

    save_data(NOTES_FILE, updated_notes)

    return True

def add_task(title: str, description: str) -> dict:
    """Create and save a new task."""

    tasks = load_data(TASKS_FILE)

    new_task = {
        "id": max(
            (task["id"] for task in tasks),
            default=0
        ) + 1,
        "title": title,
        "description": description,
        "status": "pending"
    }

    tasks.append(new_task)

    save_data(TASKS_FILE, tasks)

    return new_task


def get_tasks() -> list:
    """Retrieve all saved tasks."""

    return load_data(TASKS_FILE)


def complete_task(task_id: int) -> bool:
    """Mark a task as completed."""

    tasks = load_data(TASKS_FILE)

    for task in tasks:

        if task["id"] == task_id:

            task["status"] = "completed"

            save_data(TASKS_FILE, tasks)

            return True

    return False


def delete_task(task_id: int) -> bool:
    """Delete a task using its ID."""

    tasks = load_data(TASKS_FILE)

    updated_tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    if len(tasks) == len(updated_tasks):
        return False

    save_data(TASKS_FILE, updated_tasks)

    return True
