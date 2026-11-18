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
LAB_CHECKS = (11, 11)  # verify.sh: passed, total

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
    "github": "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12",
    "linkedin": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
}
LINKS = [("website", "Website"), ("linkedin", "LinkedIn"), ("email", "Email"), ("github", "GitHub")]
DAILY = [  # label, three short lines (the old "What I do day to day" bullets, condensed)
    ("INVESTIGATE", ["Production clusters over SSH: logs,", "services, kernel messages, hardware", "health and networking"]),
    ("ROOT CAUSE", ["Findings from evidence, explained to", "customers, escalated with a timeline,", "verified facts kept apart from guesses"]),
    ("PLATFORM", ["KVM/libvirt VMs, OpenStack compute,", "networking and volumes, a distributed", "storage cluster and its alerting"]),
    ("DOCUMENT", ["Notes on recurring issues, tracked in", "ticketing systems and issue trackers"]),
]
LOOKING = ["Linux administration", "Infrastructure operations", "SRE / DevOps"]

PROJECT_ICONS = {  # simple-icons paths (CC0)
    "terraform": "M1.44 0v7.575l6.561 3.79V3.787zm21.12 4.227l-6.561 3.791v7.574l6.56-3.787zM8.72 4.23v7.575l6.561 3.787V8.018zm0 8.405v7.575L15.28 24v-7.578z",
    "kubernetes": "M10.204 14.35l.007.01-.999 2.413a5.171 5.171 0 0 1-2.075-2.597l2.578-.437.004.005a.44.44 0 0 1 .484.606zm-.833-2.129a.44.44 0 0 0 .173-.756l.002-.011L7.585 9.7a5.143 5.143 0 0 0-.73 3.255l2.514-.725.002-.009zm1.145-1.98a.44.44 0 0 0 .699-.337l.01-.005.15-2.62a5.144 5.144 0 0 0-3.01 1.442l2.147 1.523.004-.002zm.76 2.75l.723.349.722-.347.18-.78-.5-.623h-.804l-.5.623.179.779zm1.5-3.095a.44.44 0 0 0 .7.336l.008.003 2.134-1.513a5.188 5.188 0 0 0-2.992-1.442l.148 2.615.002.001zm10.876 5.97l-5.773 7.181a1.6 1.6 0 0 1-1.248.594l-9.261.003a1.6 1.6 0 0 1-1.247-.596l-5.776-7.18a1.583 1.583 0 0 1-.307-1.34L2.1 5.573c.108-.47.425-.864.863-1.073L11.305.513a1.606 1.606 0 0 1 1.385 0l8.345 3.985c.438.209.755.604.863 1.073l2.062 8.955c.108.47-.005.963-.308 1.34zm-3.289-2.057c-.042-.01-.103-.026-.145-.034-.174-.033-.315-.025-.479-.038-.35-.037-.638-.067-.895-.148-.105-.04-.18-.165-.216-.216l-.201-.059a6.45 6.45 0 0 0-.105-2.332 6.465 6.465 0 0 0-.936-2.163c.052-.047.15-.133.177-.159.008-.09.001-.183.094-.282.197-.185.444-.338.743-.522.142-.084.273-.137.415-.242.032-.024.076-.062.11-.089.24-.191.295-.52.123-.736-.172-.216-.506-.236-.745-.045-.034.027-.08.062-.111.088-.134.116-.217.23-.33.35-.246.25-.45.458-.673.609-.097.056-.239.037-.303.033l-.19.135a6.545 6.545 0 0 0-4.146-2.003l-.012-.223c-.065-.062-.143-.115-.163-.25-.022-.268.015-.557.057-.905.023-.163.061-.298.068-.475.001-.04-.001-.099-.001-.142 0-.306-.224-.555-.5-.555-.275 0-.499.249-.499.555l.001.014c0 .041-.002.092 0 .128.006.177.044.312.067.475.042.348.078.637.056.906a.545.545 0 0 1-.162.258l-.012.211a6.424 6.424 0 0 0-4.166 2.003 8.373 8.373 0 0 1-.18-.128c-.09.012-.18.04-.297-.029-.223-.15-.427-.358-.673-.608-.113-.12-.195-.234-.329-.349-.03-.026-.077-.062-.111-.088a.594.594 0 0 0-.348-.132.481.481 0 0 0-.398.176c-.172.216-.117.546.123.737l.007.005.104.083c.142.105.272.159.414.242.299.185.546.338.743.522.076.082.09.226.1.288l.16.143a6.462 6.462 0 0 0-1.02 4.506l-.208.06c-.055.072-.133.184-.215.217-.257.081-.546.11-.895.147-.164.014-.305.006-.48.039-.037.007-.09.02-.133.03l-.004.002-.007.002c-.295.071-.484.342-.423.608.061.267.349.429.645.365l.007-.001.01-.003.129-.029c.17-.046.294-.113.448-.172.33-.118.604-.217.87-.256.112-.009.23.069.288.101l.217-.037a6.5 6.5 0 0 0 2.88 3.596l-.09.218c.033.084.069.199.044.282-.097.252-.263.517-.452.813-.091.136-.185.242-.268.399-.02.037-.045.095-.064.134-.128.275-.034.591.213.71.248.12.556-.007.69-.282v-.002c.02-.039.046-.09.062-.127.07-.162.094-.301.144-.458.132-.332.205-.68.387-.897.05-.06.13-.082.215-.105l.113-.205a6.453 6.453 0 0 0 4.609.012l.106.192c.086.028.18.042.256.155.136.232.229.507.342.84.05.156.074.295.145.457.016.037.043.09.062.129.133.276.442.402.69.282.247-.118.341-.435.213-.71-.02-.039-.045-.096-.065-.134-.083-.156-.177-.261-.268-.398-.19-.296-.346-.541-.443-.793-.04-.13.007-.21.038-.294-.018-.022-.059-.144-.083-.202a6.499 6.499 0 0 0 2.88-3.622c.064.01.176.03.213.038.075-.05.144-.114.28-.104.266.039.54.138.87.256.154.06.277.128.448.173.036.01.088.019.13.028l.009.003.007.001c.297.064.584-.098.645-.365.06-.266-.128-.537-.423-.608zM16.4 9.701l-1.95 1.746v.005a.44.44 0 0 0 .173.757l.003.01 2.526.728a5.199 5.199 0 0 0-.108-1.674A5.208 5.208 0 0 0 16.4 9.7zm-4.013 5.325a.437.437 0 0 0-.404-.232.44.44 0 0 0-.372.233h-.002l-1.268 2.292a5.164 5.164 0 0 0 3.326.003l-1.27-2.296h-.01zm1.888-1.293a.44.44 0 0 0-.27.036.44.44 0 0 0-.214.572l-.003.004 1.01 2.438a5.15 5.15 0 0 0 2.081-2.615l-2.6-.44-.004.005z",
    "ansible": "M10.617 11.473l4.686 3.695-3.102-7.662zM12 0C5.371 0 0 5.371 0 12s5.371 12 12 12 12-5.371 12-12S18.629 0 12 0zm5.797 17.305c-.011.471-.403.842-.875.83-.236 0-.416-.09-.664-.293l-6.19-5-2.079 5.203H6.191L11.438 5.44c.124-.314.427-.52.764-.506.326-.014.63.189.742.506l4.774 11.494c.045.111.08.234.08.348-.001.009-.001.009-.001.023z",
    "docker": "M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.118a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m0 2.716h2.118a.187.187 0 00.186-.186V6.29a.186.186 0 00-.186-.185h-2.118a.185.185 0 00-.185.185v1.887c0 .102.082.185.185.186m-2.93 0h2.12a.186.186 0 00.184-.186V6.29a.185.185 0 00-.185-.185H8.1a.185.185 0 00-.185.185v1.887c0 .102.083.185.185.186m-2.964 0h2.119a.186.186 0 00.185-.186V6.29a.185.185 0 00-.185-.185H5.136a.186.186 0 00-.186.185v1.887c0 .102.084.185.186.186m5.893 2.715h2.118a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.118a.185.185 0 00-.185.185v1.888c0 .102.082.185.185.185m-2.93 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.185.185 0 00.185-.185V9.006a.185.185 0 00-.184-.186h-2.12a.186.186 0 00-.186.186v1.887c0 .102.084.185.186.185m-2.92 0h2.12a.185.185 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.082.185.185.185M23.763 9.89c-.065-.051-.672-.51-1.954-.51-.338.001-.676.03-1.01.087-.248-1.7-1.653-2.53-1.716-2.566l-.344-.199-.226.327c-.284.438-.49.922-.612 1.43-.23.97-.09 1.882.403 2.661-.595.332-1.55.413-1.744.42H.751a.751.751 0 00-.75.748 11.376 11.376 0 00.692 4.062c.545 1.428 1.355 2.48 2.41 3.124 1.18.723 3.1 1.137 5.275 1.137.983.003 1.963-.086 2.93-.266a12.248 12.248 0 003.823-1.389c.98-.567 1.86-1.288 2.61-2.136 1.252-1.418 1.998-2.997 2.553-4.4h.221c1.372 0 2.215-.549 2.68-1.009.309-.293.55-.65.707-1.046l.098-.288Z",
    "github": "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12",
}
PROJECTS = [  # key, repo url, icon, brand colour, title, summary, tech chips, metrics (value, label), full text for alt
    ("terraform", "https://github.com/Nitaru/AWS-Terraform-Hands-On", "terraform", "#7B42BC", "AWS Terraform Hands-On",
     "VPC, bastion and Auto Scaling web tier on AWS",
     ["Terraform", "S3 state", "ALB", "Auto Scaling", "Checkov", "tflint"],
     [("37", "resources applied"), ("11/11", "live checks"), ("102 s", "self-heal")],
     "A VPC with public and private subnets, a bastion limited to one admin address and an Auto Scaling web tier behind an Application Load Balancer, written as Terraform modules with remote state in S3. Applied to a real account (37 resources), verified from outside (11 checks), tested by killing an instance (capacity back in 102 s, 5.2% of requests failed meanwhile), then destroyed. Checkov and tflint run in CI."),
    ("kubernetes", "https://github.com/Nitaru/Kubernetes-Hands-On", "kubernetes", "#326CE5", "Kubernetes Hands-On",
     "Production-style platform on a 3-node kind cluster",
     ["Helm", "Traefik", "HPA", "Calico", "Redis StatefulSet", "NetworkPolicies"],
     [("3", "nodes"), ("5", "demos"), ("1", "build script")],
     "A production-style platform on a 3-node kind cluster, built with Helm: Traefik ingress, HPA autoscaling, zero-downtime rollouts, a PodDisruptionBudget, hardened pods, a Redis StatefulSet and default-deny NetworkPolicies enforced by Calico. Built from scratch by one script, with demos for rollouts, self-healing, autoscaling, network isolation and node drain, plus smoke tests and CI."),
    ("linux", "https://github.com/Nitaru/Linux-Hands-On", "ansible", "#EE0000", "Linux Hands-On",
     "Hardened two-VM environment, configured with Ansible",
     ["Ansible", "Key-only SSH", "UFW", "fail2ban", "WireGuard", "bastion"],
     [("2", "VMs"), ("42", "point check"), ("2", "attack demos")],
     "A hardened two-VM Linux environment configured entirely with Ansible. Key-only SSH, UFW, fail2ban, a bastion host with ProxyJump, a WireGuard VPN with NAT, and a SHA-256 file integrity checker on a systemd timer. Comes with a 42-point verification script and scripted attack demos (SSH brute force, log tampering)."),
    ("devops", "https://github.com/Nitaru/Nitaru_DevOps_Shenanigans", "docker", "#2496ED", "DevOps Hands-On",
     "Four projects, each runs locally with Docker Compose",
     ["Consul", "blue-green", "CI/CD", "Prometheus", "Grafana", "Loki"],
     [("4", "projects"), ("5", "services"), ("3", "monitoring tools")],
     "Four projects that each run locally with Docker Compose: Consul service discovery, a 5-service Docker app, zero-downtime blue-green deployments with CI/CD, and a Prometheus + Grafana + Loki monitoring stack with custom exporters and alerting."),
    ("portfolio", "https://nitaru.github.io", "github", "#6e7681", "Portfolio site",
     "The same projects, with write-ups",
     [], [],
     "My portfolio site, with the same projects and write-ups."),
]

HEADINGS = [("intro", "Hi, I'm Nika \U0001F9E2"), ("daily", "What I do day to day"), ("skills", "Skills"),
            ("projects", "Featured labs & projects"), ("numbers", "By the numbers"),
            ("studying", "Studying"), ("looking", "Looking for")]

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
        if r["isFork"] or r["name"] == OWNER:  # forks and the profile repo itself (it only holds this README's assets)
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
    W, H = 880, 156
    chips, x = [], 28
    for label in LOOKING:
        w = round(len(label) * 10.2 + 40)
        chips.append(f'<rect x="{x}" y="28" width="{w}" height="42" rx="12" fill="{c["accent"]}" fill-opacity="0.14" stroke="{c["accent"]}" stroke-width="1.5"/>'
                     f'<text x="{x + w / 2}" y="55" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{c["text"]}">{label}</text>')
        x += w + 14
    y0 = 134  # faint trace along the bottom, same motif as the header
    d = f"M0 {y0}"
    for b in (120, 360, 600, 840):
        d += f" L{b - 40} {y0} L{b - 30} {y0 - 8} L{b - 20} {y0} L{b - 6} {y0} L{b - 2} {y0 + 6} L{b + 4} {y0 - 16} L{b + 10} {y0 + 8} L{b + 14} {y0} L{b + 40} {y0}"
    d += f" L{W} {y0}"
    body = (f'  <style>.p{{stroke-dasharray:180 2400;animation:s 6s linear infinite}}@keyframes s{{from{{stroke-dashoffset:180}}to{{stroke-dashoffset:-2400}}}}'
            f'@media (prefers-reduced-motion:reduce){{.p{{animation:none}}}}</style>\n'
            f'  {"".join(chips)}\n'
            f'  <text x="28" y="100" font-family="{FONT}" font-size="14" fill="{c["dim"]}">Roles where I can keep growing by doing.</text>\n'
            f'  <path d="{d}" fill="none" stroke="{c["track"]}" stroke-width="1.5" stroke-linejoin="round" opacity="0.8"/>\n'
            f'  <path class="p" d="{d}" fill="none" stroke="{c["accent"]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>\n')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="Looking for: {", ".join(LOOKING)}. Roles where I can keep growing by doing.">\n'
            f'  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'{body}</svg>\n')



def link_button(key, title, t):
    c = THEMES[t]
    W, H = 176, 56
    if key == "website":  # globe
        icon = (f'<g fill="none" stroke="{c["accent"]}" stroke-width="1.9" stroke-linecap="round" transform="translate(16 16)">'
                f'<circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="4.2" ry="10"/><path d="M2 12h20"/></g>')
    else:
        icon = f'<g transform="translate(16 16)" fill="{c["accent"]}"><path d="{ICONS[key]}"/></g>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}">\n'
            f'  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'  <rect x="10" y="10" width="36" height="36" rx="10" fill="{c["accent"]}" fill-opacity="0.14"/>\n'
            f'  {icon}\n'
            f'  <text x="58" y="34" font-family="{FONT}" font-size="16" font-weight="700" fill="{c["text"]}">{title}</text>\n</svg>\n')


def daily_card(t):
    c = THEMES[t]
    W, cw, ch, top = 880, 440, 124, 14
    H = top * 2 + ch * 2 - 12
    parts = []
    for i, (label, lines) in enumerate(DAILY):
        cx, cy = 28 + (i % 2) * cw, top + (i // 2) * ch
        parts.append(f'<circle cx="{cx + 4}" cy="{cy + 20}" r="4" fill="{c["accent"]}"/>'
                     f'<text x="{cx + 18}" y="{cy + 25}" font-family="{FONT}" font-size="11.5" letter-spacing="2" fill="{c["label"]}">{label}</text>')
        for j, ln in enumerate(lines):
            parts.append(f'<text x="{cx}" y="{cy + 54 + j * 21}" font-family="{FONT}" font-size="14" fill="{c["text"]}">{ln}</text>')
    mid = top + ch - 8
    alt = " ".join(f"{l.title()}: {' '.join(ls)}." for l, ls in DAILY)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{alt}">\n'
            f'  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'  <line x1="{cw - 12}" y1="22" x2="{cw - 12}" y2="{H - 22}" stroke="{c["border"]}" stroke-width="1" opacity="0.7"/>\n'
            f'  <line x1="28" y1="{mid}" x2="{W - 28}" y2="{mid}" stroke="{c["border"]}" stroke-width="1" opacity="0.7"/>\n'
            f'  {"".join(parts)}\n</svg>\n')


def project_card(pr, t):
    key, url, icon, brand, title, summary, chips, metrics, full = pr
    c = THEMES[t]
    if t == "dark":  # a lighter tint of the brand colour so numbers and icons read on a dark page
        brand = {"#7B42BC": "#A97BE8", "#326CE5": "#5B90F0", "#EE0000": "#FF5A5A", "#2496ED": "#4DB0F5"}.get(brand, brand)
    W = 880
    H = 172 if chips else 96
    parts = [f'<rect x="28" y="24" width="52" height="52" rx="14" fill="{brand}" fill-opacity="0.16"/>'
             f'<g transform="translate(42 38) scale(1)" fill="{brand}"><path d="{PROJECT_ICONS[icon]}"/></g>'
             f'<text x="98" y="48" font-family="{FONT}" font-size="20" font-weight="700" fill="{c["text"]}">{title}</text>'
             f'<text x="98" y="70" font-family="{FONT}" font-size="14" fill="{c["dim"]}">{summary}</text>']
    colw = 108
    for i, (val, label) in enumerate(metrics):
        mx = W - 28 - (len(metrics) - i) * colw + colw / 2
        parts.append(f'<text x="{mx}" y="52" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="{brand}">{val}</text>'
                     f'<text x="{mx}" y="72" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{c["dim"]}">{label}</text>')
    x = 28
    for chip in chips:
        w = round(len(chip) * 6.8 + 24)
        parts.append(f'<rect x="{x}" y="112" width="{w}" height="28" rx="9" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>'
                     f'<text x="{x + w / 2}" y="130.5" text-anchor="middle" font-family="{FONT}" font-size="12.5" fill="{c["text"]}">{chip}</text>')
        x += w + 8
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}. {full}">\n'
            f'  <rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="14" fill="none" stroke="{c["border"]}" stroke-width="1.5"/>\n'
            f'  <rect x="0.75" y="26" width="3.5" height="{H - 52}" rx="1.75" fill="{brand}"/>\n'
            f'  {"".join(parts)}\n</svg>\n')


def heading(text, t):
    c = THEMES[t]
    W, H, cy = 880, 48, 24
    tw = len(text) * 12.4                       # rough width of the title
    gap = 22
    lx, rx = 440 - tw / 2 - gap, 440 + tw / 2 + gap
    blip = [(0, 0), (10, 0), (16, -7), (22, 0), (28, 0), (31, 8), (35, -15), (39, 6), (42, 0)]  # heartbeat, drawn outwards
    left = f"M{lx:.1f} {cy} " + " ".join(f"L{lx - px:.1f} {cy + py}" for px, py in blip[1:]) + f" L28 {cy}"
    right = f"M{rx:.1f} {cy} " + " ".join(f"L{rx + px:.1f} {cy + py}" for px, py in blip[1:]) + f" L852 {cy}"
    esc = text.replace("&", "&amp;")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc}">\n'
            f'  <path d="{left}" fill="none" stroke="{c["border"]}" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>\n'
            f'  <path d="{right}" fill="none" stroke="{c["border"]}" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round"/>\n'
            f'  <text x="440" y="{cy + 8}" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="700" fill="{c["text"]}">{esc}</text>\n</svg>\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    shares = language_shares()
    for t in THEMES:
        open(os.path.join(OUT, f"languages-{t}.svg"), "w").write(languages_card(t, shares))
        open(os.path.join(OUT, f"lab-{t}.svg"), "w").write(lab_card(t))
        open(os.path.join(OUT, f"skills-{t}.svg"), "w").write(skills_card(t))
        open(os.path.join(OUT, f"looking-{t}.svg"), "w").write(looking_card(t))
        for key, title in LINKS:
            open(os.path.join(OUT, f"link-{key}-{t}.svg"), "w").write(link_button(key, title, t))
        open(os.path.join(OUT, f"daily-{t}.svg"), "w").write(daily_card(t))
        for slug, text in HEADINGS:
            open(os.path.join(OUT, f"heading-{slug}-{t}.svg"), "w").write(heading(text, t))
        for pr in PROJECTS:
            open(os.path.join(OUT, f"project-{pr[0]}-{t}.svg"), "w").write(project_card(pr, t))
    for n, p in shares:
        print(f"{n:12s} {p:5.1f}%")


if __name__ == "__main__":
    sys.exit(main())
