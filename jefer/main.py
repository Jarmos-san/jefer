"""The main entrypoint file for Jefer."""

import subprocess
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def message() -> None:
    """Print a "Hello World!" message."""
    typer.echo("Hello Jarmos!")


@app.command()
def init(
    source: Path = typer.Option(
        Path.home() / ".dotfiles", help="The path for storing the dotfiles."
    )
) -> None:
    """Create & initialise an empty Git repository locally."""
    # Store the expanded path as a variable for easier manipulation later on.
    dotfiles_dir = source.expanduser()

    # Create the "dotfiles" source directory if doesn't already exist.
    if not dotfiles_dir.exists():
        dotfiles_dir.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run(
            ["git", "init", f"{dotfiles_dir}"], check=True, stdout=subprocess.PIPE
        )
        print(f"Created a local Git repository for your dotfiles at {dotfiles_dir}")
    except FileNotFoundError as error:
        print(error)
        print(
            "Intialising local Git repository failed, see if Git is installed or not."
        )


@app.command()
def remove() -> None:
    """Remove a source file & its destination link from the system."""
    pass


@app.command()
def link() -> None:
    """Create a symbolic link for a source file."""
    pass


@app.command()
def list() -> None:
    """Show the list of files & the path to their destined links."""
    pass


@app.command()
def healthcheck() -> None:
    """Check if a source file(s) has a linked destination."""
    pass


if __name__ == "__main__":
    app()
