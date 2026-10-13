"""Genera los SVG animados del README (assets/*.svg). Uso: python3 scripts/build_assets.py"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

BG, PANEL, LINE = "#0a0d14", "#10141e", "#232a3b"
TS, CYAN, MINT, AMBER, PINK, DIM, TXT = "#3178c6", "#61dafb", "#7ee787", "#ffb454", "#ff7eb6", "#6b7690", "#c9d3ea"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

FONT = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    ".": ["0", "0", "0", "0", "0", "0", "1"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
}


def pixel_text(word, x0, y0, px, gap, colors, delay0=1.6):
    """Texto en pixel-art: cada pixel aparece con parpadeo escalonado."""
    out, x, i = [], x0, 0
    for ch in word:
        glyph = FONT[ch]
        col = colors(ch)
        for r, row in enumerate(glyph):
            for c, v in enumerate(row):
                if v == "1":
                    d = delay0 + (i % 17) * 0.035 + (x - x0) / 2200
                    out.append(
                        f'<rect class="px" x="{x + c * px}" y="{y0 + r * px}" width="{px - 2}" height="{px - 2}" rx="2" '
                        f'fill="{col}" style="animation-delay:{d:.2f}s"/>'
                    )
                    i += 1
        x += len(glyph[0]) * px + gap
    return "".join(out), x - gap


def banner():
    px = 15
    ander, xe = pixel_text("ANDER", 0, 0, px, 14, lambda c: CYAN)
    tsx, xe2 = pixel_text(".TSX", xe + 14, 0, px, 14, lambda c: TS if c != "." else AMBER, delay0=2.2)
    total = xe2
    ox = (960 - total) / 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 340" width="960" height="340" role="img" aria-label="Ander.tsx — Desarrollador Full-Stack">
<defs>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{LINE}" stroke-width="1" opacity=".55"/></pattern>
  <linearGradient id="edge" x1="0" x2="1"><stop stop-color="{TS}"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>
  <linearGradient id="scan" x1="0" x2="0" y1="0" y2="1"><stop stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}" stop-opacity=".18"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient>
  <filter id="glow" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <clipPath id="card"><rect x="8" y="8" width="944" height="324" rx="16"/></clipPath>
</defs>
<style>
  text{{font-family:{MONO}}}
  .px{{opacity:0;animation:pop .5s steps(2,end) forwards}}
  @keyframes pop{{0%{{opacity:0}}50%{{opacity:1}}70%{{opacity:.3}}100%{{opacity:1}}}}
  .glow{{animation:pulse 3.6s ease-in-out 3.5s infinite}}
  @keyframes pulse{{50%{{filter:drop-shadow(0 0 7px {CYAN})}}}}
  .boot{{opacity:0;animation:in .01s forwards}}
  .b1{{animation-delay:.1s}}.b2{{animation-delay:.5s}}.b3{{animation-delay:.9s}}
  @keyframes in{{to{{opacity:1}}}}
  .sub{{opacity:0;animation:in .6s 3.4s forwards}}
  .cur{{animation:blink 1.05s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
  .sweep{{animation:sweep 5.5s linear 2s infinite}}
  @keyframes sweep{{from{{transform:translateY(-90px)}}to{{transform:translateY(340px)}}}}
</style>
<rect width="960" height="340" fill="{BG}"/>
<g clip-path="url(#card)">
  <rect x="8" y="8" width="944" height="324" fill="url(#grid)"/>
  <rect class="sweep" x="8" y="0" width="944" height="90" fill="url(#scan)"/>
</g>
<rect x="8" y="8" width="944" height="324" rx="16" fill="none" stroke="url(#edge)" stroke-width="2"/>
<text class="boot b1" x="32" y="40" font-size="13" fill="{DIM}">$ boot ander.tsx --mode=fullstack</text>
<text class="boot b2" x="32" y="60" font-size="13" fill="{MINT}">[ ok ] ui · ux · react · next · node · mongo</text>
<text class="boot b3" x="32" y="80" font-size="13" fill="{MINT}">[ ok ] coding non-stop since 2021</text>
<text x="928" y="40" font-size="13" fill="{MINT}" text-anchor="end">● SYSTEM ONLINE</text>
<g class="glow" transform="translate({ox:.0f},112)" filter="url(#glow)">{ander}{tsx}</g>
<g class="sub">
  <text x="480" y="270" font-size="22" fill="{TXT}" text-anchor="middle" font-weight="700">&lt; Desarrollador Full-Stack /&gt;</text>
  <text x="480" y="300" font-size="15" fill="{DIM}" text-anchor="middle">Construyo experiencias digitales de valor<tspan class="cur" fill="{AMBER}">▌</tspan></text>
</g>
</svg>'''


def whoami():
    lines = [  # (y, items, delay)
        (74, [("❯ ", CYAN, 700), ("whoami", TXT, 700)], 0.2),
        (104, [("ander", AMBER, 700), (" — ", DIM, 400), ("Full-Stack Developer · estudiante de ingeniería", TXT, 400)], 1.0),
        (134, [("age        ", DIM, 400), ("20", MINT, 400)], 1.8),
        (160, [("school     ", DIM, 400), ("UTEZ · Ing. en Desarrollo de Software", CYAN, 400)], 2.3),
        (186, [("focus      ", DIM, 400), ("UX/UI · MERN · web interactiva (Three.js)", PINK, 400)], 2.8),
        (212, [("langs      ", DIM, 400), ("es (nativo) · en (B2)", TXT, 400)], 3.3),
        (254, [("❯ ", CYAN, 700), ("status", TXT, 700)], 4.0),
        (284, [("● ", MINT, 400), ("abierto a proyectos y colaboraciones", MINT, 400)], 4.7),
    ]
    out = []
    for i, (y, items, d) in enumerate(lines):
        tspans = "".join(f'<tspan fill="{c}" font-weight="{w}">{t.replace("&", "&amp;").replace("<", "&lt;")}</tspan>' for t, c, w in items)
        out.append(f'<text class="ln" x="36" y="{y}" font-size="17" xml:space="preserve" style="animation-delay:{d}s" clip-path="url(#c{i})">{tspans}</text>')
    clips = "".join(
        f'<clipPath id="c{i}"><rect class="rv" x="0" y="{y - 22}" width="0" height="30" style="animation-delay:{d}s"/></clipPath>'
        for i, (y, _, d) in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 330" width="960" height="330" role="img" aria-label="Terminal con el perfil de Ander">
<defs>
  <linearGradient id="edge" x1="0" x2="1"><stop stop-color="{TS}"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>
  {clips}
</defs>
<style>
  text{{font-family:{MONO}}}
  .rv{{animation:rv .7s steps(34,end) forwards}}
  @keyframes rv{{to{{width:900px}}}}
  .cur{{animation:blink 1s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
</style>
<rect x="4" y="4" width="952" height="322" rx="14" fill="{PANEL}" stroke="url(#edge)" stroke-width="2"/>
<circle cx="32" cy="30" r="6" fill="{PINK}"/><circle cx="54" cy="30" r="6" fill="{AMBER}"/><circle cx="76" cy="30" r="6" fill="{MINT}"/>
<text x="100" y="35" font-size="14" fill="{DIM}">~/ander.tsx — zsh</text>
<path d="M4 48H956" stroke="{LINE}"/>
{"".join(out)}
<text class="cur" x="36" y="314" font-size="17" fill="{AMBER}">▌</text>
</svg>'''


def divider():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 24" width="960" height="24" role="presentation">
<defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="{TS}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></linearGradient></defs>
<style>.d{{animation:m 3s linear infinite}}@keyframes m{{from{{transform:translateX(-80px)}}to{{transform:translateX(960px)}}}}</style>
<path d="M0 12H960" stroke="url(#g)" stroke-width="2" opacity=".6"/>
<path class="d" d="M0 12H80" stroke="{CYAN}" stroke-width="4" stroke-linecap="round" opacity=".9"/>
</svg>'''


def footer():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 90" width="960" height="90" role="img" aria-label="ander.tsx">
<defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="{TS}"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient></defs>
<style>
  text{{font-family:{MONO}}}
  .w{{stroke-dasharray:960;stroke-dashoffset:960;animation:dash 4s ease-in-out infinite alternate}}
  @keyframes dash{{to{{stroke-dashoffset:0}}}}
  .cur{{animation:blink 1s steps(1) infinite}}@keyframes blink{{50%{{opacity:0}}}}
</style>
<path class="w" d="M0 30H220l14-14 14 28 14-28 14 14H440l12-12 12 24 12-24 12 12H960" fill="none" stroke="url(#g)" stroke-width="2.5"/>
<text x="480" y="72" font-size="14" fill="{DIM}" text-anchor="middle">$ exit 0  ·  gracias por pasar<tspan class="cur" fill="{AMBER}"> ▌</tspan></text>
</svg>'''


for name, fn in [("banner", banner), ("whoami", whoami), ("divider", divider), ("footer", footer)]:
    (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
    print("wrote", name)
