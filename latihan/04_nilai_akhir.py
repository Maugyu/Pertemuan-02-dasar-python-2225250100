# Input data nama dan nilai
nama = input("Nama mahasiswa: ")
nilai_tugas = float(input("Nilai Tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

# Perhitungan nilai akhir berdasarkan bobot (20%, 30%, 50%)
nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.30) + (nilai_uas * 0.50)

# Menampilkan hasil
print("\n" + "="*30)
print(f"Nama        : {nama}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")
print("="*30)