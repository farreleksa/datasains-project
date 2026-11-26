
import os
import requests

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

params = {
    "sumber": 1,
    "periode": 1,
    "kodehs": "03",
    "jenishs": 1,
    "tahun": 2025,
    "key": API_KEY
}

response = requests.get(url, params=params, timeout=60)

print("HTTP STATUS:", response.status_code)

if response.status_code == 200:
    data = response.json()
    records = data.get("data", [])

    print("STATUS BPS:", data.get("status"))
    print("KETERSEDIAAN:", data.get("data-availability"))
    print("JUMLAH OBSERVASI:", len(records))

    if records:
        print("\nNAMA KELOMPOK HS:")
        print(records[0]["kodehs"])

        print("\nCONTOH DATA:")
        for item in records[:5]:
            print(item)
else:
    print("DETAIL ERROR:")
    print(response.text[:2000])