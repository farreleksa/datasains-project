import requests
import os
import json
import time

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan.")

VAR_ID = 543

periode_tahun = {
    2021: 121,
    2022: 122,
    2023: 123,
    2024: 124,
    2025: 125
}

semua_data = {}

for tahun, th_id in periode_tahun.items():

    url = (
        "https://webapi.bps.go.id/v1/api/list/model/data/"
        f"lang/ind/domain/0000/var/{VAR_ID}/th/{th_id}/key/{API_KEY}"
    )

    response = requests.get(url, timeout=60)

    print(f"Mengambil data TPT {tahun}: HTTP {response.status_code}")

    response.raise_for_status()

    semua_data[tahun] = response.json()

    time.sleep(1)

with open(
    "data_raw_tpt_2021_2025.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        semua_data,
        file,
        indent=2,
        ensure_ascii=False
    )

print("\nPENGAMBILAN DATA TPT SELESAI")
print("Jumlah tahun:", len(semua_data))
print("File data_raw_tpt_2021_2025.json berhasil disimpan.")