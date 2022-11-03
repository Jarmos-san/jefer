# How to Use Jefer

As mentioned earlier, Jefer was built with simplicity in mind. In other words,
Jefer compromises on a wide variety of features but takes care of what its
supposed to do **REALLY** well. This intentional withdrawal of certain features
ensures the user knows exactly which command to invoke & when.

That said, this following section will share some more insights on using Jefer
in an CLI environment.

### Initialising a Local Dotfiles Repository

Use the following command to initialise a local `git` repository for managing
you dotfiles.

```shell
# Its compulsory to pass a string representing the remote dotfiles repository
# on GitHub (for now only supports GitHub).
jefer init --remote "Jarmos-san/dotfiles"

# Optionally, tell "jefer" where to store the dotfile sources on the local
# system.
jefer init --source "~/projects/dotfiles" --remote "Jarmos-san/dotfiles"
```

### Removing/Deleting a Local Source File

Unlike a symlink & remove the source from the local repository.

```shell
jefer remove --file "~/.config/nvim/init.lua"
```

### Setup a Symlink for a Certain Source File

Create a symlink of an existing source file to a target location.

```shell
jefer link --source ".config/nvim/init.lua"
```

### List Out All the Source Files & Their Destination

List out all the source files & their respective target links.

```shell
jefer list
```

### Perform an Health-Check Operation

Perform a quick health check to see if `jefer` will operate as expected.

```shell
jefer healthcheck
```
