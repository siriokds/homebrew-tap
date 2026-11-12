# homebrew-tap

The Homebrew tap of siriokds's programs, already built (macOS on Apple silicon).

Each program is installed with its own line below, to copy and paste in Terminal. The whole name
(`siriokds/tap/…`) is needed the first time: Homebrew loads programs from a tap that is not its
own only when they are named in full, and from then on trusts them.

## texa

Yet another shell text editor: a small editor for the terminal, in the spirit of nano and vim.
Open a file, change it, save, quit.

```sh
brew install siriokds/tap/texa
```

Then `texa notes.txt` opens a file.

`texa --version` tells the version. texa uses the engine of Microsoft Edit (MIT License); its
notice is installed with the program (`CREDITS.md`, in `$(brew --prefix)/share/doc/texa`).

## SparkEdit

A text editor for the Mac whose tabs are miniatures of their pages, with the `spk` command for
the shell (as CotEditor's `cot`). macOS 14 or later.

```sh
brew install --cask siriokds/tap/sparkedit
```

Then `spk notes.txt` opens a file in SparkEdit, starting it if it is not running; a file that
does not exist yet is made, empty. `spk -h` tells the rest.

SparkEdit is not notarized by Apple: open it once from Applications, macOS stops it; then
System Settings › Privacy & Security, **Open Anyway**. From then on it opens as any app, and
`spk` works (until then macOS stops `spk` too).

## From the old taps

texa and SparkEdit had a tap each (`siriokds/texa`, `siriokds/sparkedit`); they are both here
now. Installed from there, move them once:

```sh
brew uninstall texa && brew install siriokds/tap/texa
brew uninstall --cask sparkedit && brew install --cask siriokds/tap/sparkedit
brew untap siriokds/texa siriokds/sparkedit
```

Uninstalling SparkEdit does not touch its notes and settings.

## Updates

`brew update` first, so that Homebrew reads the new versions:

```sh
brew update && brew upgrade
```
