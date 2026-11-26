import requests
import os
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan.")

semua_subjek = []

for halaman in range(1, 7):
    url = (
        "https://webapi.bps.go.id/v1/api/list/model/subject/"
        f"domain/0000/page/{halaman}/key/{API_KEY}"
    )

    response = requests.get(url, timeout=30)
    print(f"Mengambil halaman {halaman}: HTTP {response.status_code}")
    response.raise_for_status()

    hasil = response.json()
    daftar = hasil["data"][1]

    semua_subjek.extend(daftar)

# Simpan seluruh subjek
with open("daftar_subjek_bps_lengkap.json", "w", encoding="utf-8") as file:
    json.dump(semua_subjek, file, indent=2, ensure_ascii=False)

# Cari subjek terkait ketenagakerjaan
print("\nHASIL PENCARIAN SUBJEK:")
print("=" * 50)

kata_kunci = ["tenaga kerja", "ketenagakerjaan", "pengangguran", "angkatan kerja"]

for item in semua_subjek:
    if any(k in item["title"].lower() for k in kata_kunci):
        print("ID SUBJEK:", item["sub_id"])
        print("NAMA:", item["title"])
        print("-" * 40)

print("\nTotal subjek berhasil diambil:", len(semua_subjek))
print("File daftar_subjek_bps_lengkap.json berhasil disimpan.")