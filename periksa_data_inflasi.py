import json
from collections import Counter

with open(
    "data_raw_inflasi_2021_2025.json",
    "r",
    encoding="utf-8"
) as file:
    data = json.load(file)

isi = data["2021"]

print("=" * 55)
print("ANALISIS KODE OBSERVASI INFLASI")
print("=" * 55)

print("\n1. INFORMASI VARIABEL")
print(json.dumps(isi["var"], indent=2, ensure_ascii=False))

print("\n2. SELURUH PERIODE")
for item in isi["turtahun"]:
    print(item["val"], "-", item["label"])

print("\n3. CONTOH KODE WILAYAH")
for item in isi["vervar"][:10]:
    print(item["val"], "-", item["label"])

print("\n4. POLA KODE DATACONTENT")
datacontent = isi["datacontent"]

print("Jumlah observasi:", len(datacontent))
print("Panjang kode:", Counter(
    len(str(kode)) for kode in datacontent.keys()
))

print("\n10 KODE OBSERVASI PERTAMA:")
for kode, nilai in list(datacontent.items())[:10]:
    print("Kode:", kode, "| Nilai:", nilai)

print("\n5. CONTOH KODE TERAKHIR:")
for kode, nilai in list(datacontent.items())[-10:]:
    print("Kode:", kode, "| Nilai:", nilai)

print("\nPEMERIKSAAN SELESAI")