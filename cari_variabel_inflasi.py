
import os
import requests
import json
import time

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum tersedia.")

# ID 3 = Inflasi
SUBJECT_ID = 3

BASE_URL = "https://webapi.bps.go.id/v1/api/list"

# Mengatur retry otomatis jika terkena HTTP 429
retry_strategy = Retry(
    total=8,
    backoff_factor=3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    respect_retry_after_header=True
)

session = requests.Session()

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)

def ambil_halaman(page):

    url = (
        f"{BASE_URL}/model/var/"
        f"domain/0000/subject/{SUBJECT_ID}/"
        f"key/{API_KEY}"
    )

    response = session.get(
        url,
        params={
            "lang": "ind",
            "page": page
        },
        timeout=60
    )

    response.raise_for_status()

    return response.json()


print("=" * 60)
print("PENCARIAN VARIABEL INFLASI BPS")
print("=" * 60)

try:

    hasil_awal = ambil_halaman(1)

    metadata = hasil_awal["data"][0]
    total_halaman = int(metadata["pages"])

    print("Total variabel:", metadata.get("total"))
    print("Total halaman:", total_halaman)

    semua_variabel = []

    for halaman in range(1, total_halaman + 1):

        hasil = (
            hasil_awal
            if halaman == 1
            else ambil_halaman(halaman)
        )

        data = hasil["data"][1]

        semua_variabel.extend(data)

        print(
            f"Halaman {halaman}/{total_halaman}"
            f" | Data: {len(data)}"
        )

        time.sleep(1.5)

    print("\nDAFTAR VARIABEL INFLASI")
    print("=" * 60)

    for item in semua_variabel:

        print("ID:", item.get("var_id"))
        print("Nama:", item.get("title"))
        print("Satuan:", item.get("unit"))
        print("Subjek:", item.get("sub_name"))
        print("-" * 50)

    with open(
        "katalog_variabel_inflasi.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            semua_variabel,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("\nTOTAL VARIABEL:", len(semua_variabel))
    print("FILE JSON BERHASIL DISIMPAN!")

except requests.exceptions.RequestException as error:

    print("\nGAGAL MENGAKSES API BPS.")
    print("Jenis error:", type(error).__name__)
    print("Silakan coba kembali setelah beberapa saat.")

