#Operasi Matematika
print("OPERASI ARITMATIKA")
a = 10
b = 4

#penjumlahan (+)
hasil = a + b
print("hasil", a , "+", b, "=", hasil)
#pengurangan (-)
hasil = a - b
print("hasil", a , "-", b, "=", hasil)
#perkalian (*)
hasil = a * b
print("hasil", a , "x", b, "=", hasil)
#pembagian
hasil = a / b
print("hasil", a , "/", b, "=", hasil)
#perpangkatan (**)
hasil = a ** b
print("hasil", a , "**", b, "=", hasil)
#modulus (%)
hasil = a % b
print("hasil", a , "%", b, "=", hasil)
#floor division
hasil = a // b
print("hasil", a, "//", b, "=", hasil)

# latihan konversi satuan temperature
# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah", celcius, "Celcius")
#konversi celcius ke reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")
#konversi celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")
#konversi celcius ke kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")
print() #Buat baris baru

print("OPERASI KOMPARASI")
#Operasi komperasi di python ada 8, diantaranya >,<,>=,<=,==,!=,is,is not
#Setiap hasil dari operasi komperasi adalah boolean
a = 8
b = 7
#lebih besar dari (>)
hasil = a > b
print(a, ">", b, "=", hasil)
hasil = b > a
print(b, ">", a, "=", hasil)
#lebih kecil dari (<)
hasil = a < b
print(a, "<", b, "=", hasil)
hasil = b < a
print(b, "<", a, "=", hasil)
#lebih besar atau sama dengan (>=)
hasil = a >= 8
print(a, ">=", 8, "=", hasil)
hasil = a >= 9
print(a, ">=", 9, "=", hasil)
#lebih kecil atau sama dengan (<=)
hasil = a <= b
print(a, "<=", b, "=", hasil)
hasil = a <= 9
print(a, "<=", 9, "=", hasil)
#sama dengan (==)
hasil = a == b
print(a, "==", b, "=", hasil)
hasil = b == 7
print(b, "==", 7, "=", hasil)
#tidak sama dengan (!=)
hasil = a != b
print(a, "!=", b, "=", hasil)
hasil = a != 8
print(a, "!=", 8, "=", hasil)