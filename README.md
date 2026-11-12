# homebrew-tap

The Homebrew tap of siriokds's programs, already built (macOS on Apple silicon).

```sh
brew install siriokds/tap/texa
brew install --cask siriokds/tap/sparkedit
```

Always with the whole name (`siriokds/tap/…`) the first time: Homebrew loads programs from a tap
that is not its own only when they are named in full, and from then on trusts them (`brew
upgrade` works by itself).

## texa

Yet another shell text editor: a small editor for the terminal, in the spirit of nano and vim.
Open a file, change it, save, quit.

```sh
brew install siriokds/tap/texa
texa notes.txt
```

`texa --version` tells the version. texa uses the engine of Microsoft Edit (MIT License); its
notice is installed with the program (`CREDITS.md`, in `$(brew --prefix)/share/doc/texa`).

## SparkEdit

A text editor for the Mac whose tabs are miniatures of their pages, with the `spk` command for
the shell (as CotEditor's `cot`). macOS 14 or later.

```sh
brew install --cask siriokds/tap/sparkedit
spk notes.txt
```

`spk file` opens the file in SparkEdit, starting it if it is not running; a file that does not
exist yet is made, empty. `spk -h` tells the rest.

SparkEdit is not notarized by Apple: open it once from Applications, macOS stops it; then
System Settings › Privacy & Security, **Open Anyway**. From then on it opens as any app, and
`spk` works (until then macOS stops `spk` too).

## Updates

`brew update` first, so that Homebrew reads the new versions:

```sh
brew update && brew upgrade
```
