import json
from pathlib import Path

file_path = Path("data_raw_pdb/pdb_2021_2025_raw.json")

with file_path.open("r", encoding="utf-8") as file:
    records = json.load(file)

print("PEMERIKSAAN METADATA PDB")
print("=" * 60)

for record in records[:1]:

    response = record["response"]

    print("TAHUN:", record["period"])

    # Memeriksa seluruh dimensi
    dimensions = [
        "subject",
        "var",
        "turvar",
        "labelvervar",
        "vervar",
        "tahun",
        "turtahun",
        "related"
    ]

    for dimension in dimensions:

        print("\nDIMENSI:", dimension)

        values = response.get(dimension)

        if isinstance(values, list):
            for item in values[:15]:
                print(item)
        else:
            print(values)

    # Memeriksa kode datacontent
    content = response.get("datacontent", {})

    print("\nCONTOH KODE DATACONTENT")

    for index, (key, value) in enumerate(content.items()):
        print("Kode:", key, "| Nilai:", value)

        if index >= 14:
            break

print("\nPEMERIKSAAN SELESAI")