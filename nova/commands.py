
from datetime import datetime
from nova.storage import (
    add_note,
    get_notes,
    delete_note,
    add_task,
    get_tasks,
    complete_task,
    delete_task
)

def process_message(message: str) -> str:
    """
    Process a user's message and return a response.
    """

    message = message.strip()
    normalized_message = message.lower()

    # Add a new note
    if normalized_message.startswith("note add |"):

        parts = message.split("|", 2)

        if len(parts) != 3:
            return "Invalid format. Use: note add | title | content"

        title = parts[1].strip()
        content = parts[2].strip()

        if not title or not content:
            return "Note title and content cannot be empty."

        note = add_note(title, content)

        return f"Note saved successfully! Note ID: {note['id']}"

    # Display all notes
    elif normalized_message == "note list":

        notes = get_notes()

        if not notes:
            return "You don't have any saved notes yet."

        response = "YOUR SAVED NOTES:\n"

        for note in notes:
            response += (
                f"\nID: {note['id']}"
                f"\nTitle: {note['title']}"
                f"\nContent: {note['content']}\n"
            )

        return response

    # Delete a note
    elif normalized_message.startswith("note delete |"):

        parts = message.split("|", 1)

        if len(parts) != 2:
            return "Invalid format. Use: note delete | ID"

        try:
            note_id = int(parts[1].strip())

        except ValueError:
            return "Please provide a valid numeric note ID."

        if delete_note(note_id):
            return f"Note {note_id} deleted successfully!"

        return f"No note found with ID {note_id}."
    
    # Add a new task
    elif normalized_message.startswith("task add |"):

        parts = message.split("|", 2)

        if len(parts) != 3:
            return "Invalid format. Use: task add | title | description"

        title = parts[1].strip()
        description = parts[2].strip()

        if not title or not description:
            return "Task title and description cannot be empty."

        task = add_task(title, description)

        return f"Task added successfully! Task ID: {task['id']}"

    # Display all tasks
    elif normalized_message == "task list":

        tasks = get_tasks()

        if not tasks:
            return "You don't have any saved tasks yet."

        response = "YOUR TASKS:\n"

        for task in tasks:
            response += (
                f"\nID: {task['id']}"
                f"\nTitle: {task['title']}"
                f"\nDescription: {task['description']}"
                f"\nStatus: {task['status']}\n"
            )

        return response

    # Complete a task
    elif normalized_message.startswith("task complete |"):

        parts = message.split("|", 1)

        if len(parts) != 2:
            return "Invalid format. Use: task complete | ID"

        try:
            task_id = int(parts[1].strip())

        except ValueError:
            return "Please provide a valid numeric task ID."

        if complete_task(task_id):
            return f"Task {task_id} marked as completed!"

        return f"No task found with ID {task_id}."

    # Delete a task
    elif normalized_message.startswith("task delete |"):

        parts = message.split("|", 1)

        if len(parts) != 2:
            return "Invalid format. Use: task delete | ID"

        try:
            task_id = int(parts[1].strip())

        except ValueError:
            return "Please provide a valid numeric task ID."

        if delete_task(task_id):
            return f"Task {task_id} deleted successfully!"

        return f"No task found with ID {task_id}."


    # Greetings
    elif normalized_message in ["hello", "hi", "hey"]:
        return "Hello! How can I help you today?"

    # Assistant identity
    elif "your name" in normalized_message:
        return "I'm NOVA, your personal assistant."

    # Assistant capabilities
    elif "what can you do" in normalized_message:
        return (
            "I can chat with you, manage tasks, "
            "perform calculations and help you learn Python."
        )

    # Time
    elif "time" in normalized_message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # Date
    elif "date" in normalized_message:
        current_date = datetime.now().strftime("%A, %d %B %Y")
        return f"Today's date is {current_date}."

    # Custom responses
    elif normalized_message == "how are you":
        return "I'm doing great! Thanks for asking. How can I help?"

    elif normalized_message == "who created you":
        return "I was created by Tobenna."

    elif normalized_message == "tell me a joke":
        return (
            "Why do Python programmers prefer dark mode? "
            "Because light attracts bugs!"
        )

    else:
        return (
            "I'm still learning! I don't understand that "
            "request yet."
        )
