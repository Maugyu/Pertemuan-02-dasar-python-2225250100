# Konstanta
TAHUN_SEKARANG = 2026

# Input data dari pengguna
nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

# Perhitungan umur
umur = TAHUN_SEKARANG - tahun_lahir

# Menampilkan kartu biodata terformat
print("\n" + "="*30)
print(f"Nama  : {nama}")
print(f"NIM   : {nim}")
print(f"Kelas : {kelas}")
print(f"Umur  : sekitar {umur} tahun")
print("="*30)