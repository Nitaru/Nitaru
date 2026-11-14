# Hi, I'm Nika 👋

Support engineer (L2) at **Virtuozzo** in Tbilisi, and a Computer Science student at Ilia State University (graduating 2027).
Since March 2026 I investigate incidents on production cloud and storage clusters built on Linux, KVM and OpenStack, and I'm building my path toward **Linux administration, infrastructure operations and SRE/DevOps-style work**.

---

## 🧭 What I do day to day
- Investigate problems on production clusters over SSH: logs, services, kernel messages, hardware health and networking
- Find root causes from evidence, explain them clearly to customers, and escalate to developers with a timeline and a clear split between what is verified and what is not
- Work with KVM/libvirt VMs, OpenStack services (compute, networking, volumes), a distributed storage cluster and the platform's alerting
- Write documentation and notes on recurring issues, and track work in ticketing systems and issue trackers

---

## 🛠️ Skills (practical, from about 9 months of production support)

**Linux & troubleshooting**
- journalctl, dmesg, systemd, packages and updates, time sync
- Memory and NUMA pressure, OOM-killer reports, swap behavior
- Disk and NVMe health (SMART, kernel I/O errors), BMC/IPMI event logs

**Virtualization & cloud**
- KVM/QEMU/libvirt, live migration, HA and node maintenance
- OpenStack: Nova, Neutron with Open vSwitch, Cinder
- Platform CLI and REST-based tooling

**Storage & networking**
- Distributed storage basics: disks, chunk services, cluster health
- VLANs, bonds, MTU, DHCP/DNS basics, Open vSwitch ports and bridges
- Still strengthening networking (CCNA track)

**Automation & infrastructure as code**
- Bash: loops that run the same read-only checks on many nodes, log filtering with grep, awk and sed
- Terraform (my lab), Git
- Learning Ansible

**Monitoring & scripting**
- Daily work with platform alerts and telemetry
- Prometheus, Grafana and Loki: built full monitoring stacks with custom exporters and alerting (see projects)
- Python basics, JavaScript/Node basics, Docker basics

---

## 🧪 Lab & projects
- **[Kubernetes Hands-On](https://github.com/Nitaru/Kubernetes-Hands-On)**: a production-style platform on a 3-node kind cluster, built with Helm: Traefik ingress, HPA autoscaling, zero-downtime rollouts, a PodDisruptionBudget, hardened pods, a Redis StatefulSet and default-deny NetworkPolicies enforced by Calico. Built from scratch by one script, with demos for rollouts, self-healing, autoscaling, network isolation and node drain, plus smoke tests and CI.
- **[Linux Hands-On](https://github.com/Nitaru/Linux-Hands-On)**: a hardened two-VM Linux environment configured entirely with Ansible. Key-only SSH, UFW, fail2ban, a bastion host with ProxyJump, a WireGuard VPN with NAT, and a SHA-256 file integrity checker on a systemd timer. Comes with a 42-point verification script and scripted attack demos (SSH brute force, log tampering).
- **[DevOps Hands-On](https://github.com/Nitaru/Nitaru_DevOps_Shenanigans)**: four projects that each run locally with Docker Compose: Consul service discovery, a 5-service Docker app, zero-downtime blue-green deployments with CI/CD, and a Prometheus + Grafana + Loki monitoring stack with custom exporters and alerting.

---

## 📚 Learning now
RHCSA · CCNA · Ansible · Prometheus/Grafana/Loki · Python for automation · Kubernetes basics

---

## 🧩 How I work
- Evidence first, and read-only checks before any change
- Separate verified facts from guesses
- Write it down, so the next person doesn't have to rediscover it
- Use AI assistants to speed up analysis, and always verify against the documentation and a lab

---

## 🎯 Looking for
Linux administration, infrastructure operations and SRE/DevOps-oriented roles, where I can keep growing by doing.

---

## 📫 Contact
- 🌐 https://nitaru.github.io
- 📧 nikoloztolordava10@gmail.com
- 💼 https://www.linkedin.com/in/nika-tolordava-2b82a6231
