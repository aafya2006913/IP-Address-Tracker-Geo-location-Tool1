import requests
from datetime import datetime

# ================================
# IP Address Tracker & GeoLocation
# ================================

def track_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") != "success":
            print("\n❌ Invalid IP Address or API Error!")
            return

        print("\n===============================")
        print("   IP TRACKER REPORT")
        print("===============================")
        print("Scan Time:", datetime.now())
        print("--------------------------------")
        print("IP Address      :", data.get("query"))
        print("Country         :", data.get("country"))
        print("Region          :", data.get("regionName"))
        print("City            :", data.get("city"))
        print("ZIP Code        :", data.get("zip"))
        print("Latitude        :", data.get("lat"))
        print("Longitude       :", data.get("lon"))
        print("ISP             :", data.get("isp"))
        print("Organization    :", data.get("org"))
        print("Time Zone       :", data.get("timezone"))
        print("--------------------------------")
        print("Status          : SUCCESS")
        print("===============================\n")

    except Exception as e:
        print("\n⚠ Error:", e)

def main():
    print("=" * 55)
    print("     IP ADDRESS TRACKER & GEOLOCATION TOOL")
    print("=" * 55)
    ip = input("Enter IP Address to Track: ")

    track_ip(ip)

if __name__ == "__main__":
    main()
