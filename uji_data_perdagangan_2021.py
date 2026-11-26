
import os
import requests

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

daftar_sumber = [
    (1, "EKSPOR"),
    (2, "IMPOR")
]

print("UJI KETERSEDIAAN EKSPOR DAN IMPOR")
print("=" * 55)

for sumber, nama in daftar_sumber:

    print("\nJENIS DATA:", nama)

    for tahun in range(2021, 2026):

        params = {
            "sumber": sumber,
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

            if response.status_code == 200:

                data = response.json()
                records = data.get("data", [])

                print(
                    f"Tahun {tahun} | "
                    f"Ketersediaan: "
                    f"{data.get('data-availability')} | "
                    f"Observasi: {len(records)}"
                )

            else:
                print(
                    f"Tahun {tahun} | "
                    f"HTTP {response.status_code}"
                )

        except requests.exceptions.RequestException as error:
            print("Kesalahan:", error)

print("\nPENGUJIAN SELESAI")