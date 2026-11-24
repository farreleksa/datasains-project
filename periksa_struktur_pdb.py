
import json
from pathlib import Path

file_path = Path("data_raw_pdb/pdb_2021_2025_raw.json")

with file_path.open("r", encoding="utf-8") as file:
    records = json.load(file)

print("JUMLAH PERIODE:", len(records))

for record in records:

    response = record.get("response", {})
    content = response.get("datacontent")

    print("\n" + "=" * 60)
    print("PERIODE:", record.get("period"))
    print("STATUS:", response.get("status"))
    print("KETERSEDIAAN:", response.get("data-availability"))
    print("SUBJEK:", response.get("subject"))
    print("VARIABEL:", response.get("var"))

    print("\nTIPE DATACONTENT:", type(content).__name__)

    if isinstance(content, dict):
        print("JUMLAH ITEM:", len(content))
        print("CONTOH ISI:")

        for index, (key, value) in enumerate(content.items()):
            print(key, ":", value)

            if index >= 9:
                break

    elif isinstance(content, list):
        print("JUMLAH ITEM:", len(content))
        print(json.dumps(
            content[:10],
            indent=2,
            ensure_ascii=False
        ))

    else:
        print("DATACONTENT:", content)

    print("\nINFORMASI DIMENSI:")
    print("Tahun:", response.get("tahun"))
    print("Variabel:", response.get("var"))
    print("Label:", response.get("labelvervar"))

print("\nPEMERIKSAAN SELESAI")
