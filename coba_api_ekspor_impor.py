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

data = response.json()

print("STATUS BPS:", data.get("status"))
print("KETERSEDIAAN:", data.get("data-availability"))
print("METADATA:")
print(json.dumps(data.get("metadata", {}), indent=2, ensure_ascii=False))

print("\nCONTOH DATA:")
print(json.dumps(data.get("data", [])[:3], indent=2, ensure_ascii=False))