
import os
import requests
import pandas as pd

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

params = {
    "sumber": 1,
    "periode": 1,
    "kodehs": "03",
    "jenishs": 1,
    "tahun": 2021,
    "key": API_KEY
}

print("MENGUJI DATA EKSPOR HS 03 TAHUN 2021")

response = requests.get(
    url,
    params=params,
    timeout=120
)

print("HTTP STATUS:", response.status_code)

if response.status_code == 200:

    data = response.json()
    records = data.get("data", [])

    print("STATUS BPS:", data.get("status"))
    print("JUMLAH OBSERVASI:", len(records))

    if records:
        df = pd.DataFrame(records)

        print("\nDAFTAR KOLOM:")
        print(df.columns.tolist())

        print("\nRENTANG BULAN:")
        print(df["bulan"].value_counts().sort_index())

        print("\nCONTOH DATA:")
        print(df.head(5).to_string(index=False))

else:
    print("DETAIL ERROR:")
    print(response.text[:2000])