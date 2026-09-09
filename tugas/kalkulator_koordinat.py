
# 1. Tampilkan judul program
print("KALKULATOR KOORDINAT DUA TITIK")

# 2. Baca input x1, y1, x2, y2 sebagai float
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

# 3. Hitung perubahan koordinat dx dan dy
dx = x2 - x1
dy = y2 - y1

# 4. Hitung jarak Euclidean menggunakan pemangkatan 0.5
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# 5. Hitung titik tengah
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

# 6. Tampilkan seluruh hasil menggunakan f-string dengan formatting 2 angka desimal
print(f"Titik A : ({x1:.2f}, {y1:.2f})")
print(f"Titik B : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B : {jarak:.2f}")
print(f"Titik tengah : ({mid_x:.2f}, {mid_y:.2f})")