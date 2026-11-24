import pandas as pd

df = pd.read_csv(
    "data_processed/data_inflasi.csv"
)

print("=" * 55)
print("AUDIT KELENGKAPAN DATA INFLASI")
print("=" * 55)

for tahun in sorted(df["tahun"].unique()):

    data_tahun = df[df["tahun"] == tahun]

    bulanan = data_tahun[
        data_tahun["periode"] != "Tahunan"
    ]

    tahunan = data_tahun[
        data_tahun["periode"] == "Tahunan"
    ]

    print(f"\nTAHUN {tahun}")
    print("Jumlah wilayah bulanan:",
          bulanan["kode_wilayah"].nunique())
    print("Jumlah observasi bulanan:", len(bulanan))
    print("Jumlah observasi tahunan:", len(tahunan))
    print("Jumlah bulan tersedia:",
          bulanan["kode_periode"].nunique())

    print("\nJumlah observasi setiap bulan:")
    print(
        bulanan.groupby("periode").size().to_string()
    )

print("\nAUDIT SELESAI")