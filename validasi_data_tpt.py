import pandas as pd

# Membaca data
df = pd.read_csv("data_processed/data_tpt.csv")
agustus = pd.read_csv("data_processed/data_tpt_agustus.csv")

print("=" * 55)
print("VALIDASI DATA TPT INDONESIA")
print("=" * 55)

# 1. Ukuran dataset
print("\n1. UKURAN DATA")
print("Baris:", len(df))
print("Kolom:", len(df.columns))

# 2. Missing values
print("\n2. MISSING VALUES")
print(df.isnull().sum())

# 3. Duplikasi
print("\n3. DUPLIKASI")
print("Duplikat seluruh baris:", df.duplicated().sum())

kolom_kunci = [
    "tahun",
    "kode_wilayah",
    "kode_periode"
]

print(
    "Duplikat identitas:",
    df.duplicated(subset=kolom_kunci).sum()
)

# 4. Jumlah observasi per tahun dan periode
print("\n4. OBSERVASI PER TAHUN DAN PERIODE")
print(
    df.groupby(["tahun", "periode"]).size()
)

# 5. Jumlah wilayah per tahun
print("\n5. JUMLAH WILAYAH")
print(
    df.groupby("tahun")["kode_wilayah"].nunique()
)

# 6. Statistik TPT
print("\n6. STATISTIK DESKRIPTIF")
print(df["nilai_tpt"].describe())

# 7. Validasi data Agustus
print("\n7. DATA AGUSTUS")
print(
    agustus.groupby("tahun").size()
)

# 8. Memisahkan agregat Indonesia
provinsi = agustus[
    agustus["kode_wilayah"] != 9999
].copy()

nasional = agustus[
    agustus["kode_wilayah"] == 9999
].copy()

print("\n8. PEMISAHAN DATA AGUSTUS")
print("Observasi provinsi:", len(provinsi))
print("Observasi Indonesia:", len(nasional))

print("\nVALIDASI SELESAI")