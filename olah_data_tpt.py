import json
import pandas as pd
import os
import re

# 1. Membaca data mentah
with open(
    "data_raw_tpt_2021_2025.json",
    "r",
    encoding="utf-8"
) as file:
    raw_data = json.load(file)

# 2. Membuat folder output
os.makedirs("data_processed", exist_ok=True)

semua_baris = []

# 3. Pemetaan periode
periode_mapping = {
    "189": "Februari",
    "190": "Agustus",
    "191": "Tahunan"
}

# 4. Mengolah setiap tahun
for tahun, data in raw_data.items():

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
        # wilayah + variabel + turvar + tahun + periode

        match = re.fullmatch(
            r"(\d{4})(543)(\d)(\d{3})(\d{3})",
            str(kode)
        )

        if not match:
            print("Kode tidak dikenali:", kode)
            continue

        kode_wilayah = match.group(1)
        id_variabel = match.group(2)
        kode_turvar = match.group(3)
        th_id = match.group(4)
        kode_periode = match.group(5)

        nama_wilayah = daftar_wilayah.get(
            kode_wilayah,
            "Tidak diketahui"
        )

        nama_periode = daftar_periode.get(
            kode_periode,
            periode_mapping.get(
                kode_periode,
                "Tidak diketahui"
            )
        )

        semua_baris.append({
            "tahun": int(tahun),
            "kode_wilayah": kode_wilayah,
            "nama_wilayah": nama_wilayah,
            "id_variabel": int(id_variabel),
            "kode_turvar": kode_turvar,
            "indikator": "Tingkat Pengangguran Terbuka",
            "kode_periode": kode_periode,
            "periode": nama_periode,
            "satuan": "Persen",
            "nilai_tpt": float(nilai)
        })

# 5. Membuat DataFrame
df = pd.DataFrame(semua_baris)

if df.empty:
    raise ValueError(
        "Data TPT kosong. Periksa kembali pola kode BPS."
    )

# 6. Mengurutkan data
df = df.sort_values(
    ["tahun", "kode_wilayah", "kode_periode"]
)

# 7. Menyimpan seluruh data
df.to_csv(
    "data_processed/data_tpt.csv",
    index=False,
    encoding="utf-8-sig"
)

# 8. Memisahkan data Agustus
df_agustus = df[
    df["periode"].str.lower() == "agustus"
].copy()

df_agustus.to_csv(
    "data_processed/data_tpt_agustus.csv",
    index=False,
    encoding="utf-8-sig"
)

# 9. Memisahkan data Februari
df_februari = df[
    df["periode"].str.lower() == "februari"
].copy()

df_februari.to_csv(
    "data_processed/data_tpt_februari.csv",
    index=False,
    encoding="utf-8-sig"
)

# 10. Ringkasan hasil
print("\nDATA CLEANING TPT SELESAI")
print("=" * 50)

print("Total observasi:", len(df))
print("Data Agustus:", len(df_agustus))
print("Data Februari:", len(df_februari))

print("\nJumlah data per tahun:")
print(df.groupby("tahun").size())

print("\nStatistik deskriptif TPT:")
print(df["nilai_tpt"].describe())

print("\nJumlah wilayah per tahun:")
print(
    df.groupby("tahun")["kode_wilayah"].nunique()
)

print("\nFile berhasil disimpan:")
print("- data_processed/data_tpt.csv")
print("- data_processed/data_tpt_agustus.csv")
print("- data_processed/data_tpt_februari.csv")