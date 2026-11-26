
import pandas as pd

# Membaca hasil pemeriksaan kode HS
df = pd.read_csv("daftar_seluruh_kode_hs.csv")

print("=" * 55)
print("RINGKASAN PEMERIKSAAN KODE HS")
print("=" * 55)

print("Total kode diperiksa :", len(df))
print(
    "Kode dengan data     :",
    (df["jumlah_observasi"] > 0).sum()
)
print(
    "Kode tanpa data      :",
    (df["jumlah_observasi"] == 0).sum()
)

# Menampilkan kode HS yang tidak memiliki observasi
tanpa_data = df[df["jumlah_observasi"] == 0]

print("\nDAFTAR KODE HS TANPA DATA:")
if len(tanpa_data) > 0:
    print(tanpa_data.to_string(index=False))
else:
    print("Semua kode memiliki data.")

# Menampilkan kode HS dengan data
ada_data = df[df["jumlah_observasi"] > 0]

print("\nDAFTAR KODE HS DENGAN DATA:")
print(ada_data.to_string(index=False))

print("\nPEMERIKSAAN SELESAI")