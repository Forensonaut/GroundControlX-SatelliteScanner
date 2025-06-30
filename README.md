# 🛰️ GroundControlX – Satellite OSINT Exposure Scanner

A lightweight Python tool to identify **publicly exposed satellite infrastructure** using Shodan.  
Built for educational research and awareness — especially in digital forensics and national cybersecurity.

---

## 🔍 What It Does

This script performs automated Shodan queries for satellite-related systems like:

- 📡 VSAT modems  
- 🛰️ Satellite uplink controllers  
- 🌍 iDirect & Norsat devices  
- ⚙️ Other satellite communication endpoints

It fetches:
- Device IP address  
- Country of exposure  
- Hosting organization  
- Preview of open port service data

---

## 📁 Files in This Repo

| File             | Purpose                      |
|------------------|------------------------------|
| `scanner.py`     | The main Python script        |
| `requirements.txt` | List of dependencies         |
| `README.md`      | You're reading it :)         |

---

## 🚀 How to Use

1. Install Dependencies
Make sure Python 3 is installed, then run:

pip install -r requirements.txt

2. Get Your Shodan API Key
Sign up at https://account.shodan.io
Copy your API key.

3. Paste API Key in Script
Edit scanner.py and replace:

API_KEY = "YOUR_API_KEY"

4. Run the Tool

python scanner.py

---

## 🖥️ Sample Output (Example)

 🔍 Searching: vsat  
 📊 Total found: 271  
 🛰️ IP: 192.0.2.123  
 🌍 Country: United States  
 🏢 Org: Satellite Comms Inc.  
 🧾 Data: HTTP/1.1 200 OK...

---

## ⚠️ Disclaimer

This tool is intended for **educational and research use only**.  
It does not exploit or intrude — it passively uses public OSINT data from Shodan.

**Do NOT use for unauthorized scanning, intrusion, or attacks.**  
Always comply with Shodan's Terms of Service.

---

Credits

Developed by **Tanish Kathpalia**  
Cyber Ambassador, GPCSSI 2025  
