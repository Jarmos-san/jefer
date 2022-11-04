# Jefer: A Simple Dotfiles Manager

Jefer is a **VERY** simple (with <200 lines of code!) dotfiles management tool
written in Python.

If you Google for dotfiles manager, you will stumble upon a countless
alternatives. And each one of those tools are very good due to their
maturity & the community support. You can read more of such alternatives in the
project documentation -
"[https://jefer.vercel.app/about-the-project/alternatives-to-jefer][1]"

And when compared to the existing alternatives, Jefer provides:

1. True cross-platform support thanks to Python (but support for Windows is not
   tested reliably).

2. Hands-on configuration experience for your tools, Jefer stays away from how
   you configure your tools. It only manages them in a version-control
   environment.

3. Offers a minimal & intuitive user-experience meaning, the user no longer has
   to memorise way too many command-line options & flags.

**NOTE**: Development on Jefer is still underway & its still a very
work-in-progress project, so expect things to break or behave in unintended
ways! If you come across such behaviour, please open an issue/discussion
thread.

## Usage Guidelines

Jefer will eventually be available on a lot other platforms like [Homebrew][2],
[FlatHub][3] & more but for now it's only available through [PyPi][4]. If you
want Jefer to be available on more platforms, then please refer to the docs on
"[_Distribution & Release Guidelines][5]" section before opening a discussion
thread and/or a pull request.

That said, here's how you can install Jefer right now:

```console
pipx install jefer
```

For those of you who're not aware, [`pipx`][6] is the recommended way to install
Python-based CLI tools.

## Usage Terms & Conditions

The project is licensed under the terms & conditions of the MIT License. Hence
you're free to modify, copy, redistribute & use the project for commercial
purposes as long as you adhere to the terms & conditions of the license.

For more information on the licensing details, check out the [LICENSE][1]
document.

Interested in contributing to the project? Check out the contribution guidelines
then.

<!-- Reference Links -->

[1]: https://jefer.vercel.app/about-the-project/alternatives-to-jefer
[2]: https://brew.sh
[3]: https://flathub.org
[4]: https://pypi.org
[5]: https://jefer.vercel.app/contributing-to-the-project/distribution-and-release-guidelines
[6]: https://pypa.github.io/pipx
[7]: ./LICENSE
