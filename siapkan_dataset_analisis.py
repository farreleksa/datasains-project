import pandas as pd
from pathlib import Path

print("=" * 60)
print("MENYIAPKAN DATASET ANALISIS PDB")
print("=" * 60)

df = pd.read_csv(
    "data_processed/data_pdb_clean.csv"
)

# Ambil data triwulanan
triwulan = df[
    df["periode"].str.contains(
        "Triwulan", na=False
    )
].copy()

# Ambil data tahunan
tahunan = df[
    df["periode"] == "Tahunan"
].copy()

# Dataset pertumbuhan triwulanan
ctoc = triwulan[
    triwulan["jenis_pertumbuhan"] == "c-to-c"
].copy()

qtoq = triwulan[
    triwulan["jenis_pertumbuhan"] == "q-to-q"
].copy()

yoy = triwulan[
    triwulan["jenis_pertumbuhan"] == "y-on-y"
].copy()

# Dataset pertumbuhan tahunan
ctoc_tahunan = tahunan[
    tahunan["jenis_pertumbuhan"] == "c-to-c"
].copy()

# Folder output
output = Path("data_processed")
output.mkdir(exist_ok=True)

# Simpan dataset
ctoc.to_csv(
    output / "pdb_triwulanan_ctoc.csv",
    index=False
)

qtoq.to_csv(
    output / "pdb_triwulanan_qtoq.csv",
    index=False
)

yoy.to_csv(
    output / "pdb_triwulanan_yoy.csv",
    index=False
)

ctoc_tahunan.to_csv(
    output / "pdb_tahunan_ctoc.csv",
    index=False
)

print("\nHASIL PEMISAHAN DATA")
print("c-to-c triwulanan:", len(ctoc))
print("q-to-q triwulanan:", len(qtoq))
print("y-on-y triwulanan:", len(yoy))
print("c-to-c tahunan:", len(ctoc_tahunan))

print("\nDATASET BERHASIL DISIAPKAN!")