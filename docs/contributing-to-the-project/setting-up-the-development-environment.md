# Setting Up the Development Environment

Jefer is written in Python & hence you need to have a working Python
environment on your local system to develop Jefer. As such this section of the
documentations details how you can setup the development environment.

## Installing the Prerequisite Tools

Python isn't the only tool used to develop Jefer. There are a handful of other
tools like [Poetry][1] & [Task][2] which makes the development experience very
smooth. Hence, before you write & contribute your first line of code, its
necessary to setup those tools beforehand.

And this section of the article will shed some insights into setting up those
development tools for you & how to use them afterwards.

So, follow these guidelines to setup the development environment:

1. Ensure Python is installed & verify by invoking this command:

    ```shell
    python --version
    ```

2. Install Poetry (the Python Package Manager) by following the [official
installation instruction][3] & verify it works as expected:

    ```shell
    poetry --version
    ```

3. Install Task (an intuitive alternative to [GNU/Make][4]) by following the
[instructions laid down in the official documentations][5] & verify it:

    ```shell
    task --version
    ```

With all the necessary development tools installed & verified, it's time to
understand how to use those in context to developing Jefer. The next section of
the documentations will guide you through exactly that.

## Writing Your First Line of Code

As mentioned earlier, Jefer uses `poetry` for its package management
requirements. Its intuititve, fast (_subjectively_) & is actively developed as
you read this documentation. Besides, package management, Poetry also takes
care of activating the virtual environment. Regardless, all of these monotonous
& mundane tasks are automated using `task`. At no point in time while developing
Jefer, will you ever have to directly invoke `poetry`. And this level of
automation was achieved thanks to `task`.

`task` is configured through the `Taskfile.yml` & its recommended to go through
the official documentations before understanding how `task` operates.

But the gist is, you can invoke the following command & print a list of all the
available "_tasks_" you can invoke with a single line of code!

```shell
task --list
```

And invoke the following command to get the "_summary_" of what an individual
"_task_" is about.

```shell
task docs:serve --summary
```

In other words, following are quick examples to get you started with developing
Jefer;

```shell
# Execute the virtual environment.
task venv

# Install all the necessary dependencies for the project.
task install:deps

# Build & run a development version of the documentations which is accessible
# at: localhost:8000
task docs:serve
```

With this information you can now confidently proceed ahead & contribute your
first line of code to Jefer's source code!

!!! Note
    Found something missing information which you believe should be noted down
    here? Then feel free to create a disccusion thread and/or open a pull
    request.

<!-- Reference Links -->
[1]: https://python-poetry.org
[2]: https://taskfile.dev
[3]: https://python-poetry.org/docs/#installation
[4]: https://www.gnu.org/software/make
[5]: https://taskfile.dev/installation
