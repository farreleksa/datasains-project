import pandas as pd

df = pd.read_csv("data_processed/data_pdb_clean.csv")

annual = df[df["periode"] == "Tahunan"].copy()

print("PEMERIKSAAN DATA TAHUNAN")
print("=" * 50)

print("Jumlah observasi:", len(annual))

print("\nJumlah setiap jenis pertumbuhan:")
print(annual["jenis_pertumbuhan"].value_counts())

print("\nContoh data tahunan:")
print(
    annual[
        [
            "tahun",
            "lapangan_usaha",
            "jenis_pertumbuhan",
            "nilai"
        ]
    ].head(15).to_string(index=False)
)

print("\nPEMERIKSAAN SELESAI")