import json

nama_file = "data_raw_inflasi_2021_2025.json"

with open(nama_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Periksa respons lengkap untuk tahun 2021
isi = data["2021"]

print("KUNCI UTAMA:")
print(list(isi.keys()))

print("\nRESPONS LENGKAP TAHUN 2021:")
print(json.dumps(
    isi,
    indent=2,
    ensure_ascii=False
)[:8000])