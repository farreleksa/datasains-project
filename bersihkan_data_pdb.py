import pandas as pd
import re
import html
from pathlib import Path

print("=" * 60)
print("DATA CLEANING PDB INDONESIA")
print("=" * 60)

# 1. MEMBACA DATA
df = pd.read_csv("data_pdb.csv")

print("Data awal:", df.shape)

# 2. MEMBERSIHKAN HTML
def clean_text(value):
    if pd.isna(value):
        return value

    value = html.unescape(str(value))
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\s+", " ", value)

    return value.strip()

text_columns = [
    "periode",
    "lapangan_usaha",
    "kategori_turvar",
    "indikator",
    "satuan",
    "status_data",
    "catatan"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].apply(clean_text)

# 3. MEMASTIKAN TIPE DATA
df["tahun"] = pd.to_numeric(
    df["tahun"], errors="coerce"
)

df["nilai"] = pd.to_numeric(
    df["nilai"], errors="coerce"
)

# 4. MEMBERI NAMA JENIS PERTUMBUHAN
growth_mapping = {
    "3": "c-to-c",
    "4": "q-to-q",
    "5": "y-on-y"
}

df["jenis_pertumbuhan"] = (
    df["kode_turvar"].astype(str)
    .str.replace(r"\.0$", "", regex=True)
    .map(growth_mapping)
)

# 5. MEMERIKSA DATA
print("\nPEMERIKSAAN HASIL CLEANING")

print("Jumlah baris:", len(df))
print("Nilai kosong:", df.isnull().sum().sum())
print("Duplikasi:", df.duplicated().sum())

print("\nJENIS PERTUMBUHAN:")
print(df["jenis_pertumbuhan"].value_counts(dropna=False))

# 6. MEMISAHKAN PERIODE
triwulanan = df[
    df["periode"].str.contains(
        "Triwulan", na=False
    )
].copy()

tahunan = df[
    df["periode"] == "Tahunan"
].copy()

# 7. MEMBUAT FOLDER OUTPUT
output_dir = Path("data_processed")
output_dir.mkdir(exist_ok=True)

# 8. MENYIMPAN DATA
df.to_csv(
    output_dir / "data_pdb_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

triwulanan.to_csv(
    output_dir / "data_pdb_triwulanan.csv",
    index=False,
    encoding="utf-8-sig"
)

tahunan.to_csv(
    output_dir / "data_pdb_tahunan.csv",
    index=False,
    encoding="utf-8-sig"
)

# 9. MEMISAHKAN TIGA JENIS INDIKATOR
for code, name in growth_mapping.items():

    subset = df[
        df["kode_turvar"].astype(str)
        .str.replace(r"\.0$", "", regex=True)
        == code
    ]

    subset.to_csv(
        output_dir / f"data_pdb_{name}.csv",
        index=False,
        encoding="utf-8-sig"
    )

# 10. LAPORAN
print("\nHASIL DATA CLEANING")
print("=" * 60)

print("Total data bersih:", len(df))
print("Data triwulanan:", len(triwulanan))
print("Data tahunan:", len(tahunan))

print("\nFILE BERHASIL DIBUAT:")

for file in sorted(output_dir.glob("*.csv")):
    print("-", file)

print("\nDATA CLEANING SELESAI!")