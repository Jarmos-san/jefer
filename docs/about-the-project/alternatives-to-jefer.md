# Existing Alternatives for Managing Your Dotfiles

As mentioned earlier in a previous section of the documentations, Jefer isn't
the only one of its kind in existence. Some of those alternatives has been in
development for a **VERY** long time & are mature projects. Having used most of
the existing alternatives, I've stumbled across certain concerns which simply
didn't work out for me well enough. Hence, I started this venture into
developing my own tool instead!

That said, following are some popular dotfiles manager which you might want to
look at before deciding on using either Jefer or a more mature one mentioned
below;

- [Chezmoi][1]
- [GNU/Stow][2]
- [YADM][3]

...and many more!

The said alternatives didn't work out for me because:

1. Chezmoi felt too "bloated" with too many CLI flags/options, features &
   capabilities.

2. GNU/Stow felt too "minimal" & I was continuosly reinventing the wheel with
   customised Bash scripts to automate my configuration workflow.

3. YADM was created keeping in mind the needs a MacBook user while I use a wide
   variety of machines.

For a more detailed explanation on why I created Jefer check out the ["_Why I
Created Jefer_"][4] section of the documentation.

<!-- Reference Links -->
[1]: https://chezmoi.io
[2]: https://www.gnu.org/software/stow
[3]: https://yadm.io
[4]: ../why-was-jefer-created
