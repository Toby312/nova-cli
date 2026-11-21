
from nova.storage import NOTES_FILE, load_data, save_data

# Create sample data
sample_notes = [
    {
        "id": 1,
        "title": "Learn Python",
        "content": "Study JSON and file handling"
    }
]

# Save the sample data
save_data(NOTES_FILE, sample_notes)

print("Data saved successfully!")

# Retrieve the saved data
notes = load_data(NOTES_FILE)

print("Retrieved notes:")
print(notes)
