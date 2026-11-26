import os
import requests
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

params = {
    "sumber": 1,
    "periode": 1,
    "kodehs": "01",
    "jenishs": 1,
    "tahun": 2025,
    "key": API_KEY
}

response = requests.get(url, params=params, timeout=60)

print("HTTP STATUS:", response.status_code)

if response.status_code == 200:
    data = response.json()
    records = data.get("data", [])

    kode_hs = sorted(
        set(item.get("kodehs") for item in records if item.get("kodehs"))
    )

    print("\nJUMLAH KELOMPOK HS:", len(kode_hs))
    print("\nDAFTAR HS:")

    for item in kode_hs:
        print(item)

else:
    print(response.text[:2000])