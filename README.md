# Analisis Data Penyewaan Sepeda Menggunakan Python

## Ringkasan Proyek
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan kondisi cuaca, waktu, dan kategori pengguna. Analisis dilakukan menggunakan dataset harian (`day.csv`) dan per jam (`hour.csv`) untuk menemukan insight bisnis yang dapat mendukung pengambilan keputusan operasional.

## Latar Belakang
Penyewaan sepeda sangat dipengaruhi oleh faktor eksternal seperti cuaca, jam sibuk, hari kerja, dan hari libur. Dengan memahami pola tersebut, perusahaan dapat mengatur strategi operasional, distribusi armada, dan promosi dengan lebih efektif.

## Tujuan Penelitian
Penelitian ini dilakukan untuk menjawab dua pertanyaan utama:
1. Bagaimana pengaruh kondisi cuaca terhadap total penyewaan sepeda pada jam sibuk selama musim gugur tahun 2012?
2. Bagaimana perbandingan penggunaan sepeda antara pelanggan kasual dan pelanggan terdaftar pada hari kerja dibandingkan hari libur/akhir pekan?

## Dataset
Dataset yang digunakan berasal dari data penyewaan sepeda dengan dua file utama:
- `day.csv` → data penyewaan harian
- `hour.csv` → data penyewaan per jam

Beberapa variabel yang dianalisis antara lain:
- `cnt` : total penyewaan sepeda
- `casual` : jumlah pengguna kasual
- `registered` : jumlah pengguna terdaftar
- `weathersit` : kondisi cuaca
- `season` : musim
- `workingday` : hari kerja atau hari libur/akhir pekan
- `hr` : jam

## Metodologi
Tahapan analisis yang dilakukan:
1. **Data Wrangling**
    - Memuat data dari file CSV
    - Mengubah tipe data tanggal
    - Memetakan nilai numerik menjadi label kategori
    - Membuat kategori jam sibuk (`Rush Hour`) dan non-sibuk

2. **Exploratory Data Analysis (EDA)**
    - Menganalisis pengaruh cuaca terhadap jumlah penyewaan
    - Membandingkan perilaku pengguna kasual dan terdaftar
    - Mengelompokkan data berdasarkan kategori yang relevan

3. **Visualisasi Data**
    - Membuat bar chart untuk membandingkan total penyewaan berdasarkan kondisi cuaca
    - Membuat grouped bar chart untuk membandingkan pengguna kasual vs terdaftar

4. **Analisis Lanjutan**
    - Menerapkan clustering K-Means untuk mengelompokkan jam berdasarkan tingkat permintaan penyewaan

## Hasil Analisis
### Pertanyaan 1
Pada jam sibuk di musim gugur tahun 2012, kondisi cuaca cerah atau partly cloudy menghasilkan total penyewaan tertinggi. Sebaliknya, saat cuaca semakin buruk seperti misty/cloudy dan light rain/snow, jumlah penyewaan cenderung menurun.

### Pertanyaan 2
Pengguna terdaftar mendominasi penggunaan sepeda pada hari kerja, sedangkan pengguna kasual memiliki proporsi yang lebih besar pada hari libur atau akhir pekan. Hal ini menunjukkan perbedaan pola penggunaan antara komuter rutin dan pengguna rekreasional.

## Kesimpulan
Secara umum, kondisi cuaca dan jenis hari memiliki pengaruh yang jelas terhadap pola penyewaan sepeda. Cuaca yang baik meningkatkan jumlah penyewaan, terutama pada jam sibuk. Di sisi lain, hari kerja lebih banyak digunakan oleh pelanggan terdaftar, sedangkan akhir pekan dan hari libur lebih banyak menarik pengguna kasual.

## Rekomendasi
1. Menyediakan armada lebih banyak saat cuaca cerah dan jam sibuk.
2. Menerapkan strategi promosi saat cuaca kurang mendukung untuk menjaga permintaan.
3. Memfokuskan layanan untuk pengguna terdaftar pada hari kerja.
4. Menawarkan program konversi dari pengguna kasual menjadi pengguna terdaftar pada akhir pekan atau hari libur.

## Tools yang Digunakan
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
  
## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd notebook
pipenv install
pipenv shell
pip install -r requirements.txt

## Run Streamlit App
cd dashboard
streamlit run dashboard.py

## Link Dashboard
https://aipun-bike-sharing-analysis.streamlit.app/
