import math

# Input panjang alas segitiga, tinggi segitiga, tinggi prisma
panjang_alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

# Hitung luas permukaan prisma segitiga
luas_permukaan = (2 * panjang_alas_segitiga * tinggi_segitiga) + (panjang_alas_segitiga * tinggi_prisma)

# Hitung volume prisma segitiga
volume = (panjang_alas_segitiga * tinggi_segitiga * tinggi_prisma) / 2

# Tampilkan hasil
print(f"Luas Permukaan Prisma Segitiga: {luas_permukaan:.2f}")
print(f"Volume Prisma Segitiga: {volume:.2f}")
