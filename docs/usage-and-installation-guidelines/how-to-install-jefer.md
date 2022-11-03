# How to Install Jefer

Jefer was created with simplicity in mind & hence its also made available on a
wide range of platforms (like [PyPi][1], [Homebrew][2] & much more!). As such,
this section of the documentation shares some insight in to how to install
Jefer on to your local system. The documentation also sheds some insight into
how you should get started using Jefer post-installation.

## Installing Jefer

The recommended approach for installing Jefer right now is using [`pipx`][3].
It makes installing Python-based CLI applications a breeze since you no longer
have to meddle with creating virtual environments & `$PATH` issues! `pipx` will
take care of everything for you.

That said, run the following command to install Jefer:

```shell
pipx install jefer
```

!!! Note
    Make sure you've `pipx` installed on your local machine. If not check its
    documentation for guidelines on doing so. Thereafter you can check if its
    installed or not by running this command:

    ```shell
    pipx --version
    ```

Once you've Jefer installed, you can start using it! The next section details
the usage guidelines for Jefer.

<!-- Reference Links -->
[1]: https://pypi.org
[2]: https://brew.sh
[3]: https://pypa.github.io/pipx
