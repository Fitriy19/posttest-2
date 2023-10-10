from prettytable import PrettyTable

kamar = [
    ['single', 101, 'tersedia', 500000],
    ['single', 102, 'tersedia', 500000],
    ['double', 201, 'tersedia', 750000],
    ['double', 202, 'tersedia', 750000],
    ['twin', 301, 'tersedia', 700000],
    ['twin', 302, 'tersedia', 700000],
    ['family', 401, 'tersedia', 2000000],
    ['family', 402, 'tersedia', 2000000],
    ['presidential suite', 501, 'tersedia', 5000000],
    ['presidential suite', 502, 'tersedia', 5000000],
]

kamar_pesanan = []

# Pemilihan Peran
def pilih_menu():
    print('===================================================')
    print('|        SELAMAT DATANG DI HOTEL DEL LUNA         |')
    print('===================================================\n')
    print('[1.] Penyewa')
    print('[2.] Admin  ')
    pilihan = int(input('Masukkan Pilihan Anda :'))
    if pilihan == 1:
        menu_penyewa()
    elif pilihan == 2:
        usn = input('Masukkan username :')
        pw = int(input('Masukkan Password :'))
        if usn == 'Ipit' :
            if pw == 7 :
                menu_admin()
            else: 
                print ('Mohon maaf password Salah')
        else:
            print ('Maaf username Anda salah')

#Menampilkan Menu Penyewa
def menu_penyewa():
    tampilan_kamar()
    print('\n===== MENU PENYEWA =====')
    print('[1.] Pesan Kamar')
    print('[2.] Keluar\n')
    pilihan_penyewa = int(input('Apa yang Anda Butuhkan? :'))
    if pilihan_penyewa == 1:
        pesan_kamar()
    else:
        exit

# Menu Admin
def menu_admin():
    while True:
        print('\n===== MENU ADMIN =====')
        print('[1.] Tampilkan Daftar Kamar')
        print('[2.] Tambahkan Kamar Baru')
        print('[3.] Perbarui Informasi Kamar')
        print('[4.] Hapus nomor Kamar')
        print('[5.] Keluar\n')
        pilihan_admin = int(input('Masukkan Pilihan Anda :'))

        if pilihan_admin == 1:
            tampilan_kamar()
        elif pilihan_admin == 2:
            tambahkan_kamar()
        elif pilihan_admin == 3:
            update_kamar()
        elif pilihan_admin == 4:
            hapus_kamar()
        elif pilihan_admin == 5:
            break

# Proses Pemesanan kamar
def pesan_kamar():
    while True :
        tampilan_kamar()
        pesanan = int(input('Masukkan nomor kamar yang ingin dipesan (Masukan "0" untuk selesai): '))
        if pesanan == 0:
            break
        
        for baris in kamar:
            if baris[1] == pesanan:
                jumlah_pemesanan = int(input('Ingin menginap berapa malam? : '))
                total_hari = baris[3] * jumlah_pemesanan
                kamar_pesanan.append([baris[0], baris[1], jumlah_pemesanan, total_hari])
                print(f'{baris[1]} ({jumlah_pemesanan} malam) telah dipesan.')

    print('\nTabel Pesanan')
    tabel_pesan_kamar = PrettyTable(['Tipe Kamar', 'Nomor Kamar', 'Jumlah malam', 'Harga'])
    total_harga = 0
    for baris_pesan in kamar_pesanan:
        tabel_pesan_kamar.add_row(baris_pesan)
        total_harga += baris_pesan[3]
    print(tabel_pesan_kamar)
    print(f'Total tagihan pembayaran Anda: {total_harga}')
    print('=============================================')

# Menampilkan Kamar yang tersedia/Read
def tampilan_kamar() :
    tabel_kamar = PrettyTable(['Tipe Kamar', 'Nomor Kamar', 'Status', 'Harga'])
    for baris in kamar :
        tabel_kamar.add_row(baris)
    print(tabel_kamar)

#create
def tambahkan_kamar ():
    tampilan_kamar()
    tipe = str(input('Masukkan Tipe kamar yang ingin ditambahkan :'))
    nomor_kamar =int(input("Masukkan Nomor Kamar yang ingin ditambahkan :"))
    status=str(input("Masukkan Status Kamar yang ingin ditambahkan:"))
    harga = int(input('Masukkan harga yang ingin ditambahkan :'))

    kamar.append([tipe, nomor_kamar, status, harga])
    tampilan_kamar()
    print('==============Berhasil menambahkan kamar baru=============')

#update
def update_kamar():
    tampilan_kamar ()
    nomor_kamar = int(input ('Masukkan nomor kamar yang akan diubah :'))
    for baris in kamar :
        if baris [1]== nomor_kamar:
            statusbaru = input ('Masukan status yang baru :')
            hargabaru = int(input('Masukkan harga yang baru :'))
            baris[2] = statusbaru
            baris[3] = hargabaru
            tampilan_kamar()
            print('==============Data Kamar Berhasil Di Ubah==============')

#Delete
def hapus_kamar():
    tampilan_kamar()
    hapusnomor = int(input('Masukkan nomor kamar yang ingin dihapus : '))
    for baris in kamar:
        if baris[1] == hapusnomor:
            kamar.remove(baris)
            tampilan_kamar
            print('==============Data kamar berhasil dihapus=============')

pilih_menu()