
import pandas as pd

file = "data_processed/data_inflasi.csv"

df = pd.read_csv(file)

print("=" * 55)
print("VALIDASI KUALITAS DATA INFLASI")
print("=" * 55)

print("\n1. UKURAN DATA")
print("Jumlah baris:", len(df))
print("Jumlah kolom:", len(df.columns))

print("\n2. NILAI KOSONG")
print(df.isnull().sum())

print("\n3. DUPLIKASI")
print("Duplikasi seluruh baris:", df.duplicated().sum())

kunci = [
    "tahun",
    "kode_wilayah",
    "kode_periode"
]

print(
    "Duplikasi berdasarkan identitas observasi:",
    df.duplicated(subset=kunci).sum()
)

print("\n4. STATISTIK INFLASI")
print(df["nilai_inflasi"].describe())

print("\n5. NILAI MINIMUM DAN MAKSIMUM")
print("Minimum:", df["nilai_inflasi"].min())
print("Maksimum:", df["nilai_inflasi"].max())

print("\n6. JUMLAH WILAYAH PER TAHUN")
print(
    df.groupby("tahun")["kode_wilayah"].nunique()
)

print("\n7. JUMLAH DATA PER PERIODE")
print(df["periode"].value_counts())

print("\nVALIDASI SELESAI")