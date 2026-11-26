import json
import pandas as pd
import os
import re

# Membaca data mentah
with open(
    "data_raw_tpt_2021_2025.json",
    "r",
    encoding="utf-8"
) as file:
    raw_data = json.load(file)

# Folder output
os.makedirs("data_processed", exist_ok=True)

semua_baris = []

# Pemetaan periode
periode_mapping = {
    "189": "Februari",
    "190": "Agustus",
    "191": "Tahunan"
}

for tahun, data in raw_data.items():

    tahun_label = tahun

    daftar_wilayah = {
        str(item["val"]): item["label"]
        for item in data["vervar"]
    }

    daftar_periode = {
        str(item["val"]): item["label"]
        for item in data["turtahun"]
    }

    datacontent = data["datacontent"]

    for kode, nilai in datacontent.items():

        # Format kode:
        # kode_wilayah + id_variabel + tahun_id + periode_id

        match = re.fullmatch(
            r"(\d{4})(543)(\d{3})(\d{3})",
            str(kode)
        )

        if not match:
            print("Kode tidak dikenali:", kode)
            continue

        kode_wilayah = match.group(1)
        id_variabel = match.group(2)
        th_id = match.group(3)
        kode_periode = match.group(4)

        nama_wilayah = daftar_wilayah.get(
            kode_wilayah,
            "Tidak diketahui"
        )

        nama_periode = daftar_periode.get(
            kode_periode,
            periode_mapping.get(kode_periode, "Tidak diketahui")
        )

        semua_baris.append({
            "tahun": int(tahun_label),
            "kode_wilayah": kode_wilayah,
            "nama_wilayah": nama_wilayah,
            "id_variabel": int(id_variabel),
            "indikator": "Tingkat Pengangguran Terbuka",
            "kode_periode": kode_periode,
            "periode": nama_periode,
            "satuan": "Persen",
            "nilai_tpt": float(nilai)
        })

# Membuat DataFrame
df = pd.DataFrame(semua_baris)

# Mengurutkan data
df = df.sort_values(
    ["tahun", "kode_wilayah", "kode_periode"]
)

# Menyimpan seluruh data
df.to_csv(
    "data_processed/data_tpt.csv",
    index=False,
    encoding="utf-8-sig"
)

# Data Agustus
df_agustus = df[df["periode"] == "Agustus"].copy()

df_agustus.to_csv(
    "data_processed/data_tpt_agustus.csv",
    index=False,
    encoding="utf-8-sig"
)

# Data Februari
df_februari = df[df["periode"] == "Februari"].copy()

df_februari.to_csv(
    "data_processed/data_tpt_februari.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nDATA CLEANING TPT SELESAI")
print("=" * 50)

print("Total observasi:", len(df))
print("Data Agustus:", len(df_agustus))
print("Data Februari:", len(df_februari))

print("\nJumlah data per tahun:")
print(df.groupby("tahun").size())

print("\nStatistik deskriptif TPT:")
print(df["nilai_tpt"].describe())

print("\nFile berhasil disimpan:")
print("- data_processed/data_tpt.csv")
print("- data_processed/data_tpt_agustus.csv")
print("- data_processed/data_tpt_februari.csv")