# Home

Jefer is a simple ["dotfiles"](1) management tool developed using Python.

And if you're wondering, "Ah! Yet another dotfiles manager" then you're
probably right in thinking so. I've used everything from [GNU/Stow][2] to
[Chezmoi][3] & none of them suited my needs. Hence, I ventured towards building
my own personalised dotfiles management tool!

## What Does Jefer Have to Offer

A quick Google Search will land you on many such similar projects (_and some of
which are pretty mature_). If you've been programming for quite a while, you'll
probably be aware of some of those alternatives. And if this is your first time
stumbling across the term "_dotfiles management tools_", well don't worry I'll
share some of those aforementioned tools below.

Regardless, following are the core benefits you'll receive when using `jefer`:

- True cross-platform support thanks to Python (_for now only Linux support is
  actively worked on_).
- You've complete control over your configuration files & `jefer` doesn't poke
  its nose anywhere.
- Extremely intuitive UI/UX enabling the user to not memorise all the available
  CLI options & flags.

!!! Warning
    
    Development on `jefer` is still **VERY MUCH** a work-in-progress & there's
    no guranteed, certain features will work as expected! Hence, its
    recommended to either wait till the first `major` version is released or
    use the project at your own risk. The project follows
    [Semantic Versioning][4] & you'll be notified of the latest updates if you
    subscribe to the repository.

## Existing Alternatives & Their Issues

As mentioned earlier, quite a few such projects already exists but none worked
out well for me. As such, following are some of the well-known dotfiles manager
I'm aware of. Please feel free to open a PR if you figured I missed out on
some of the other existing alternatives.

- [Chezmoi][3]
- [GNU/Stow][2]
- [YADM][7]

...and many more!

The said alternatives didn't work out for me because:

1. Chezmoi felt too "bloated" with too many CLI flags/options, features &
   capabilities.

2. GNU/Stow felt too "minimal" & I was continuosly reinventing the wheel with
   customised Bash scripts to automate my configuration workflow.

3. YADM was created keeping in mind the needs a MacBook user while I use a wide
   variety of machines.

For a more detailed explanation on why I created `jefer` check out the ["_Why I
Created `jefer`_"][8] section of the documentation.

## Getting Started Using the Project

Installing & using `jefer` is a rather simple affair, you'll only need to
invoke a single line of command & you're good to go! That said, this section
will help you get started with using `jefer`.

!!! info

    The recommended approach to install `jefer` right now is to use
    [`pipx`][6]. Its a tool to make installing & using Python-based CLI tools
    much easier.

Before you head over to installing & using `jefer`, ensure you've [`pipx`][6]
installed. It'll install `jefer` inside a [virtual environment] for you & make
`jefer` available on `$PATH` as well for you. Once you've installed `pipx`, run
the following commands to get started:

```shell
# Check if "pipx" was installed & made available on $PATH or not.
pipx --version

# Install "jefer" using "pipx".
pipx install jefer
```

If you successfully installed `jefer`, check out the "[_Usage Guidelines_][10]"
section for more information on the daily usage instructions.

## Contributing to the Project

`jefer` is an open-source project & licensed under the [MIT License][5] as
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
the "[_Contribution Guidelines_][9]" section of the documentations.

!!! tip
    
    Not comfortable writing Python code, yet you would still like to contribute
    to the project? Well don't worry there are countless ways to share your
    skills with the community! ❤️

## Distribution & Usage Rights

The project is licensed under the terms & conditions (T&Cs) of the MIT License.
Hence, you're free to copy, modify, redistribute & use the project for both
commerical & non-commercial purposes as long as you adhere to the T&Cs of the
license.

For more information on the licensing details, refer to the [LICENSE][5]
document.

<!-- Reference Links -->
[1]: https://dotfiles.github.io
[2]: https://www.gnu.org/software/stow
[3]: https://chezmoi.io
[4]: https://semver.org
[5]: ../license
[6]: https://pypa.github.io/pipx
[7]: https://yadm.io
[8]: ../about/why-was-jefer-created
[9]: ./contributing-to-the-project
[10]: ./usage-guidelines
