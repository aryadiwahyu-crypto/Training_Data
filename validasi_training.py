import pandas as pd

INPUT_FILE = "training_data.csv"
OUTPUT_FILE = "training_data_clean.csv"

# Baca data
df = pd.read_csv(INPUT_FILE)

# Normalisasi format tanggal agar seragam YYYY-MM-DD
if 'Tanggal_Pelatihan' in df.columns:
    df['Tanggal_Pelatihan'] = pd.to_datetime(df['Tanggal_Pelatihan'], errors='coerce').dt.date

# Bersihkan spasi berlebih pada kolom penting
kolom_bersih = ['Valid_Pelatihan', 'Nama', 'Departemen', 'Jabatan', 'Judul_Pelatihan']
for col in kolom_bersih:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Simpan file hasil pembersihan
df.to_csv(OUTPUT_FILE, index=False)

print("Selesai! File bersih tersimpan sebagai:", OUTPUT_FILE)
