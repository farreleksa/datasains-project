
import os
import requests

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

print("UJI KLASIFIKASI HS 2021-2022")
print("=" * 55)

for tahun in [2021, 2022]:
    for jenis_hs in [1, 2]:

        params = {
            "sumber": 1,
            "periode": 1,
            "kodehs": "03",
            "jenishs": jenis_hs,
            "tahun": tahun,
            "key": API_KEY
        }

        response = requests.get(
            url,
            params=params,
            timeout=120
        )

        print(
            f"\nTahun: {tahun} | "
            f"Jenis HS: {jenis_hs}"
        )

        print("HTTP:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            records = data.get("data", [])

            print(
                "Ketersediaan:",
                data.get("data-availability")
            )
            print("Observasi:", len(records))

            if records:
                print("Contoh:", records[0])

        else:
            print(response.text[:500])

print("\nPENGUJIAN SELESAI")