import math

# Input jari-jari dan tinggi tabung
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

# Hitung luas permukaan tabung
luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Hitung volume tabung
volume = math.pi * jari_jari ** 2 * tinggi

# Tampilkan hasil
print(f"Luas Permukaan Tabung: {luas_permukaan:.2f}")
print(f"Volume Tabung: {volume:.2f}")
