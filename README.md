# Keith

Branch: main (default)
Auth: github.com (umrmycelium-crypto)

## Verified hardware inventory (local, read-only)

- OS: Microsoft Windows 11 Pro, build 22631
- Computer: DJTRIPKIE
- Motherboard: HP 82C1, BIOS American Megatrends Inc. F.10
- CPU: Intel Core i7-7500U, 2 cores / 4 logical, 2.70 GHz
- RAM: 32 GB (2x16 GB), speed 2400 MHz, configured at 2133 MHz
- GPU: Intel HD Graphics 620, NVIDIA GeForce 940MX
- Disk: Samsung MZVLW512HMJP-000H1 (NVMe), Healthy, C: 74.6% free
- Volume D: NTFS, 11.3 GB total, 1.4 GB free (12.4%) - needs attention
- Network: Wi-Fi (Intel Dual Band Wireless-AC 8265) Up; Tailscale tunnel Up

## Docker environment state

- Docker CLI: installed and on PATH at C:\Program Files\Docker\Docker\resources\bin
- Docker contexts:
  - default: npipe://./pipe/docker_engine
  - desktop-linux: npipe://./pipe/dockerDesktopLinuxEngine
- Docker Desktop service: com.docker.service = Stopped (manual start type)
- WSL2: no WSL distribution installed on this host
- Docker commands using the desktop-linux context fail with:
  "failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine"
- Docker Desktop must be started (or the service started manually) before any
  `docker ps`, `docker network ls`, `docker inspect`, or `docker compose` command can succeed.

## Recommended next step

Start Docker Desktop so the local container network for the Mycelium stack can be
inspected with `docker ps`, `docker network ls`, `docker inspect`, and `docker compose`.
Once it is running, we can map connected containers, exposed ports, and bridge network
details before making any changes.

## Battery

- Model: HP Spectre x360 Convertible 15-bl0XX (SKU Z4Z35UA#ABA)
- Charger capacity from battery report: 65,419 mWh / 65,419 mWh, cycle count blank
- Live battery telemetry reads 0% on AC with no usage history; health is
  inconclusive, so an OEM or replacement battery check is recommended.
- Search results picked up a compatible Li-Ion replacement (approx 11.5 V / 79 Whr,
  HP part families KB06XL / 902401-2C1 / 902499-855).

## Open items

- Battery diagnosis requires a reboot/OEM diagnostic test (user approval needed).
- Docker container network inspection needs Docker Desktop running.
- Local battery replacement search near the user needs location input.
