"""Genera las ventanas de terminal (SVG estáticos, monocromo) del README.
Uso: python3 scripts/build_assets.py"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

BG, BORDER, BAR = "#1b1d23", "#3a3d46", "#252830"
FG, DIM, BOLD = "#d4d4d4", "#7f848e", "#ffffff"
GREEN, BLUE, CYAN, YELLOW, MAGENTA, RED = "#6fc276", "#6ea8fe", "#5fc9d6", "#e5c07b", "#c678dd", "#e06c75"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
PROMPT = [("ander", GREEN), ("@", FG), ("MacBook-Air", GREEN), (" ", FG), ("~", BLUE), (" % ", FG)]
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
    return PROMPT + [(c, BOLD)]


def window(name, title, lines):
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
    h = y + 4
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{escape(title)}">
<style>text{{font-family:{MONO};font-size:{FS}px}}</style>
<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>
<path d="M.5 {TOP}V10.5a10 10 0 0 1 10-10h{W - 21}a10 10 0 0 1 10 10V{TOP}z" fill="{BAR}"/>
<path d="M0 {TOP}H{W}" stroke="{BORDER}"/>
<circle cx="24" cy="24" r="6" fill="#ff5f57"/><circle cx="46" cy="24" r="6" fill="#febc2e"/><circle cx="68" cy="24" r="6" fill="#28c840"/>
<text x="{W // 2}" y="29" text-anchor="middle" fill="{DIM}" style="font-size:13px">{escape(title)}</text>
{"".join(body)}
</svg>'''
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
    print("wrote", name)


def kv(k, v, kc=CYAN):
    return [(f"{k:<10}", kc), (v, FG)]


def row(a, b, c, d, w=36):
    return [(a, DIM), (b.ljust(w), FG), (c, DIM)]


window("terminal", "ander — zsh — 100×40", [
    cmd("cat ander.txt"), None, "ART", None,
    [("Desarrollador Full-Stack", YELLOW)],
    [("Construyo experiencias digitales de valor.", FG)],
    None,
    cmd("whoami"),
    [("ander", GREEN), (" — Full-Stack Developer · estudiante de ingeniería", FG)],
    kv("age", "20"), kv("school", "UTEZ · Ing. en Desarrollo de Software"),
    kv("focus", "UX/UI · MERN · web interactiva (Three.js)"),
    kv("langs", "es (nativo) · en (B2)"), kv("since", "nov 2021 · coding non-stop"),
    None,
    cmd("git log --oneline --education"),
    [("2025 ago → presente  ", YELLOW), ("Ing. en Desarrollo de Software".ljust(38), FG), ("UTEZ", BLUE)],
    [("2023 sep → 2025 ago  ", YELLOW), ("TSU en Tecnologías de la Información".ljust(38), FG), ("UTEZ", BLUE)],
    [("2023 feb → 2023 jun  ", YELLOW), ("Dip. en Automatización y Mecatrónica".ljust(38), FG), ("UAEM", BLUE)],
    None,
    cmd("ls certs/"),
    [("MongoDB-Nodejs-Developer-Path      ", BLUE), ("nov 2025", DIM)],
    [("Introduction-to-MongoDB            ", BLUE), ("feb 2025", DIM)],
    [("CCNA-Switching-Routing-Wireless    ", BLUE), ("may 2024", DIM)],
    [("CCNA-Introduction-to-Networks      ", BLUE), ("dic 2023", DIM)],
    [("IT-Essentials-Cisco                ", BLUE), ("dic 2023", DIM)],
    None, PROMPT + [("█", FG)],
])
