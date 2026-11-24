import pandas as pd

df = pd.read_csv("data_pdb.csv")

print("=" * 60)
print("AUDIT DIMENSI DATA PDB")
print("=" * 60)

# 1. Daftar seluruh kategori turvar
print("\n1. DAFTAR KODE TURVAR")

turvar = df[
    ["kode_turvar", "kategori_turvar"]
].drop_duplicates()

print(turvar.to_string(index=False))

print("\nJUMLAH TURVAR:", len(turvar))

# 2. Pemeriksaan kategori lapangan usaha
print("\n2. JUMLAH KATEGORI LAPANGAN USAHA")

sektor = df[
    ["kode_lapangan_usaha", "lapangan_usaha"]
].drop_duplicates()

print(sektor.to_string(index=False))
print("TOTAL:", len(sektor))

# 3. Periksa satu sektor yang ekstrem
print("\n3. DETAIL ANGKUTAN UDARA")

udara = df[
    df["lapangan_usaha"].str.contains(
        "Angkutan Udara",
        case=False,
        na=False
    )
]

print(
    udara[
        [
            "tahun",
            "periode",
            "kode_turvar",
            "kategori_turvar",
            "nilai"
        ]
    ].sort_values(
        ["tahun", "periode", "kode_turvar"]
    ).to_string(index=False)
)

# 4. Pemeriksaan jenis periode
print("\n4. PEMISAHAN PERIODE")

print("Triwulanan:",
      df["periode"].str.contains(
          "Triwulan", na=False
      ).sum())

print("Tahunan:",
      (df["periode"] == "Tahunan").sum())

# 5. Identitas unik
print("\n5. IDENTITAS OBSERVASI")

keys = [
    "tahun",
    "periode",
    "kode_lapangan_usaha",
    "kode_turvar",
    "id_variabel"
]

print("Total baris:", len(df))
print("Identitas unik:", df[keys].drop_duplicates().shape[0])

print("\nAUDIT DIMENSI SELESAI")