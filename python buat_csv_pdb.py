import json
import csv
from pathlib import Path
from itertools import product

# ==========================================
# 1. MEMBACA DATA JSON
# ==========================================

input_file = Path("data_raw_pdb/pdb_2021_2025_raw.json")
output_file = Path("data_pdb.csv")

with input_file.open("r", encoding="utf-8") as file:
    records = json.load(file)

rows = []

# ==========================================
# 2. MENGEKSTRAK SETIAP PERIODE
# ==========================================

print("MEMULAI EKSTRAKSI DATA PDB...")

def get_dimensions(response, name):
    values = response.get(name)
    if isinstance(values, list) and values:
        return values
    return [{"val": "", "label": ""}]

for record in records:

    response = record.get("response", {})
    content = response.get("datacontent", {})

    if not isinstance(content, dict):
        continue

    vervars = get_dimensions(response, "vervar")
    variables = get_dimensions(response, "var")
    turvars = get_dimensions(response, "turvar")
    years = get_dimensions(response, "tahun")
    subperiods = get_dimensions(response, "turtahun")

    metadata = variables[0]

    for vv, var, tv, year, subperiod in product(
        vervars,
        variables,
        turvars,
        years,
        subperiods
    ):

        # Kunci dibentuk dari gabungan ID dimensi
        key = "".join(
            str(item["val"])
            for item in [vv, var, tv, year, subperiod]
            if item["val"] != ""
        )

        if key not in content:
            continue

        value = content[key]

        if value is None:
            continue

        rows.append({
            "tahun": year.get("label", ""),
            "periode": subperiod.get("label", ""),
            "kode_lapangan_usaha": vv.get("val", ""),
            "lapangan_usaha": vv.get("label", ""),
            "kode_turvar": tv.get("val", ""),
            "kategori_turvar": tv.get("label", ""),
            "id_variabel": var.get("val", ""),
            "indikator": var.get("label", ""),
            "satuan": metadata.get("unit", ""),
            "nilai": value,
            "kode_datacontent": key,
            "status_data": response.get("data-availability", ""),
            "catatan": metadata.get("note", "")
        })

# ==========================================
# 3. MENYIMPAN CSV
# ==========================================

if not rows:
    raise ValueError(
        "Tidak ada observasi yang berhasil dipetakan. "
        "Periksa kembali dimensi dan kode datacontent."
    )

fieldnames = list(rows[0].keys())

with output_file.open(
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(rows)

# ==========================================
# 4. LAPORAN HASIL
# ==========================================

print("\nEKSTRAKSI SELESAI!")
print("Jumlah observasi:", len(rows))
print("Nama file:", output_file)

print("\nCONTOH 10 DATA PERTAMA:")

for row in rows[:10]:
    print(
        row["tahun"],
        "|",
        row["periode"],
        "|",
        row["lapangan_usaha"],
        "|",
        row["nilai"]
    )