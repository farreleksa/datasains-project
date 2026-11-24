import pandas as pd

df = pd.read_csv(
    "data_processed/data_pdb_tahunan.csv"
)

print("PEMERIKSAAN KONSISTENSI DATA")
print("=" * 50)

print("\n1. RENTANG TAHUN")
print(df["tahun"].value_counts().sort_index())

print("\n2. JUMLAH KATEGORI")
print(df["lapangan_usaha"].nunique())

print("\n3. PERBANDINGAN JENIS PERTUMBUHAN")

pivot = df.pivot_table(
    index=["tahun", "lapangan_usaha"],
    columns="jenis_pertumbuhan",
    values="nilai"
)

print(pivot.head(15).to_string())

print("\n4. JUMLAH NILAI BERBEDA")
print(pivot.nunique())

print("\n5. PEMERIKSAAN SELESAI")