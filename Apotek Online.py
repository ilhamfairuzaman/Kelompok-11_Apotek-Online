# Username = admin
# Password = admin

import json
import datetime

# buka json
stokbarang = open('datastok.json','r')

#global variable
idb = []
hargab = []
jumlahb = []
namab = []
list_belanja = [namab,jumlahb]
totalpb = []
bayar = []

def struk():
    print('')
    print('=' * 30)
    print('SELAMAT DATANG DI APOTEK SUSET')
    print('=' * 30) 
    print("Lengkapi identitas dibawah")
    nama_pembeli = input("Masukkan nama pembeli : ")
    bayar = int(input("Berapa uang anda: "))

    # Memilih Metode
    carabayar = input("""\nMetode Pembayaran
1. Online Payment
2. Bayar Ditempat (cash)
Pilih (1/2)\n >> """)
    hargatot = sum(totalpb)

    # UI Nota
    print('')
    print('=' * 30)
    x = 'NOTA PEMBAYARAN APOTEK SUSET'
    print(x.center(30))
    print('=' * 30)    
    print('')
    print('Tanggal\t\t:',datetime.datetime.now())
    print('Atas nama\t:', nama_pembeli)
    print('-' * 15)
    lst = len(jumlahb)
    i = 0
    print('Nama\t\tJumlah\tHarga\tTotal')
    while i < lst:
        print(f'{namab[i]}\t{jumlahb[i]}\t{hargab[i]}\t{hargab[i]*jumlahb[i]}')
        i += 1
    print('-' * 15)
    print('Harga Total\t:', hargatot)
    print(f"Keterangan\t: {'Lunas' if carabayar == '1' else 'Belum Dibayar'}")
    print('')
    print('=' * 30)
    print('uang anda\t: ', bayar)
    kembalian = int(bayar-hargatot)
    print('kembalian anda\t: ', kembalian)
    x = 'MOHON UNTUK MEMBAWA NOTA SAAT MELAKUKAN PENGAMBILAN OBAT'
    print(x.center(30))
    print('=' * 30)

    #tanya
    tanya_habisbeli = input("Apakah ingin membeli lagi?(y/n): ")
    if tanya_habisbeli == "y":
        beli_pembeli()
    elif tanya_habisbeli == "n":
        menu_pembeli()
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
    print('')
    print('=' * 30)
    print('STOK YANG TERSEDIA APOTEK SUSET')
    print('=' * 30)  
    with open('datastok.json') as f:
        data = json.load(f)
    i = 1

    # Showing stok
    for stok in data['List']:
        print(f"[{i}] {stok['nama']} \t: {stok['harga']} \t{stok['stok']}")
        i += 1

    # Tanya
    tanya_beli = str(input('Apakah anda ingin membeli (y/n) >> '))
    if tanya_beli == 'y':
        beli_pembeli()
    elif tanya_beli == 'n':
        menu_pembeli()

def beli_pembeli():
    print('')
    print('=' * 30)
    print('SELAMAT DATANG DI APOTEK SUSET')
    print('=' * 30) 
    fjason = open('datastok.json','r')
    data = json.load(fjason)
    temp = data['List']

    #Showing stok
    for indeks in range(len(temp)):
        print("[%d] %s %s %s" % (indeks,temp[indeks]['nama'],temp[indeks]['harga'],temp[indeks]['stok']))

    # Inputting    
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

    tanya= (input('Apakah keluhan anda ada dalam daftar ?(Y/N)\n: '))
    if tanya == 'Y':
        #menanyakan apakah keluhan 
        keluhan_yang_kamurasain = int(input('Masukkan keluhan penyakit yang anda rasakan (1/2/3/4/5/6/7/8/9) \n:'))
        if keluhan_yang_kamurasain == 1:
            print("\nObat yang sesuai dengan keluhan Anda adalah Microlax")
        elif keluhan_yang_kamurasain == 2:
            print("\nObat yang sesuai dengan keluhan Anda adalah Paracetamol")
        elif keluhan_yang_kamurasain == 3:
            print("\nObat yang sesuai dengan keluhan Anda adalah Ibuprofen")
        elif keluhan_yang_kamurasain == 4:
            print("\nObat yang sesuai dengan keluhan Anda adalah Amoxcicilin")
        elif keluhan_yang_kamurasain == 5:
            print("\nObat yang sesuai dengan keluhan Anda adalah Kortikosteroid")
        elif keluhan_yang_kamurasain == 6:
            print("\nObat yang sesuai dengan keluhan Anda adalah Penisilin")
        elif keluhan_yang_kamurasain == 7:
            print("\nObat yang sesuai dengan keluhan Anda adalah Neurobion")
        elif keluhan_yang_kamurasain == 8:
            print("\nObat yang sesuai dengan keluhan Anda adalah Gentian Violet")
        elif keluhan_yang_kamurasain == 9:
            print("\nObat yang sesuai dengan keluhan Anda adalah Insto")
        else:
            print('Mohon ulangi masukan')
            konsultasi()
        tanya = input('Apakah anda ingin membeli obatnya? (y/n) >> ')
        if tanya == 'y':
            beli_pembeli()
        elif tanya =='n':
            menu_pembeli()
    elif tanya == 'N':
        print("\nMohon maaf, apotek kami belum bisa melayani keluhan penyakit tersebut\nkami sangat menyarankan untuk menghubungi nomor rumah sakit yang sesuai dengan kota anda, berikut adalah nomor rumah sakit di setiap provinsi :\n ")
        list_rs=[
        'RSUP dr Kariadi, Semarang.Telepon: (024) 8413476',
        'RSUD KRMT Wongsonegoro, Kota Semarang. Telepon: (024) 6711500',
        'RSUD Tugurejo, Semarang. Telepon: (024) 7605297',
        'RSU Sultan Agung, Semarang.T elepon: (024) 6580019',
        'RSU St Elizabeth, Semarang. Telepon: (024) 8310035',
        'RSU Telogorejo, Semarang. Telepon: (024) 86466000', 
        'RSU Columbia Asia, Semarang. Telepon: (024) 7629999',
        'RSU Tk III Bhakti Wira Tamtama, Kota Semarang. Telepon: (024) 3555944',
        'RSU Bhayangkara, Semarang. Telepon: (024) 6720675',
        'RSUD Salatiga. Telepon: (0298) 324074',
        'RS Paru Dr Ario Wirawan, Salatiga. Telepon: (0298) 326130',
        'RSU Tk IV 04.07.03 dr Asmir, Salatiga. Telepon: (0298) 326045',
        'RSUD Dr H Soewondo, Kendal.Telepon: (0294) 381433',
        'RSUD Ambarawa Telepon: (0298)591020',
        'RSUD Sunan Kalijaga Demak. Telepon:(0291)685018',
        'RSUD dr R Soedjati, Grobogan.Telepon:(0292) 421004']
        for rs in list_rs:
            print(rs)

def menu_pembeli():
    print('')
    print('=' * 30)
    print('SELAMAT DATANG DI APOTEK SUSET')
    print('=' * 30)
    choice = int((input('''
    Selamat datang, pelanggan:
[1] Cek Stok
[2] Beli stok
[3] Konsultasi
[4] Kembali ke menu utama
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
    print('')
    print('=' * 30)
    print('STOK YANG TERSEDIA APOTEK SUSET')
    print('=' * 30)  
    with open('datastok.json') as f:
        data = json.load(f)
    i = 1

    # Showing stok 
    for stok in data['List']:
        print(f"[{i}] {stok['nama']} : {stok['harga']} : {stok['stok']}")
        i += 1
    menu_penjual()

    # pass

def tambah_stok_baru():
    print('')
    print('=' * 30)
    print('MENAMBAH STOK APOTEK SUSET')
    print('=' * 30)
    print('Berikut stok barang yang tersedia')
    fjason = open('datastok.json', 'r')
    data = json.load(fjason)
    temp = data['List']

    # Showing stok
    for indeks in range(len(temp)):
        print("[%d] %s %s" % (indeks, temp[indeks]['nama'], temp[indeks]['stok']))

    # Tanya    
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

def tambah_stok_lama():
    print('')
    print('=' * 30)
    print('MENAMBAH STOK APOTEK SUSET')
    print('=' * 30)
    print('Berikut stok barang yang tersedia')
    fjason = open('datastok.json', 'r')
    data = json.load(fjason)
    temp = data['List']
    for indeks in range(len(temp)):
        print("[%d] %s : %s" % (indeks, temp[indeks]['nama'], temp[indeks]['stok']))

    # input
    n = int(input('Masukkan ID barang yang ingin ditambah >> '))
    m = int(input('Masukkan jumlah barang baru >> '))

    # Edit  json
    temp[n]["stok"] = temp[n]["stok"] + m
    jsonFile = open("datastok.json","w+")
    jsonFile.write(json.dumps(data,indent=2))
    jsonFile.close()    

    # Menambah lagi ? 
    lagi = input('Apakah ingin menambah barang lain? [y/n] >> ')
    if lagi == 'y':
        tambah_stok_lama()
    else:
        print('Data sudah ter-update !!!')
        menu_penjual()

def kurangi_stok():
    ## space buat ngisi ##
    print('')
    print('=' * 30)
    print('MENGURANGI STOK APOTEK SUSET')
    print('=' * 30)
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
    print('')
    print('=' * 30)
    print('SELAMAT DATANG DI APOTEK SUSET')
    print('=' * 30)
    choice = int((input('''
    Selamat datang, admin:
[1] Cek Stok
[2] Tambah stok
[3] Kurangi stok
[4] Kembali ke menu utama
>> ''')))

    if choice == 1:
        penjual_stok()
    elif choice == 2:
        tanya = int(input('''Jenis stok yang ingin ditambah
        [1] Stok Lama
        [2] Stok Baru\n>> '''))
        if tanya == 1:
            tambah_stok_lama()
        elif tanya ==2:
            tambah_stok_baru()
        else:
            print('Masukkan Ulang pilihan !!!')
            menu_penjual()
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
            login_penjual()
    else:
        print('Username Salah !!!')
        login_penjual()
    # pass

def show_menu():
    print('')
    print('=' * 30)
    print('SELAMAT DATANG DI APOTEK SUSET')
    print('=' * 30)    
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
