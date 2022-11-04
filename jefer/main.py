"""The main entrypoint file for Jefer."""

import json
import os
import subprocess
from pathlib import Path
from typing import Optional

import typer

JEFER_DATA_FILE = Path.home() / ".local/share/jefer/jefer.json"

app = typer.Typer()


@app.command()
def init(
    source: Path = typer.Option(
        Path.home() / ".dotfiles", help="The path for storing the dotfiles."
    ),
    remote: Optional[str] = typer.Option(
        None, help="The remote repository for backing up the dotfiles."
    ),
) -> None:
    """Create & initialise an empty Git repository locally."""
    # Store the expanded path as a variable for easier manipulation later on.
    dotfiles_dir = source.expanduser()

    # Create the "dotfiles" source directory if doesn't already exist.
    if not dotfiles_dir.exists():
        dotfiles_dir.mkdir(parents=True, exist_ok=True)

    # Dictionary representing the initial data about the local dotfiles repository.
    jefer_initialisation_data = {"source_directory": str(dotfiles_dir)}

    try:
        with open(JEFER_DATA_FILE, "w") as file:
            json.dump(jefer_initialisation_data, file)
    except FileNotFoundError as error:
        raise error

    try:
        subprocess.run(
            ["git", "init", f"{dotfiles_dir}"], check=True, stdout=subprocess.PIPE
        )

        if not remote:
            subprocess.run(
                ["git", "remote", "add", "origin", f"git@github.com:{remote}"],
                stdout=subprocess.PIPE,
            )

        print(f"Created a local Git repository for your dotfiles at {dotfiles_dir}")
    except FileNotFoundError as error:
        raise error


@app.command()
def remove(
    file: Path = typer.Option(..., help="Relative path to the file/folder to remove.")
) -> None:
    """Remove a source file & its destination link from the system."""
    try:
        with open(JEFER_DATA_FILE, "r") as jefer_data_file:
            data = json.load(jefer_data_file)
    except FileNotFoundError as error:
        raise error

    source_directory = Path(data.get("source_directory"))
    source_file = source_directory / file

    if source_file in source_directory.iterdir():
        source_file.unlink(missing_ok=True)

    print(f"{file} was unlinked & removed from {source_directory}")


@app.command()
def link(
    file: Path = typer.Option(
        ..., help="The source file which should point to a link somewhere else."
    ),
    target: Path = typer.Option(..., help="The target location for the symlink."),
) -> None:
    """Create a symbolic link for an individual source file."""
    with open(JEFER_DATA_FILE, "r") as jefer_data_file:
        data = json.load(jefer_data_file)

    source_directory = Path(data.get("source_directory"))
    source_file = source_directory / file

    if not source_file.is_symlink():
        os.symlink(source_file, Path(target).expanduser())

    print(f"The {file} is now linked to {file.resolve()}")


@app.command()
def list() -> None:
    """Show the list of files & the path to their destined links."""
    try:
        with open(JEFER_DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise error

    for element in Path(data.get("source_directory")).iterdir():
        if element.is_symlink():
            print(f"{element} is linked to {element.resolve()}")


@app.command()
def healthcheck() -> None:
    """Check if all of Jefer's features are working as expected."""
    try:
        # Check if "git" was installed or not.
        subprocess.run(["git", "--version"], stdout=subprocess.DEVNULL, check=True)
    except FileNotFoundError:
        print("Git was not found, recheck & reinstall it for Jefer to work properly!")

    # INFO: Check if Jefer was initialised or not.
    if not Path(JEFER_DATA_FILE).exists():
        print(
            "Forgot to initialise Jefer? Check 'jefer init --help' for more information"
        )

    # TODO: Print out some info based on exit codes of the logic above.


if __name__ == "__main__":
    app()
