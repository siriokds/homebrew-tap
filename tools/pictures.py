#!/usr/bin/env python3
"""The pictures of this README, made here and kept in images/.

  texa.svg    texa's real screen as an SVG terminal window, from a dump of the program's own
              cells and colours (tools/texa-screen.json). To make the dump again, in the Texa
              repository, at every version (the version is in the title):
                  TEXA_DUMP=<this folder>/texa-screen.json cargo test readme_screen -- --ignored
              The same run writes texa-find.json and texa-about.json beside it.
  hexa.svg    the same for hexa (tools/hexa-screen.json, hexa-find.json, hexa-commands.json,
              hexa-about.json), in the Hexa repository:
                  COLORTERM=truecolor HEXA_THEME=dark HEXA_DUMP=<this folder>/hexa-screen.json \
                      cargo test -p hexa-tui readme_screen -- --ignored
  banner.svg  the heading, with the install lines typed one after the other.

  python3 tools/pictures.py tools images

SparkEdit's pictures are screenshots of a copy started with --demo-tabs=N (its sample texts),
cut and rounded by tools/crop.swift: crop in out x y width height radius outWidth.
N = 6 the first picture (wait some seconds: the content titles arrive from the Mac's model),
24, 30, 35 and 128 the four states of the tabs; All Pages is N = 100 after Cmd+. sent to the
copy without bringing it to the front (tools/keyto.swift: keyto <pid> 47 cmd).
"""
import json, sys, html, re

MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"
BG, FG = "#222733", "#e6e6e6"      # texa's palette: BACKGROUND, TEXT
FRAME = "#3a4050"

def esc(t): return html.escape(t, quote=False)

def words(text, x0, y, cw, fill, extra=""):
    """Each word at its own column, as wide as its cells: no run of spaces is left to the
    viewer's font or to its way of keeping them."""
    out = []
    for m in re.finditer(r"\S+", text):
        w = m.group(0)
        out.append(f'<text x="{x0 + m.start()*cw:.1f}" y="{y}" textLength="{len(w)*cw:.1f}" lengthAdjust="spacingAndGlyphs" fill="{fill}"{extra}>{esc(w)}</text>')
    return "".join(out)

# The lines of the frames, drawn as lines: as text they leave gaps between the rows.
BOX = "─│┃╭╮╰╯"

def box(sym, x0, y0, cw, lh, colour):
    """A frame's piece in its cell, as a stroke: continuous from cell to cell."""
    cx, cy = x0 + cw / 2, y0 + lh / 2
    r = min(cw, lh) * 0.45
    paths = {
        "─": f"M{x0:.1f} {cy:.1f}H{x0 + cw:.1f}",
        "│": f"M{cx:.1f} {y0:.1f}V{y0 + lh:.1f}",
        "┃": f"M{cx:.1f} {y0:.1f}V{y0 + lh:.1f}",
        "╭": f"M{x0 + cw:.1f} {cy:.1f}H{cx + r:.1f}Q{cx:.1f} {cy:.1f} {cx:.1f} {cy + r:.1f}V{y0 + lh:.1f}",
        "╮": f"M{x0:.1f} {cy:.1f}H{cx - r:.1f}Q{cx:.1f} {cy:.1f} {cx:.1f} {cy + r:.1f}V{y0 + lh:.1f}",
        "╰": f"M{cx:.1f} {y0:.1f}V{cy - r:.1f}Q{cx:.1f} {cy:.1f} {cx + r:.1f} {cy:.1f}H{x0 + cw:.1f}",
        "╯": f"M{cx:.1f} {y0:.1f}V{cy - r:.1f}Q{cx:.1f} {cy:.1f} {cx - r:.1f} {cy:.1f}H{x0:.1f}",
    }
    width = 2.6 if sym == "┃" else 1.3
    return f'<path d="{paths[sym]}" fill="none" stroke="{colour}" stroke-width="{width}"/>'

def dots(x, y):
    return "".join(f'<circle cx="{x + i*20}" cy="{y}" r="6" fill="{c}"/>' for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]))

def screen(dump, out, name):
    """A terminal program's real screen (`dump`: its cells and colours) as an SVG window."""
    d = json.load(open(dump))
    W, H, cells = d["w"], d["h"], d["cells"]
    cw, lh, fs = 8.6, 21, 14
    pad, bar = 16, 38
    width, height = W * cw + pad * 2, H * lh + bar + pad
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}" width="{width:.0f}" height="{height:.0f}" role="img" aria-label="{name} in a terminal window">',
         f'<rect x="0.5" y="0.5" width="{width-1:.0f}" height="{height-1:.0f}" rx="12" fill="{BG}" stroke="{FRAME}"/>',
         dots(22, 19),
         f'<text x="{width/2:.0f}" y="24" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#8a8f9c">{name} — {W}×{H}</text>',
         f'<g font-family="{MONO}" font-size="{fs}" xml:space="preserve">']
    for y in range(H):
        row = cells[y * W:(y + 1) * W]
        # runs of the same look
        runs, start = [], 0
        for x in range(1, W + 1):
            if x == W or row[x][1:] != row[start][1:]:
                runs.append((start, x))
                start = x
        ty = bar + y * lh
        for a, b in runs:
            sym, fg, bg, bold = row[a]
            if bg:
                o.append(f'<rect x="{pad + a*cw:.1f}" y="{ty}" width="{(b-a)*cw:.1f}" height="{lh}" fill="{bg}"/>')
        for a, b in runs:
            _, fg, _, bold = row[a]
            for x in range(a, b):
                if row[x][0] in BOX:
                    o.append(box(row[x][0], pad + x*cw, ty, cw, lh, fg or FG))
            text = "".join(" " if c[0] in BOX else c[0] for c in row[a:b])
            if not text.strip(" "):
                continue
            o.append(words(text, pad + a*cw, ty + 15, cw, fg or FG, ' font-weight="700"' if bold else ""))
    # the cursor, as the Terminal's block (none where the program hides it)
    if d["cx"] >= 0 and d["cy"] >= 0:
        o.append(f'<rect x="{pad + d["cx"]*cw:.1f}" y="{bar + d["cy"]*lh}" width="{cw:.1f}" height="{lh}" fill="#b4b7bf"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.2s" repeatCount="indefinite"/></rect>')
    # The character under the cursor shows through it, as in the terminal.
    under = cells[d["cy"] * W + d["cx"]][0] if d["cy"] < H and d["cx"] < W else " "
    if under.strip():
        o.append(f'<text x="{pad + d["cx"]*cw:.1f}" y="{bar + d["cy"]*lh + 15}" textLength="{cw:.1f}" lengthAdjust="spacingAndGlyphs" fill="{BG}">{esc(under)}<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.2s" repeatCount="indefinite"/></text>')
    o.append("</g></svg>")
    open(out, "w").write("\n".join(o) + "\n")

def banner(out):
    Wd, Ht = 960, 326
    cx0, cy0, cwid, chei = 452, 34, 476, 258   # the terminal card
    fs, cw, lh = 14, 8.45, 25
    tx = cx0 + 22
    lines = [  # (text, colour, typed?)
        ("# once, for all the apps", "#7f8594", False),
        ("$ brew tap siriokds/tap && brew trust siriokds/tap", FG, True),
        ("# then one line per app", "#7f8594", False),
        ("$ brew install texa", FG, True),
        ("$ brew install hexa", FG, True),
        ("$ brew install --cask sparkedit", FG, True),
    ]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {Wd} {Ht}" width="{Wd}" height="{Ht}" role="img" aria-label="siriokds/tap: brew tap siriokds/tap, then brew install texa, brew install hexa and brew install --cask sparkedit">',
         '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1b1d24"/><stop offset="1" stop-color="#15161b"/></linearGradient></defs>',
         f'<rect x="0.5" y="0.5" width="{Wd-1}" height="{Ht-1}" rx="18" fill="url(#g)" stroke="#2c303a"/>',
         # the left side: what this is
         f'<text x="48" y="105" font-family="{MONO}" font-size="13" letter-spacing="3" fill="#8a8f9c">HOMEBREW TAP</text>',
         f'<text x="46" y="163" font-family="{MONO}" font-size="46" font-weight="700" fill="{FG}">siriokds<tspan fill="#e15646">/</tspan>tap</text>',
         f'<text x="48" y="209" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Helvetica, Arial, sans-serif" font-size="19" fill="#c3c6cf">Small editors for the Mac,</text>',
         f'<text x="48" y="235" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Helvetica, Arial, sans-serif" font-size="19" fill="#c3c6cf">ready to install with Homebrew.</text>',
         f'<rect x="48" y="259" width="56" height="3" rx="1.5" fill="#e15646"/><rect x="110" y="259" width="56" height="3" rx="1.5" fill="#ffc107"/>',
         # the terminal
         f'<rect x="{cx0}" y="{cy0}" width="{cwid}" height="{chei}" rx="12" fill="{BG}" stroke="{FRAME}"/>',
         dots(cx0 + 22, cy0 + 19),
         f'<g font-family="{MONO}" font-size="{fs}" xml:space="preserve">']
    t = 0.6            # when the typing of the next typed line starts
    total = 0
    plan = []
    for text, colour, typed in lines:
        dur = len(text) * 0.035 if typed else 0
        plan.append((t, dur))
        t += dur + (0.55 if typed else 0.0)
    total = t
    for i, ((text, colour, typed), (begin, dur)) in enumerate(zip(lines, plan)):
        y = cy0 + 62 + i * lh
        w = len(text) * cw
        if typed:
            # Shown whole where animations do not run; where they do, hidden from the start and
            # typed in its turn.
            k0, k1 = begin / total, (begin + dur) / total
            o.append(f'<clipPath id="l{i}"><rect x="{tx-2}" y="{y-16}" width="{w+4:.1f}" height="{lh}"><animate attributeName="width" values="0;0;{w+4:.1f};{w+4:.1f}" keyTimes="0;{k0:.4f};{k1:.4f};1" dur="{total:.2f}s" fill="freeze"/></rect></clipPath>')
            o.append(f'<g clip-path="url(#l{i})">{words("$", tx, y, cw, "#ffc107")}{words(" " + text[1:], tx, y, cw, colour)}</g>')
        else:
            k0 = max(begin - 0.25, 0) / total
            o.append(f'<g>{words(text, tx, y, cw, colour)}<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{k0:.4f};{min(k0+0.02,1):.4f};1" dur="{total:.2f}s" fill="freeze"/></g>')
    # the prompt waiting, after the last line
    y = cy0 + 62 + len(lines) * lh
    o.append(f'<g><animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.98;0.99;1" dur="{total:.2f}s" fill="freeze"/><text x="{tx}" y="{y}" fill="#ffc107">$</text>'
             f'<rect x="{tx + 2*cw:.1f}" y="{y-14}" width="{cw:.1f}" height="18" fill="#b4b7bf"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.2s" repeatCount="indefinite"/></rect></g>')
    o.append("</g></svg>")
    open(out, "w").write("\n".join(o) + "\n")

if __name__ == "__main__":
    tools, outdir = sys.argv[1], sys.argv[2]
    # Each program's view, then the other screens shown in the page.
    shots = {
        "texa": ["find", "about"],
        "hexa": ["find", "commands", "about"],
    }
    for name, others in shots.items():
        screen(f"{tools}/{name}-screen.json", f"{outdir}/{name}.svg", name)
        for other in others:
            screen(f"{tools}/{name}-{other}.json", f"{outdir}/{name}-{other}.svg", name)
    banner(f"{outdir}/banner.svg")
