#Nama : M. Riki Imamuddin
#NPM : 2605060009
#Kelas : Rombel 1
#Tugas : Literal Data

#1. Berikut ini adalah daftar nama variabel beserta tipe data dan nilainya:
nama = "M. Riki Imamuddin"
umur = 18
berat = 59.9
print("Nama :", nama)
print("Umur :", umur, "tahun")
print("Berat:", berat, "Kg")

print("\n")
#2. Ubah tipe data berikut
angka_string = "123"
angka_float = 45.67
angka_integer = 89
# 1. Konversi angka_string menjadi integer
angka_integer1 = int(angka_string)
print(type(angka_integer1))
print(angka_integer1)
# 2. Konversi angka_float menjadi integer
angka_integer2 = int(angka_float)
print(type(angka_integer2))
print(angka_integer2)
# 3. Konversi angka_integer menjadi float
angka_float = float(angka_integer)
print(type(angka_float))
print(angka_float)
# 4. Konversi angka_integer menjadi string
angka_string = str(angka_integer)
print(type(angka_string))
print(angka_string)

print("\n")
#3. Buat program yang:
usia = int(input("Masukkan usia Anda: "))
tinggi_badan = float(input("Masukkan tinggi badan Anda: "))
nama = input("Masukkan nama Anda: ")
print("Nama Anda adalah", nama, "dan Anda berusia", usia, "tahun dengan tinggi badan", tinggi_badan, "cm.")