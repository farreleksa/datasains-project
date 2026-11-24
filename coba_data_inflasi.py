import os
import requests
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan.")

BASE_URL = "https://webapi.bps.go.id/v1/api"

url = (
    f"{BASE_URL}/list/model/data/lang/ind/"
    f"domain/0000/var/1/key/{API_KEY}"
)

response = requests.get(url, timeout=60)
response.raise_for_status()

data = response.json()

print("STATUS:", data.get("status"))
print("JUMLAH DATA:", data.get("data-availability"))

print("\nSTRUKTUR DATA:")
print(json.dumps(data, indent=2, ensure_ascii=False)[:5000])

with open("data_inflasi_uji.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("\nFILE data_inflasi_uji.json BERHASIL DISIMPAN")