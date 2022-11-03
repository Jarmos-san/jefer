# Home

Jefer is a simple ["dotfiles"](1) management tool developed using Python.

And if you're wondering, "Ah! Yet another dotfiles manager" then you're
probably right in thinking so. I've used everything from [GNU/Stow][2] to
[Chezmoi][3] & none of them suited my needs. Hence, I ventured towards building
my own personalised dotfiles management tool!

You can read more about the reasons behind developing the project in the
"[Reasons Behind Creating Jefer][4]". But the gist is, Jefer provides a more
intuitive & less bloated alternative to existing alternatives. You can read
more bout the existing alternatives & Jefer's features at - "[Other Existing
Dotfiles Management Alternatives][5]" & "[Features Jefer Offers][6]".

## Getting Started Using the Project

Installing & using `jefer` is a rather simple affair, you'll only need to
invoke a single line of command & you're good to go! That said, this section
will help you get started with using `jefer`.

!!! info

    The recommended approach to install `jefer` right now is to use
    [`pipx`][6]. Its a tool to make installing & using Python-based CLI tools
    much easier.

Before you head over to installing & using `jefer`, ensure you've [`pipx`][7]
installed. It'll install `jefer` inside a [virtual environment][8] for you &
make `jefer` available on `$PATH` as well for you. Once you've installed
`pipx`, run the following commands to get started:

```shell
# Check if "pipx" was installed & made available on $PATH or not.
pipx --version

# Install "jefer" using "pipx".
pipx install jefer
```

If you successfully installed `jefer`, check out the "[_Usage Guidelines_][9]"
section for more information on the daily usage instructions.

## Contributing to the Project

`jefer` is an open-source project & licensed under the [MIT License][10] as
well! What it means is, you as an user are free to take a look at the source &
contribute to the project as well!

That said, following are some ways to contribute to the project:

1. Report bugs & related concerns, open an issue/discussion thread for further
   clarification on the concern.

2. Improve the documentations (_which is also a great way to get started
   contributing to open-source projects_).

3. Suggest improvements, features and/or write more test cases for the project.

...and much more! Those were only a handful ways you could contribute towards
the success of the project. But I'm sure your skills & knowledge might prove
helpful in one way or the other. Having second thoughts about opening your
first PR? Then feel free to reach out to us.

For more information on the contribution guidelines of the project, refer to
the "[_Contribution Guidelines_][11]" section of the documentations.

!!! tip
    
    Not comfortable writing Python code, yet you would still like to contribute
    to the project? Well don't worry there are countless ways to share your
    skills with the community! ❤️

## Distribution & Usage Rights

The project is licensed under the terms & conditions (T&Cs) of the MIT License.
Hence, you're free to copy, modify, redistribute & use the project for both
commerical & non-commercial purposes as long as you adhere to the T&Cs of the
license.

For more information on the licensing details, refer to the [LICENSE][10]
document.

<!-- Reference Links -->
[1]: https://dotfiles.github.io
[2]: https://www.gnu.org/software/stow
[3]: https://chezmoi.io
[4]: ./about-the-project/why-was-jefer-created
[5]: ./about-the-project/alternatives-to-jefer
[6]: ./about-the-project/features-jefer-offers
[7]: https://pypa.github.io/pipx
[8]: https://docs.python.org/3/tutorial/venv.html
[9]: ./usage-guidelines
[10]: ../license
[11]: ./contributing-to-the-project
