print("PERULANGAN FOR")
# for kondisi:
# aksi
#dengan list
angka2 = [0,1,2,3,4] # ini adalah list
for i in angka2:
    print(f"i sekarang → {i}") #print(f) -> kombinasi text dan variabel
print("akhiri dari program\n")

#dengan range
angka3 = range(5)
for i in angka3:
    print(f"i sekarang → {i}")
print("akhiri dari program\n")

# menggunakan string
data_str = "saya ganteng abiies"
for huruf in data_str:
    print(huruf)
print("akhiri dari program\n")

print("PERULANGAN WHILE")
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang → {angka}")
print("program berakhir")

print("CONTINUE, PASS, AND BREAK")
#continue
angka = 0
while angka < 5:
    angka = angka + 1
    if angka == 4:
        continue  # Melewati sisa kode di bawahnya khusus untuk angka 4
    print(f"angka sekarang → {angka}")

#pass → dia berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
while angka < 5:
    angka = angka + 1
    if(angka == 3):
        pass # ini tidak akan dieksekusi
    else:   
        print(angka)

# break
angka = 0
print(f"angka sekarang → {angka}")
while angka < 5:
    angka = angka + 1
    print(f"angka sekarang → {angka}") # aksi 1
    if(angka == 3):
        print("nice")
        break
    print("whasssup")
print("cukup mass")