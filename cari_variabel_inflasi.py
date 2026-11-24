import os
import requests
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError(
        "API Key tidak ditemukan. "
        "Periksa variabel BPS_API_KEY."
    )

BASE_URL = "https://webapi.bps.go.id/v1/api"

url = (
    f"{BASE_URL}/list/model/var/"
    f"domain/0000/key/{API_KEY}"
)

print("MENGHUBUNGKAN KE KATALOG BPS...")

response = requests.get(url, timeout=30)

print("HTTP STATUS:", response.status_code)

if response.status_code != 200:
    print("Pesan server:", response.text[:1000])
    raise SystemExit("Gagal mengambil katalog.")

result = response.json()

print("\nSTATUS:", result.get("status"))

# Mencari seluruh informasi variabel
def cari_variabel(obj, hasil):
    if isinstance(obj, dict):

        teks = str(obj).lower()

        kata_kunci = [
            "inflasi",
            "harga konsumen",
            "indeks harga",
            "ihk"
        ]

        if any(k in teks for k in kata_kunci):
            hasil.append(obj)

        for value in obj.values():
            cari_variabel(value, hasil)

    elif isinstance(obj, list):
        for item in obj:
            cari_variabel(item, hasil)

hasil = []
cari_variabel(result.get("data", []), hasil)

print("\nHASIL PENCARIAN VARIABEL INFLASI")
print("=" * 60)

if hasil:
    for item in hasil:
        print(json.dumps(
            item,
            ensure_ascii=False,
            indent=2
        ))
        print("-" * 60)
else:
    print("Belum ditemukan variabel dengan kata kunci tersebut.")
    print("\nStruktur respons API:")
    print(json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    )[:5000])

print("\nPENCARIAN SELESAI")