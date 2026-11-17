<a href="https://nitaru.github.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/header/header-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/header/header-light.svg">
    <img alt="Nika Tolordava. Linux, infrastructure and SRE." src="./assets/header/header-dark.svg" width="100%">
  </picture>
</a>

<p align="center">
  <sub>↑ The pulse never stops. Neither should the service.</sub>
</p>

<p align="center">
  <!-- Keep tags adjacent so link whitespace does not appear underlined. -->
  <a href="https://nitaru.github.io"><picture><source media="(prefers-color-scheme: dark)"
    srcset="./assets/social/website-dark.svg"><source media="(prefers-color-scheme: light)"
    srcset="./assets/social/website-light.svg"><img src="./assets/social/website-dark.svg"
    alt="Website" width="104" height="44"></picture></a>
  <a href="https://www.linkedin.com/in/nika-tolordava-2b82a6231"><picture><source media="(prefers-color-scheme: dark)"
    srcset="./assets/social/linkedin-dark.svg"><source media="(prefers-color-scheme: light)"
    srcset="./assets/social/linkedin-light.svg"><img src="./assets/social/linkedin-dark.svg"
    alt="LinkedIn" width="112" height="44"></picture></a>
  <a href="mailto:nikoloztolordava10@gmail.com"><picture><source media="(prefers-color-scheme: dark)"
    srcset="./assets/social/email-dark.svg"><source media="(prefers-color-scheme: light)"
    srcset="./assets/social/email-light.svg"><img src="./assets/social/email-dark.svg"
    alt="Email" width="87" height="44"></picture></a>
  <a href="https://github.com/Nitaru?tab=repositories"><picture><source media="(prefers-color-scheme: dark)"
    srcset="./assets/social/github-dark.svg"><source media="(prefers-color-scheme: light)"
    srcset="./assets/social/github-light.svg"><img src="./assets/social/github-dark.svg"
    alt="GitHub" width="95" height="44"></picture></a>
</p>

<br>

<p align="center">
  <a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2FNitaru">
    <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FNitaru&label=visitors&labelColor=%232d3440&countColor=%2380a0c0&style=flat-square" alt="visitors">
  </a>
</p>

## Hi, I'm Nika 👋

Support engineer (L2) at **Virtuozzo** in Tbilisi, and a Computer Science student at Ilia State University (graduating 2027).
Since March 2026 I investigate incidents on production cloud and storage clusters built on Linux, KVM and OpenStack, and I'm building my path toward **Linux administration, infrastructure operations and SRE/DevOps-style work**.

---

## 🛠️ What I do day to day

- Investigate problems on production clusters over SSH: logs, services, kernel messages, hardware health and networking
- Find root causes from evidence, explain them clearly to customers, and escalate to developers with a timeline and a clear split between what is verified and what is not
- Work with KVM/libvirt VMs, OpenStack services (compute, networking, volumes), a distributed storage cluster and the platform's alerting
- Write documentation and notes on recurring issues, and track work in ticketing systems and issue trackers

---

## 🧰 Skills

<sub>Practical, from about 9 months of production support.</sub>

<details>
  <summary><strong>Linux &amp; troubleshooting</strong></summary>
  <br>

- journalctl, dmesg, systemd, packages and updates, time sync
- Memory and NUMA pressure, OOM-killer reports, swap behavior
- Disk and NVMe health (SMART, kernel I/O errors), BMC/IPMI event logs

</details>

<details>
  <summary><strong>Virtualization &amp; cloud</strong></summary>
  <br>

- KVM/QEMU/libvirt, live migration, HA and node maintenance
- OpenStack: Nova, Neutron with Open vSwitch, Cinder
- Platform CLI and REST-based tooling

</details>

<details>
  <summary><strong>Storage &amp; networking</strong></summary>
  <br>

- Distributed storage basics: disks, chunk services, cluster health
- VLANs, bonds, MTU, DHCP/DNS basics, Open vSwitch ports and bridges
- Still strengthening networking (CCNA track)

</details>

<details>
  <summary><strong>Automation &amp; infrastructure as code</strong></summary>
  <br>

- Bash: loops that run the same read-only checks on many nodes, log filtering with grep, awk and sed
- Terraform: modules, remote state and a policy-checked stack on AWS (see projects)
- Ansible: a two-VM hardened environment configured entirely by roles (see projects), Git

</details>

<details>
  <summary><strong>Monitoring &amp; scripting</strong></summary>
  <br>

- Daily work with platform alerts and telemetry
- Prometheus, Grafana and Loki: built full monitoring stacks with custom exporters and alerting (see projects)
- Python basics, JavaScript/Node basics, Docker basics

</details>

---

## 🧪 Lab & projects

Each one runs, is tested, and says what it does not cover.

- **[AWS Terraform Hands-On](https://github.com/Nitaru/AWS-Terraform-Hands-On)**: a VPC with public and private subnets, a bastion limited to one admin address and an Auto Scaling web tier behind an Application Load Balancer, written as Terraform modules with remote state in S3. Applied to a real account (37 resources), verified from outside (9 checks), tested by killing an instance (capacity back in 102 s, 5.2% of requests failed meanwhile), then destroyed. Checkov and tflint run in CI.
- **[Kubernetes Hands-On](https://github.com/Nitaru/Kubernetes-Hands-On)**: a production-style platform on a 3-node kind cluster, built with Helm: Traefik ingress, HPA autoscaling, zero-downtime rollouts, a PodDisruptionBudget, hardened pods, a Redis StatefulSet and default-deny NetworkPolicies enforced by Calico. Built from scratch by one script, with demos for rollouts, self-healing, autoscaling, network isolation and node drain, plus smoke tests and CI.
- **[Linux Hands-On](https://github.com/Nitaru/Linux-Hands-On)**: a hardened two-VM Linux environment configured entirely with Ansible. Key-only SSH, UFW, fail2ban, a bastion host with ProxyJump, a WireGuard VPN with NAT, and a SHA-256 file integrity checker on a systemd timer. Comes with a 42-point verification script and scripted attack demos (SSH brute force, log tampering).
- **[DevOps Hands-On](https://github.com/Nitaru/Nitaru_DevOps_Shenanigans)**: four projects that each run locally with Docker Compose: Consul service discovery, a 5-service Docker app, zero-downtime blue-green deployments with CI/CD, and a Prometheus + Grafana + Loki monitoring stack with custom exporters and alerting.

---

## 📚 Learning now

<p align="center">
  <strong>RHCSA</strong> · <strong>CCNA</strong> · <strong>Python for automation</strong>
</p>

---

## 🧭 How I work

- Evidence first, and read-only checks before any change
- Separate verified facts from guesses
- Write it down, so the next person doesn't have to rediscover it
- Use AI assistants to speed up analysis, and always verify against the documentation and a lab

---

## 🎯 Looking for

Linux administration, infrastructure operations and SRE/DevOps-oriented roles, where I can keep growing by doing.

---

## 📬 Contact

<p align="center">
  <a href="https://nitaru.github.io">nitaru.github.io</a> ·
  <a href="mailto:nikoloztolordava10@gmail.com">nikoloztolordava10@gmail.com</a> ·
  <a href="https://www.linkedin.com/in/nika-tolordava-2b82a6231">LinkedIn</a>
</p>
