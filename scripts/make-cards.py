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

SKILLS = [  # group, chips (the old Skills section, condensed; Python, Node.js and Docker were "basics", said in the README caption)
    ("LINUX", ["journalctl", "dmesg", "systemd", "OOM / memory", "NVMe & SMART", "IPMI logs"]),
    ("VIRTUALIZATION & CLOUD", ["KVM", "QEMU/libvirt", "live migration", "HA", "OpenStack", "Open vSwitch"]),
    ("STORAGE & NETWORKING", ["distributed storage", "VLANs", "bonds", "MTU", "DHCP & DNS"]),
    ("AUTOMATION & IaC", ["Bash", "Terraform", "Ansible", "Git"]),
    ("MONITORING & SCRIPTING", ["Prometheus", "Grafana", "Loki", "Python", "Node.js", "Docker"]),
]

# simple-icons paths (CC0), 24x24 viewBox; the globe is drawn by hand below
ICONS = {
    "email": "M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z",
    "linkedin": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
}
CONTACTS = [  # key, title, subtitle
    ("website", "Website", "nitaru.github.io"),
    ("email", "Email", "nikoloztolordava10@gmail.com"),
    ("linkedin", "LinkedIn", "in/nika-tolordava-2b82a6231"),
]
LOOKING = ["Linux administration", "Infrastructure operations", "SRE / DevOps"]

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


def skills_card(t):
    c = THEMES[t]
    W, labx, chipx, right = 880, 28, 250, 852
    ch, gx, gy, pad = 28, 8, 8, 16
    parts, y = [], 8
    for gi, (group, chips) in enumerate(SKILLS):
        # flow the chips into lines
        lines, line, x = [], [], chipx
        for chip in chips:
            w = round(len(chip) * 6.9 + 22)
            if x + w > right and line:
                lines.append(line); line, x = [], chipx
            line.append((chip, x, w)); x += w + gx
        lines.append(line)
        top = y + pad
        parts.append(f'<text x="{labx}" y="{top + 19}" font-family="{FONT}" font-size="11.5" letter-spacing="1.8" fill="{c["label"]}">{group.replace("&", "&amp;")}</text>')
        for li, ln in enumerate(lines):
            cy = top + li * (ch + gy)
            for chip, x, w in ln:
                parts.append(f'<rect x="{x}" y="{cy}" width="{w}" height="{ch}" rx="9" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>'
                             f'<text x="{x + w / 2}" y="{cy + 18.5}" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{c["text"]}">{chip.replace("&", "&amp;")}</text>')
        y = top + len(lines) * (ch + gy) - gy + pad
        if gi < len(SKILLS) - 1:
            parts.append(f'<line x1="{labx}" y1="{y}" x2="{right}" y2="{y}" stroke="{c["border"]}" stroke-width="1" opacity="0.6"/>')
    H = y + 8
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="Skills: {"; ".join(g.title() + ": " + ", ".join(ch) for g, ch in SKILLS).replace("&", "and")}">\n'
            f'  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'  {"".join(parts)}\n</svg>\n')


def looking_card(t):
    c = THEMES[t]
    W, H = 880, 200
    chips, x = [], 28
    for label in LOOKING:
        w = round(len(label) * 10.2 + 40)
        chips.append(f'<rect x="{x}" y="74" width="{w}" height="42" rx="12" fill="{c["accent"]}" fill-opacity="0.14" stroke="{c["accent"]}" stroke-width="1.5"/>'
                     f'<text x="{x + w / 2}" y="101" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{c["text"]}">{label}</text>')
        x += w + 14
    y0 = 180  # faint trace along the bottom, same motif as the header
    d = f"M0 {y0}"
    for b in (120, 360, 600, 840):
        d += f" L{b - 40} {y0} L{b - 30} {y0 - 8} L{b - 20} {y0} L{b - 6} {y0} L{b - 2} {y0 + 6} L{b + 4} {y0 - 16} L{b + 10} {y0 + 8} L{b + 14} {y0} L{b + 40} {y0}"
    d += f" L{W} {y0}"
    body = (f'  <style>.p{{stroke-dasharray:180 2400;animation:s 6s linear infinite}}@keyframes s{{from{{stroke-dashoffset:180}}to{{stroke-dashoffset:-2400}}}}'
            f'@media (prefers-reduced-motion:reduce){{.p{{animation:none}}}}</style>\n'
            f'  <text x="28" y="40" font-family="{FONT}" font-size="11.5" letter-spacing="2" fill="{c["label"]}">LOOKING FOR</text>\n'
            f'  {"".join(chips)}\n'
            f'  <text x="28" y="146" font-family="{FONT}" font-size="14" fill="{c["dim"]}">Roles where I can keep growing by doing.</text>\n'
            f'  <path d="{d}" fill="none" stroke="{c["track"]}" stroke-width="1.5" stroke-linejoin="round" opacity="0.8"/>\n'
            f'  <path class="p" d="{d}" fill="none" stroke="{c["accent"]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>\n')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="Looking for: {", ".join(LOOKING)}. Roles where I can keep growing by doing.">\n'
            f'  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'{body}</svg>\n')


def contact_tile(key, title, sub, t):
    c = THEMES[t]
    W, H = 270, 84
    if key == "website":  # globe
        icon = (f'<g fill="none" stroke="{c["accent"]}" stroke-width="1.8" stroke-linecap="round" transform="translate(24 28) scale(1.17)">'
                f'<circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="4.2" ry="10"/><path d="M2 12h20"/></g>')
    else:
        icon = f'<g transform="translate(24 28) scale(1.17)" fill="{c["accent"]}"><path d="{ICONS[key]}"/></g>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}: {sub}">\n'
            f'  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'  <rect x="14" y="14" width="56" height="56" rx="14" fill="{c["accent"]}" fill-opacity="0.12"/>\n'
            f'  {icon}\n'
            f'  <text x="86" y="39" font-family="{FONT}" font-size="17" font-weight="700" fill="{c["text"]}">{title}</text>\n'
            f'  <text x="86" y="60" font-family="{FONT}" font-size="12" fill="{c["dim"]}">{sub}</text>\n</svg>\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    shares = language_shares()
    for t in THEMES:
        open(os.path.join(OUT, f"languages-{t}.svg"), "w").write(languages_card(t, shares))
        open(os.path.join(OUT, f"lab-{t}.svg"), "w").write(lab_card(t))
        open(os.path.join(OUT, f"skills-{t}.svg"), "w").write(skills_card(t))
        open(os.path.join(OUT, f"looking-{t}.svg"), "w").write(looking_card(t))
        for key, title, sub in CONTACTS:
            open(os.path.join(OUT, f"contact-{key}-{t}.svg"), "w").write(contact_tile(key, title, sub, t))
    for n, p in shares:
        print(f"{n:12s} {p:5.1f}%")


if __name__ == "__main__":
    sys.exit(main())
