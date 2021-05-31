# Username = admin
# Password = admin

import json
import datetime
# ini adalah mahakarya
# buka json
stokbarang = open('datastok.json','r')

#global variable
idb = []
hargab = []
jumlahb = []
namab = []
list_belanja = [namab,jumlahb]
totalpb = []


def struk():

    print("Lengkapi identitas dibawah")
    nama_pembeli = input("Masukkan nama pembeli : ")
    # Memilih Metode
    carabayar = input("""\nMetode Pembayaran
1. Online Payment
2. Bayar Ditempat (cash)
Pilih (1/2)\n >> """)
    hargatot = sum(totalpb)
    print('')
    print('=' * 15)
    print('KWITANSI APOTEK SUSAH SEHAT')
    print('=' * 15)    
    print('')
    print('Tgl\t:',datetime.datetime.now())
    print('Atas nama\t:', nama_pembeli)
    print('-' * 15)
    lst = len(jumlahb)
    i = 0
    print('Nama\tJumlah\tHarga\tTotal')
    while i < lst:
        print(f'{namab[i]}\t{jumlahb[i]}\t{hargab[i]}\t{hargab[i]*jumlahb[i]}')
        i += 1
    print('-' * 15)
    print('Harga Total\t:', hargatot)
    print(f"Keterangan\t:{'Lunas' if carabayar == '1' else 'Belum Dibayar'}")
#   pass
    i = 0
    n = len(idb)
    # update json setelah beli
    while i < n:
        bukaF = open('datastok.json','r')
        data = json.load(bukaF)
        temp = data['List']
        temp[idb[i]]["stok"] -= jumlahb[i]
        
        # write json
        bukaF = open('datastok.json','w+')
        bukaF.write(json.dumps(data,indent=2))
        bukaF.close()

        # limitting while
        i+=1

def cek_stok():
    with open('datastok.json') as f:
        data = json.load(f)
    i = 1
    for stok in data['List']:
        print(f"[{i}] {stok['nama']} \t: {stok['harga']} \t {stok['stok']}")
        i += 1

    tanya_beli = str(input('Apakah anda ingin membeli (y/n)'))
    if tanya_beli == 'y':
        beli_pembeli()
    elif tanya_beli == 'n':
        menu_pembeli()

def beli_pembeli():
    fjason = open('datastok.json','r')
    data = json.load(fjason)
    temp = data['List']
    for indeks in range(len(temp)):
        print("[%d] %s %s %s" % (indeks,temp[indeks]['nama'],temp[indeks]['harga'],temp[indeks]['stok']))
    idbeli = int(input('Masukkan ID barang yang mau dibeli >> '))
    jumlahbeli = int(input('Masukkan jumlah barang yang mau dibeli >> '))
    
    idb.append(idbeli)
    hargab.append(temp[idbeli]['harga'])
    jumlahb.append(jumlahbeli)
    namab.append(temp[idbeli]['nama'])
    totalpb.append(temp[idbeli]['harga']*jumlahbeli)

    if jumlahbeli > temp[idbeli]['stok']:
        print('Anda membeli terlalu banyak, mohon dikurangi !!! ')
        idb.pop()
        hargab.pop()
        jumlahb.pop()
        namab.pop()
        totalpb.pop()
        beli_pembeli()
    elif jumlahbeli <= temp[idbeli]['stok']:
        beli_lg = input("Apakah ingin membeli obat lain? (y/n): ")
        if beli_lg == 'y':
            beli_pembeli()
        elif beli_lg =='n':
            struk()

def konsultasi():
    #keluhan keluhan asyik
    keluhan=["1. susah bab",
            "2. pusing kepala",
            "3. suhu badan tinggi",
            "4. gigi bengkak",
            "5. terasa nyeri otot",
            "6. bisul",
            "7. gampang lelah",
            "8. sariawan",
            "9. mata kerasa perih \n"]

    #menunjukkan keluhan ke pembeli
    for keluh in keluhan :
        print(keluh)

    tanya= (input('Apakah keluhan anda ada dalam daftar ?(Y/N)\n:'))
    if tanya == 'Y':
        #menanyakan apakah keluhan 
        keluhan_yang_kamurasain = int(input('Masukkan keluhan penyakit yang anda rasakan (1/2/3/4/5/6/7/8/9) \n:'))
        if keluhan_yang_kamurasain == 1:
            print("\nObat yang sesuai dengan keluhan Anda adalah Microlax Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 2:
            print("\nObat yang sesuai dengan keluhan Anda adalah Paracetamol Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 3:
            print("\nObat yang sesuai dengan keluhan Anda adalah Ibuprofen Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 4:
            print("\nObat yang sesuai dengan keluhan Anda adalah Amoxcicilin Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 5:
            print("\nObat yang sesuai dengan keluhan Anda adalah  Kortikosteroid Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 6:
            print("\nObat yang sesuai dengan keluhan Anda adalah Penisilin Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 7:
            print("\nObat yang sesuai dengan keluhan Anda adalah Neurobion Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 8:
            print("\nObat yang sesuai dengan keluhan Anda adalah Gentian Violet Apotek kami obat untuk keluhan penyakit anda tersebut")
        elif keluhan_yang_kamurasain == 9:
            print("\nObat yang sesuai dengan keluhan Anda adalah Insto Apotek kami obat untuk keluhan penyakit anda tersebut")
        else:
            pass
    elif tanya == 'N':
        print("\nMohon maaf, apotek kami belum bisa melayani keluhan penyakit tersebut\nkami sangat menyarankan untuk menghubungi nomor rumah sakit yang sesuai dengan kota anda, berikut adalah nomor rumah sakit di setiap provinsi :\n ")
        list_rs=[
        'RSUP dr Kariadi, Semarang.Telepon: (024) 8413476',
        'RSUD KRMT Wongsonegoro, Kota Semarang.Telepon: (024) 6711500',
        'RSUD Tugurejo, Semarang.Telepon: (024) 7605297',
        'RSU Sultan Agung, Semarang.Telepon: (024) 6580019',
        'RSU St Elizabeth, Semarang.Telepon: (024) 8310035',
        'RSU Telogorejo, Semarang.Telepon: (024) 86466000', 
        'RSU Columbia Asia, Semarang.Telepon: (024) 7629999',
        'RSU Tk III Bhakti Wira Tamtama, Kota Semarang.Telepon: (024) 3555944',
        'RSU Bhayangkara, Semarang.Telepon: (024) 6720675',
        'RSUD Salatiga.Telepon: (0298) 324074',
        'RS Paru Dr Ario Wirawan, Salatiga.Telepon: (0298) 326130',
        'RSU Tk IV 04.07.03 dr Asmir, SalatigaTelepon: (0298) 326045',
        'RSUD Dr H Soewondo, Kendal.Telepon: (0294) 381433',
        'RSUD Ambarawa Telepon: (0298)591020',
        'RSUD Sunan Kalijaga Demak Telepon:(0291)685018',
        'RSUD dr R Soedjati, Grobogan.Telepon:(0292) 421004']
        for rs in list_rs:
            print(rs)

def menu_pembeli():
    print('SELAMAT DATANG DI APOTEK SUSET')
    choice = int((input('''
    Selamat datang, pelanggan:
    [1] Cek Stok
    [2] Beli stok
    [3] Konsultasi
    [4] Keluar
    >> ''')))

    if choice == 1:
        cek_stok()
    elif choice == 2:
        beli_pembeli()
    elif choice == 3:
        konsultasi()
    elif choice == 4:
        show_menu()
    else:
        print('Masukkan ulang pilihan')
        menu_pembeli()

def penjual_stok():
    with open('datastok.json') as f:
        data = json.load(f)
    i = 1
    for stok in data['List']:
        print(f"[{i}] {stok['nama']} : {stok['harga']}")
        i += 1
    menu_penjual()

    # pass

def tambah_stok_baru():
    print('SELAMAT DATANG DI APOTEK SUSET')
    print('Berikut stok barang yang tersedia')
    fjason = open('datastok.json', 'r')
    data = json.load(fjason)
    temp = data['List']
    for indeks in range(len(temp)):
        print("[%d] %s" % (indeks, temp[indeks]['nama']))
    n = int((input('Masukkan jumlah barang yang akan ditambahkan >> ')))
    i = 0
    while i < n:
        fjason = open('datastok.json','r')
        data = json.load(fjason)
        fjason.close()
        temp = data['List']
        a = input('Nama Barang >>')
        b = int(input('Harga Barang >> '))
        c = int(input('Jumlah stok >> '))
        y = {"nama": a,"harga": b, "stok":c}
        temp.append(y)

        fjason = open('datastok.json','w+')
        fjason.write(json.dumps(data, indent=2))
        fjason.close()
        i += 1
    else:
        print('Data sudah ter-update !!!')
        menu_penjual()
    # pass

def kurangi_stok():
    ## space buat ngisi ##
    print('SELAMAT DATANG DI APOTEK SUSET')
    fjason = open('datastok.json','r')
    data = json.load(fjason)
    temp = data['List']
    for indeks in range(len(temp)):
        print("[%d] %s" % (indeks,temp[indeks]['nama']))
    hapus = int(input('Masukkan ID barang yang mau dihapus >> '))
    temp.pop(hapus)
    fjason = open('datastok.json','w+')
    fjason.write(json.dumps(data, indent=2))
    fjason.close()
    menu_penjual()
    # pass

def menu_penjual():
    print('SELAMAT DATANG DI APOTEK SUSET')
    choice = int((input('''
    Selamat datang, admin:
    [1] Cek Stok
    [2] Tambah stok
    [3] Kurangi stok
    [4] Keluar
    >> ''')))

    if choice == 1:
        penjual_stok()
    elif choice == 2:
        tambah_stok_baru()
    elif choice == 3:
        kurangi_stok()
    elif choice == 4:
        show_menu()
    else:
        print('Masukkan ulang pilihan')
    # pass

def login_penjual():
    admindata = {"admin":{"pw":"admin"}}
    username = input('Masukkan Username >> ')
    if username in admindata:
        password = input('Masukkan Password >> ')
        if password == admindata['admin']['pw']:
            print('Login Berhasil')
            menu_penjual()
        else:
            print('Password salah !!!')
    else:
        print('Username Salah !!!')
    # pass

def show_menu():
    print('SELAMAT DATANG DI APOTEK SUSET')
    choice = int((input('''
    Anda Masuk Sebagai:
    [1] Penjual
    [2] Pembeli
    [3] Keluar
    >> ''')))

    if choice == 1:
        login_penjual()
    elif choice == 2:
        menu_pembeli()
    elif choice == 3:
        exit()
    else:
        print('Masukkan ulang pilihan')

show_menu()

if '__name__' == '__main__':
    while True:
        show_menu()
