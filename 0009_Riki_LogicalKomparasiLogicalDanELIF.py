age = int(input("Masukkan Usia Anda : "))
if age >= 0 and age <= 12:
    print("Usia Anda :", age, ", Anda masih anak anak")
elif age > 12 and age  <= 17:
    print("Usia Anda :", age, ", Anda sudah memasuki masa remaja")
elif age > 17 and age <= 59:
    print("Usia Anda :", age, ", Anda sudah dewasa")
elif age > 59:
    print("Usia Anda :", age, ", Anda sudah memasuki masa lansia")
else:
    print("Usia tidak valid")