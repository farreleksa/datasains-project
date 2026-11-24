import pandas as pd

df = pd.read_csv("data_pdb.csv")

print("=" * 60)
print("AUDIT DATA MENTAH PDB BPS")
print("=" * 60)

print("\n1. DAFTAR KOLOM")
print(df.columns.tolist())

print("\n2. DISTRIBUSI KODE TURVAR")
print(df["kode_turvar"].value_counts(dropna=False))

print("\n3. DISTRIBUSI KATEGORI TURVAR")
print(df["kategori_turvar"].value_counts(dropna=False))

print("\n4. CONTOH DATA BERDASARKAN KODE TURVAR")

for kode in df["kode_turvar"].dropna().unique():

    subset = df[
        df["kode_turvar"] == kode
    ]

    print("\nKODE TURVAR:", kode)
    print(
        subset[
            [
                "tahun",
                "periode",
                "lapangan_usaha",
                "kode_turvar",
                "kategori_turvar",
                "nilai"
            ]
        ].head(5).to_string(index=False)
    )

print("\n5. AUDIT SELESAI")