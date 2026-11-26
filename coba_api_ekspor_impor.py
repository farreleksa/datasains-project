
import os
import requests

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

for sumber, nama in [(1, "EKSPOR"), (2, "IMPOR")]:
    for kodehs in ["01", "02"]:
        params = {
            "sumber": sumber,
            "periode": 1,
            "kodehs": kodehs,
            "jenishs": 1,
            "tahun": 2025,
            "key": API_KEY
        }

        response = requests.get(url, params=params, timeout=60)

        print("\n------------------------------")
        print(nama, "| HS", kodehs)
        print("HTTP STATUS:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            records = data.get("data", [])
            print("STATUS:", data.get("status"))
            print("KETERSEDIAAN:", data.get("data-availability"))
            print("JUMLAH DATA:", len(records))
            print("CONTOH:", records[:2])
        else:
            print("PESAN ERROR:", response.text[:1000])
