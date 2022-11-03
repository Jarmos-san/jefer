# What Does Jefer Have to Offer

Jefer was developed while standing on the "_shoulders of the giants_". Many of
its features were inspired from existing alternatives (_take a look at [some of
the alternatives][1]_).

Regardless, following are the core benefits you'll receive when using Jefer:

- True cross-platform support thanks to Python (_for now only Linux support is
  actively worked on_).
- You've complete control over your configuration files & Jefer doesn't poke
  its nose anywhere.
- Extremely intuitive UI/UX enabling the user to not memorise all the available
  CLI options & flags.

## Cross-Platform Capabilities

Some of the other dotfiles management tools I used earlier like [GNU/Stow][2]
aren't cross-platform (_its only available for Linux-based OSes_). While I
enjoyed using `stow` for its "_no nonsense_" approach I needed something which
simply "_just works_".

The other popular alternatives like [YADM][3] were built with MacOS
capabilities in mind. Its in-built `git` features were something I yearned for
but unfortunately it simply didn't serve my cross-platform needs either.

## Complete Ownership of Your Dotfiles

While I was looking for a true "_cross-platform_" dotfiles management
application, I stumbled across [Chezmoi][4]. Its a compiled binary application
written in Go (_which means its fast!_) but it had some caveats which I didn't
suit my particular preferences.

Following are some of the concerns I've with Chezmoi:

1. Its UI/UX experience is bloated & unintuitive.

2. It relies on [Go Templates][5] to dynamically generate the configuration
   files. It led to a lot of ambiguity & each time some tools needed some
   reconfiguration, the user had to use the `chezmoi edit <config_file>`
   instead of directly editing the `<config_file>`,

3. Chezmoi offers a ton of features which I **RARELY** used! For example, it's
   [file encryption][6] features. Sure encrypting SSH private files is handy
   but how often do you generate those? And its actually better to use
   [Bitwarden][7] instead.

All-in-all Chezmoi is an amazing tool & kudos to its creating it! But I only
wish it was made more intuitive, a little less bloated & stayed away from my
way when editing my configuration files.

Jefer on the other hand offers a **VERY** intuitive & minimal UI/UX which means
you'll remember & know when to invoke which command.

!!! Disclosure

    I still use Chezmoi for managing my dotfiles & I plan on sticking with it
    until Jefer is "_stable_" enough.

## Intuitive & Easy to Remember CLI UI/UX

One core feature of managing dotfiles every other alternative has
over-capitalised on is, "_automating a one-click setup_"! Everything from
GNU/Stow to Chezmoi or YADM offers some form of automation wherein you invoke a
single line of code & the tool/script takes care of the rest.

Users of GNU/Stow relies on custom Shell scripts while YADM & Chezmoi has their
own in-built features to do the same. While its understandable automating
mundane tasks like these is a "_good-to-have_" feature, but the user needs to
ask themselves this question before requesting such features - "_How often do
you setup a brand new machine?_"

If you question is a resounding "**NO**"? Then trust me, you don't want to
complicate your workflow further than how it already is.

Hence, Jefer doesn't offer as much automation as custom Shell scripts or
Chezmoi can provide. But you can expect Jefer to have your back when you need
it the most.

For a more detailed usage guideline on using Jefer, refer to the ["Usage &
Installation Guidelines"][8] section of the documentations.

!!! Warning
    
    Development on Jefer is still **VERY MUCH** a work-in-progress & there's
    no guranteed, certain features will work as expected! Hence, its
    recommended to either wait till the first `major` version is released or
    use the project at your own risk. The project follows
    [Semantic Versioning][9] & you'll be notified of the latest updates if you
    subscribe to the repository.

<!-- Reference Links -->
[1]: ../alternatives-to-jefer
[2]: https://www.gnu.org/software/stow
[3]: https://yadm.io
[4]: https://chezmoi.io
[5]: https://pkg.go.dev/text/template
[6]: https://www.chezmoi.io/user-guide/encryption
[7]: https://bitwarden.com
[8]: ../../usage-guidelines
[9]: https://semver.org
