panjang = 12
lebar = 5
tinggi = 8

#a. Hitunglah luas, volume dan keliling dari bangunan tersebut!
luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar *tinggi)) #hitung luas
print("Luas bangunan tersebut adalah :", luas)
volume = panjang * lebar * tinggi #hitung volume
print("volume bangunan tersebut adalah :", volume)
keliling = 4 * (panjang + lebar + tinggi) #hitung keliling
print("keliling bangunan tersebut adalah :", keliling)

#b. Apakah luas bangunan tersebut lebih luas dari 50?
isLuas = luas > 50
print(luas, ">", 50, "=", isLuas)
#c. Apakah volume tersebut bernilai 480?
isVolume = volume == 480
print(volume, "==", 480, "=", isVolume)