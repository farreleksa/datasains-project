import pandas as pd

df = pd.read_csv(
    "data_processed/data_pdb_tahunan.csv"
)

pivot = df.pivot_table(
    index=["tahun", "lapangan_usaha"],
    columns="jenis_pertumbuhan",
    values="nilai"
)

print("AUDIT PERBEDAAN PERTUMBUHAN PDB")
print("=" * 55)

print("\n1. JUMLAH BARIS PERBANDINGAN")
print(len(pivot))

print("\n2. JUMLAH BARIS DENGAN NILAI BERBEDA")
berbeda = pivot.nunique(axis=1) > 1
print(berbeda.sum())

print("\n3. CONTOH BARIS YANG BERBEDA")
print(pivot[berbeda].head(10))

print("\n4. CONTOH BARIS YANG SAMA")
print(pivot[~berbeda].head(10))

print("\n5. AUDIT SELESAI")