#operasi logika atau boolean
#not. or, and, xor
print("LOGIKA DALAM PYTHON")
print("===NOT===")
#Jika kondisi aslinya True, maka diberi not akan menjadi False
a = True
b = not a
print("nilai b =", b)

print("===OR===")
#benar jika salah satu atau dua"nya benar
a = True
b = False
c = a or b
print(c)
a = False
b = False
c = a or b
print(c)

print("===AND===")
#benar jika dua"nya benar
a = True
b = True
c = a and b
print(c)
a = True
b = False
c = a and b
print(c)

print("===XOR===")
#benar jika salah satu benar, jika keduanya false atau true maka hasilnya false
a = True
b = False
c = a ^ b
print(c)
a = True
b = True
c = a ^ b
print(c)
print() #buat baris baru


print("PROGRAM LOGIKA DAN KOMPARASI")
#nilainya akan True jika < 3 atau > 10
inputUsers =  float(input("Masukkan angka : "))
isKurangDari = inputUsers < 3
isLebihDari = inputUsers > 10
Hasil = isKurangDari or isLebihDari
print("Apakah", inputUsers, "Nilainya < 3 atau > 10 ? =", Hasil) 

#nilainya akan True jika > 3 dan < 10
inputUsers =  float(input("Masukkan angka : "))
isKurangDari = inputUsers > 3
isLebihDari = inputUsers < 10 
Hasil = isKurangDari and isLebihDari
print("Apakah", inputUsers, "Nilainya > 3 dan < 10 ? =", Hasil)
print()

# If Else Statement
print("IF ELSE STATEMENT")
nama = input("Masukkan nama kamu : ")
# 1. If inline
if nama == "Rikz": print("Kamu ganteng abiezz")
# 2. If indentation
if nama == "Rikz":
    print("Kamu ganteng abiezz")
    print("Anjay kamu keren banget")
# 3. Else statement
if nama == "Rikz":
    print("Kamu ganteng abiezz")
else:
    print("Skip ah kamu bukan Rikz")
# 4. Elif Statement
if nama == "Rikz":
    print("Kamu ganteng abiezz") #kondisi 1
elif nama == "Riki":
    print("Anjay si paling keren") #kondisi 2
elif nama == "Imam":
    print("Ah kece banget lu") #kondisi 3
else:
    print("Skip ah ga kenal")
