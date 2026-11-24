import pandas as pd

# Membaca data
df = pd.read_csv("data_pdb.csv")

print("=" * 60)
print("AUDIT ANOMALI DATA PDB INDONESIA")
print("=" * 60)

# 1. Menampilkan 10 nilai pertumbuhan tertinggi
print("\n1. SEPULUH NILAI TERTINGGI")

top = df.nlargest(10, "nilai")[
    ["tahun", "periode", "lapangan_usaha", "nilai"]
]

print(top.to_string(index=False))

# 2. Menampilkan 10 nilai terendah
print("\n2. SEPULUH NILAI TERENDAH")

bottom = df.nsmallest(10, "nilai")[
    ["tahun", "periode", "lapangan_usaha", "nilai"]
]

print(bottom.to_string(index=False))

# 3. Memeriksa jumlah nilai ekstrem
print("\n3. PEMERIKSAAN NILAI EKSTREM")

print("Nilai di bawah -20%:",
      (df["nilai"] < -20).sum())

print("Nilai di atas 20%:",
      (df["nilai"] > 20).sum())

# 4. Memeriksa duplikasi berdasarkan identitas observasi
keys = [
    "tahun",
    "periode",
    "kode_lapangan_usaha",
    "kode_turvar",
    "id_variabel"
]

print("\n4. DUPLIKASI IDENTITAS OBSERVASI")
print("Jumlah:", df.duplicated(subset=keys).sum())

# 5. Perbandingan data tahunan dan triwulanan
print("\n5. RATA-RATA BERDASARKAN PERIODE")

print(
    df.groupby("periode")["nilai"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
)

print("\nAUDIT SELESAI")