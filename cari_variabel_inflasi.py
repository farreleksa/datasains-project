
import os
import requests
import time
import json

API_KEY = os.getenv("BPS_API_KEY")
BASE_URL = "https://webapi.bps.go.id/v1/api"

if not API_KEY:
    raise ValueError("BPS_API_KEY belum tersedia.")

def ambil_halaman(page):
    url = (
        f"{BASE_URL}/list/model/var/"
        f"domain/0000/key/{API_KEY}?page={page}"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    return response.json()

print("=" * 60)
print("PENCARIAN SELURUH KATALOG VARIABEL BPS")
print("=" * 60)

# Ambil halaman pertama
hasil_awal = ambil_halaman(1)

metadata = hasil_awal["data"][0]
total_halaman = metadata["pages"]

print("Total variabel:", metadata["total"])
print("Total halaman:", total_halaman)

semua_variabel = []

# Membaca seluruh halaman
for halaman in range(1, total_halaman + 1):

    hasil = hasil_awal if halaman == 1 else ambil_halaman(halaman)

    data_halaman = hasil["data"][1]

    semua_variabel.extend(data_halaman)

    print(
        f"Halaman {halaman}/{total_halaman} "
        f"| Data: {len(data_halaman)}"
    )

    time.sleep(0.15)

# Pencarian kata kunci
kata_kunci = [
    "inflasi",
    "indeks harga konsumen",
    "harga konsumen",
    "consumer price index",
    "ihk"
]

print("\nHASIL PENCARIAN INFLASI")
print("=" * 60)

ditemukan = []

for item in semua_variabel:

    teks = " ".join([
        str(item.get("title", "")),
        str(item.get("sub_name", "")),
        str(item.get("subcsa_name", "")),
        str(item.get("notes", ""))
    ]).lower()

    if any(k in teks for k in kata_kunci):
        ditemukan.append(item)

for item in ditemukan:

    print("ID VARIABEL:", item.get("var_id"))
    print("NAMA:", item.get("title"))
    print("SUBJEK:", item.get("sub_name"))
    print("KATEGORI:", item.get("subcsa_name"))
    print("SATUAN:", item.get("unit"))
    print("-" * 60)

print("\nTOTAL VARIABEL DITEMUKAN:", len(ditemukan))

# Simpan hasil pencarian
with open(
    "katalog_variabel_inflasi.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        ditemukan,
        file,
        ensure_ascii=False,
        indent=2
    )

print("\nPENCARIAN KATALOG SELESAI!")
