"""The main entrypoint file for Jefer."""

import typer

app = typer.Typer()


@app.command()
def message() -> None:
    """Print a "Hello World!" message."""
    typer.echo("Hello Jarmos!")


if __name__ == "__main__":
    app()
