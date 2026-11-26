import os

import requests
import json

# ==========================================
# 1. MEMBACA API KEY
# ==========================================

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError(
        "BPS_API_KEY belum terbaca. "
        "Periksa environment variable terlebih dahulu."
    )

# ==========================================
# 2. ALAMAT API BPS
# ==========================================

url = "https://webapi.bps.go.id/v1/api/dataexim/"

# ==========================================
# 3. PENGUJIAN EKSPOR DAN IMPOR
# ==========================================

daftar_pengujian = [
    (1, "EKSPOR", "01"),
    (1, "EKSPOR", "02"),
    (2, "IMPOR", "01"),
    (2, "IMPOR", "02")
]

for sumber, nama, kodehs in daftar_pengujian:

    print("\n" + "=" * 60)
    print("JENIS DATA :", nama)
    print("KODE HS    :", kodehs)
    print("=" * 60)

    params = {
        "sumber": sumber,
        "periode": 1,
        "kodehs": kodehs,
        "jenishs": 1,
        "tahun": 2025,
        "key": API_KEY
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=60
        )

        print("HTTP STATUS :", response.status_code)
        print("URL REQUEST :", response.url.replace(API_KEY, "[API KEY DISEMBUNYIKAN]"))

        print("\nDETAIL RESPONSE:")
        print(response.text[:2000])

        if response.status_code == 200:

            data = response.json()

            print("\nSTATUS BPS :", data.get("status"))
            print("KETERSEDIAAN :", data.get("data-availability"))

            records = data.get("data", [])

            print("JUMLAH OBSERVASI :", len(records))

            print("\nCONTOH DATA:")

            print(
                json.dumps(
                    records[:3],
                    indent=2,
                    ensure_ascii=False
                )
            )

        else:

            print("\nPERMINTAAN GAGAL.")
            print("Periksa detail response di atas.")

    except requests.exceptions.RequestException as error:

        print("TERJADI KESALAHAN KONEKSI:")
        print(error)

print("\n" + "=" * 60)
print("PENGUJIAN SELESAI")
print("=" * 60)