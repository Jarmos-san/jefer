"""The main entrypoint file for Jefer."""

import json
import os
import subprocess
from pathlib import Path

import typer

app = typer.Typer()


def validate_remote_repo(repo: str) -> bool:
    """Utilitarian function to check if a remote repository is valid or not."""
    # TODO: Configure the logic a bit more using regex to check if the suggested remote
    # repository is valid or not.
    print(repo)
    return True


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
def remove(
    file: Path = typer.Option(..., help="The source file to unlink & remove"),
) -> None:
    """Remove a source file & its destination link from the system."""
    source_file = Path(Path.cwd() / file).expanduser()

    if source_file.is_symlink():
        os.unlink(source_file)

    os.remove(source_file)


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


@app.command()
def list() -> None:
    """Show the list of files & the path to their destined links."""
    pass


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
