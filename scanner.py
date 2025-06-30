import shodan

API_KEY = "YOUR_API_KEY"  

satellite_keywords = ["vsat", "norsat", "iDirect", "comtech", "satellite uplink"]

api = shodan.Shodan(API_KEY)

def search_satellite_devices():
    for keyword in satellite_keywords:
        print(f"\n🔍 Searching: {keyword}")
        try:
            results = api.search(keyword)
            print(f"📊 Total found: {results['total']}")
            for result in results['matches'][:3]:
                print(f"🛰️ IP: {result['ip_str']}")
                print(f"🌍 Country: {result.get('location', {}).get('country_name')}")
                print(f"🏢 Org: {result.get('org', 'N/A')}")
                print(f"🧾 Data:\n{result['data'][:150]}...\n")
        except shodan.APIError as e:
            print(f"❌ Error: {e}")

search_satellite_devices()
