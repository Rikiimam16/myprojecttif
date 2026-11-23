#Fungsi Persegi Panjang
print("PROGRAM LUAS PERSEGI PANJANG")
def luas_persegi_panjang(p = float(input("Masukkan Panjang : ")),l = float(input("Masukkan Lebar : "))):
    luas = p * l
    print("Luas Persegi panjang = ", luas)
luas_persegi_panjang()

#Fungsi Volume Balok
print("PROGRAM VOLUME BALOK")
def volume_balok(p = float(input("Masukkan Panjang : ")),l = float(input("Masukkan Lebar : ")), t = float(input("Masukkan Tinggi : "))):
    volume = p * l * t
    print(f"Volume balok : {volume}")
volume_balok()

#Fungsi Luas Lingkaran
print("PROGRAM LUAS LINGKARAN")
def luas_lingkaran(r = float(input("Masukkan jari jari : "))):
    if r % 7 == 0:
        phi = 22/7
    else:
        phi = 3.14
    luas = phi * (r **2)
    print(f"Luas lingkaran : {luas}")
luas_lingkaran()

#Volume Bola
print("PROGRAM VOLUME BOLA")
def volume_bola(r = float(input("Masukkan jari jari : "))):
    if r % 7 == 0:
        phi = 22/7
    else:
        phi = 3.14
    volume = 4/3 * phi * (r ** 3)
    print(f"Volume Bola : {volume}")
volume_bola()