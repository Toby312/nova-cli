
import typer

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from nova.assistant import run_assistant

app = typer.Typer(
    name="nova",
    help="NOVA - Your Personal AI Assistant",
    no_args_is_help=True
)

console = Console()


def show_banner():
    banner = Text()

    banner.append("NOVA", style="bold cyan")
    banner.append(" CLI", style="bold white")

    console.print(
        Panel(
            banner,
            subtitle="[dim]Your Personal AI Assistant[/dim]",
            border_style="cyan",
            padding=(1, 4)
        )
    )


@app.command()
def start():
    """Start the NOVA assistant."""

    show_banner()
    run_assistant()

@app.command()
def about():
    """Display information about NOVA."""

    console.print(
        Panel(
            "NOVA is a Python-powered personal assistant "
            "built to demonstrate AI development, "
            "automation and intelligent applications.",
            title="About NOVA",
            border_style="blue"
        )
    )


if __name__ == "__main__":
    app()
