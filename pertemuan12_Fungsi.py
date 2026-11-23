#Fungi paling simple
def hello_world():
    print("Halo, Selamat Pagi Semua")
hello_world()
#Fungsi dengan argumen
# def nama_fungsi(argumen):
    # badan fungsi
    # return output
def sapa_orang(siapa, pesan):
    print(f"Hello {siapa}, aku mau titip {pesan}")
sapa_orang("Pak Agus", "Bakso")

#Fungsi dengan return
# def nama_fungsi(argumen):
#     badan fungsi
#     return output
def tambah(x,y):
    hasil = x + y
    return hasil
akhir = tambah(3,7)
print("Hasil Pertambahan :", akhir)
# Default argument
# def fungsi(argument):
# def fungsi(argument = nilai default):
def halo(nama = "Rikz", pesan = "Apa kabar, masih inget ga?"):
    print(f"Halo {nama}, {pesan}")
halo()