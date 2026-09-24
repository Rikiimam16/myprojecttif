print("PROGRAM BILANGAN GANJIL GENAP")
angka = range(1,51)
for i in angka:
    if i % 2 == 0:
        print(f"angka {i} : bilangan genap")
    else:
        print(f"angka {i} : bilangan ganjil")

print("PROGRAM BILANGAN PRIMA")
for angka in range(1, 101):
    
    if angka > 1:
        cek_prima = True
    for i in range(2, angka):
        if angka % i == 0:
            cek_prima = False
            break
    if cek_prima:
        print(angka)