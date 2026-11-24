import pandas as pd
from pathlib import Path

# Membaca dataset
file_path = Path("data_pdb.csv")
df = pd.read_csv(file_path)

print("=" * 55)
print("LAPORAN VALIDASI DATA PDB")
print("=" * 55)

# 1. Ukuran dataset
print("\n1. UKURAN DATA")
print("Jumlah baris:", len(df))
print("Jumlah kolom:", len(df.columns))

# 2. Tahun yang tersedia
print("\n2. DISTRIBUSI TAHUN")
print(df["tahun"].value_counts().sort_index())

# 3. Pemeriksaan nilai kosong
print("\n3. NILAI KOSONG")
print(df.isnull().sum())

# 4. Pemeriksaan duplikasi
print("\n4. DATA DUPLIKAT")
print("Jumlah duplikat:", df.duplicated().sum())

# 5. Pemeriksaan nilai statistik
print("\n5. STATISTIK DESKRIPTIF")
print(df["nilai"].describe())

# 6. Pemeriksaan periode
print("\n6. DISTRIBUSI PERIODE")
print(df["periode"].value_counts())

# 7. Pemeriksaan kategori lapangan usaha
print("\n7. JUMLAH KATEGORI")
print(df["lapangan_usaha"].nunique())

# 8. Pemeriksaan satuan
print("\n8. SATUAN")
print(df["satuan"].value_counts(dropna=False))

print("\nVALIDASI SELESAI")