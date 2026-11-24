import json

nama_file = "data_raw_inflasi_2021_2025.json"

with open(nama_file, "r", encoding="utf-8") as file:
    data = json.load(file)

print("=" * 50)
print("PEMERIKSAAN DATA INFLASI BPS")
print("=" * 50)

for tahun, isi in data.items():
    print(f"\nTAHUN: {tahun}")
    print("Status:", isi.get("status"))
    print("Ketersediaan:", isi.get("data-availability"))

    bagian_data = isi.get("data", [])

    print("Tipe data:", type(bagian_data).__name__)
    print("Jumlah bagian data:", len(bagian_data))

    if len(bagian_data) > 1:
        print("\nCONTOH DATA:")
        print(json.dumps(
            bagian_data[1],
            indent=2,
            ensure_ascii=False
        )[:2000])

print("\nPEMERIKSAAN SELESAI")