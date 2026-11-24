import os
import requests
import json
import time

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum ditemukan.")

BASE_URL = "https://webapi.bps.go.id/v1/api"

periode = {
    "2021": 121,
    "2022": 122,
    "2023": 123,
    "2024": 124,
    "2025": 125
}

semua_data = {}

for tahun, th_id in periode.items():

    print(f"Mengambil data inflasi tahun {tahun}...")

    url = (
        f"{BASE_URL}/list/model/data/lang/ind/"
        f"domain/0000/var/1/th/{th_id}/key/{API_KEY}"
    )

    response = requests.get(url, timeout=60)
    print("Status HTTP:", response.status_code)
    response.raise_for_status()

    data = response.json()
    semua_data[tahun] = data

    print(f"Data tahun {tahun} berhasil diambil.")

    time.sleep(1)

with open(
    "data_raw_inflasi_2021_2025.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        semua_data,
        file,
        indent=2,
        ensure_ascii=False
    )

print("\n===================================")
print("PENGAMBILAN DATA INFLASI SELESAI")
print("File: data_raw_inflasi_2021_2025.json")
print("===================================")