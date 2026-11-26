import os
import requests
import json

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

for sumber, nama in [(1, "EKSPOR"), (2, "IMPOR")]:
    params = {
        "sumber": sumber,
        "periode": 1,
        "kodehs": "01;02",
        "jenishs": 1,
        "tahun": 2025,
        "key": API_KEY
    }

    response = requests.get(url, params=params, timeout=120)

    print("\n", "=" * 40)
    print("JENIS DATA:", nama)
    print("HTTP STATUS:", response.status_code)

    data = response.json()

    print("STATUS BPS:", data.get("status"))
    print("KETERSEDIAAN:", data.get("data-availability"))

    records = data.get("data", [])

    print("JUMLAH OBSERVASI:", len(records))
    print("CONTOH DATA:")
    print(json.dumps(records[:5], indent=2, ensure_ascii=False))