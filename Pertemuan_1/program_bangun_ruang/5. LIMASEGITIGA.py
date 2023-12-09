import math

# Input panjang alas segitiga, tinggi segitiga, dan tinggi limas
panjang_alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Hitung luas permukaan limas segitiga
luas_permukaan = panjang_alas_segitiga ** 2 + 3 * (panjang_alas_segitiga * math.sqrt((panjang_alas_segitiga / 2) ** 2 + tinggi_segitiga ** 2))

# Hitung volume limas segitiga
volume = (panjang_alas_segitiga ** 2 * tinggi_limas) / 6

# Tampilkan hasil
print(f"Luas Permukaan Limas Segitiga: {luas_permukaan:.2f}")
print(f"Volume Limas Segitiga: {volume:.2f}")
