def explain_python(topic: str) -> str:
    """
    Explain basic Python programming concepts.
    """

    lessons = {
        "variables": (
            "A variable is a name used to store a value.\n\n"
            "Example:\n"
            "name = 'Tobenna'\n"
            "age = 25\n\n"
            "Here, name and age are variables."
        ),

        "lists": (
            "A list is a collection used to store multiple values.\n\n"
            "Example:\n"
            "fruits = ['Apple', 'Mango', 'Orange']\n\n"
            "You can access items using their index.\n"
            "fruits[0] returns Apple."
        ),

        "dictionaries": (
            "A dictionary stores information as key-value pairs.\n\n"
            "Example:\n"
            "person = {'name': 'Tobenna', 'age': 25}\n\n"
            "You can access a value using its key:\n"
            "person['name'] returns Tobenna."
        ),

        "functions": (
            "A function is a reusable block of code.\n\n"
            "Example:\n"
            "def greet():\n"
            "    print('Hello!')\n\n"
            "You can execute the function by calling greet()."
        ),

        "loops": (
            "A loop allows you to repeat a block of code.\n\n"
            "Example:\n"
            "for number in range(5):\n"
            "    print(number)\n\n"
            "This prints numbers from 0 to 4."
        )
    }

    topic = topic.lower().strip()

    return lessons.get(
        topic,
        f"I don't have a lesson about '{topic}' yet."
    )