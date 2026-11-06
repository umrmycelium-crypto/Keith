# Cross-Node Architecture Reference

> Status: draft based on the canonical host map and vault notes (2026‑10‑04).
> Only convey verified information; mark anything still *pending* verification.

## Node inventory

| Node name        | Kind          | OS / hardware                              | Tailnet IP          | Notes |
|------------------|---------------|--------------------------------------------|---------------------|-------|
| `veinweave`      | Physical workstation | Windows 11, HP Envy TE01‑2xxx, i7‑11700 8c/16t | 100.102.238.109 | 11.7 GB RAM, 477 GB + 932 GB storage. Tailscale host. |
| `forged-intent`  | Physical server | Ubuntu 26.04.1, ASUS ROG STRIX Z790‑E, i9‑14900K 32c | 100.75.163.20 | 61 GB RAM, 1.8 TB (1.1 TB free). Main Docker host (working node). |
| `the-studio`     | Physical Mac mini (2023) M2 `Blizzard-M2` | macOS (user `mdgt`) & Asahi (user `mycelium`) | 100.105.50.88 (macOS) / 100.97.43.76 (asahi) | Two boots share the same hardware; only one reachable at a time. `the‑studio‑dev` is the Asahi name (retired as a node). |
| `the-archive`    | VM (HVM domU) | Debian 13, Xeon E5‑2620 v4 6c | 100.79.186.25 | 15 GB RAM, 139 GB disk, 23 GB free. |
| `the-gateway`    | VM | Debian 13, Xeon E5‑2620 v4 2c | 100.123.27.13 | 1 GB RAM, 18 GB disk. Smallest VM. |
| `renewal-core`   | Hypervisor (XCP‑ng 8.3.0) | Xeon E5‑2620 v4 16 threads, 63.9 GB RAM | 100.79.39.38 | Hosts `the-gateway` and `the-archive`. |
| `djtripkie`      | Local desktop (Windows 11) | — | 10.0.0.10 (LAN) / tailnet not used | Local development machine; no Docker/WSL2. |
| `galaxy-tab`     | Android tablet | — | — | Used as a mobile client; no dedicated tailnet node. |
| `spore-scribe`   | Agent / service | — | — | Software component; communication via The One. |
| `the-studio-dev` | Alias for the Asahi boot of `the-studio` | (retired) | — | Use `the-studio` + `os: asahi`. |

> **Note:** The above list reflects measured values from the vault notes (2026‑10‑04).  
> Any *pending* items are marked accordingly.

## Connectivity highlights

- **Tailscale** connects 14 nodes. The studio macOS is currently offline, Asahi online.
- **Cloudflare tunnel** (`mdgt.systems`, `vault.mdgt.systems`, `admin.mdgt.systems`) → 200, 4 HA connections.
- **Syncthing** pairs `veinweave` ↔ `forged-intent` (tcp‑client, ingesting).
- **DNS**: unbound on `the-archive`; forwarders Quad9 + Cloudflare; ACLs block non‑mesh traffic.
- All nodes are reachable over **SSH** via Tailscale; the main development host is `forged-intent` (100.75.163.20).

## Relationship to Mycelium dev‑stack

The Mycelium daemon (`mycelium-hub-core`) runs on `forged-intent`. Its development replica lives in a Docker stack (`mycelium-hub-dev`) also on `forged-intent`. The UI is served on port 8084 via Nginx, and the daemon API is on port 8001.

EOF
