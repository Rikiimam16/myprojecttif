import datetime
import os
import random
import string

# Template sistem manajemen perpustakaan
buku_template = {
    'judul_buku': 'nama',
    'penulis': '00000000',
    'tahun_terbit': 0,
    'tanggal_terakhir_pinjam': datetime.datetime(2026, 12, 12),
    'status': 'TERSEDIA'
}

data_buku = {}

while True:
    os.system("cls")

    print("-" * 72)
    print(f"{'SELAMAT DATANG DI PERPUSTAKAAN':^72}")
    print(f"{'MASUKKAN DATA BUKU DIBAWAH INI':^72}")
    print("-" * 72)

    buku = dict.fromkeys(buku_template.keys())
    buku['judul_buku'] = input("JUDUL BUKU : ")
    buku['penulis'] = input("PENULIS : ")
    buku['tahun_terbit'] = int(input("TAHUN TERBIT : "))

    tgl_input = input("TANGGAL TERAKHIR PINJAM (DD/MM/YYYY) : ")
    buku['tanggal_terakhir_pinjam'] = datetime.datetime.strptime(
        tgl_input, "%d/%m/%Y"
    )

    buku['status'] = input("STATUS (TERSEDIA/TIDAK) : ").upper()

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_buku.update({KEY: buku})

    print(f"\n{'KEY':<8} {'JUDUL BUKU':<15} {'PENULIS':<12} {'TAHUN':<8} {'TGL PINJAM':<14} {'STATUS':<10}")
    print('-' * 72)

    for key_buku in data_buku:
        JUDUL_BUKU = data_buku[key_buku]['judul_buku']
        PENULIS = data_buku[key_buku]['penulis']
        TAHUN_TERBIT = data_buku[key_buku]['tahun_terbit']
        TANGGAL_TERAKHIR_PINJAM = data_buku[key_buku]['tanggal_terakhir_pinjam'].strftime("%d/%m/%Y")
        STATUS = data_buku[key_buku]['status']

        print(f"{key_buku:<8} {JUDUL_BUKU:<15} {PENULIS:<12} {TAHUN_TERBIT:<8} {TANGGAL_TERAKHIR_PINJAM:<14} {STATUS:<10}")

    print("\n")
    is_tambahlagi = input("TAMBAH DATA BUKU LAGI (Y/N)? : ").lower()

    if is_tambahlagi == "n":
        break