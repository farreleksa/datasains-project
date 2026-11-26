
import os
import requests
import pandas as pd
import time

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

hasil = []

print("PEMERIKSAAN KELOMPOK HS 01-97")
print("=" * 55)

for nomor in range(1, 98):

    kodehs = f"{nomor:02d}"

    params = {
        "sumber": 1,
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
            timeout=120
        )

        if response.status_code == 200:
            data = response.json()
            records = data.get("data", [])

            nama = (
                records[0]["kodehs"]
                if records else "Tidak ada data"
            )

            jumlah = len(records)
            status = data.get("status")

        else:
            nama = "-"
            jumlah = 0
            status = f"HTTP {response.status_code}"

        hasil.append({
            "kode_hs": kodehs,
            "nama_hs": nama,
            "jumlah_observasi": jumlah,
            "status": status
        })

        print(
            f"HS {kodehs} | {nama} | "
            f"Observasi: {jumlah} | {status}"
        )

        time.sleep(1)

    except requests.exceptions.RequestException as error:
        print(f"HS {kodehs} gagal: {error}")

        hasil.append({
            "kode_hs": kodehs,
            "nama_hs": "-",
            "jumlah_observasi": 0,
            "status": "ERROR"
        })

df = pd.DataFrame(hasil)

df.to_csv(
    "daftar_seluruh_kode_hs.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nPEMERIKSAAN SELESAI")
print("Jumlah kode diperiksa:", len(df))
print("Kode dengan data:", (df["jumlah_observasi"] > 0).sum())
print("File: daftar_seluruh_kode_hs.csv")
