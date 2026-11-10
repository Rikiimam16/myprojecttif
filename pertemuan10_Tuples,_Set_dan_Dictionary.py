#Tuple
# ciri ciri : tidak dapat diubah elemennya (immutable)
data_tuples = (7,8,10,11)
print(data_tuples)
print(data_tuples[1])

# sets (himpunan)
# ciri : unordered/tidak diberi indeks, tidak dapat diduplikasi elemennya
data_sets = {10,4,3,2,7,6,5}
print(data_sets)

#Dictionary
data_mahasiswa = {
    "nama" : "Siti",
    "umur" : 12,
    "JK" : "Pria",
    "BB" : 30,
    "TB" : 90,
}
print(data_mahasiswa)
#Operasi Dictionary
#len = panjang dictionary
print(len(data_mahasiswa))
#Mengecek Key
KEY = "nama"
CHECKKEY = KEY in data_mahasiswa
print(f"Apakah ada {KEY} di data_mahasiswa? = {CHECKKEY}")
#Mengupdate Data / Menambah Data
data_mahasiswa["nama"] = "Rikz"
data_mahasiswa.update({"Bio" : "OhMyRikz"})
#Menghapus Data
del data_mahasiswa["nama"]
#Looping Dictionary
data_mahasiswa = {
    "nama" : "Rikz",
    "umur" : 12,
    "JK" : "Pria",
    "BB" : 30,
    "TB" : 90,
}
#Looping Key saja
for mahasiswa in data_mahasiswa:
    print(mahasiswa)
#Looping Value saja
for mahasiswa in data_mahasiswa.values():
    print(mahasiswa)
#Looping dengan key dan juga value
for key, value in data_mahasiswa.items():
    print(key, ":", value)