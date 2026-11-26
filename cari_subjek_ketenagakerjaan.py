import os
import requests
import os

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan. Periksa environment variable Windows.")

url = (
    "https://webapi.bps.go.id/v1/api/list/"
    "model/subject/domain/0000/key/" + API_KEY
)

response = requests.get(url, timeout=60)

print("STATUS HTTP:", response.status_code)

response.raise_for_status()

data = response.json()

print("\nDAFTAR SUBJEK BPS:")
print("=" * 50)

hasil = []

for bagian in data.get("data", []):
    if isinstance(bagian, list):
        hasil.extend(bagian)

for item in hasil:
    nama = str(item.get("title", item.get("name", "")))

    if "tenaga kerja" in nama.lower() or "ketenagakerjaan" in nama.lower():
        print("ID SUBJEK:", item.get("sub_id", item.get("id")))
        print("NAMA:", nama)
        print("-" * 40)

with open(
    "daftar_subjek_bps.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("\nFile daftar_subjek_bps.json berhasil disimpan.")