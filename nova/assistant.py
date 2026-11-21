
from rich.console import Console
from rich.panel import Panel

from nova.commands import process_message

console = Console()


def run_assistant():
    """
    Start NOVA's interactive conversation session.
    """

    console.print(
        Panel(
            "Hello! I'm NOVA, your personal assistant.\n"
            "Type 'help' to see what I can do.\n"
            "Type 'exit' to end our conversation.",
            title="NOVA",
            border_style="cyan"
        )
    )

    while True:

        user_input = console.input(
            "\n[bold green]You:[/bold green] "
        )

        if user_input.lower().strip() in ["exit", "quit"]:
            console.print(
                "\n[bold cyan]NOVA:[/bold cyan] "
                "Goodbye! Have a productive day."
            )
            break

        if user_input.lower().strip() == "help":
            console.print(
                Panel(
                    "Available features:\n"
                    "- Greetings\n"
                    "- Ask for my name\n"
                    "- Ask what I can do\n"
                    "- Save notes: note add | title | content\n"
                    "- View notes: note list\n"
                    "- Delete notes: note delete | ID\n"
                    "- Add task: task add | title | description\n"
                    "- View tasks: task list\n"
                    "- Complete task: task complete | ID\n"
                    "- Delete task: task delete | ID\n"
                    "- Check the date\n"
                    "- Check the time\n"
                    "- Type exit to quit",
                    title="NOVA Help",
                    border_style="blue"
                )
            )
            continue

        response = process_message(user_input)

        console.print(
            f"\n[bold cyan]NOVA:[/bold cyan] {response}"
        )
