
import os
import requests

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

print("PENGUJIAN HS 03 UNTUK TAHUN 2021-2025")
print("=" * 55)

for tahun in range(2021, 2026):

    params = {
        "sumber": 1,
        "periode": 1,
        "kodehs": "03",
        "jenishs": 1,
        "tahun": tahun,
        "key": API_KEY
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=120
        )

        print("\nTAHUN:", tahun)
        print("HTTP STATUS:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            records = data.get("data", [])

            print("STATUS BPS:", data.get("status"))
            print("KETERSEDIAAN:", data.get("data-availability"))
            print("JUMLAH OBSERVASI:", len(records))

            if records:
                print("CONTOH:", records[0])

        else:
            print("ERROR:", response.text[:500])

    except requests.exceptions.RequestException as error:
        print("KESALAHAN KONEKSI:", error)

print("\nPENGUJIAN SELESAI")