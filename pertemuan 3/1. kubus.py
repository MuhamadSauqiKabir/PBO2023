import tkinter as tk

# Fungsi untuk menghitung luas permukaan dan volume kubus
def hitung_luas_dan_volume():
    try:
        sisi = float(sisi_entry.get())

        luas_permukaan = 6 * (sisi ** 2)
        volume = sisi ** 3

        luas_label.config(text=f"Luas Permukaan: {luas_permukaan}")
        volume_label.config(text=f"Volume: {volume}")
    except ValueError:
        luas_label.config(text="Masukkan angka valid untuk sisi kubus.")
        volume_label.config(text="")

# Membuat jendela utama
window = tk.Tk()
window.title("Kalkulator Luas Permukaan dan Volume Kubus")

# Label dan Entry untuk sisi kubus
sisi_label = tk.Label(window, text="Sisi Kubus:")
sisi_label.pack()
sisi_entry = tk.Entry(window)
sisi_entry.pack()

# Tombol "Hitung"
hitung_button = tk.Button(window, text="Hitung", command=hitung_luas_dan_volume)
hitung_button.pack()

# Label untuk hasil perhitungan
luas_label = tk.Label(window, text="")
luas_label.pack()
volume_label = tk.Label(window, text="")
volume_label.pack()

# Menjalankan aplikasi
window.mainloop()
