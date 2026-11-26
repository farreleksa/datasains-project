
import os
import requests

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

print("UJI DATA PERDAGANGAN TAHUNAN")
print("=" * 55)

for sumber, nama in [(1, "EKSPOR"), (2, "IMPOR")]:

    print("\nJENIS DATA:", nama)

    for tahun in [2021, 2022, 2023, 2024, 2025]:

        params = {
            "sumber": sumber,
            "periode": 2,
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

            print("\nTahun:", tahun)
            print("HTTP:", response.status_code)

            if response.status_code == 200:

                data = response.json()
                records = data.get("data", [])

                print(
                    "Ketersediaan:",
                    data.get("data-availability")
                )
                print("Jumlah observasi:", len(records))

                if records:
                    print("Contoh:", records[0])

            else:
                print(response.text[:500])

        except requests.exceptions.RequestException as error:
            print("Kesalahan:", error)

print("\nPENGUJIAN SELESAI")