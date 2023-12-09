import math

# Input panjang alas, lebar alas, dan tinggi limas
panjang_alas = float(input("Masukkan panjang alas: "))
lebar_alas = float(input("Masukkan lebar alas: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Hitung luas permukaan limas segiempat
luas_permukaan = panjang_alas * lebar_alas + panjang_alas * math.sqrt((lebar_alas / 2) ** 2 + tinggi_limas ** 2) + lebar_alas * math.sqrt((panjang_alas / 2) ** 2 + tinggi_limas ** 2)

# Hitung volume limas segiempat
volume = (panjang_alas * lebar_alas * tinggi_limas) / 3

# Tampilkan hasil
print(f"Luas Permukaan Limas Segiempat: {luas_permukaan:.2f}")
print(f"Volume Limas Segiempat: {volume:.2f}")
