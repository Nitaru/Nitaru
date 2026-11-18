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

## What I do day to day

- Investigate problems on production clusters over SSH: logs, services, kernel messages, hardware health and networking
- Find root causes from evidence, explain them clearly to customers, and escalate to developers with a timeline and a clear split between what is verified and what is not
- Work with KVM/libvirt VMs, OpenStack services (compute, networking, volumes), a distributed storage cluster and the platform's alerting
- Write documentation and notes on recurring issues, and track work in ticketing systems and issue trackers

---

## Skills

<p align="center">
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/skills-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/cards/skills-light.svg"><img src="./assets/cards/skills-dark.svg" width="100%" alt="Skills. Linux: journalctl, dmesg, systemd, OOM and memory pressure, NVMe and SMART, IPMI logs. Virtualization and cloud: KVM, QEMU/libvirt, live migration, HA, OpenStack, Open vSwitch. Storage and networking: distributed storage, VLANs, bonds, MTU, DHCP and DNS. Automation and IaC: Bash, Terraform, Ansible, Git. Monitoring and scripting: Prometheus, Grafana, Loki, Python, Node.js, Docker."></picture>
</p>

<p align="center">
  <sub>From about 9 months of production support. Python, Node.js and Docker at a basic level.</sub>
</p>

---

## Featured labs & projects

> **Each one runs, is tested, and says what it does not cover.**

<p>
<a href="https://github.com/Nitaru/AWS-Terraform-Hands-On"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/projects/terraform-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/projects/terraform-v2-light.svg"><img src="./assets/projects/terraform-v2-dark.svg" alt="AWS Terraform Hands-On" align="left" width="241" height="35"></picture></a>
A VPC with public and private subnets, a bastion limited to one admin address and an Auto Scaling web tier behind an Application Load Balancer, written as Terraform modules with remote state in S3. Applied to a real account (37 resources), verified from outside (9 checks), tested by killing an instance (capacity back in 102 s, 5.2% of requests failed meanwhile), then destroyed. Checkov and tflint run in CI.
<br clear="left">
</p>

---

<p>
<a href="https://github.com/Nitaru/Kubernetes-Hands-On"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/projects/kubernetes-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/projects/kubernetes-v2-light.svg"><img src="./assets/projects/kubernetes-v2-dark.svg" alt="Kubernetes Hands-On" align="left" width="217" height="35"></picture></a>
A production-style platform on a 3-node kind cluster, built with Helm: Traefik ingress, HPA autoscaling, zero-downtime rollouts, a PodDisruptionBudget, hardened pods, a Redis StatefulSet and default-deny NetworkPolicies enforced by Calico. Built from scratch by one script, with demos for rollouts, self-healing, autoscaling, network isolation and node drain, plus smoke tests and CI.
<br clear="left">
</p>

---

<p>
<a href="https://github.com/Nitaru/Linux-Hands-On"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/projects/linux-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/projects/linux-v2-light.svg"><img src="./assets/projects/linux-v2-dark.svg" alt="Linux Hands-On" align="left" width="176" height="35"></picture></a>
A hardened two-VM Linux environment configured entirely with Ansible. Key-only SSH, UFW, fail2ban, a bastion host with ProxyJump, a WireGuard VPN with NAT, and a SHA-256 file integrity checker on a systemd timer. Comes with a 42-point verification script and scripted attack demos (SSH brute force, log tampering).
<br clear="left">
</p>

---

<p>
<a href="https://github.com/Nitaru/Nitaru_DevOps_Shenanigans"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/projects/devops-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/projects/devops-v2-light.svg"><img src="./assets/projects/devops-v2-dark.svg" alt="DevOps Hands-On" align="left" width="185" height="35"></picture></a>
Four projects that each run locally with Docker Compose: Consul service discovery, a 5-service Docker app, zero-downtime blue-green deployments with CI/CD, and a Prometheus + Grafana + Loki monitoring stack with custom exporters and alerting.
<br clear="left">
</p>

---

<p>
<a href="https://nitaru.github.io"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/projects/portfolio-v2-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/projects/portfolio-v2-light.svg"><img src="./assets/projects/portfolio-v2-dark.svg" alt="Portfolio site" align="left" width="176" height="35"></picture></a>
My portfolio site, with the same projects and write-ups.
<br clear="left">
</p>

---

## By the numbers

<p align="center">
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/languages-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/cards/languages-light.svg"><img src="./assets/cards/languages-dark.svg" width="400" alt="Most used languages across public repos"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/lab-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/cards/lab-light.svg"><img src="./assets/cards/lab-dark.svg" width="400" alt="Lab results from the AWS Terraform Hands-On project"></picture>
</p>

<p align="center">
  <sub>Languages: bytes of code in my public repos, as GitHub detects them. Lab results: measured in <a href="https://github.com/Nitaru/AWS-Terraform-Hands-On">AWS Terraform Hands-On</a> on a real account, then destroyed.</sub>
</p>

---

## Studying

<!-- Keep tags adjacent so link whitespace does not appear underlined. -->
<a href="https://aws.amazon.com/certification/certified-solutions-architect-associate/"><picture><source media="(prefers-color-scheme: dark)"
  srcset="./assets/study/aws-dark.svg"><source media="(prefers-color-scheme: light)"
  srcset="./assets/study/aws-light.svg"><img src="./assets/study/aws-dark.svg"
  alt="AWS Solutions Architect" width="120" height="132"></picture></a>
<a href="https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam"><picture><source media="(prefers-color-scheme: dark)"
  srcset="./assets/study/redhat-dark.svg"><source media="(prefers-color-scheme: light)"
  srcset="./assets/study/redhat-light.svg"><img src="./assets/study/redhat-dark.svg"
  alt="RHCSA, Red Hat" width="120" height="132"></picture></a>
<a href="https://www.cisco.com/site/us/en/learn/training-certifications/certifications/enterprise/ccna/index.html"><picture><source media="(prefers-color-scheme: dark)"
  srcset="./assets/study/cisco-dark.svg"><source media="(prefers-color-scheme: light)"
  srcset="./assets/study/cisco-light.svg"><img src="./assets/study/cisco-dark.svg"
  alt="CCNA, Cisco" width="120" height="132"></picture></a>
<a href="https://www.python.org"><picture><source media="(prefers-color-scheme: dark)"
  srcset="./assets/study/python-dark.svg"><source media="(prefers-color-scheme: light)"
  srcset="./assets/study/python-light.svg"><img src="./assets/study/python-dark.svg"
  alt="Python for automation" width="120" height="132"></picture></a>

---

## Looking for

<p align="center">
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/looking-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/cards/looking-light.svg"><img src="./assets/cards/looking-dark.svg" width="100%" alt="Looking for: Linux administration, Infrastructure operations, SRE / DevOps. Roles where I can keep growing by doing."></picture>
</p>

---

## Contact

<p align="center">
  <a href="https://nitaru.github.io"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/contact-website-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/cards/contact-website-light.svg"><img src="./assets/cards/contact-website-dark.svg" width="270" height="84" alt="Website: nitaru.github.io"></picture></a>
  <a href="mailto:nikoloztolordava10@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/contact-email-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/cards/contact-email-light.svg"><img src="./assets/cards/contact-email-dark.svg" width="270" height="84" alt="Email: nikoloztolordava10@gmail.com"></picture></a>
  <a href="https://www.linkedin.com/in/nika-tolordava-2b82a6231"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/cards/contact-linkedin-dark.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/cards/contact-linkedin-light.svg"><img src="./assets/cards/contact-linkedin-dark.svg" width="270" height="84" alt="LinkedIn: in/nika-tolordava-2b82a6231"></picture></a>
</p>
