
import os
import requests
import pandas as pd
import time

API_KEY = os.getenv("BPS_API_KEY")

if not API_KEY:
    raise ValueError("BPS_API_KEY belum terbaca.")

url = "https://webapi.bps.go.id/v1/api/dataexim/"

hasil = []

print("PENGUJIAN HS 01 SAMPAI HS 10")
print("=" * 55)

for nomor in range(1, 11):

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

        print(f"\nHS {kodehs} | HTTP {response.status_code}")

        if response.status_code == 200:

            data = response.json()
            records = data.get("data", [])

            nama_hs = (
                records[0]["kodehs"]
                if records else "Tidak ada data"
            )

            jumlah = len(records)

            print("Nama:", nama_hs)
            print("Jumlah observasi:", jumlah)

            hasil.append({
                "kode_hs": kodehs,
                "nama_hs": nama_hs,
                "jumlah_observasi": jumlah,
                "status": data.get("status")
            })

        else:
            print("Pesan:", response.text[:300])

            hasil.append({
                "kode_hs": kodehs,
                "nama_hs": "-",
                "jumlah_observasi": 0,
                "status": f"HTTP {response.status_code}"
            })

        time.sleep(1)

    except requests.exceptions.RequestException as error:
        print("Kesalahan:", error)

# Menyimpan hasil pemeriksaan

df = pd.DataFrame(hasil)

df.to_csv(
    "hasil_pemeriksaan_kode_hs.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "=" * 55)
print("HASIL AKHIR")
print(df.to_string(index=False))
print("\nFile tersimpan: hasil_pemeriksaan_kode_hs.csv")