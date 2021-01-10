import sqlite3
import User as User
import Produk as Produk
import Pesanan as Pesanan
import DetailPesanan as DetailPesanan

database = 'sejatiUAS.db'
connection = sqlite3.connect(database)

jalanUser = True
def pilihanUser():
    print(70*"*")
    print('SELAMAT DATANG'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Pilih User:')
    print('1. Pemilik')
    print('2. Admin Gudang')
    print('3. Kasir')
    print('4. Customer')
    print()
    pilihUser = input('Masukkan pilihan: ')
    print()
    return pilihUser

def register():
    print(70*"*")
    print('SELAMAT DATANG PEMILIK'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Menu Register:')
    print('1. Melihet Data ID User Terakhir')
    print('2. Buat Akun')
    pilihRegister = input('Masukkan pilihan: ')
    print()
    return pilihRegister

def tampilanPemilik():
    print(70*"*")
    print('SELAMAT DATANG PEMILIK'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Menu Pemilik:')
    print('1. LOGIN')
    print('2. REGISTER')
    print('3. LOGOUT')
    pilihPemilik = input('Masukkan pilihan: ')
    print()
    return pilihPemilik

def tampilanAdmin():
    print(70*"*")
    print('SELAMAT DATANG ADMIN GUDANG'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Menu Admin Gudang:')
    print('1. LOGIN')
    print('2. REGISTER')
    print('3. LOGOUT')
    pilihAdmin = input('Masukkan pilihan: ')
    print()
    return pilihAdmin

def tampilanKasir():
    print(70*"*")
    print('SELAMAT DATANG KASIR'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Menu Kasir:')
    print('1. LOGIN')
    print('2. REGISTER')
    print('3. LOGOUT')
    pilihKasir = input('Masukkan pilihan: ')
    print()
    return pilihKasir

def tampilanCustomer():
    print(70*"*")
    print('SELAMAT DATANG CUSTOMER'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Menu Customer:')
    print('1. LOGIN')
    print('2. REGISTER')
    print('3. LOGOUT')
    pilihCustomer = input('Masukkan pilihan: ')
    print()
    return pilihCustomer

def lihatIDUser():
    global connection
    print('\nDaftar User')
    for user_row in connection.execute('SELECT id_user FROM user ORDER BY id_user DESC LIMIT 1'):
        print()
        print("ID User:", user_row[0])
        print()

def hapusDataUser():
    global connection
    print('\nData User Yang Akan Dihapus')
    _id_user = input('Masukkan ID User: ')
    query = 'DELETE FROM user WHERE id_user=?'
    cur = connection.cursor()
    cur.execute(query,(_id_user,))
    connection.commit()
    print('Data berhasil Dihapus')

def tampilkanDataUser():
    global connection
    print('Daftar User'.center(133, "-"))
    for row in connection.execute('SELECT * FROM user'):
        print(row)
    print('\n')

def tambahDataPemilik():
    global connection
    print('\nTambah data Pemilik')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    pemilik = User.Pemilik(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role)
    queryStr = f'INSERT INTO user (id_user, username, password, namaLengkap, tanggalLahir, status, role) VALUES ({pemilik._getIdUser()}, "{pemilik._getUsername()}", "{pemilik._getPassword()}", "{pemilik._getNamaLengkap()}", "{pemilik._getTanggalLahir()}", "{pemilik._getStatus()}", "{pemilik._getRole()}")'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(queryStr)
    connection.commit()

def tampilkanDataPemilik():
    global connection
    print('Daftar Pemilik'.center(133, "-"))
    print('''
-------------------------------------------------------------------------------------------------------------------------------------
| ID Pemilik |    Username    |  Password  |          Nama Lengkap          | Tanggal Lahir |    Status    |          Role          |
-------------------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT id_user, username, password, namaLengkap, tanggalLahir, status, role FROM user WHERE role = "PEMILIK"'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(12-1-len(isi)):
            print(' ', end='')
        isi2 = str(user_row[1])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[2])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[3])
        print('| '+isi4, end='')
        for x in range(32-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[4])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[5])
        print('| '+isi6, end='')
        for x in range(14-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[6])
        print('| '+isi7, end='')
        for x in range(24-1-len(isi7)):
            print(' ', end='')
        print('|')
    print('-------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataPemilik():
    global connection
    print('\nUbah data Pemilik')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    pemilik = User.Pemilik(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role)
    connection.execute('UPDATE user SET username=?, password=?, namaLengkap=?, tanggalLahir=?, status=?, role=? WHERE id_user=?', (pemilik._getUsername(), pemilik._getPassword(), pemilik._getNamaLengkap(), pemilik._getTanggalLahir(), pemilik._getStatus(), pemilik._getRole(),pemilik._getIdUser()))
    connection.commit()
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataAdmin():
    global connection
    print('\nTambah Data Admin Gudang')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    _bagian = input('Masukkan Bagian Admin Gudang: ')
    _jamKerja = input('Masukkan Jam Kerja Admin Gudang: ')
    adm = User.Admin(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _bagian, _jamKerja)
    queryStr = f'INSERT INTO user (id_user, username, password, namaLengkap, tanggalLahir, status, role, bagian, jamKerja) VALUES ({adm._getIdUser()}, "{adm._getUsername()}", "{adm._getPassword()}", "{adm._getNamaLengkap()}", "{adm._getTanggalLahir()}", "{adm._getStatus()}", "{adm._getRole()}", "{adm._getBagian()}", "{adm._getJamKerja()}")'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(queryStr)
    connection.commit()

def tampilkanDataAdmin():
    global connection
    print('Daftar Admin Gudang'.center(167, "-"))
    print('''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID Admin  |    Username    |  Password  |        Nama Lengkap        | Tanggal Lahir |    Status    |       Role       |    Bagian    |          Jam Kerja         |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT id_user, username, password, namaLengkap, tanggalLahir, status, role, bagian, jamKerja FROM user WHERE role = "ADMIN GUDANG"'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(12-1-len(isi)):
            print(' ', end='')
        isi2 = str(user_row[1])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[2])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[3])
        print('| '+isi4, end='')
        for x in range(28-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[4])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[5])
        print('| '+isi6, end='')
        for x in range(14-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[6])
        print('| '+isi7, end='')
        for x in range(18-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[7])
        print('| '+isi8, end='')
        for x in range(14-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[8])
        print('| '+isi9, end='')
        for x in range(28-1-len(isi9)):
            print(' ', end='')
        print('|')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataAdmin():
    global connection
    print('\nUbah Data Admin')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    _bagian = input('Masukkan Bagian Admin Gudang: ')
    _jamKerja = input('Masukkan Jam Kerja Admin Gudang: ')
    adm = User.Admin(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _bagian, _jamKerja)
    connection.execute('UPDATE user SET username=?, password=?, namaLengkap=?, tanggalLahir=?, status=?, role=?, bagian=?, jamKerja=? WHERE id_user=?', (adm._getUsername(), adm._getPassword(), adm._getNamaLengkap(), adm._getTanggalLahir(), adm._getStatus(), adm._getRole(), adm._getBagian(), adm._getJamKerja(), adm._getIdUser()))
    connection.commit()
    print('\n')
    print('Data Berhasil Diubah')

def tampilkanSatuDataAdmin():
    global connection
    print('\nData Admin Gudang')
    _username = input('Masukkan Username: ')
    query = 'SELECT id_user, username, password, namaLengkap, tanggalLahir, status, role, bagian, jamKerja FROM user WHERE username = ?'
    cur = connection.cursor()
    for user_row in cur.execute(query,(_username,)):
        print()
        print("ID Admin: ", user_row[0])
        print("Username: ", user_row[1])
        print("Password: ", user_row[2])
        print("Nama Lengkap: ", user_row[3])
        print("Tanggal Lahir: ", user_row[4])
        print("Status: ", user_row[5])
        print("Role: ", user_row[6])
        print("Bagian: ", user_row[7])
        print("Jam Kerja: ", user_row[8])
        print()

def tambahDataKasir():
    global connection
    print('\nTambah Data Kasir')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    _jamKerja = input('Masukkan Jam Kerja Kasir: ')
    _nomorHandphone = input('Masukkan nomorHandphone Kasir: ')
    casher = User.Kasir(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _jamKerja, _nomorHandphone)
    queryStr = f'INSERT INTO user (id_user, username, password, namaLengkap, tanggalLahir, status, role, jamKerja, nomorHandphone) VALUES ({casher._getIdUser()}, "{casher._getUsername()}", "{casher._getPassword()}", "{casher._getNamaLengkap()}", "{casher._getTanggalLahir()}", "{casher._getStatus()}", "{casher._getRole()}", "{casher._getJamKerja()}", "{casher._getNomorHandphone()}")'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(queryStr)
    connection.commit()

def tampilkanDataKasir():
    global connection
    print('Daftar Kasir'.center(166, "-"))
    print('''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID Kasir  |    Username    |  Password  |      Nama Lengkap      | Tanggal Lahir |   Status   |       Role       |          Jam Kerja         |  Nomor Handphone  |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT id_user, username, password, namaLengkap, tanggalLahir, status, role, jamKerja, nomorHandphone FROM user WHERE role = "KASIR"'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(12-1-len(isi)):
            print(' ', end='')
        isi2 = str(user_row[1])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[2])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[3])
        print('| '+isi4, end='')
        for x in range(24-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[4])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[5])
        print('| '+isi6, end='')
        for x in range(12-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[6])
        print('| '+isi7, end='')
        for x in range(18-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[7])
        print('| '+isi8, end='')
        for x in range(28-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[8])
        print('| '+isi9, end='')
        for x in range(19-1-len(isi9)):
            print(' ', end='')
        print('|')
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataKasir():
    global connection
    print('\nUbah Data Kasir')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    _jamKerja = input('Masukkan Jam Kerja Kasir: ')
    _nomorHandphone = input('Masukkan Nomor Handphone Kasir: ')
    casher = User.Kasir(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _jamKerja, _nomorHandphone)
    connection.execute('UPDATE user SET username=?, password=?, namaLengkap=?, tanggalLahir=?, status=?, role=?, jamKerja=?, nomorHandphone=? WHERE id_user=?', (casher._getUsername(), casher._getPassword(), casher._getNamaLengkap(), casher._getTanggalLahir(), casher._getStatus(), casher._getRole(), casher._getJamKerja(), casher._getNomorHandphone(), casher._getIdUser()))
    connection.commit()
    print('\n')
    print('Data Berhasil Diubah')

def tampilkanSatuDataKasir():
    global connection
    print('\nData Kasir')
    _username = input('Masukkan Username: ')
    query = 'SELECT id_user, username, password, namaLengkap, tanggalLahir, status, role, jamKerja, nomorHandphone FROM user WHERE username = ?'
    cur = connection.cursor()
    for user_row in cur.execute(query,(_username,)):
        print()
        print("ID Kasir: ", user_row[0])
        print("Username: ", user_row[1])
        print("Password: ", user_row[2])
        print("Nama Lengkap: ", user_row[3])
        print("Tanggal Lahir: ", user_row[4])
        print("Status: ", user_row[5])
        print("Role: ", user_row[6])
        print("Jam Kerja: ", user_row[7])
        print("Nomor Handphone: ", user_row[8])
        print()

def tambahDataCustomer():
    global connection
    print('\nTambah Data Customer')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    _nomorHandphone = input('Masukkan nomorHandphone Customer: ')
    _alamatRumah = input('Masukkan Alamat Rumah Customer: ')
    pelanggan = User.Customer(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _nomorHandphone, _alamatRumah)
    queryStr = f'INSERT INTO user (id_user, username, password, namaLengkap, tanggalLahir, status, role, nomorHandphone, alamatRumah) VALUES ({pelanggan._getIdUser()}, "{pelanggan._getUsername()}", "{pelanggan._getPassword()}", "{pelanggan._getNamaLengkap()}", "{pelanggan._getTanggalLahir()}", "{pelanggan._getStatus()}", "{pelanggan._getRole()}", "{pelanggan._getNomorHandphone()}", "{pelanggan._getAlamatRumah()}")'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(queryStr)
    connection.commit()

def tampilkanDataCustomer():
    global connection
    print('Daftar Customer'.center(169, "-"))
    print('''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| ID Customer |    Username    |  Password  |    Nama Lengkap    | Tanggal Lahir |   Status   |    Role    |  Nomor Handphone  |              Alamat Rumah              |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT id_user, username, password, namaLengkap, tanggalLahir, status, role, nomorHandphone, alamatRumah FROM user WHERE role = "CUSTOMER"'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(13-1-len(isi)):
            print(' ', end='')
        isi2 = str(user_row[1])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[2])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[3])
        print('| '+isi4, end='')
        for x in range(20-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[4])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[5])
        print('| '+isi6, end='')
        for x in range(12-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[6])
        print('| '+isi7, end='')
        for x in range(12-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[7])
        print('| '+isi8, end='')
        for x in range(19-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[8])
        print('| '+isi9, end='')
        for x in range(40-1-len(isi9)):
            print(' ', end='')
        print('|')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataCustomer():
    global connection
    print('\nUbah Data Customer')
    _id_user = input('Masukkan ID User: ')
    _username = input('Masukkan Username: ')
    _password = input('Masukkan Password: ')
    _namaLengkap = input('Masukkan Nama Lengkap: ')
    _tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    _status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    _role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    _nomorHandphone = input('Masukkan Nomor Handphone Customer: ')
    _alamatRumah = input('Masukkan Alamat Rumah Customer: ')
    pelanggan = User.Customer(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _nomorHandphone, _alamatRumah)
    connection.execute('UPDATE user SET username=?, password=?, namaLengkap=?, tanggalLahir=?, status=?, role=?, nomorHandphone=?, alamatRumah=? WHERE id_user=?', (pelanggan._getUsername(), pelanggan._getPassword(), pelanggan._getNamaLengkap(), pelanggan._getTanggalLahir(), pelanggan._getStatus(), pelanggan._getRole(), pelanggan._getNomorHandphone(), pelanggan._getAlamatRumah(), pelanggan._getIdUser()))
    connection.commit()
    print('\n')
    print('Data Berhasil Diubah')

def tampilkanSatuDataCustomer():
    global connection
    print('\nData Customer')
    _username = input('Masukkan Username: ')
    query = 'SELECT id_user, username, password, namaLengkap, tanggalLahir, status, role, nomorHandphone, alamatRumah FROM user WHERE username = ?'
    cur = connection.cursor()
    for user_row in cur.execute(query,(_username,)):
        print()
        print("ID Customer: ", user_row[0])
        print("Username: ", user_row[1])
        print("Password: ", user_row[2])
        print("Nama Lengkap: ", user_row[3])
        print("Tanggal Lahir: ", user_row[4])
        print("Status: ", user_row[5])
        print("Role: ", user_row[6])
        print("Nomor Handphone: ", user_row[7])
        print("Alamat Rumah: ", user_row[8])
        print()

def tambahDataCelana():
    global connection
    print('\nTambah Data Celana')
    _id = input('Masukkan ID Produk: ')
    _jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    _merk = input('Memasukkan Merk: ')
    _deskripsi = input("Memasukkan Deskripsi Produk: ")
    _warna = input('Memasukkan Warna: ')
    _ukuran = input('Memasukkan Ukuran: ')
    _jenisBahan = input('Memasukkan Jenis Bahan: ')
    _harga = int(input('Memasukkan Harga: '))
    _stok = int(input('Memasukkan Stok: '))
    _modelCelana = input('Masukkan Model Celana: ')
    cel = Produk.Celana( _id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _modelCelana)
    query = f'INSERT INTO produk (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, modelCelana) VALUES ({cel._getId()}, "{cel._getJenisProduk()}", "{cel._getMerk()}", "{cel._getDeskripsi()}", "{cel._getWarna()}", "{cel._getUkuran()}", "{cel._getJenisBahan()}", {cel._getHarga()}, {cel._getStok()}, "{cel._getModelCelana()}")'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(query)
    connection.commit()

def tampilkanDataCelana():
    global connection
    print('Daftar Produk Celana'.center(170, "-"))
    print('''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| ID Celana | Jenis Prod |  Merk  |                              Deskripsi                              | Warna |     Ukuran    | Jenis Bahan | Harga | Stok | Model Cel |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, modelCelana FROM produk WHERE jenisProduk = "CELANA"'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(11-1-len(isi)):
            print(' ', end='')
        isi2 = str(user_row[1])
        print('| '+isi2, end='')
        for x in range(12-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[2])
        print('| '+isi3, end='')
        for x in range(8-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[3])
        print('| '+isi4, end='')
        for x in range(69-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[4])
        print('| '+isi5, end='')
        for x in range(7-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[5])
        print('| '+isi6, end='')
        for x in range(15-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[6])
        print('| '+isi7, end='')
        for x in range(13-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[7])
        print('| '+isi8, end='')
        for x in range(7-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[8])
        print('| '+isi9, end='')
        for x in range(6-1-len(isi9)):
            print(' ', end='')
        isi10 = str(user_row[9])
        print('| '+isi10, end='')
        for x in range(11-1-len(isi10)):
            print(' ', end='')
        print('|')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataCelana():
    global connection
    print('\nUbah Data Produk Celana')
    _id = input('Masukkan ID Produk: ')
    _jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    _merk = input('Memasukkan Merk: ')
    _deskripsi = input("Memasukkan Deskripsi Produk: ")
    _warna = input('Memasukkan Warna: ')
    _ukuran = input('Memasukkan Ukuran: ')
    _jenisBahan = input('Memasukkan Jenis Bahan: ')
    _harga = int(input('Memasukkan Harga: '))
    _stok = int(input('Memasukkan Stok: '))
    _modelCelana = input('Masukkan Model Celana: ')
    cel = Produk.Celana( _id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _modelCelana)
    query = f'UPDATE produk SET (jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, modelCelana) = ("{cel._getJenisProduk()}", "{cel._getMerk()}", "{cel._getDeskripsi()}", "{cel._getWarna()}", "{cel._getUkuran()}", "{cel._getJenisBahan()}", {cel._getHarga()}, {cel._getStok()}, "{cel._getModelCelana()}") WHERE id={cel._getId()}'
    print('\n')
    print('Data Berhasil Diubah')
    connection.execute(query)
    connection.commit()

def tambahDataBaju():
    global connection
    print('\nTambah Data Baju')
    _id = input('Masukkan ID Produk: ')
    _jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    _merk = input('Memasukkan Merk: ')
    _deskripsi = input("Memasukkan Deskripsi Produk: ")
    _warna = input('Memasukkan Warna: ')
    _ukuran = input('Memasukkan Ukuran: ')
    _jenisBahan = input('Memasukkan Jenis Bahan: ')
    _harga = int(input('Memasukkan Harga: '))
    _stok = int(input('Memasukkan Stok: '))
    _modelBaju = input('Masukkan Model Baju: ')
    baj = Produk.Baju(_id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _modelBaju)
    query = f'INSERT INTO produk (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, modelBaju) VALUES ({baj._getId()}, "{baj._getJenisProduk()}", "{baj._getMerk()}", "{baj._getDeskripsi()}", "{baj._getWarna()}", "{baj._getUkuran()}", "{baj._getJenisBahan()}", {baj._getHarga()}, {baj._getStok()}, "{baj._getModelBaju()}")'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(query)
    connection.commit()

def tampilkanDataBaju():
    global connection
    print('Daftar Produk Baju'.center(171, "-"))
    print('''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID Baju  | Jenis Prod |  Merk  |                              Deskripsi                              | Warna |     Ukuran    | Jenis Bahan | Harga | Stok | Model Baju |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, modelBaju FROM produk WHERE jenisProduk = "BAJU"'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(11-1-len(isi)):
            print(' ', end='')
        isi2 = str(user_row[1])
        print('| '+isi2, end='')
        for x in range(12-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[2])
        print('| '+isi3, end='')
        for x in range(8-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[3])
        print('| '+isi4, end='')
        for x in range(69-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[4])
        print('| '+isi5, end='')
        for x in range(7-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[5])
        print('| '+isi6, end='')
        for x in range(15-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[6])
        print('| '+isi7, end='')
        for x in range(13-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[7])
        print('| '+isi8, end='')
        for x in range(7-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[8])
        print('| '+isi9, end='')
        for x in range(6-1-len(isi9)):
            print(' ', end='')
        isi10 = str(user_row[9])
        print('| '+isi10, end='')
        for x in range(12-1-len(isi10)):
            print(' ', end='')
        print('|')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataBaju():
    global connection
    print('\nUbah Data Produk Baju')
    _id = input('Masukkan ID Produk: ')
    _jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    _merk = input('Memasukkan Merk: ')
    _deskripsi = input("Memasukkan Deskripsi Produk: ")
    _warna = input('Memasukkan Warna: ')
    _ukuran = input('Memasukkan Ukuran: ')
    _jenisBahan = input('Memasukkan Jenis Bahan: ')
    _harga = int(input('Memasukkan Harga: '))
    _stok = int(input('Memasukkan Stok: '))
    _modelBaju = input('Masukkan Model Baju: ')
    baj = Produk.Baju(_id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _modelBaju)
    query = f'UPDATE produk SET (jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, modelBaju) = ("{baj._getJenisProduk()}", "{baj._getMerk()}", "{baj._getDeskripsi()}", "{baj._getWarna()}", "{baj._getUkuran()}", "{baj._getJenisBahan()}", {baj._getHarga()}, {baj._getStok()}, "{baj._getModelBaju()}") WHERE id={baj._getId()}'
    print('\n')
    print('Data Berhasil Diubah')
    connection.execute(query)
    connection.commit()

def tambahDataTas():
    global connection
    print('\nTambah Data Tas')
    _id = input('Masukkan ID Produk: ')
    _jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    _merk = input('Memasukkan Merk: ')
    _deskripsi = input("Memasukkan Deskripsi Produk: ")
    _warna = input('Memasukkan Warna: ')
    _ukuran = input('Memasukkan Ukuran: ')
    _jenisBahan = input('Memasukkan Jenis Bahan: ')
    _harga = int(input('Memasukkan Harga: '))
    _stok = int(input('Memasukkan Stok: '))
    _namaTas = input('Masukkan Nama Tas: ')
    taS = Produk.Tas(_id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _namaTas)
    query = f'INSERT INTO produk (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, namaTas) VALUES ({taS._getId()}, "{taS._getJenisProduk()}", "{taS._getMerk()}", "{taS._getDeskripsi()}", "{taS._getWarna()}", "{taS._getUkuran()}", "{taS._getJenisBahan()}", {taS._getHarga()}, {taS._getStok()}, "{taS._getNamaTas()}")'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(query)
    connection.commit()

def tampilkanDataTas():
    global connection
    print('Daftar Produk Tas'.center(170, "-"))
    print('''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID  Tas  | Jenis Prod |  Merk  |                              Deskripsi                              | Warna |     Ukuran    | Jenis Bahan | Harga | Stok | Nama  Tas |
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, namaTas FROM produk WHERE jenisProduk = "TAS"'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(11-1-len(isi)):
            print(' ', end='')
        isi2 = str(user_row[1])
        print('| '+isi2, end='')
        for x in range(12-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[2])
        print('| '+isi3, end='')
        for x in range(8-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[3])
        print('| '+isi4, end='')
        for x in range(69-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[4])
        print('| '+isi5, end='')
        for x in range(7-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[5])
        print('| '+isi6, end='')
        for x in range(15-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[6])
        print('| '+isi7, end='')
        for x in range(13-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[7])
        print('| '+isi8, end='')
        for x in range(7-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[8])
        print('| '+isi9, end='')
        for x in range(6-1-len(isi9)):
            print(' ', end='')
        isi10 = str(user_row[9])
        print('| '+isi10, end='')
        for x in range(11-1-len(isi10)):
            print(' ', end='')
        print('|')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataTas():
    global connection
    print('\nUbah Data Produk Tas')
    _id = input('Masukkan ID Produk: ')
    _jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    _merk = input('Memasukkan Merk: ')
    _deskripsi = input("Memasukkan Deskripsi Produk: ")
    _warna = input('Memasukkan Warna: ')
    _ukuran = input('Memasukkan Ukuran: ')
    _jenisBahan = input('Memasukkan Jenis Bahan: ')
    _harga = int(input('Memasukkan Harga: '))
    _stok = int(input('Memasukkan Stok: '))
    _namaTas = input('Masukkan Nama Tas: ')
    taS = Produk.Tas(_id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _namaTas)
    query = f'UPDATE produk SET (jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, namaTas) = ("{taS._getJenisProduk()}", "{taS._getMerk()}", "{taS._getDeskripsi()}", "{taS._getWarna()}", "{taS._getUkuran()}", "{taS._getJenisBahan()}", {taS._getHarga()}, {taS._getStok()}, "{taS._getNamaTas()}") WHERE id={taS._getId()}'
    print('\n')
    print('Data Berhasil Diubah')
    connection.execute(query)
    connection.commit()

def hapusDataProduk():
    global connection
    print('\nData Produk Yang Akan Dihapus')
    _id = input('Masukkan ID User: ')
    query = 'DELETE FROM produk WHERE id=?'
    cur = connection.cursor()
    cur.execute(query,(_id,))
    connection.commit()
    print('Data berhasil Dihapus')

def tambahDataPesanan():
    global connection
    print('\nTambah Data Pesanan')
    _id_pesanan = input('Masukkan ID Pesanan: ')
    _statusPesanan = input('Masukkan Status Pesanan: ')
    _tanggalPenerimaan = input('Masukkan Tanggal Penerimaan Pesanan: ')
    _verifikasi = input('Masukkan Verifikasi Pesanan: ')
    _id_user = input('Masukkan Id Kasir: ')
    order = Pesanan.pesanan(_id_pesanan, _statusPesanan, _tanggalPenerimaan, _verifikasi, _id_user)
    queryStr = f'INSERT INTO pesanan (id_pesanan, statusPesanan, tanggalPenerimaan, verifikasi, id_user) VALUES ({order._getIdPesanan()}, "{order._getStatusPesanan()}", "{order._getTglPenerimaan()}", "{order._getVerifikasi()}", {order._getIdUser()})'
    print('\n')
    print('Data Berhasil Ditambahkan')
    connection.execute(queryStr)
    connection.commit()

def ubahDataPesanan():
    global connection
    print('\nUbah Data Pesanan')
    _id_pesanan = input('Masukkan ID Pesanan: ')
    _statusPesanan = input('Masukkan Status Pesanan: ')
    _tanggalPenerimaan = input('Masukkan Tanggal Penerimaan Pesanan: ')
    _verifikasi = input('Masukkan Verifikasi Pesanan: ')
    _id_user = input('Masukkan Id Kasir: ')
    order = Pesanan.pesanan(_id_pesanan, _statusPesanan, _tanggalPenerimaan, _verifikasi, _id_user)
    query = f'UPDATE pesanan SET (statusPesanan, tanggalPenerimaan, verifikasi, id_user) = ("{order._getStatusPesanan()}", "{order._getTglPenerimaan()}", "{order._getVerifikasi()}", {order._getIdUser()}) WHERE id_pesanan={order._getIdPesanan()}'
    print('\n')
    print('Data Berhasil Diubah')
    connection.execute(query)
    connection.commit()

def tampilkanDataPesanan():
    global connection
    print('Daftar Pesanan'.center(125, "-"))
    print('''
-----------------------------------------------------------------------------------------------------------------------------
| ID Pesanan | Status Pesanan | Tgl Penerimaan |  Verifikasi  | ID Kasir |          Nama Lengkap          | Nomor Handphone |
-----------------------------------------------------------------------------------------------------------------------------''')
    for user_row in connection.execute('SELECT t1.id_pesanan, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t2.id_user, t2.namaLengkap, t2.nomorHandphone FROM pesanan t1 INNER JOIN user t2 ON t1.id_user=t2.id_user'):
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(12-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(15-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(14-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(10-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(32-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(17-1-len(isi6)):
            print(' ', end='')
        print('|')
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def lihatIDDetPesanan():
    global connection
    print('\nDaftar Data Detail Pesanan')
    for user_row in connection.execute('SELECT id_DetPesanan FROM detailPesanan ORDER BY id_DetPesanan DESC LIMIT 1'):
        print()
        print("ID Data Detail Pesanan:", user_row[0])
        print()

def tambahDataDetPesanan():
    global connection
    print('\nTambah Data Detail Pesanan')
    _id_DetPesanan = input('Masukkan ID Detail Pesanan: ')
    _id_pesanan = input('Masukkan ID Pesanan: ')
    _tanggalPesanan = input('Masukkan Tanggal Pesanan: ')
    _jumlahBaju = int(input('Masukkan jumlah baju yang dibeli: '))
    _jumlahCelana = int(input('Masukkan jumlah celana yang dibeli: '))
    _jumlahTas = int(input('Masukkan jumlah tas yang dibeli: '))
    _id_tas = input('Masukkan ID Tas: ')
    _id_celana = input('Masukkan ID Celana: ')
    _id_baju = input('Masukkan ID Baju: ')
    _id_user = input('Masukkan ID Customer: ')
    detailOrder = DetailPesanan.detailPesanan(_id_DetPesanan, _id_pesanan, _tanggalPesanan, _jumlahBaju, _jumlahCelana, _jumlahTas, _id_tas, _id_celana, _id_baju, _id_user)
    totHarBaju = connection.cursor().execute(f"SELECT harga FROM produk WHERE id = {detailOrder._getIdBaju()}").fetchone()
    harBaju = totHarBaju[0]
    totHarCel = connection.cursor().execute(f"SELECT harga FROM produk WHERE id = {detailOrder._getIdCelana()}").fetchone()
    harCel = totHarCel[0]
    totHarTas = connection.cursor().execute(f"SELECT harga FROM produk WHERE id = {detailOrder._getIdTas()}").fetchone()
    harTas = totHarTas[0]
    totalHarBaju = int(_jumlahBaju) * int(harBaju)
    totalHarCelana = int(_jumlahCelana) * int(harCel)
    totalHarTas = int(_jumlahTas) * int(harTas)
    jumlahPemesanan = int(_jumlahBaju) + int(_jumlahCelana) + int(_jumlahTas)
    totalHargPemesanan = totalHarBaju + totalHarCelana + totalHarTas
    query = f'INSERT INTO detailPesanan (id_DetPesanan, id_pesanan, tanggalPesanan, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPemesanan, totalHargPemesanan, id_tas, id_celana, id_baju, id_user) VALUES ({detailOrder._getIdDetPesanan()}, {detailOrder._getIdPesanan()}, "{detailOrder._getTglPesanan()}", {detailOrder._getJumlahBaju()}, {totalHarBaju}, {detailOrder._getJumlahCelana()}, {totalHarCelana}, {detailOrder._getJumlahTas()}, {totalHarTas}, {jumlahPemesanan}, {totalHargPemesanan}, {detailOrder._getIdTas()}, {detailOrder._getIdCelana()}, {detailOrder._getIdBaju()}, {detailOrder._getIdUser()})'
    print('\n')
    connection.execute(query)
    query2 = f'UPDATE produk SET stok = (stok-{_jumlahBaju}) WHERE id={detailOrder._getIdBaju()}'
    connection.execute(query2)
    query3 = f'UPDATE produk SET stok = (stok-{_jumlahCelana}) WHERE id={detailOrder._getIdCelana()}'
    connection.execute(query3)
    query4 = f'UPDATE produk SET stok = (stok-{_jumlahTas}) WHERE id={detailOrder._getIdTas()}'
    connection.execute(query4)
    connection.commit()
    print('Data Berhasil Ditambahkan')

def ubahDataDetPesananKasir():
    global connection
    print('\nUbah Data Detail Pesanan')
    _id_DetPesanan = input('Masukkan ID Detail Pesanan: ')
    _id_pesanan = input('Masukkan ID Pesanan: ')
    query = f'UPDATE detailPesanan SET (id_pesanan) = {_id_pesanan} WHERE id_DetPesanan = {_id_DetPesanan}'
    print('\n')
    print('Data Berhasil Diubah')
    connection.execute(query)
    connection.commit()

def ubahDataDetPesanan():
    global connection
    print('\nUbah Data Detail Pesanan')
    _id_DetPesanan = input('Masukkan ID Detail Pesanan: ')
    _id_pesanan = input('Masukkan ID Pesanan: ')
    _tanggalPesanan = input('Masukkan Tanggal Pesanan: ')
    _jumlahBaju = int(input('Masukkan jumlah baju yang dibeli: '))
    _jumlahCelana = int(input('Masukkan jumlah celana yang dibeli: '))
    _jumlahTas = int(input('Masukkan jumlah tas yang dibeli: '))
    _id_tas = input('Masukkan ID Tas: ')
    _id_celana = input('Masukkan ID Celana: ')
    _id_baju = input('Masukkan ID Baju: ')
    _id_user = input('Masukkan ID Customer: ')
    detailOrder = DetailPesanan.detailPesanan(_id_DetPesanan, _id_pesanan, _tanggalPesanan, _jumlahBaju, _jumlahCelana, _jumlahTas, _id_tas, _id_celana, _id_baju, _id_user)
    totHarBaju = connection.cursor().execute(f"SELECT harga FROM produk WHERE id = {detailOrder._getIdBaju()}").fetchone()
    harBaju = totHarBaju[0]
    totHarCel = connection.cursor().execute(f"SELECT harga FROM produk WHERE id = {detailOrder._getIdCelana()}").fetchone()
    harCel = totHarCel[0]
    totHarTas = connection.cursor().execute(f"SELECT harga FROM produk WHERE id = {detailOrder._getIdTas()}").fetchone()
    harTas = totHarTas[0]
    totalHarBaju = int(_jumlahBaju) * int(harBaju)
    totalHarCelana = int(_jumlahCelana) * int(harCel)
    totalHarTas = int(_jumlahTas) * int(harTas)
    jumlahPemesanan = int(_jumlahBaju) + int(_jumlahCelana) + int(_jumlahTas)
    totalHargPemesanan = totalHarBaju + totalHarCelana + totalHarTas
    query = f'UPDATE detailPesanan SET (id_pesanan, tanggalPesanan, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPemesanan, totalHargPemesanan, id_tas, id_celana, id_baju, id_user) = ({detailOrder._getIdPesanan()}, "{detailOrder._getTglPesanan()}", {detailOrder._getJumlahBaju()}, {totalHarBaju}, {detailOrder._getJumlahCelana()}, {totalHarCelana}, {detailOrder._getJumlahTas()}, {totalHarTas}, {jumlahPemesanan}, {totalHargPemesanan}, {detailOrder._getIdTas()}, {detailOrder._getIdCelana()}, {detailOrder._getIdBaju()}, {detailOrder._getIdUser()}) WHERE id_DetPesanan={detailOrder._getIdDetPesanan()}'
    print('\n')
    print('Data Berhasil Diubah')
    connection.execute(query)
    connection.commit()

def tampilkanSatuDataDetPesanan():
    global connection
    print('\nData Detail Pesanan')
    _id_DetPesanan = input('Masukkan ID Detail Pesanan: ')
    query = 'SELECT detailPesanan.id_user, user1.namaLengkap, user1.nomorHandphone, user1.alamatRumah, detailPesanan.id_DetPesanan, detailPesanan.tanggalPesanan, detailPesanan.id_celana, produk.jenisProduk, produk.modelCelana, produk.merk, produk.deskripsi, produk.warna, produk.ukuran, produk.jenisBahan, produk.harga, detailPesanan.jumlahCelana, detailPesanan.totalHarCelana, detailPesanan.id_baju, produk1.jenisProduk, produk1.modelBaju, produk1.merk, produk1.deskripsi, produk1.warna, produk1.ukuran, produk1.jenisBahan, produk1.harga, detailPesanan.jumlahBaju, detailPesanan.totalHarBaju, detailPesanan.id_tas, produk2.jenisProduk, produk2.namaTas, produk2.merk, produk2.deskripsi, produk2.warna, produk2.ukuran, produk2.jenisBahan, produk2.harga, detailPesanan.jumlahTas, detailPesanan.totalHarTas, detailPesanan.id_pesanan, pesanan.statusPesanan, pesanan.tanggalPenerimaan, pesanan.verifikasi, user.namaLengkap, user.nomorHandphone, detailPesanan.jumlahPemesanan, detailPesanan.totalHargPemesanan FROM detailPesanan INNER JOIN pesanan ON detailPesanan.id_pesanan = pesanan.id_pesanan INNER JOIN user ON detailPesanan.id_user = user.id_user INNER JOIN user user1 ON detailPesanan.id_user = user1.id_user INNER JOIN produk ON detailPesanan.id_celana = produk.id INNER JOIN produk produk1 ON detailPesanan.id_baju = produk1.id INNER JOIN produk produk2 ON detailPesanan.id_tas = produk2.id WHERE detailPesanan.id_DetPesanan = ?'
    cur = connection.cursor()
    for user_row in cur.execute(query,(_id_DetPesanan,)):
        print("** Identitas Customer **")
        print("ID Customer: ", user_row[0])
        print("Nama Lengkap: ", user_row[1])
        print("Nomor Handphone: ", user_row[2])
        print("Alamat Rumah: ", user_row[3])
        print()
        print("** Pesanan Celana **")
        print("ID Celana: ", user_row[6])
        print("Jenis Produk: ", user_row[7])
        print("Model Celana: ", user_row[8])
        print("Merk Celana: ", user_row[9])
        print("Deskripsi Celana: ", user_row[10])
        print("Warna Celana: ", user_row[11])
        print("Ukuran Celana: ", user_row[12])
        print("Jenis Bahan Celana: ", user_row[13])
        print("Harga Celana: ", user_row[14])
        print("Jumlah Celana Pesanan: ", user_row[15])
        print("Total Harga Celana Pesanan: ", user_row[16])
        print()
        print("** Pesanan Baju **")
        print("ID Baju: ", user_row[17])
        print("Jenis Baju: ", user_row[18])
        print("Model Baju: ", user_row[19])
        print("Merk Baju: ", user_row[20])
        print("Deskripsi Baju: ", user_row[21])
        print("Warna Baju: ", user_row[22])
        print("Ukuran Baju: ", user_row[23])
        print("Jenis Bahan Baju: ", user_row[24])
        print("Harga Baju: ", user_row[25])
        print("Jumlah Baju Pesanan: ", user_row[26])
        print("Total Harga Baju Pesanan: ", user_row[27])
        print()
        print("** Pesanan Tas **")
        print("ID Tas: ", user_row[28])
        print("Jenis Tas: ", user_row[29])
        print("Nama Tas: ", user_row[30])
        print("Merk Tas: ", user_row[31])
        print("Deskripsi Tas: ", user_row[32])
        print("Warna Tas: ", user_row[33])
        print("Ukuran Tas: ", user_row[34])
        print("Jenis Bahan Tas: ", user_row[35])
        print("Harga Tas: ", user_row[36])
        print("Jumlah Tas Pesanan: ", user_row[37])
        print("Total Harga Tas Pesanan: ", user_row[38])
        print()
        print("** Pesanan **")
        print("ID Detail Pesanan: ", user_row[4])
        print("Tanggal Pesanan: ", user_row[5])
        print("ID Pesanan: ", user_row[39])
        print("Status Pesanan: ", user_row[40])
        print("Tanggal Penerimaan: ", user_row[41])
        print("Verifikasi Pesanan: ", user_row[42])
        print("Nama Lengkap Kasir: ", user_row[43])
        print("Nomor Handphone Kasir: ", user_row[44])
        print("Jumlah Pembelian Produk: ", user_row[45])
        print("Total Harga Pemesanan Produk: ", user_row[46])
        print()
    print('\n')

def tampilkanSatuDataDetPesananCus():
    global connection
    print('\nData Detail Pesanan')
    _username = input('Masukkan Username: ')
    query = 'SELECT detailPesanan.id_user, user1.namaLengkap, user1.nomorHandphone, user1.alamatRumah, detailPesanan.id_DetPesanan, detailPesanan.tanggalPesanan, detailPesanan.id_celana, produk.jenisProduk, produk.modelCelana, produk.merk, produk.deskripsi, produk.warna, produk.ukuran, produk.jenisBahan, produk.harga, detailPesanan.jumlahCelana, detailPesanan.totalHarCelana, detailPesanan.id_baju, produk1.jenisProduk, produk1.modelBaju, produk1.merk, produk1.deskripsi, produk1.warna, produk1.ukuran, produk1.jenisBahan, produk1.harga, detailPesanan.jumlahBaju, detailPesanan.totalHarBaju, detailPesanan.id_tas, produk2.jenisProduk, produk2.namaTas, produk2.merk, produk2.deskripsi, produk2.warna, produk2.ukuran, produk2.jenisBahan, produk2.harga, detailPesanan.jumlahTas, detailPesanan.totalHarTas, detailPesanan.id_pesanan, pesanan.statusPesanan, pesanan.tanggalPenerimaan, pesanan.verifikasi, user.namaLengkap, user.nomorHandphone, detailPesanan.jumlahPemesanan, detailPesanan.totalHargPemesanan FROM detailPesanan INNER JOIN pesanan ON detailPesanan.id_pesanan = pesanan.id_pesanan INNER JOIN user ON detailPesanan.id_user = user.id_user INNER JOIN user user1 ON detailPesanan.id_user = user1.id_user INNER JOIN produk ON detailPesanan.id_celana = produk.id INNER JOIN produk produk1 ON detailPesanan.id_baju = produk1.id INNER JOIN produk produk2 ON detailPesanan.id_tas = produk2.id WHERE user1.username = ?'
    cur = connection.cursor()
    for user_row in cur.execute(query,(_username,)):
        print("** Identitas Customer **")
        print("ID Customer: ", user_row[0])
        print("Nama Lengkap: ", user_row[1])
        print("Nomor Handphone: ", user_row[2])
        print("Alamat Rumah: ", user_row[3])
        print()
        print("** Pesanan Celana **")
        print("ID Celana: ", user_row[6])
        print("Jenis Produk: ", user_row[7])
        print("Model Celana: ", user_row[8])
        print("Merk Celana: ", user_row[9])
        print("Deskripsi Celana: ", user_row[10])
        print("Warna Celana: ", user_row[11])
        print("Ukuran Celana: ", user_row[12])
        print("Jenis Bahan Celana: ", user_row[13])
        print("Harga Celana: ", user_row[14])
        print("Jumlah Celana Pesanan: ", user_row[15])
        print("Total Harga Celana Pesanan: ", user_row[16])
        print()
        print("** Pesanan Baju **")
        print("ID Baju: ", user_row[17])
        print("Jenis Baju: ", user_row[18])
        print("Model Baju: ", user_row[19])
        print("Merk Baju: ", user_row[20])
        print("Deskripsi Baju: ", user_row[21])
        print("Warna Baju: ", user_row[22])
        print("Ukuran Baju: ", user_row[23])
        print("Jenis Bahan Baju: ", user_row[24])
        print("Harga Baju: ", user_row[25])
        print("Jumlah Baju Pesanan: ", user_row[26])
        print("Total Harga Baju Pesanan: ", user_row[27])
        print()
        print("** Pesanan Tas **")
        print("ID Tas: ", user_row[28])
        print("Jenis Tas: ", user_row[29])
        print("Nama Tas: ", user_row[30])
        print("Merk Tas: ", user_row[31])
        print("Deskripsi Tas: ", user_row[32])
        print("Warna Tas: ", user_row[33])
        print("Ukuran Tas: ", user_row[34])
        print("Jenis Bahan Tas: ", user_row[35])
        print("Harga Tas: ", user_row[36])
        print("Jumlah Tas Pesanan: ", user_row[37])
        print("Total Harga Tas Pesanan: ", user_row[38])
        print()
        print("** Pesanan **")
        print("ID Detail Pesanan: ", user_row[4])
        print("Tanggal Pesanan: ", user_row[5])
        print("ID Pesanan: ", user_row[39])
        print("Status Pesanan: ", user_row[40])
        print("Tanggal Penerimaan: ", user_row[41])
        print("Verifikasi Pesanan: ", user_row[42])
        print("Nama Lengkap Kasir: ", user_row[43])
        print("Nomor Handphone Kasir: ", user_row[44])
        print("Jumlah Pembelian Produk: ", user_row[45])
        print("Total Harga Pemesanan Produk: ", user_row[46])
        print()
    print('\n')

def tampilkanSatuDataDetPesananPemilik():
    global connection
    print('\nData Detail Pesanan')
    _tanggalPesanan = input('Masukkan Tanggal Pesanan : ')
    query = 'SELECT detailPesanan.id_user, user1.namaLengkap, user1.nomorHandphone, user1.alamatRumah, detailPesanan.id_DetPesanan, detailPesanan.tanggalPesanan, detailPesanan.id_celana, produk.jenisProduk, produk.modelCelana, produk.merk, produk.deskripsi, produk.warna, produk.ukuran, produk.jenisBahan, produk.harga, detailPesanan.jumlahCelana, detailPesanan.totalHarCelana, detailPesanan.id_baju, produk1.jenisProduk, produk1.modelBaju, produk1.merk, produk1.deskripsi, produk1.warna, produk1.ukuran, produk1.jenisBahan, produk1.harga, detailPesanan.jumlahBaju, detailPesanan.totalHarBaju, detailPesanan.id_tas, produk2.jenisProduk, produk2.namaTas, produk2.merk, produk2.deskripsi, produk2.warna, produk2.ukuran, produk2.jenisBahan, produk2.harga, detailPesanan.jumlahTas, detailPesanan.totalHarTas, detailPesanan.id_pesanan, pesanan.statusPesanan, pesanan.tanggalPenerimaan, pesanan.verifikasi, user.namaLengkap, user.nomorHandphone, detailPesanan.jumlahPemesanan, detailPesanan.totalHargPemesanan FROM detailPesanan INNER JOIN pesanan ON detailPesanan.id_pesanan = pesanan.id_pesanan INNER JOIN user ON detailPesanan.id_user = user.id_user INNER JOIN user user1 ON detailPesanan.id_user = user1.id_user INNER JOIN produk ON detailPesanan.id_celana = produk.id INNER JOIN produk produk1 ON detailPesanan.id_baju = produk1.id INNER JOIN produk produk2 ON detailPesanan.id_tas = produk2.id WHERE detailPesanan.tanggalPesanan = ?'
    cur = connection.cursor()
    for user_row in cur.execute(query,(_tanggalPesanan,)):
        print("** Identitas Customer **")
        print("ID Customer: ", user_row[0])
        print("Nama Lengkap: ", user_row[1])
        print("Nomor Handphone: ", user_row[2])
        print("Alamat Rumah: ", user_row[3])
        print()
        print("** Pesanan Celana **")
        print("ID Celana: ", user_row[6])
        print("Jenis Produk: ", user_row[7])
        print("Model Celana: ", user_row[8])
        print("Merk Celana: ", user_row[9])
        print("Deskripsi Celana: ", user_row[10])
        print("Warna Celana: ", user_row[11])
        print("Ukuran Celana: ", user_row[12])
        print("Jenis Bahan Celana: ", user_row[13])
        print("Harga Celana: ", user_row[14])
        print("Jumlah Celana Pesanan: ", user_row[15])
        print("Total Harga Celana Pesanan: ", user_row[16])
        print()
        print("** Pesanan Baju **")
        print("ID Baju: ", user_row[17])
        print("Jenis Baju: ", user_row[18])
        print("Model Baju: ", user_row[19])
        print("Merk Baju: ", user_row[20])
        print("Deskripsi Baju: ", user_row[21])
        print("Warna Baju: ", user_row[22])
        print("Ukuran Baju: ", user_row[23])
        print("Jenis Bahan Baju: ", user_row[24])
        print("Harga Baju: ", user_row[25])
        print("Jumlah Baju Pesanan: ", user_row[26])
        print("Total Harga Baju Pesanan: ", user_row[27])
        print()
        print("** Pesanan Tas **")
        print("ID Tas: ", user_row[28])
        print("Jenis Tas: ", user_row[29])
        print("Nama Tas: ", user_row[30])
        print("Merk Tas: ", user_row[31])
        print("Deskripsi Tas: ", user_row[32])
        print("Warna Tas: ", user_row[33])
        print("Ukuran Tas: ", user_row[34])
        print("Jenis Bahan Tas: ", user_row[35])
        print("Harga Tas: ", user_row[36])
        print("Jumlah Tas Pesanan: ", user_row[37])
        print("Total Harga Tas Pesanan: ", user_row[38])
        print()
        print("** Pesanan **")
        print("ID Detail Pesanan: ", user_row[4])
        print("Tanggal Pesanan: ", user_row[5])
        print("ID Pesanan: ", user_row[39])
        print("Status Pesanan: ", user_row[40])
        print("Tanggal Penerimaan: ", user_row[41])
        print("Verifikasi Pesanan: ", user_row[42])
        print("Nama Lengkap Kasir: ", user_row[43])
        print("Nomor Handphone Kasir: ", user_row[44])
        print("Jumlah Pembelian Produk: ", user_row[45])
        print("Total Harga Pemesanan Produk: ", user_row[46])
        print()
    print('\n')

def fiturPemilik():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Pemilik:')
    print('1. Melihat Data User')
    print('2. Menghapus Data User')
    print('3. Melihat Data Pemilik')
    print('4. Menambah Data Pemilik')
    print('5. Mengubah Data Pemilik')
    print('6. Melihat Data Admin Gudang')
    print('7. Menambah Data Admin Gudang')
    print('8. Mengubah Data Admin Gudang')
    print('9. Melihat Data Kasir')
    print('10. Menambah Data Kasir')
    print('11. Mengubah Data Kasir')
    print('12. Melihat Data Customer')
    print('13. Menambah Data Customer')
    print('14. Mengubah Data Customer')
    print('15. Melihat Data Celana')
    print('16. Melihat Data Baju')
    print('17. Melihat Data Tas')
    print('18. Melihat Rekap Pesanan')
    print('19. LOGOUT')
    pilihFiturPemilik = input('Masukkan pilihan: ')
    print()
    return pilihFiturPemilik

def fiturAdmin():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Admin Gudang:')
    print('1. Melihat Data Admin Gudang')
    print('2. Mengubah Data Admin Gudang')
    print('3. Menghapus Data Produk')
    print('4. Melihat Data Celana')
    print('5. Menambah Data Celana')
    print('6. Mengubah Data Celana')
    print('7. Melihat Data Baju')
    print('8. Menambah Data Baju')
    print('9. Mengubah Data Baju')
    print('10. Melihat Data Tas')
    print('11. Menambah Data Tas')
    print('12. Mengubah Data Tas')
    print('13. LOGOUT')
    pilihFiturAdmin = input('Masukkan pilihan: ')
    print()
    return pilihFiturAdmin

def fiturKasir():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Kasir:')
    print('1. Melihat Data Kasir')
    print('2. Mengubah Data Kasir')
    print('3. Melihat Data Celana')
    print('4. Melihat Data Baju')
    print('5. Melihat Data Tas')
    print('6. Melihat Data Pesanan')
    print('7. Menambah Data Pesanan')
    print('8. Mengubah Data Pesanan')
    print('9. Melihat Data Detail Pesanan')
    print('10. Mengubah Data Detail Pesanan')
    print('11. LOGOUT')
    pilihFiturKasir = input('Masukkan pilihan: ')
    print()
    return pilihFiturKasir

def fiturCustomer():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Customer:')
    print('1. Melihat Data Customer')
    print('2. Mengubah Data Customer')
    print('3. Melihat Data Celana')
    print('4. Melihat Data Baju')
    print('5. Melihat Data Tas')
    print('6. Melihat Data ID Detail Pesanan Terakhir')
    print('7. Menambah Data Detail Pesanan')
    print('8. Mengubah Data Detail Pesanan')
    print('9. Melihat Data Detail Pesanan')
    print('10. Melihat Riwayat Pesanan')
    print('11. LOGOUT')

    pilihFiturCustomer = input('Masukkan pilihan: ')
    print()
    return pilihFiturCustomer

while jalanUser:
    pilihUser = pilihanUser()
    if pilihUser == '1':
        jalanPemilik = True
        
        while jalanPemilik:
            pilihPemilik= tampilanPemilik()
            if pilihPemilik == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                accept_Login = User.Login.login(username, password)
                if accept_Login == False:
                    break

                jalanFiturPemilik = True

                while jalanFiturPemilik:
                    pilihFiturPemilik = fiturPemilik()
                    if pilihFiturPemilik == '1':
                        tampilkanDataUser()
                    elif pilihFiturPemilik == '2':
                        hapusDataUser()
                    elif pilihFiturPemilik == '3':
                        tampilkanDataPemilik()
                    elif pilihFiturPemilik == '4':
                        tambahDataPemilik()
                    elif pilihFiturPemilik == '5':
                        ubahDataPemilik()
                    elif pilihFiturPemilik == '6':
                        tampilkanDataAdmin()
                    elif pilihFiturPemilik == '7':
                        tambahDataAdmin()
                    elif pilihFiturPemilik == '8':
                        ubahDataAdmin()
                    elif pilihFiturPemilik == '9':
                        tampilkanDataKasir()
                    elif pilihFiturPemilik == '10':
                        tambahDataKasir()
                    elif pilihFiturPemilik == '11':
                        ubahDataKasir()
                    elif pilihFiturPemilik == '12':
                        tampilkanDataCustomer()
                    elif pilihFiturPemilik == '13':
                        tambahDataCustomer()
                    elif pilihFiturPemilik == '14':
                        ubahDataCustomer()
                    elif pilihFiturPemilik == '15':
                        tampilkanDataCelana()
                    elif pilihFiturPemilik == '16':
                        tampilkanDataBaju()
                    elif pilihFiturPemilik == '17':
                        tampilkanDataTas()
                    elif pilihFiturPemilik == '18':
                        tampilkanSatuDataDetPesananPemilik()
                    elif pilihFiturPemilik == '19':
                        exit()

            elif pilihPemilik == '2':
                jalanRegister = True

                while jalanRegister:
                    pilihRegister = register()
                    if pilihRegister == '1':
                        lihatIDUser()
                    elif pilihRegister == '2':
                        tambahDataPemilik()
                        
            elif pilihPemilik == '3':
                exit()
    
    elif pilihUser == '2':
        jalanAdmin = True

        while jalanAdmin:
            pilihAdmin= tampilanAdmin()
            if pilihAdmin == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                accept_Login = User.Login.login(username, password)
                if accept_Login == False:
                    break

                jalanFiturAdmin = True

                while jalanFiturAdmin:
                    pilihFiturAdmin = fiturAdmin()
                    if pilihFiturAdmin == '1':
                        tampilkanSatuDataAdmin()
                    elif pilihFiturAdmin == '2':
                        ubahDataAdmin()
                    elif pilihFiturAdmin == '3':
                        hapusDataProduk()
                    elif pilihFiturAdmin == '4':
                        tampilkanDataCelana()
                    elif pilihFiturAdmin == '5':
                        tambahDataCelana()
                    elif pilihFiturAdmin == '6':
                        ubahDataCelana()
                    elif pilihFiturAdmin == '7':
                        tampilkanDataBaju()
                    elif pilihFiturAdmin == '8':
                        tambahDataBaju()
                    elif pilihFiturAdmin == '9':
                        ubahDataBaju()
                    elif pilihFiturAdmin == '10':
                        tampilkanDataTas()
                    elif pilihFiturAdmin == '11':
                        tambahDataTas()
                    elif pilihFiturAdmin == '12':
                        ubahDataTas()
                    elif pilihFiturAdmin == '13':
                        exit()

            elif pilihAdmin == '2':
                jalanRegister = True

                while jalanRegister:
                    pilihRegister = register()
                    if pilihRegister == '1':
                        lihatIDUser()
                    elif pilihRegister == '2':
                        tambahDataAdmin()
                        
            elif pilihAdmin == '3':
                exit()

    elif pilihUser == '3':
        jalanKasir = True

        while jalanKasir:
            pilihKasir= tampilanKasir()
            if pilihKasir == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                accept_Login = User.Login.login(username, password)
                if accept_Login == False:
                    break

                jalanFiturKasir = True

                while jalanFiturKasir:
                    pilihFiturKasir = fiturKasir()
                    if pilihFiturKasir == '1':
                        tampilkanSatuDataKasir()
                    elif pilihFiturKasir == '2':
                        ubahDataKasir()
                    elif pilihFiturKasir == '3':
                        tampilkanDataCelana()
                    elif pilihFiturKasir == '4':
                        tampilkanDataBaju()
                    elif pilihFiturKasir == '5':
                        tampilkanDataTas()
                    elif pilihFiturKasir == '6':
                        tampilkanDataPesanan()
                    elif pilihFiturKasir == '7':
                        tambahDataPesanan()
                    elif pilihFiturKasir == '8':
                        ubahDataPesanan()
                    elif pilihFiturKasir == '9':
                        tampilkanSatuDataDetPesananPemilik()
                    elif pilihFiturKasir == '10':
                        ubahDataDetPesananKasir()
                    elif pilihFiturKasir == '11':
                        exit()

            elif pilihKasir == '2':
                jalanRegister = True

                while jalanRegister:
                    pilihRegister = register()
                    if pilihRegister == '1':
                        lihatIDUser()
                    elif pilihRegister == '2':
                        tambahDataKasir()
                        
            elif pilihKasir == '3':
                exit()

    elif pilihUser == '4':
        jalanCustomer = True

        while jalanCustomer:
            pilihCustomer= tampilanCustomer()
            if pilihCustomer == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                accept_Login = User.Login.login(username, password)
                if accept_Login == False:
                    break

                jalanFiturCustomer = True

                while jalanFiturCustomer:
                    pilihFiturCustomer = fiturCustomer()
                    if pilihFiturCustomer == '1':
                        tampilkanSatuDataCustomer()
                    elif pilihFiturCustomer == '2':
                        ubahDataCustomer()
                    elif pilihFiturCustomer == '3':
                        tampilkanDataCelana()
                    elif pilihFiturCustomer == '4':
                        tampilkanDataBaju()
                    elif pilihFiturCustomer == '5':
                        tampilkanDataTas()
                    elif pilihFiturCustomer == '6':
                        lihatIDDetPesanan()
                    elif pilihFiturCustomer == '7':
                        tambahDataDetPesanan()
                    elif pilihFiturCustomer == '8':
                        ubahDataDetPesanan()
                    elif pilihFiturCustomer == '9':
                        tampilkanSatuDataDetPesanan()
                    elif pilihFiturCustomer == '10':
                        tampilkanSatuDataDetPesananCus()
                    elif pilihFiturCustomer == '11':
                        exit()

            elif pilihCustomer == '2':
                jalanRegister = True

                while jalanRegister:
                    pilihRegister = register()
                    if pilihRegister == '1':
                        lihatIDUser()
                    elif pilihRegister == '2':
                        tambahDataCustomer()
                        
            elif pilihCustomer == '3':
                exit()

