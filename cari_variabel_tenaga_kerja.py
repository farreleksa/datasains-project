import requests
import os
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan.")

url = (
    "https://webapi.bps.go.id/v1/api/list/model/var/"
    f"domain/0000/subject/6/key/{API_KEY}"
)

response = requests.get(url, timeout=30)

print("STATUS HTTP:", response.status_code)
response.raise_for_status()

data = response.json()

with open("variabel_tenaga_kerja.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("\nDAFTAR VARIABEL TENAGA KERJA:")
print("=" * 60)

for item in data.get("data", [[], []])[1]:
    if isinstance(item, dict):
        print(
            "ID:", item.get("var_id"),
            "| NAMA:", item.get("title")
        )

print("\nFile variabel_tenaga_kerja.json berhasil disimpan.")