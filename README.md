# homebrew-tap

The Homebrew tap of siriokds's programs, already built (macOS on Apple silicon).

```sh
brew tap siriokds/tap
```

## texa

Yet another shell text editor: a small editor for the terminal, in the spirit of nano and vim.
Open a file, change it, save, quit.

```sh
brew install texa
texa notes.txt
```

`texa --version` tells the version. texa uses the engine of Microsoft Edit (MIT License); its
notice is installed with the program (`CREDITS.md`, in `$(brew --prefix)/share/doc/texa`).

## SparkEdit

A text editor for the Mac whose tabs are miniatures of their pages, with the `spk` command for
the shell (as CotEditor's `cot`). macOS 14 or later.

```sh
brew install --cask sparkedit
spk notes.txt
```

`spk file` opens the file in SparkEdit, starting it if it is not running; a file that does not
exist yet is made, empty. `spk -h` tells the rest.

SparkEdit is not notarized by Apple: the first time, macOS stops it. Open System Settings ›
Privacy & Security and click **Open Anyway**; from then on it opens as any app.

## Updates

`brew update` first, so that Homebrew reads the new versions:

```sh
brew update && brew upgrade
```
