#1. Tuple
#a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama","NIM", "Prodi").
mahasiswa = ("M. Riki", "2605060009", "Teknologi Informasi")
#b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya
print(mahasiswa[1], mahasiswa[2])
#c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi
mahasiswa[2] = "Teknologi Informasi"
#Tuple memiliki sifat immutable (tidak dapat diubah), jadi tuple tidak dapat diubah, dihapus, atau ditambahkan data di dalam elemennya. Makanya, kode di atas akan error ketika dijalankan.
#d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali!
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)
#Set memiliki ciri tidak ada duplikasi, jadi ketika kita membuat nilainya 2 kali atau lebih, ketika di-print maka yang tercetak hanya 1 karena ciri yang dimiliki oleh tipe data set.

#2. Manipulasi Dictionary
#a. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut:
data_mahasiswa = { 
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi",
}
#b. Ubah nilai "prodi" menjadi "Sastra Mesin " sekaligus menambahkan key baru "angkatan" dengan nilai 2026.
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026
#c. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar.
del data_mahasiswa["nim"]
print(data_mahasiswa)

#3. Perulangan pada Dictionary
#a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
keranjang = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000
}
#b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000"
for key, value in keranjang.items() :
    print(f"Harga {key}: Rp {value}")
#c. Tampilkan total belanja
total_belanja = 0
for value in keranjang.values() :
    total_belanja = total_belanja + value
print(f"Total Belanja : Rp {total_belanja}")