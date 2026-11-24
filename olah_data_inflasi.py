import json
import csv
import os

# 1. Membaca data mentah
with open(
    "data_raw_inflasi_2021_2025.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

semua_baris = []
kode_tidak_dikenal = []

# 2. Mengolah data setiap tahun
for tahun, isi in data.items():

    print(f"Mengolah data inflasi tahun {tahun}...")

    var = isi["var"][0]
    tahun_info = isi["tahun"][0]
    datacontent = isi["datacontent"]

    # Membuat daftar kode wilayah
    wilayah_dict = {
        str(item["val"]): item["label"]
        for item in isi["vervar"]
    }

    # Membuat daftar periode
    periode_dict = {
        str(item["val"]): item["label"]
        for item in isi["turtahun"]
    }

    # Mencocokkan kode observasi dengan metadata
    for kode, nilai in datacontent.items():

        ditemukan = False

        for kode_wilayah, nama_wilayah in wilayah_dict.items():

            for kode_periode, nama_periode in periode_dict.items():

                kode_prediksi = (
                    kode_wilayah
                    + str(var["val"])
                    + str(tahun_info["val"])
                    + kode_periode
                )

                if kode == kode_prediksi:

                    baris = {
                        "tahun": tahun,
                        "periode": nama_periode,
                        "kode_periode": kode_periode,
                        "kode_wilayah": kode_wilayah,
                        "nama_wilayah": nama_wilayah,
                        "id_variabel": var["val"],
                        "indikator": var["label"],
                        "satuan": var.get("unit", ""),
                        "nilai_inflasi": nilai
                    }

                    semua_baris.append(baris)
                    ditemukan = True
                    break

            if ditemukan:
                break

        if not ditemukan:
            kode_tidak_dikenal.append({
                "tahun": tahun,
                "kode": kode,
                "nilai": nilai
            })

# 3. Memisahkan data bulanan dan tahunan
data_bulanan = [
    baris for baris in semua_baris
    if baris["periode"] != "Tahunan"
]

data_tahunan = [
    baris for baris in semua_baris
    if baris["periode"] == "Tahunan"
]

# 4. Menyimpan CSV
os.makedirs("data_processed", exist_ok=True)

kolom = [
    "tahun",
    "periode",
    "kode_periode",
    "kode_wilayah",
    "nama_wilayah",
    "id_variabel",
    "indikator",
    "satuan",
    "nilai_inflasi"
]

def simpan_csv(nama_file, daftar_baris):
    with open(
        nama_file,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=kolom
        )
        writer.writeheader()
        writer.writerows(daftar_baris)

simpan_csv(
    "data_processed/data_inflasi.csv",
    semua_baris
)

simpan_csv(
    "data_processed/data_inflasi_bulanan.csv",
    data_bulanan
)

simpan_csv(
    "data_processed/data_inflasi_tahunan.csv",
    data_tahunan
)

# 5. Laporan hasil pengolahan
print("\n" + "=" * 50)
print("HASIL PENGOLAHAN DATA INFLASI")
print("=" * 50)

print("Total observasi:", len(semua_baris))
print("Data bulanan:", len(data_bulanan))
print("Data tahunan:", len(data_tahunan))
print("Kode tidak dikenali:", len(kode_tidak_dikenal))

print("\nJumlah data per tahun:")
for tahun in sorted(data.keys()):
    jumlah = sum(
        1 for baris in semua_baris
        if baris["tahun"] == tahun
    )
    print(tahun, ":", jumlah)

if kode_tidak_dikenal:
    print("\nContoh kode yang belum cocok:")
    for item in kode_tidak_dikenal[:10]:
        print(item)

print("\nFile berhasil disimpan di folder data_processed.")