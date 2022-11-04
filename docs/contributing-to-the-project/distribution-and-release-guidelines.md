# Distribution & Release Guidelines

Jefer is supported on every platform (_from Linux to Windows & MacOS_) although
its been extensively tested on Linux. So the other platforms are free to
download Jefer, use it & provide feedback on unintended behaviour.

But to be able to do that, one needs Jefer to be available for distribution on
their platforms! Hence, this section of the documentation sheds light on how
should Jefer be distributed.

**DO NOTE**, the contents of this documentation are by no means written in stone
& hence use your best judgement to suggest/contribute towards making Jefer
available on other platforms as well!

But for now, Jefer is [available only on PyPi][1] & the recommended approach
for downloading it is using [`pipx`][2]. That said, here's how you can install
Jefer on your local system.

```shell
pipx install jefer
```

Once installed, you can check if `jefer` works as expected by running the
following command:

```shell
jefer --help
```


!!! Info
    Distribution on other platforms like [Homebrew][3], [FlatHub][4] will be
    supported eventually but for now, if you would like to make Jefer be
    available on your favourite platform as well? Please don't hesitate to open
    a discussion/issue thread and/or a pull request with your suggestions.

<!-- Reference Links -->
[1]: https://pypi.org/project/jefer
[2]: https://pypa.github.io/pipx
[3]: https://brew.sh
[4]: https://flathub.org
