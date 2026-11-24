
import json

with open(
    "data_raw_inflasi_2021_2025.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

isi = data["2021"]

print("=" * 55)
print("PEMERIKSAAN STRUKTUR OBSERVASI INFLASI 2021")
print("=" * 55)

for nama in ["tahun", "turtahun", "vervar", "datacontent"]:
    bagian = isi.get(nama)

    print(f"\n--- {nama.upper()} ---")
    print("Tipe:", type(bagian).__name__)

    if isinstance(bagian, list):
        print("Jumlah:", len(bagian))
        print("Contoh:")
        print(json.dumps(
            bagian[:5],
            indent=2,
            ensure_ascii=False
        ))

    elif isinstance(bagian, dict):
        print("Jumlah:", len(bagian))
        print("Contoh:")
        contoh = dict(list(bagian.items())[:10])
        print(json.dumps(
            contoh,
            indent=2,
            ensure_ascii=False
        ))

    else:
        print(bagian)

print("\nPEMERIKSAAN SELESAI")
