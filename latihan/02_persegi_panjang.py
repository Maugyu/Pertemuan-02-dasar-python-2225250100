# Input panjang dan lebar sebagai float
panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))

# Perhitungan luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil dengan dua angka desimal beserta satuan
print(f"Luas     : {luas:.2f} cm²")
print(f"Keliling : {keliling:.2f} cm")