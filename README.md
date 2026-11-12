<p align="center">
  <img src="images/banner.svg" alt="siriokds/tap — small text editors for the Mac, ready to install with Homebrew" width="100%">
</p>

<p align="center">
  <a href="#get-started"><b>Get started</b></a> &nbsp;·&nbsp;
  <a href="#texa"><b>texa</b></a> &nbsp;·&nbsp;
  <a href="#sparkedit"><b>SparkEdit</b></a> &nbsp;·&nbsp;
  <a href="https://github.com/siriokds/homebrew-tap/releases"><b>Releases</b></a>
</p>

<p align="center"><sub>Mac with Apple silicon &nbsp;·&nbsp; programs already built, nothing to compile</sub></p>

<br>

## Get started

**1 · Add the tap** — only once. It serves every app of this page, now and later.

```sh
brew tap siriokds/tap && brew trust siriokds/tap
```

**2 · Install what you like** — one short line each. Every box has a copy button at its top right.

<table>
<tr>
<td width="50%" valign="top">

**[texa](#texa)** &nbsp;—&nbsp; the editor for the terminal

```sh
brew install texa
```

</td>
<td width="50%" valign="top">

**[SparkEdit](#sparkedit)** &nbsp;—&nbsp; the editor for the Mac

```sh
brew install --cask sparkedit
```

</td>
</tr>
</table>

<sub>`brew trust` tells Homebrew that it may load programs from this tap: Homebrew 7 refuses the
short names of a tap that is not its own until then.</sub>

<br>

---

## texa

<p align="center">
  <img src="images/texa.svg" alt="texa in a terminal window: the file, the line numbers, the keys at the bottom" width="760">
</p>

A small text editor for the **terminal**, in the spirit of nano and vim: open a file, change it,
save, quit.

<table>
<tr><td width="150"><b>Find and replace</b></td><td><code>Ctrl+F</code>, as Visual Studio's: <code>F3</code> goes to the next place, replace one or all (one undo takes it back)</td></tr>
<tr><td width="150"><b>Word wrap</b></td><td>long lines go on in the next row; <code>Ctrl+K W</code> switches it</td></tr>
<tr><td width="150"><b>Clipboard</b></td><td>the system's: <code>Ctrl+C</code>, <code>Ctrl+X</code>, <code>Ctrl+V</code></td></tr>
<tr><td width="150"><b>Save As</b></td><td><code>Ctrl+O</code>, with <code>Tab</code> completing the name and a question before writing over a file</td></tr>
<tr><td width="150"><b>Keys in sight</b></td><td>always written at the bottom; they rearrange themselves as the window narrows</td></tr>
</table>

**Install**

```sh
brew install texa
```

**Update** &nbsp;<sub>`brew update` first reads the new versions</sub>

```sh
brew update && brew upgrade texa
```

**Use** &nbsp;—&nbsp; `texa notes.txt` opens a file, `texa` alone an empty page. The version is
beside the name, at the top left; `F10` quits.

<sub>texa uses the engine of Microsoft Edit (MIT License); its notice is installed with the
program (`CREDITS.md`, in `$(brew --prefix)/share/doc/texa`).</sub>

<br>

---

## SparkEdit

<p align="center">
  <img src="images/sparkedit.png" alt="SparkEdit: each tab has a miniature of its page, its name and, in red, what it contains" width="760">
</p>

A text editor for the **Mac** whose tabs are miniatures of their pages. Beside each name, in
red, a few words on what the document contains: the Mac writes them by itself. macOS 14 or
later.

**The tabs follow how many documents are open** (up to 128):

<table>
<tr><td align="center"><sub><b>a few documents</b> — the names</sub><br><img src="images/tabs-names.png" alt="Tabs with their names" width="700"></td></tr>
<tr><td align="center"><sub><b>more</b> — the names shorten, the number stays</sub><br><img src="images/tabs-short.png" alt="Tabs with shortened names" width="700"></td></tr>
<tr><td align="center"><sub><b>many</b> — each tab is a miniature of its page</sub><br><img src="images/tabs-miniatures.png" alt="Tabs as miniatures of the pages" width="700"></td></tr>
<tr><td align="center"><sub><b>a hundred and more</b> — bars, as tall as their text is long</sub><br><img src="images/tabs-bars.png" alt="Tabs as bars" width="700"></td></tr>
</table>

**All Pages** (`⌘.`) — every document as a page, with its first lines and what it contains;
type, and only the pages with those words stay.

<p align="center">
  <img src="images/all-pages.png" alt="All Pages: a grid of the open documents as pages, with a field to filter them" width="760">
</p>

<table>
<tr><td width="150"><b>Titles by themselves</b></td><td>a few words on what each document contains, beside its name: written on the Mac by Apple's on-device model (Apple Intelligence, macOS 26 or later), with nothing to ask for</td></tr>
<tr><td width="150"><b>All Pages</b></td><td><code>⌘.</code> shows every document as a page, filtered by what it contains</td></tr>
<tr><td width="150"><b>Session</b></td><td>every document comes back at the next start, the ones never saved too</td></tr>
<tr><td width="150"><b>Find & Replace</b></td><td><code>⌘F</code> and <code>⌘H</code>, with regular expressions; Replace All is one undo</td></tr>
<tr><td width="150"><b>Big files</b></td><td>a file of megabytes has its tab at once and fills in while you look</td></tr>
<tr><td width="150"><b>From the shell</b></td><td><code>spk notes.txt</code> opens the file here, as CotEditor's <code>cot</code></td></tr>
</table>

**Install**

```sh
brew install --cask sparkedit
```

> [!IMPORTANT]
> **The first time only.** SparkEdit is not notarized by Apple, so macOS stops it:
> 1. open SparkEdit from Applications and close macOS's message;
> 2. open **System Settings › Privacy & Security** and click **Open Anyway**.
>
> From then on it opens as any app, and `spk` works (until then macOS stops `spk` too).

**Update** &nbsp;<sub>`brew update` first reads the new versions; Homebrew closes SparkEdit if it is open</sub>

```sh
brew update && brew upgrade --cask sparkedit
```

<sub>If macOS stops SparkEdit after an update, **Open Anyway** again as the first time.</sub>

**Use** &nbsp;—&nbsp; `spk notes.txt` opens the file in SparkEdit, starting it if it is not
running; a file that does not exist yet is made, empty. `spk -h` tells the rest.

<br>

---

<details>
<summary><b>Installed from the old taps</b> (<code>siriokds/texa</code>, <code>siriokds/sparkedit</code>)?</summary>

<br>

Both programs are here now. Move them once (SparkEdit's notes and settings are not touched):

```sh
brew uninstall texa && brew uninstall --cask sparkedit
brew untap siriokds/texa siriokds/sparkedit
brew tap siriokds/tap && brew trust siriokds/tap
brew install texa && brew install --cask sparkedit
```

</details>
