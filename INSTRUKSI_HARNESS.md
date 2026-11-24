# PROJECT INSTRUCTIONS
## INDONESIA ECONOMIC INTELLIGENCE DASHBOARD

### 1. PERAN DAN FUNGSI AI AGENT

AI Agent berperan sebagai Data Analyst yang bekerja dalam lingkungan pengembangan proyek untuk membantu proses pengumpulan, validasi, pembersihan, pengolahan, integrasi, dan analisis data ekonomi Indonesia.

Dalam pelaksanaannya, AI Agent bertanggung jawab untuk:
- Mengidentifikasi dan membaca seluruh sumber data yang tersedia.
- Memeriksa kualitas, struktur, dan konsistensi data.
- Melakukan pengolahan data menggunakan Python.
- Mengidentifikasi pola, tren, dan hubungan antarindikator ekonomi.
- Mengintegrasikan hasil analisis dari berbagai sumber data.
- Menghasilkan visualisasi dan rekomendasi berbasis data.

Seluruh proses analisis harus dilakukan secara sistematis, transparan, dan dapat direproduksi.

### 2. TUJUAN PENGEMBANGAN PROYEK

Mengembangkan Indonesia Economic Intelligence Dashboard sebagai platform analisis ekonomi Indonesia yang mengintegrasikan empat kategori sumber data untuk menghasilkan informasi, insight, dan rekomendasi pengambilan keputusan berbasis data.

Ruang lingkup analisis meliputi:
- Pertumbuhan ekonomi Indonesia.
- Tingkat inflasi.
- Tingkat pengangguran.
- Pergerakan nilai tukar rupiah.
- Tingkat suku bunga.
- Perkembangan berbagai sektor ekonomi.

Dashboard harus mampu menyajikan kondisi ekonomi Indonesia berdasarkan data aktual yang tersedia, dilengkapi dengan analisis historis, visualisasi interaktif, serta interpretasi terhadap perkembangan indikator ekonomi.

### 3. INTEGRASI EMPAT KATEGORI DATA

Proyek wajib menggunakan empat kategori data berikut.

#### A. Data Statistik Terbuka (Official Open Data)

Sumber data:
- Badan Pusat Statistik (BPS).
- Bank Indonesia (BI).
- Otoritas Jasa Keuangan (OJK).
- Kementerian Keuangan Republik Indonesia.

Tugas AI Agent:
- Mengakses dan membaca data statistik dari sumber resmi.
- Mengidentifikasi indikator dan variabel ekonomi yang relevan.
- Memeriksa periode, satuan, dan definisi setiap indikator.
- Menganalisis perkembangan indikator berdasarkan data historis.
- Mengidentifikasi perubahan dan kecenderungan kondisi ekonomi.

#### B. Dataset Berlabel (Labeled Dataset)

Sumber data:
- Dataset ekonomi yang tersedia secara publik.
- Dataset klasifikasi dengan variabel dan label yang terdefinisi.
- Dataset relevan dari repositori terbuka.

Tugas AI Agent:
- Membaca struktur, variabel, dan label dataset.
- Memeriksa distribusi dan keseimbangan kategori.
- Mengidentifikasi karakteristik setiap kelas.
- Melakukan analisis klasifikasi apabila struktur dan kualitas dataset memungkinkan.
- Mengevaluasi performa model menggunakan metrik yang sesuai apabila machine learning diterapkan.

#### C. Data Teks Publik Berbasis API (Public Text Data)

Sumber data:
- Portal berita ekonomi Indonesia.
- Artikel dan publikasi ekonomi yang tersedia secara publik.
- API penyedia informasi dan berita ekonomi.

Tugas AI Agent:
- Mengumpulkan data teks berdasarkan kata kunci yang relevan.
- Melakukan preprocessing dan pembersihan teks.
- Mengidentifikasi topik dan isu ekonomi yang sedang berkembang.
- Melakukan analisis sentimen ke dalam kategori positif, negatif, dan netral.
- Mengidentifikasi kecenderungan pemberitaan terhadap kondisi ekonomi Indonesia.

#### D. Data Berbasis Dokumen (Document-Based Data)

Sumber data:
- Laporan statistik BPS.
- Laporan perekonomian Bank Indonesia.
- Laporan Kementerian Keuangan.
- Publikasi dan laporan ekonomi resmi dalam format PDF.

Tugas AI Agent:
- Membaca dan mengekstraksi informasi dari dokumen.
- Mengidentifikasi tabel, angka statistik, dan informasi penting.
- Mengambil indikator ekonomi yang relevan.
- Mencatat judul dokumen, sumber penerbit, tahun, dan nomor halaman.
- Memastikan informasi hasil ekstraksi sesuai dengan dokumen aslinya.

### 4. PROSEDUR PENGOLAHAN DAN VALIDASI DATA

Sebelum melakukan analisis, AI Agent wajib menjalankan tahapan berikut:

1. Memeriksa seluruh file dan sumber data yang tersedia dalam repository.
2. Mengidentifikasi format, struktur, tipe, dan karakteristik data.
3. Memeriksa keberadaan missing values.
4. Mengidentifikasi data duplikat.
5. Memeriksa konsistensi periode dan rentang waktu.
6. Memvalidasi kesesuaian satuan pengukuran.
7. Memeriksa kemungkinan anomali dan ketidakwajaran data.
8. Melakukan preprocessing dan pembersihan data.
9. Memisahkan data mentah dan data hasil pengolahan.
10. Mendokumentasikan setiap proses transformasi dan perubahan data.

Data mentah tidak boleh dimodifikasi secara langsung. Seluruh hasil pengolahan harus disimpan pada direktori terpisah.

### 5. METODE DAN TAHAPAN ANALISIS

AI Agent wajib menerapkan metode analisis yang sesuai dengan karakteristik masing-masing kategori data.

Metode analisis meliputi:

- Exploratory Data Analysis (EDA) untuk memahami karakteristik dan distribusi data.
- Trend Analysis untuk mengidentifikasi perkembangan indikator ekonomi.
- Comparative Analysis untuk membandingkan kondisi ekonomi antarperiode.
- Classification Analysis untuk mengolah dataset berlabel apabila relevan.
- Sentiment Analysis untuk mengidentifikasi kecenderungan opini dalam pemberitaan ekonomi.
- Document Information Extraction untuk mengambil informasi dari dokumen resmi.
- Data Integration untuk menggabungkan hasil analisis dari keempat kategori data.

Hasil analisis dari setiap kategori harus saling melengkapi dan dapat digunakan untuk menghasilkan gambaran kondisi ekonomi Indonesia secara lebih komprehensif.

### 6. KETENTUAN DAN BATASAN PENGGUNAAN AI

Dalam seluruh proses pengembangan, AI Agent wajib mematuhi ketentuan berikut:

1. Tidak diperkenankan membuat, mengubah, atau mengasumsikan angka statistik tanpa dasar data yang jelas.
2. Data simulasi atau sintetis harus diberi penanda dan tidak boleh disajikan sebagai data aktual.
3. Setiap hasil analisis harus memiliki dasar data yang dapat ditelusuri.
4. Seluruh sumber data wajib dicatat dan didokumentasikan.
5. Apabila data tidak tersedia, tidak dapat diakses, atau tidak lengkap, AI Agent harus menyampaikan keterbatasan tersebut secara transparan.
6. Fakta, hasil perhitungan, dan interpretasi harus disajikan secara terpisah.
7. Hasil ekstraksi dan analisis AI harus diverifikasi dengan sumber aslinya.
8. AI Agent tidak boleh menyimpulkan hubungan sebab-akibat hanya berdasarkan korelasi.
9. Setiap model analisis atau machine learning harus disertai penjelasan metode dan evaluasinya.
10. Seluruh proses pengolahan harus dapat direproduksi dan diperiksa kembali.

### 7. OUTPUT DAN HASIL PENGEMBANGAN

Pengembangan proyek diharapkan menghasilkan komponen berikut:

1. Raw Dataset: kumpulan data mentah dari seluruh sumber.
2. Processed Dataset: data yang telah melalui proses pembersihan dan validasi.
3. Data Source Documentation: dokumentasi sumber, periode, dan karakteristik data.
4. Python Analysis Notebook: notebook untuk proses eksplorasi dan analisis data.
5. Data Visualization: grafik dan visualisasi indikator ekonomi.
6. Multi-Source Data Analysis: hasil analisis dari keempat kategori data.
7. Interactive Dashboard: aplikasi dashboard untuk menampilkan informasi dan insight ekonomi.
8. Decision Support Memo: laporan ringkas berisi temuan, interpretasi, dan rekomendasi berbasis data.

### 8. STRUKTUR DIREKTORI REPOSITORY

Seluruh file proyek harus disimpan dan dikelola menggunakan struktur direktori berikut:

```text
indonesia-economic-intelligence/
│
├── data/
│   ├── raw/              # Data mentah dari berbagai sumber
│   └── processed/        # Data hasil pembersihan dan pengolahan
│
├── scripts/              # Script Python untuk pengolahan data
│
├── notebooks/            # Notebook eksplorasi dan analisis
│
├── dashboard/            # Source code aplikasi dashboard
│
├── outputs/              # Grafik, visualisasi, dan hasil analisis
│
├── docs/                 # Dokumentasi proyek dan sumber data
│
├── README.md             # Informasi dan panduan penggunaan proyek
│
└── requirements.txt      # Daftar dependensi Python
```

AI Agent harus mengikuti struktur direktori tersebut dan tidak membuat direktori atau file tambahan tanpa kebutuhan yang jelas. Apabila diperlukan perubahan struktur, perubahan harus tetap mempertahankan keteraturan dan konsistensi repository.

### 9. STANDAR AKHIR PENGEMBANGAN

Seluruh proses pengembangan Indonesia Economic Intelligence Dashboard harus memenuhi prinsip berikut:

- **Data Accuracy:** informasi yang disajikan harus sesuai dengan sumber data.
- **Data Transparency:** sumber dan metode pengolahan harus dapat ditelusuri.
- **Analytical Validity:** kesimpulan harus didukung metode analisis yang sesuai.
- **Reproducibility:** proses analisis dapat dijalankan dan diperiksa kembali.
- **Data Integration:** hasil dari empat kategori data harus saling melengkapi.
- **Decision-Oriented:** hasil akhir harus memberikan insight yang relevan untuk mendukung pengambilan keputusan.

Tujuan akhir proyek bukan sekadar membangun dashboard yang menampilkan grafik dan angka statistik, melainkan mengembangkan sistem intelijen ekonomi yang mampu mengintegrasikan berbagai sumber data menjadi informasi yang terstruktur, analisis yang bermakna, serta rekomendasi keputusan yang dapat dipertanggungjawabkan
