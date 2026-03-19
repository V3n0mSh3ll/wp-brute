#!/usr/bin/env python3
"""
Proxy Fetcher - Automatically download free proxies
"""
import requests
import time
import sys

def fetch_from_geonode():
    """Fetch from Geonode (Best free source)"""
    print("[*] Fetching from Geonode API...")
    try:
        url = "https://proxylist.geonode.com/api/proxy-list/?limit=500&sort_by=lastChecked&sort_type=desc"
        response = requests.get(url, timeout=10)
        data = response.json()
        proxies = []
        
        for proxy in data.get('data', []):
            ip = proxy.get('ip')
            port = proxy.get('port')
            if ip and port:
                proxies.append(f"{ip}:{port}")
        
        print(f"[+] Got {len(proxies)} proxies from Geonode")
        return proxies
    except Exception as e:
        print(f"[-] Geonode error: {e}")
        return []

def fetch_from_proxy_list():
    """Fetch from Free Proxy List"""
    print("[*] Fetching from Free Proxy List...")
    try:
        url = "https://free-proxy-list.net/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
        }
        response = requests.get(url, headers=headers, timeout=10)
        proxies = []
        
        import re
        ips = re.findall(r'(\d+\.\d+\.\d+\.\d+)', response.text)
        ports = re.findall(r'<td>(\d+)</td>\s*</tr>', response.text)
        
        for i, ip in enumerate(ips[:100]):
            if i < len(ports):
                proxies.append(f"{ip}:{ports[i]}")
        
        print(f"[+] Got {len(proxies)} proxies from Free Proxy List")
        return proxies
    except Exception as e:
        print(f"[-] Free Proxy List error: {e}")
        return []

def validate_proxies(proxies):
    """Validate proxies by testing them"""
    print(f"\n[*] Validating {len(proxies)} proxies...")
    valid = []
    timeout_count = 0
    
    for i, proxy in enumerate(proxies):
        sys.stdout.write(f"\r[*] Testing [{i+1}/{len(proxies)}] - Valid: {len(valid)}")
        sys.stdout.flush()
        
        try:
            test_url = 'http://httpbin.org/ip'
            proxy_config = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            response = requests.get(test_url, proxies=proxy_config, timeout=3)
            
            if response.status_code == 200:
                valid.append(proxy)
        except requests.exceptions.Timeout:
            timeout_count += 1
        except:
            pass
    
    print(f"\n[+] {len(valid)} proxies validated successfully")
    print(f"[!] {timeout_count} proxies timed out (may still work)")
    return valid

def save_proxies(proxies, filename='proxies.txt'):
    """Save proxies to file"""
    with open(filename, 'w') as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
    print(f"[+] Saved {len(proxies)} proxies to {filename}")

def main():
    print("="*60)
    print("[*] Advanced Proxy Fetcher for WP Brute Force")
    print("="*60)
    
    all_proxies = []
    geonode_proxies = fetch_from_geonode()
    all_proxies.extend(geonode_proxies)
    time.sleep(1)
    all_proxies = list(set(all_proxies))
    print(f"\n[+] Total unique proxies: {len(all_proxies)}")
    
    validate = input("\n[?] Validate proxies? (y/n, slower): ").lower() == 'y'
    if validate:
        all_proxies = validate_proxies(all_proxies)
    
    if all_proxies:
        save_proxies(all_proxies)
        print("\n[+] Ready to use! Run wp_brute.py now")
        print(f"[*] Proxies file: proxies.txt ({len(all_proxies)} proxies)")
    else:
        print("\n[-] No proxies found! Try again later")
        print("\n[*] Using fallback proxy list...")
        fallback = [
            "1.10.141.220:8080",
            "190.61.101.126:3128",
            "177.37.166.126:8080",
        ]
        save_proxies(fallback)
        print("[+] Saved fallback proxies (may not work)")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[-] Interrupted by user")
    except Exception as e:
        print(f"\n[-] Error: {e}")
