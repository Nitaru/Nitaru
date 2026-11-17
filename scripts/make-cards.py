#!/usr/bin/env python3
"""Regenerate assets/cards/*.svg.

languages: bytes of code per language across the public, non-fork repos of the
profile owner, as GitHub detects them (needs `gh` logged in; reads public data only).
lab: the numbers below, copied by hand from the measured tables in the
AWS-Terraform-Hands-On README. They do not update on their own.
"""
import json, subprocess, sys, os

OWNER = "Nitaru"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "cards")

LAB_ROWS = [  # label, value
    ("Resources created", "37"),
    ("Self-heal recovery", "102 s"),
    ("Requests failed in test", "5.2%"),
    ("Destroy time", "1m42s"),
    ("Resources left after destroy", "0"),
]
LAB_CHECKS = (9, 9)  # verify.sh: passed, total

COLORS = {  # GitHub's language colours
    "Shell": "#89e051", "HCL": "#844FBA", "JavaScript": "#f1e05a", "Python": "#3572A5",
    "Makefile": "#427819", "Dockerfile": "#384d54", "Jinja": "#a52a22", "HTML": "#e34c26",
    "CSS": "#563d7c", "Go Template": "#00ADD8", "Other": "#6e7681",
}
THEMES = {
    "dark":  dict(border="#30363d", label="#8b98a9", text="#e6edf3", dim="#8b98a9", accent="#80a0c0", track="#30363d"),
    "light": dict(border="#d0d7de", label="#59636e", text="#1f2328", dim="#59636e", accent="#3b6ea5", track="#d0d7de"),
}
FONT = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def gh(*args):
    return json.loads(subprocess.check_output(["gh", *args], text=True))


def language_shares():
    repos = gh("repo", "list", OWNER, "--visibility", "public", "--no-archived",
               "--json", "name,isFork", "--limit", "100")
    totals = {}
    for r in repos:
        if r["isFork"]:
            continue
        for lang, b in gh("api", f"repos/{OWNER}/{r['name']}/languages").items():
            totals[lang] = totals.get(lang, 0) + b
    whole = sum(totals.values())
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    top, rest = ranked[:5], sum(b for _, b in ranked[5:])
    if rest:
        top.append(("Other", rest))
    return [(n, b / whole * 100) for n, b in top]


def frame(t, body):
    c = THEMES[t]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 219" width="450" height="219" role="img" '
            f'aria-label="{{label}}">\n'
            f'  <rect x="0.75" y="0.75" width="448.5" height="217.5" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'{body}</svg>\n')


def languages_card(t, shares):
    c = THEMES[t]
    x0, w, gap, y, h = 28, 394, 3, 58, 10
    usable = w - gap * (len(shares) - 1)
    segs, x = [], x0
    for name, pct in shares:
        sw = max(usable * pct / 100, 4)
        segs.append(f'<rect x="{x:.1f}" y="{y}" width="{sw:.1f}" height="{h}" fill="{COLORS.get(name, "#6e7681")}"/>')
        x += sw + gap
    legend = []
    for i, (name, pct) in enumerate(shares):
        cx = 28 + (i % 2) * 204
        cy = 108 + (i // 2) * 30
        legend.append(
            f'<circle cx="{cx + 5}" cy="{cy - 5}" r="5" fill="{COLORS.get(name, "#6e7681")}"/>'
            f'<text x="{cx + 18}" y="{cy}" font-family="{FONT}" font-size="15" fill="{c["text"]}">{name} '
            f'<tspan fill="{c["dim"]}">{pct:.1f}%</tspan></text>')
    body = (f'  <text x="28" y="34" font-family="{FONT}" font-size="11.5" letter-spacing="2" fill="{c["label"]}">MOST USED LANGUAGES</text>\n'
            f'  <clipPath id="bar"><rect x="{x0}" y="{y}" width="{w}" height="{h}" rx="5"/></clipPath>\n'
            f'  <g clip-path="url(#bar)">{"".join(segs)}</g>\n'
            f'  {"".join(legend)}\n'
            f'  <text x="28" y="204" font-family="{FONT}" font-size="10" fill="{c["dim"]}">public repos, bytes of code</text>\n')
    return frame(t, body).replace("{label}", "Most used languages across public repos")


def lab_card(t):
    c = THEMES[t]
    rows = []
    for i, (label, value) in enumerate(LAB_ROWS):
        y = 66 + i * 27
        rows.append(f'<text x="28" y="{y}" font-family="{FONT}" font-size="14" fill="{c["text"]}">{label}</text>'
                    f'<text x="262" y="{y}" text-anchor="end" font-family="{FONT}" font-size="15" font-weight="700" fill="{c["text"]}">{value}</text>')
    ok, total = LAB_CHECKS
    r, cx, cy = 42, 350, 120
    circ = 2 * 3.14159265 * r
    arc = circ * ok / total
    body = (f'  <text x="28" y="34" font-family="{FONT}" font-size="11.5" letter-spacing="2" fill="{c["label"]}">LAB RESULTS</text>\n'
            f'  <text x="350" y="34" text-anchor="middle" font-family="{FONT}" font-size="11.5" letter-spacing="2" fill="{c["label"]}">LIVE CHECKS</text>\n'
            f'  {"".join(rows)}\n'
            f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c["track"]}" stroke-width="8"/>\n'
            f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c["accent"]}" stroke-width="8" stroke-linecap="round" '
            f'stroke-dasharray="{arc:.1f} {circ:.1f}" transform="rotate(-90 {cx} {cy})"/>\n'
            f'  <text x="{cx}" y="{cy + 8}" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="{c["text"]}">{ok}/{total}</text>\n'
            f'  <text x="{cx}" y="{cy + 64}" text-anchor="middle" font-family="{FONT}" font-size="10" fill="{c["dim"]}">passed</text>\n'
            f'  <text x="28" y="204" font-family="{FONT}" font-size="10" fill="{c["dim"]}">AWS Terraform Hands-On, real account</text>\n')
    return frame(t, body).replace("{label}", "Lab results from the AWS Terraform Hands-On project")


def main():
    os.makedirs(OUT, exist_ok=True)
    shares = language_shares()
    for t in THEMES:
        open(os.path.join(OUT, f"languages-{t}.svg"), "w").write(languages_card(t, shares))
        open(os.path.join(OUT, f"lab-{t}.svg"), "w").write(lab_card(t))
    for n, p in shares:
        print(f"{n:12s} {p:5.1f}%")


if __name__ == "__main__":
    sys.exit(main())
