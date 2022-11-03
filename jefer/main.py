"""The main entrypoint file for Jefer."""

import json
import os
import subprocess
from pathlib import Path

import typer

JEFER_DATA_FILE = Path.home() / ".local/share/jefer/jefer.json"

app = typer.Typer()


@app.command()
def init(
    source: Path = typer.Option(
        Path.home() / ".dotfiles", help="The path for storing the dotfiles."
    ),
    remote: str = typer.Option(
        ..., help="The remote repository for backing up the dotfiles."
    ),
) -> None:
    """Create & initialise an empty Git repository locally."""
    # Store the expanded path as a variable for easier manipulation later on.
    dotfiles_dir = source.expanduser()

    # Create the "dotfiles" source directory if doesn't already exist.
    if not dotfiles_dir.exists():
        dotfiles_dir.mkdir(parents=True, exist_ok=True)

    # Dictionary representing the initial data about the local dotfiles repository.
    jefer_initialisation_data = {"source_dir": str(dotfiles_dir), "dotfiles": []}

    try:
        with open(JEFER_DATA_FILE, "w") as file:
            json.dump(jefer_initialisation_data, file)
    except FileNotFoundError as error:
        raise error

    try:
        subprocess.run(
            ["git", "init", f"{dotfiles_dir}"], check=True, stdout=subprocess.PIPE
        )

        subprocess.run(
            ["git", "remote", "add", "origin", f"git@github.com:{remote}"],
            stdout=subprocess.PIPE,
        )

        print(f"Created a local Git repository for your dotfiles at {dotfiles_dir}")
    except FileNotFoundError as error:
        print(error)
        print("Intialising local Git repository failed, is Git installed?")


@app.command()
def remove() -> None:
    """
    Remove a source file & its destination link from the system.

    (EXPERIMENTAL) Doesn't work for now.
    """
    print("This is an experimental feature & doesn't work for now.")


@app.command()
def link(
    source: Path = typer.Option(
        ..., help="The source file which should point to a link somewhere else."
    ),
    dest: Path = typer.Option(..., help="The destination of the linked source file."),
) -> None:
    """Create a symbolic link for an individual source file."""
    linked_dotfile = Path(Path.home() / dest).expanduser()

    if not linked_dotfile.is_symlink():
        os.symlink(source, dest)
        print(f"Successfully created symlink {source} -> {dest}!")

    # Recreate the data Object to write back to "jefer.json"
    data: dict[str, str] = {}

    try:
        with open(JEFER_DATA_FILE, "r") as file:
            json.dump(data, file, indent=2, sort_keys=True)
    except FileNotFoundError as error:
        raise error


@app.command()
def list() -> None:
    """Show the list of files & the path to their destined links."""
    try:
        with open(JEFER_DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise error

    for property in data.get("dotfiles"):
        if not property:
            print(f"{property.get('source')} -> {property.get('link')}")


@app.command()
def healthcheck() -> None:
    """Check if all of Jefer's features is working as expected."""
    try:
        # Check if "git" was installed or not.
        subprocess.run(["git", "--version"], stdout=subprocess.DEVNULL, check=True)
    except FileNotFoundError:
        print("Git was not found, recheck & reinstall it for Jefer to work properly!")

    # TODO: Create more logic to check if the symlinks aren't corrupted.


if __name__ == "__main__":
    app()
