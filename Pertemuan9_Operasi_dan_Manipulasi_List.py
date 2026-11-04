# --- LIST ---
# Kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)
# Kumpulan data_string
data_string = ["ucup","adit","siti"]
print(data_string)
# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)
# Kumpulan campuran
data_campuran = [1,"bakwan",2,"cireng","ucup",True,"adit",False]
print(data_campuran)
#Membuat list dengan range
data_range = list(range(0,12,2)) # range(start,stop,step)
print(data_range)
#Membuat list dengan for
list_for = [i **2 for i in range(0,10)]
print(list_for)
# membuat list pake for pake if
list_for_if = [i for i in range(0,10) if i !=2]
print(list_for_if)


#manipulasi
# mengambil data dari list
data = ["bambang", "ucup", "asep"]
print(data[0])

#mengambil info jumlah data dalam list 
data = ["bambang", "ucup", "asep"]
banyak_data = len(data)
print(banyak_data)

#insert(posisi, item)
data = ["bambang", "ucup", "asep"]
data.insert(1, "Joko")
print(data)

# menambah di akhir list 
data = ["bambang", "ucup", "asep"]
data.append("Rikz")
print(data)

# menambahkan list dengan list 
data = ["bambang", "ucup", "asep"]
data.extend(["Luffy", "Nami", "Zoro"])
print(data)

# merubah data
#ubah data 2 jadi jarwo
data = ["bambang", "ucup", "asep"]
data[2] = "Jarwo"
print(data)

# menghapus data
data = ["bambang", "ucup", "asep"]
data.remove("ucup")
print(data)

# menghapus data paling belakang
data = ["bambang", "ucup", "asep"]
data.pop()
print(data)

#====== OPERASI LIST =====
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
#count = mengetahui jumlah suatu nilai pada data
jumlah_data_4 = data_angka.count(4)
print(f"jumlah angka 4 : {jumlah_data_4}")
#index = ambil posisi data
data = ["Rendi","Iqbal","Gana","Khairil"]
print(data.index("Gana"))
# sort = mengurutkan data
data_angka.sort()
print(data_angka)
# reverse = membalikkan urutan
data_angka.reverse()
print(data_angka)

# Nested List
#contoh pertama
data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")
list_2D = [data_0, data_1, 6,7] 
print(f"list 2D = {list_2D}")
#contoh kedua
#contoh penggunaan 
peserta_0 = ["Rendi", 25, "Laki-laki"]
peserta_1 = ["Joni", 10, "Laki-laki"] 
peserta_2 = ["Eka", 50, "Wanita"] 
list_peserta = [peserta_0, peserta_1, peserta_2] 
print(f"peserta = {list_peserta}") 
for peserta in list_peserta: 
    print(f"nama\t : {peserta[0]}") 
    print(f"umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}")