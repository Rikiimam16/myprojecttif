#1. Diberikan list berikut:
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
#a. Tambahkan 'truk' di akhir list
kendaraan.append("truk")
print(kendaraan)
#b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, "becak")
print(kendaraan)
#c. Hapus data yang berada paling belakang dari list tersebut.
kendaraan.pop()
print(kendaraan)
#d. Ubah elemen 'sepeda' menjadi 'skuter'.
kendaraan[3] = "skuter"
print(kendaraan)
#e. Tampilkan informasi jumlah total data di dalam list tersebut
jumlah_kendaraan = len(kendaraan)
print(f"jumlah kendaraan : {jumlah_kendaraan}")

#2. Diberikan list berikut:
angka = [75, 80, 90, 75, 85, 100, 65]
#a. Cari tahu di indeks ke berapa skor 100 berada.
seratus = angka.index(100)
print(f"skor 100 berada di indeks {seratus}")
#b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
skor_75 = angka.count(75)
print(f"Banyak siswa yang mendapat skor 75 : {skor_75}")
#c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar
angka.sort()
print(f"Urutan skor : {angka}")
#d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil
angka.reverse()
print(f"Urutan skor terbalik : {angka}")

#3. Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
menu_utama.extend(menu_tambahan)
print(menu_utama)

#4. Diberikan data nested list berupa informasi nama barang dan harganya:
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
#a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.
harga_pensil = data_barang[1][1]
print(f"Harga pensil : {harga_pensil}")
#b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya.
for data in data_barang:
    print(f"Nama : {data[0]}, Harga : {data[1]}")