<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-lightgrey?style=flat-square" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Version-2.0.0-red?style=flat-square" alt="Version">
</p>

<h1 align="center">WP Brute v2.0</h1>
<p align="center"><b>Advanced WordPress Authentication Testing Suite</b></p>
<p align="center"><i>Multi-vector credential testing with stealth evasion, proxy rotation, and post-exploitation.</i></p>

---

## What it does

WP Brute is a purpose-built WordPress authentication testing tool designed for penetration testers and red teamers. It supports multiple attack vectors, intelligent evasion, and automated post-exploitation — all from a single script.

**Not another dumb brute forcer.** This tool was built to handle real-world hardened WordPress targets with rate limiting, WAF protection, CAPTCHA challenges, and custom login paths.

---

## Features

**Attack Vectors**
- `login` — Standard wp-login.php form-based attack
- `xmlrpc` — XML-RPC multicall batching (up to 500 passwords/request)
- `rest` — JWT REST API authentication endpoint
- `multi-vector` — Run all three simultaneously

**Intelligence**
- 7-method username enumeration (REST API, author archives, oEmbed, RSS, sitemap, login error analysis)
- Target-aware password generation from domain name, site title, and common patterns
- Smart password mutations — leet speak, year suffixes, keyboard walks, case variations
- 250+ built-in password list covering the most common WordPress credentials

**Stealth & Evasion**
- Three modes: `stealth`, `balanced`, `aggressive`
- 30+ rotating User-Agent strings (desktop, mobile, bot)
- Random `X-Forwarded-For`, `X-Real-IP`, `X-Client-IP` header spoofing
- Adaptive delay — backs off automatically when rate limiting is detected
- WAF detection with configurable cooldown

**Proxy Support**
- HTTP, SOCKS4, and SOCKS5 proxy support
- Health-based proxy rotation with automatic dead proxy removal
- TOR integration (auto-detects SOCKS5 on port 9050)
- Built-in proxy fetcher script

**Post-Exploitation**
- Validates discovered credentials
- Extracts WordPress version, active plugins, user roles
- Identifies admin-level access
- Full session cookie capture

**Other**
- Resume support — save and restore attack state
- CSV, HTML, and JSON result export
- Live browser dashboard with real-time stats
- Full target recon (30+ admin path discovery)

---

## Quick Start

```bash
# Clone
git clone https://github.com/V3n0mSh3ll/wp-brute.git
cd wp-brute

# Install dependencies
pip install requests colorama

# Interactive mode
python wp_brute.py

# CLI mode — basic
python wp_brute.py -u http://target.com -U admin -w wordlist.txt

# CLI mode — full stealth
python wp_brute.py -u http://target.com --enum-users --mutate --recon --post-exploit --mode stealth
```

---

## Usage Examples

**Username enumeration only:**
```bash
python wp_brute.py -u http://target.com --enum-users --enum-range 50
```

**XML-RPC batch attack (fast):**
```bash
python wp_brute.py -u http://target.com -U admin --vector xmlrpc --xmlrpc-batch 500 --mode aggressive
```

**Stealth attack with proxies and mutations:**
```bash
python wp_brute.py -u http://target.com --enum-users --mutate --mutation-depth 2 -p proxies.txt --spoof-headers --mode stealth
```

**Multi-vector with post-exploitation:**
```bash
python wp_brute.py -u http://target.com -U admin editor --multi-vector --post-exploit --recon
```

**Resume a previous attack:**
```bash
python wp_brute.py --resume --state-file attack_state.json
```

---

## Interactive Mode

Just run `python wp_brute.py` without arguments to get the interactive menu:

```
╔════════════════════════════════════════╗
║  WP BRUTE v2.0.0                       ║
╠════════════════════════════════════════╣
║  [1]  Quick Attack                     ║
║  [2]  Stealth Attack                   ║
║  [3]  Aggressive Attack                ║
║  [4]  XML-RPC Batch Attack             ║
║  [5]  Multi-Vector Attack              ║
║  [6]  Custom Attack                    ║
║  [7]  Username Enumeration Only        ║
║  [8]  Target Recon                     ║
║  [0]  Exit                             ║
╚════════════════════════════════════════╝
```

---

## CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `-u, --url` | Target WordPress URL | — |
| `-U, --usernames` | Space-separated usernames | — |
| `-F, --usernames-file` | File with usernames (one per line) | — |
| `-w, --wordlist` | Password wordlist | `rockyou.txt` |
| `-t, --threads` | Concurrent threads | `15` |
| `--vector` | Attack vector: `login`, `xmlrpc`, `rest` | `login` |
| `--mode` | `stealth`, `balanced`, `aggressive` | `stealth` |
| `--enum-users` | Auto-enumerate usernames | Off |
| `--mutate` | Enable password mutations | Off |
| `--mutation-depth` | `1`=light, `2`=medium, `3`=heavy | `1` |
| `--recon` | Full target recon before attack | Off |
| `--post-exploit` | Validate creds + extract info | Off |
| `--multi-vector` | Attack via all vectors in parallel | Off |
| `--spoof-headers` | Randomize forwarded headers | Off |
| `-p, --proxies` | Proxy list file | `proxies.txt` |
| `--proxy-type` | `auto`, `http`, `socks4`, `socks5` | `auto` |
| `--xmlrpc-batch` | Passwords per XML-RPC multicall | `500` |
| `--dashboard` | Start live stats dashboard | Off |
| `--resume` | Resume from saved state | Off |
| `--output-csv` | Export results as CSV | Off |
| `--output-html` | Export results as HTML report | Off |

---

## Proxy Setup

Drop a `proxies.txt` file in the project root with one proxy per line:

```
192.168.1.1:8080
socks5://10.0.0.1:1080
user:pass@proxy.example.com:3128
```

Or use the included proxy fetcher:

```bash
python fetch_proxies.py
```

TOR is auto-detected if running on `127.0.0.1:9050`.

---

## Requirements

- Python 3.8+
- `requests`
- `colorama` (optional — falls back gracefully)

```bash
pip install -r requirements.txt
```

---

## Disclaimer

This tool is intended for **authorized security testing only**. Do not use it against systems you don't own or have explicit permission to test.

Unauthorized access to computer systems is illegal. The developer takes no responsibility for misuse.

---

## Author

**Muhammad Abid** — [@V3n0mSh3ll](https://github.com/V3n0mSh3ll)

---

<p align="center"><sub>Built for pentesters who need results, not another GUI wrapper.</sub></p>
