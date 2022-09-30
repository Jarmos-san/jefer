"""The main entrypoint file for Jefer."""

import typer

app = typer.Typer()


@app.command()
def message() -> None:
    """Print a "Hello World!" message."""
    typer.echo("Hello Jarmos!")


@app.command()
def init() -> None:
    """Create an empty Git repository on the local system."""
    pass


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
def verify() -> None:
    """Check if a source file(s) has a linked destination."""
    pass


@app.command()
def backup() -> None:
    """Use Git to push the latest updates in the source file to a remote repository."""
    pass


if __name__ == "__main__":
    app()
