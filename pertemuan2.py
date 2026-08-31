print("MEMBUAT VARIABLE")
name = "Rikz"
print(name)

x = 10
y = 12
z = x + y #perhitungan ada 4, diantaranya tambah (+), kurang (-), kali (*), bagi (/) 
print(z)
print() #Buat baris baru

print("MENGENAL TIPE DATA")
#Kita gunakan type(datanya) untuk identifikasi tipe data
# tipe data: kumpulan karakter (string)
message = "Halo, nama saya Rikz"
print(message)
print(type(message))
#tipe data: Angka satuan yang gak ada komanya (integer)
age = 18
print(age)
print(type(age))
# tipe data: Angka dengan koma (float)
height = 161.5
print(height)
print(type(height))
# tipe data: biner true/false (boolean)
is_student = True
print(is_student)
print(type(is_student))
print() #Buat baris baru

print("KONVERSI TIPE DATA")
# STRING ke Tipe data lain
data_str = "10"
data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print("data : ", data_int, ",bertipe : ", type(data_int))
print("data : ", data_float, ",bertipe : ", type(data_float))
print("data : ", data_bool, ",bertipe : ", type(data_bool))
print()
# INTEGER ke Tipe data lain
data_int = 9
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) 
print("data : ", data_float, ",bertipe : ", type(data_float))
print("data : ", data_str, ",bertipe : ", type(data_str))
print("data : ", data_bool, ",bertipe : ", type(data_bool))
print()
# FLOAT ke Tipe data lain
data_float = -9.3
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) 
print("data : ", data_int, ",bertipe : ", type(data_int))
print("data : ", data_str, ",bertipe : ", type(data_str))
print("data : ", data_bool, ",bertipe : ", type(data_bool))
print()
# BOOLEAN ke Tipe data lain
data_bool = True
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data :", data_int, ", bertipe :", type(data_int))
print("data :", data_float, ", bertipe :", type(data_float))
print("data :", data_str, ", bertipe :", type(data_str))
print() #Buat baris baru

print("MENGAMBIL INPUT DATA USER")
nama = input("Masukkan nama anda : ")
print("Nama anda adalah :", nama)

x = int(input("angka pertama : "))
y = int(input("angka kedua : "))
print("Hasil :", x + y)