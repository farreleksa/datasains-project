import requests
import os
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan.")

VAR_ID = 543

url = (
    "https://webapi.bps.go.id/v1/api/list/model/th/"
    f"domain/0000/var/{VAR_ID}/key/{API_KEY}"
)

response = requests.get(url, timeout=30)

print("STATUS HTTP:", response.status_code)
response.raise_for_status()

data = response.json()

with open("periode_tpt.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("\nDAFTAR PERIODE DATA TPT:")
print("=" * 50)

print(json.dumps(data.get("data"), indent=2, ensure_ascii=False))

print("\nFile periode_tpt.json berhasil disimpan.")