import json
# ini adalah mahakarya
# buka json
stokbarang = open('datastok.json','r')

def cek_stok():
    pass

def beli_pembeli():
    obat_dibeli = input("Masukkan obat yang dibeli: ")
banyak_obat = input("Berapa jumlah obat yang dibeli: ")
if obat_dibeli and banyak_obat == 'ada':
    input("Apakah ingin membeli obat lain?(y/t): ")
    if 'y':
        pass
        #kembali ke menu menampilkan stok
    if 't':
        print("Lengkapi identitas dibawah")
        nama_pembeli = input("Masukkan nama pembeli : ")
        umur_pembeli = int(input("Masukkan umur pembeli : "))
        sex_pembeli = input("Masukkan gender pembeli : ")
        alamat_pembeli = input("Masukkan alamat pembeli : ")
        # Memilih Metode
        print("""\nMetode Pembayaran
        1. Lewat ATM/Mbanking/Bank ke no rekening xxxxxxx 
        2. Bayar Ditempat
        *Terdapat pajak 2,5%
        Pilih (1/2)
        """, end="\n")
        metode = input(">> ")
        #menampilkan struk
    else:
        print("maaf kode tidak tepat!")
else:
    pass
    #kembali ke menu lihat stok
    pass
#yang fungsi ini masih banyak yang kurang
def konsultasi():
    ## space buat ngisi ##
    pass

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
    ## space buat ngisi ##
    print('SELAMAT DATANG DI APOTEK SUSET')
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
    fjason.close()
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
