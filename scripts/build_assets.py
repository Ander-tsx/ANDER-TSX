"""Genera las ventanas de terminal (SVG estáticos, monocromo) del README.
Uso: python3 scripts/build_assets.py"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

BG, BORDER, BAR = "#0d0d0d", "#3a3a3a", "#161616"
FG, DIM, BOLD = "#c8c8c8", "#7a7a7a", "#f0f0f0"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
PROMPT = "ander@MacBook-Pro ~ % "
W, FS, LH, PADX, TOP = 900, 15, 22, 28, 48

GLYPHS = {
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


def cmd(c):
    return [(PROMPT, DIM), (c, BOLD)]


def window(name, title, lines, art=None):
    """lines: lista de listas [(texto, color)]; None = línea en blanco; 'ART' = bloque pixel-art."""
    body, y = [], TOP + 32
    for ln in lines:
        if ln == "ART":
            px, x = 9, PADX
            for ch in "ANDER.TSX":
                g = GLYPHS[ch]
                for r, row in enumerate(g):
                    for c, v in enumerate(row):
                        if v == "1":
                            body.append(f'<rect x="{x + c * px}" y="{y - 4 + r * px}" width="{px - 1}" height="{px - 1}" fill="{BOLD}"/>')
                x += len(g[0]) * px + 9
            y += 7 * 9 + 14
            continue
        if ln:
            spans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in ln)
            body.append(f'<text x="{PADX}" y="{y}" xml:space="preserve">{spans}</text>')
        y += LH
    h = y + 12
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{escape(title)}">
<style>text{{font-family:{MONO};font-size:{FS}px}}</style>
<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>
<path d="M.5 {TOP}V10.5a10 10 0 0 1 10-10h{W - 21}a10 10 0 0 1 10 10V{TOP}z" fill="{BAR}"/>
<path d="M0 {TOP}H{W}" stroke="{BORDER}"/>
<circle cx="24" cy="24" r="6" fill="#3a3a3a"/><circle cx="46" cy="24" r="6" fill="#3a3a3a"/><circle cx="68" cy="24" r="6" fill="#3a3a3a"/>
<text x="{W // 2}" y="29" text-anchor="middle" fill="{DIM}" style="font-size:13px">{escape(title)}</text>
{"".join(body)}
</svg>'''
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
    print("wrote", name)


def kv(k, v):
    return [(f"{k:<10}", DIM), (v, FG)]


window("term-banner", "ander — zsh — 96×24", [
    cmd("cat ander.txt"), None, "ART", None,
    [("Desarrollador Full-Stack", BOLD)],
    [("Construyo experiencias digitales de valor.", FG)],
    None, [(PROMPT, DIM)],
])
window("term-whoami", "ander — zsh — 96×24", [
    cmd("whoami"),
    [("ander", BOLD), (" — Full-Stack Developer · estudiante de ingeniería", FG)],
    None,
    kv("age", "20"), kv("school", "UTEZ · Ing. en Desarrollo de Software"),
    kv("focus", "UX/UI · MERN · web interactiva (Three.js)"),
    kv("langs", "es (nativo) · en (B2)"), kv("since", "nov 2021 · coding non-stop"),
    None, [(PROMPT, DIM)],
])
window("term-stack", "ander — zsh — 96×24", [
    cmd("cat stack.txt"),
    kv("frontend", "React · Next.js · TypeScript · JavaScript · Tailwind CSS · Three.js"),
    kv("backend", "Node.js · Express · Java"),
    kv("data", "MongoDB · MySQL"),
    kv("tools", "Git · GitHub · Postman · Figma · OAuth 2.0 · JWT"),
    None, [(PROMPT, DIM)],
])
window("term-edu", "ander — zsh — 96×24", [
    cmd("git log --oneline --education"),
    [("2025 ago → presente   ", DIM), ("Ing. en Desarrollo de Software", FG), (" ········ UTEZ", DIM)],
    [("2023 sep → 2025 ago   ", DIM), ("TSU en Tecnologías de la Información", FG), (" ·· UTEZ", DIM)],
    [("2023 feb → 2023 jun   ", DIM), ("Dip. en Automatización y Mecatrónica", FG), (" ·· UAEM", DIM)],
    None, cmd("ls certs/"),
    [("MongoDB-Nodejs-Developer-Path      ", FG), ("nov 2025", DIM)],
    [("Introduction-to-MongoDB            ", FG), ("feb 2025", DIM)],
    [("CCNA-Switching-Routing-Wireless    ", FG), ("may 2024", DIM)],
    [("CCNA-Introduction-to-Networks      ", FG), ("dic 2023", DIM)],
    [("IT-Essentials-Cisco                ", FG), ("dic 2023", DIM)],
    None, [(PROMPT, DIM)],
])
window("term-links", "ander — zsh — 96×24", [
    cmd("cat links.txt"),
    kv("web", "ander.icu"), kv("github", "github.com/Ander-tsx"),
    kv("linkedin", "linkedin.com/in/ander-tsx"), kv("x", "x.com/Ander_tsx"),
    kv("email", "andres.one.dev@gmail.com"),
    None, [(PROMPT, DIM)],
])
