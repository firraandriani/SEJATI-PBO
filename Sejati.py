import sqlite3

class User:
    def __init__(self):
        self.con = sqlite3.connect('sejati.db')
        self.cursor = self.con.cursor()
    
    def executeQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_results

    def setDataUser(self, id_user, username, password, namaLengkap, tanggalLahir, status, role):
        self.query = 'INSERT INTO user (id_user, username, password, namaLengkap, tanggalLahir, status, role) VALUES (%s, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
        self.query = self.query % (id_user, username, password, namaLengkap, tanggalLahir, status, role)
        self.executeQuery(self.query)
    
    def setUbahDataUser(self, id_user, username, password, namaLengkap, tanggalLahir, status, role):
        self.query = 'UPDATE user set id_user = %s, username = \'%s\', password = \'%s\', namaLengkap = \'%s\', tanggalLahir = \'%s\', status = \'%s\', role = \'%s\' WHERE id_user = %s'
        self.query = self.query % (id_user, username, password, namaLengkap, tanggalLahir, status, role, id_user)
        self.executeQuery(self.query)

    def getDataUser(self):
        self.query = 'SELECT * FROM user'
        id_user = self.executeQuery(self.query, retVal=True)
        return id_user

class Admin(User):
    def setDataAdmin(self, id_admin, bagian, jamKerja, id_user, username, password, namaLengkap, tanggalLahir, status, role):
        self.setDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        id_user = self.getDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        self.query = 'INSERT INTO admin (id_admin, bagian, jamKerja, id_user, username, password, namaLengkap, tanggalLahir, status, role) values (%s, \'%s\', \'%s\', %s, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
        self.query = self.query % (id_admin, bagian, jamKerja, id_user[0][0])
        self.executeQuery(self.query)
    
    def setUbahDataAdmin(self, id_user, id_admin, bagian, jamKerja):
        self.query = 'UPDATE admin set id_admin = %s, bagian = \'%s\', jamKerja = \'%s\', id_user = %s WHERE id_admin = %s'
        self.query = self.query % (id_admin, bagian, jamKerja, id_user, id_admin)
        self.executeQuery(self.query)

    def getDaftarAdmin(self):
        self.query = 'SELECT t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.id_admin, t1.bagian, t1.jamKerja FROM admin t1 join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar
    
    def getDataAdmin(self):
        self.query = 'SELECT t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.id_admin, t1.bagian, t1.jamKerja FROM admin t1 join user t2 on t1.id_user=t2.id_user WHERE username = \'%s\'' 
        self.query = self.query % (username)
        daftar = self.executeQuery(self.query, True)
        return daftar

class Pemilik(User):
    def setDataPemilik(self, id_user, id_pemilik):
        self.query = 'INSERT INTO pemilik (id_pemilik, id_user) values (%s, %s)' 
        self.query = self.query % (id_pemilik, id_user)
        self.executeQuery(self.query)

    def setUbahDataPemilik(self, id_user, id_pemilik):
        self.query = 'UPDATE pemilik set id_pemilik = %s, id_user = %s WHERE id_pemilik = %s'
        self.query = self.query % (id_pemilik, id_user, id_pemilik)
        self.executeQuery(self.query)

    def getDaftarPemilik(self):
        self.query = 'SELECT t1.id_pemilik, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role FROM pemilik t1 join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Customer(User):
    def setDataCustomer(self, id_user, id_customer, nomorHandphone, alamatRumah):
        self.query = 'INSERT INTO customer (id_customer, nomorHandphone, alamatRumah, id_user) values (%s, \'%s\', \'%s\', %s)' 
        self.query = self.query % (id_customer, nomorHandphone, alamatRumah, id_user)
        self.executeQuery(self.query)
    
    def setUbahDataCustomer(self, id_user, id_customer, nomorHandphone, alamatRumah):
        self.query = 'UPDATE customer set id_customer = %s, nomorHandphone = \'%s\', alamatRumah = \'%s\', id_user = %s WHERE id_customer = %s'
        self.query = self.query % (id_customer, nomorHandphone, alamatRumah, id_user, id_customer)
        self.executeQuery(self.query)

    def getDaftarCustomer(self):
        self.query = 'SELECT t1.id_customer, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.nomorHandphone, t1.alamatRumah FROM customer t1 join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataCustomer(self):
        self.query = 'SELECT t1.id_customer, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.nomorHandphone, t1.alamatRumah FROM customer t1 join user t2 on t1.id_user=t2.id_user WHERE username = \'%s\'' 
        self.query = self.query % (username)
        daftar = self.executeQuery(self.query, True)
        return daftar

class Kasir(User):
    def setDataKasir(self, id_user, id_kasir, jamKerja, nomorHandphone):
        self.query = 'INSERT INTO kasir (id_kasir, jamKerja, nomorHandphone, id_user) values (%s, \'%s\', \'%s\', %s)' 
        self.query = self.query % (id_kasir, jamKerja, nomorHandphone, id_user)
        self.executeQuery(self.query)
    
    def setUbahDataKasir(self, id_user, id_kasir, jamKerja, nomorHandphone):
        self.query = 'UPDATE kasir set id_kasir = %s, jamKerja = \'%s\', nomorHandphone = \'%s\', id_user = %s WHERE id_kasir = %s'
        self.query = self.query % (id_kasir, jamKerja, nomorHandphone, id_user, id_kasir)
        self.executeQuery(self.query)

    def getDaftarKasir(self):
        self.query = 'SELECT t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.id_kasir, t1.jamKerja, t1.nomorHandphone FROM kasir t1 join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataKasir(self):
        self.query = 'SELECT t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.id_kasir, t1.jamKerja, t1.nomorHandphone FROM kasir t1 join user t2 on t1.id_user=t2.id_user WHERE username = \'%s\'' 
        self.query = self.query % (username)
        daftar = self.executeQuery(self.query, True)
        return daftar

class Produk:
    def __init__(self):
        self.con = sqlite3.connect('sejati.db')
        self.cursor = self.con.cursor()
    
    def executeQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_results

    def setDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok):
        self.query = 'INSERT INTO produk (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok) VALUES (%s, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', %s, %s)' 
        self.query = self.query % (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        self.executeQuery(self.query)
    
    def setUbahDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok):
        self.query = 'UPDATE produk SET id = %s, jenisProduk = \'%s\', merk = \'%s\', deskripsi = \'%s\', warna = \'%s\', ukuran = \'%s\', jenisBahan = \'%s\',  harga = %s, stok = %s  WHERE id = %s'
        self.query = self.query % (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, id)
        self.executeQuery(self.query)

    def getDataProduk(self):
        self.query = 'SELECT * FROM produk'
        id = self.executeQuery(self.query, retVal=True)
        return id

class Celana(Produk):
    def setDataCelana(self, id, id_celana, modelCelana):
        self.query = 'INSERT INTO celana (id_celana, modelCelana, id) values (%s, \'%s\', %s)' 
        self.query = self.query % (id_celana, modelCelana, id)
        self.executeQuery(self.query)
    
    def setUbahDataCelana(self, id, id_celana, modelCelana):
        self.query = 'UPDATE celana set id_celana = %s, modelCelana = \'%s\', id = %s WHERE id_celana = %s'
        self.query = self.query % (id_celana, modelCelana, id, id_celana)
        self.executeQuery(self.query)

    def getDaftarCelana(self):
        self.query = 'SELECT t1.id_celana, t2.id, t2.jenisProduk, t2.merk, t2.deskripsi, t2.warna, t2.ukuran, t2.jenisBahan, t2.harga, t2.stok, t1.modelCelana FROM celana t1 join produk t2 on t1.id=t2.id' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Baju(Produk):
    def setDataBaju(self, id, id_baju, modelBaju):
        self.query = 'INSERT INTO baju (id_baju, modelBaju, id) values (%s, \'%s\', %s)' 
        self.query = self.query % (id_baju, modelBaju, id)
        self.executeQuery(self.query)
    
    def setUbahDataBaju(self, id, id_baju, modelBaju):
        self.query = 'UPDATE baju set id_baju = %s, modelBaju = \'%s\', id = %s WHERE id_baju = %s'
        self.query = self.query % (id_baju, modelBaju, id, id_baju)
        self.executeQuery(self.query)

    def getDaftarBaju(self):
        self.query = 'SELECT t1.id_baju, t2.id, t2.jenisProduk, t2.merk, t2.deskripsi, t2.warna, t2.ukuran, t2.jenisBahan, t2.harga, t2.stok, t1.modelBaju FROM baju t1 join produk t2 on t1.id=t2.id' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Tas(Produk):
    def setDataTas(self, id, id_tas, namaTas):
        self.query = 'INSERT INTO tas (id_tas, namaTas, id) values (%s, \'%s\', %s)' 
        self.query = self.query % (id_tas, namaTas, id)
        self.executeQuery(self.query)
    
    def setUbahDataTas(self, id, id_tas, namaTas):
        self.query = 'UPDATE tas set id_tas = %s, namaTas = \'%s\', id = %s WHERE id_tas = %s'
        self.query = self.query % (id_tas, namaTas, id, id_tas)
        self.executeQuery(self.query)

    def getDaftarTas(self):
        self.query = 'SELECT t1.id_tas, t2.id, t2.jenisProduk, t2.merk, t2.deskripsi, t2.warna, t2.ukuran, t2.jenisBahan, t2.harga, t2.stok, t1.namaTas FROM tas t1 join produk t2 on t1.id=t2.id' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Pesanan(Kasir, User):
    def setDataPesanan(self, id_kasir, id, statusPesanan, tanggalPenerimaan, verifikasi):
        self.query = 'INSERT INTO pesanan (id, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir) values (%s, \'%s\', \'%s\', \'%s\', %s)' 
        self.query = self.query % (id, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir)
        print(self.query)
        self.executeQuery(self.query)
    
    def setUbahDataPesanan(self, id_kasir, id, statusPesanan, tanggalPenerimaan, verifikasi):
        self.query = 'UPDATE pesanan set id = %s, statusPesanan = \'%s\', tanggalPenerimaan = \'%s\', verifikasi = \'%s\', id_kasir = %s WHERE id = %s'
        self.query = self.query % (id, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir, id)
        self.executeQuery(self.query)

    def getDaftarPesanan(self):
        self.query = 'SELECT t1.id, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t3.id_user, t3.username, t3.password, t3.namaLengkap, t3.tanggalLahir, t3.status, t3.role, t2.id_kasir, t2.jamKerja, t2.nomorHandphone FROM pesanan t1 INNER JOIN kasir t2 ON t1.id_kasir=t2.id_kasir INNER JOIN user t3 ON t2.id_user=t3.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar
    
    def getDataPesanan(self):
        self.query = 'SELECT t1.id, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t3.namaLengkap, t3.role, t2.nomorHandphone FROM pesanan t1 join kasir t2 on t1.id_kasir=t2.id_kasir join user t3 on t2.id_user=t3.id_user WHERE id = %s'
        self.query = self.query % (id)
        daftar = self.executeQuery(self.query, True)
        return daftar

class DetailPesanan(Pesanan, Tas, Celana, Baju, Customer):
    def setDataDetailPesanan(self, id, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPembelian, hargaTotalProduk, id_pesanan, id_tas, id_celana, id_baju, id_customer):
        self.query = 'INSERT INTO detailPesanan (id, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPembelian, hargaTotalProduk, id_pesanan, id_tas, id_celana, id_baju, id_customer) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' 
        self.query = self.query % (id, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPembelian, hargaTotalProduk, id_pesanan, id_tas, id_celana, id_baju, id_customer)
        self.executeQuery(self.query)
    
    def getDaftarPesanan(self):
        self.query = 'SELECT t1.id, t1.tanggalPesanan, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t2.id_kasir \ FROM pesanan t1 \ join kasir t2 on t1.id_kasir=t2.id_kasir' 
        daftar = self.executeQuery(self.query, True)
        return daftar

pengguna = User()
adm = Admin()
owner = Pemilik()
pelanggan = Customer()
casher = Kasir()
prod = Produk()
cel = Celana()
baj = Baju()
taS = Tas()
order = Pesanan()
detailOrder = DetailPesanan()
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

def tampilanPemilik():
    print(70*"*")
    print('SELAMAT DATANG PEMILIK'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Menu Pemilik:')
    print('1. LOGIN')
    print('2. Membuat Data User')
    print('3. Membuat Data Pemilik')
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
    print('2. Membuat Data User')
    print('3. Membuat Data Admin Gudang')
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
    print('2. Membuat Data User')
    print('3. Membuat Data Kasir')
    pilihKasir = input('Masukkan pilihan: ')
    print()
    return pilihKasir

def tampilanCustomer():
    print(70*"*")
    print('SELAMAT DATANG KASIR'.center(70, "*"))
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Menu Pemilik:')
    print('1. LOGIN')
    print('2. Membuat Data User')
    print('3. Membuat Data Customer')
    pilihCustomer = input('Masukkan pilihan: ')
    print()
    return pilihCustomer

def tambahDataUser():
    global pengguna
    print('\nTambah data User')
    id_user = input('Masukkan ID User: ')
    username = input('Masukkan Username: ')
    password = input('Masukkan Password: ')
    namaLengkap = input('Masukkan Nama Lengkap: ')
    tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    role = input('Masukkan role(PEMILIK, ADMIN, CUSTOMER, KASIR): ')
    pengguna.setDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataUser():
    global pengguna
    print('\nDaftar User')
    daftarPengguna = pengguna.getDataUser()
    for user_row in daftarPengguna:
        print(user_row)
    print('\n')

def ubahDataUser():
    global pengguna
    print('\nUbah data User berdasarkan ID User')
    id_user = input('Masukkan ID User: ')
    username = input('Masukkan Username: ')
    password = input('Masukkan Password: ')
    namaLengkap = input('Masukkan Nama Lengkap: ')
    tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    role = input('Masukkan role(PEMILIK, ADMIN, CUSTOMER, KASIR): ')
    pengguna.setUbahDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataPemilik():
    global owner
    print('\nTambah data Pemilik')
    id_pemilik = input('Masukkan ID Pemilik: ')
    id_user = input('Masukkan ID User: ')
    owner.setDataPemilik(id_pemilik, id_user)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataPemilik():
    global owner
    print('\nDaftar Pemilik')
    daftarPemilik = owner.getDaftarPemilik()
    for user_row in daftarPemilik:
        print(user_row)
    print('\n')

def ubahDataPemilik():
    global owner
    print('\nUbah data Pemilik berdasarkan ID Pemilik')
    id_pemilik = input('Masukkan ID Pemilik: ')
    id_user = input('Masukkan ID User: ')
    owner.setUbahDataPemilik(id_user, id_pemilik)
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataAdmin():
    global adm
    print('\nTambah Data Admin Gudang')
    id_admin = input('Masukkan ID Admin Gudang: ')
    bagian = input('Masukkan Bagian Admin Gudang: ')
    jamKerja = input('Masukkan Jam Kerja Admin Gudang: ')
    id_user = input('Masukkan ID User: ')
    username = input('Masukkan Username: ')
    password = input('Masukkan Password: ')
    namaLengkap = input('Masukkan Nama Lengkap: ')
    tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    role = input('Masukkan role(PEMILIK, ADMIN, CUSTOMER, KASIR): ')
    adm.setDataAdmin(id_admin, bagian, jamKerja, id_user, username, password, namaLengkap, tanggalLahir, status, role)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataAdmin():
    global adm
    print('\nDaftar Admin Gudang')
    daftarAdmin = adm.getDaftarAdmin()
    for user_row in daftarAdmin:
        print(user_row)
    print('\n')

def ubahDataAdmin():
    global adm
    print('\nUbah Data Admin Gudang berdasarkan ID Admin Gudang')
    id_admin = input('Masukkan ID Admin Gudang: ')
    bagian = input('Masukkan Bagian Admin Gudang: ')
    jamKerja = input('Masukkan Jam Kerja Admin Gudang: ')
    id_user = input('Masukkan ID User: ')
    adm.setUbahDataAdmin(id_user, id_admin, bagian, jamKerja)
    print('\n')
    print('Data Berhasil Diubah')

def tampilkanSatuDataAdmin():
    global adm
    print('\nData Admin Gudang')
    username = input('Masukkan Username: ')
    daftarAdmin = adm.getDataAdmin() 
    for user_row in daftarAdmin:
        print(user_row)
    print('\n')

def tambahDataKasir():
    global casher
    print('\nTambah Data Kasir')
    id_kasir = input('Masukkan ID Kasir: ')
    jamKerja = input('Masukkan Jam Kerja Kasir: ')
    nomorHandphone = input('Masukkan nomorHandphone Kasir: ')
    id_user = input('Masukkan ID User: ')
    casher.setDataKasir(id_user, id_kasir, jamKerja, nomorHandphone)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataKasir():
    global casher
    print('\nDaftar Kasir')
    daftarKasir = casher.getDaftarKasir()
    for user_row in daftarKasir:
        print(user_row)
    print('\n')

def ubahDataKasir():
    global casher
    print('\nUbah Data Kasir berdasarkan ID Kasir')
    id_kasir = input('Masukkan ID Kasir: ')
    jamKerja = input('Masukkan Jam Kerja Kasir: ')
    nomorHandphone = input('Masukkan nomorHandphone Kasir: ')
    id_user = input('Masukkan ID User: ')
    casher.setUbahDataKasir(id_user, id_kasir, jamKerja, nomorHandphone)
    print('\n')
    print('Data Berhasil Diubah')

def tampilkanSatuDataKasir():
    global casher
    print('\nData Kasir')
    username = input('Masukkan Username: ')
    daftarKasir = casher.getDataKasir()
    for user_row in daftarKasir:
        print(user_row)
    print('\n')

def tambahDataCustomer():
    global pelanggan
    print('\nTambah Data Pelanggan')
    id_customer = input('Masukkan ID Customer: ')
    nomorHandphone = input('Masukkan nomorHandphone Customer: ')
    alamatRumah = input('Masukkan Alamat Rumah Customer: ')
    id_user = input('Masukkan ID User: ')
    pelanggan.setDataCustomer(id_user, id_customer, nomorHandphone, alamatRumah)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataCustomer():
    global pelanggan
    print('\nDaftar Customer')
    daftarCustomer = pelanggan.getDaftarCustomer()
    for user_row in daftarCustomer:
        print(user_row)
    print('\n')

def ubahDataCustomer():
    global pelanggan
    print('\nUbah Data Customer berdasarkan ID Customer')
    id_customer = input('Masukkan ID Customer: ')
    nomorHandphone = input('Masukkan nomorHandphone Customer: ')
    alamatRumah = input('Masukkan Alamat Rumah Customer: ')
    id_user = input('Masukkan ID User: ')
    pelanggan.setUbahDataCustomer(id_user, id_customer, nomorHandphone, alamatRumah)
    print('\n')
    print('Data Berhasil Diubah')

def tampilkanSatuDataCustomer():
    global pelanggan
    print('\nData Customer')
    username = input('Masukkan Username: ')
    daftarCustomer = pelanggan.getDataCustomer()
    for user_row in daftarCustomer:
        print("ID Customer: ", user_row[0])
        print("ID User: ", user_row[0])
        print("Username: ", user_row[1])
        print("Password: ", user_row[2])
        print("Nama Lengkap: ", user_row[3])
        print("Tanggal Lahir: ", user_row[4])
        print("Status: ", user_row[5])
        print("Role: ", user_row[6])
        print("Nomor Handphone: ", user_row[1])
        print("Alamat Rumah: ", user_row[2])

def tambahDataProduk():
    global prod
    print('\nTambah Data Produk')
    id = input('Masukkan ID Produk: ')
    jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    merk = input('Memasukkan Merk: ')
    deskripsi = input("Memasukkan Deskripsi Produk: ")
    warna = input('Memasukkan Warna: ')
    ukuran = input('Memasukkan Ukuran: ')
    jenisBahan = input('Memasukkan JenisBahan: ')
    harga = int(input('Memasukkan Harga: '))
    stok = int(input('Memasukkan Stok: '))
    prod.setDataProduk(id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataProduk():
    global prod
    print('\nDaftar Produk')
    daftarProduk = prod.getDataProduk()
    for user_row in daftarProduk:
        print(user_row)
    print('\n')

def ubahDataProduk():
    global prod
    print('\nUbah data Produk berdasarkan ID Prod')
    id = input('Masukkan ID Produk: ')
    jenisProduk = input ('Masukkan Jenis Produk(TAS, CELANA, BAJU): ') 
    merk = input('Memasukkan Merk: ')
    deskripsi = input("Memasukkan Deskripsi Produk: ")
    warna = input('Memasukkan Warna: ')
    ukuran = input('Memasukkan Ukuran: ')
    jenisBahan = input('Memasukkan JenisBahan: ')
    harga = input('Memasukkan Harga: ')
    stok = input('Memasukkan Stok: ')
    prod.setUbahDataProduk(id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataCelana():
    global cel
    print('\nTambah Data Celana')
    id_celana = input('Masukkan ID Celana: ')
    modelCelana = input('Masukkan Model Celana: ')
    id = input('Masukkan Id Produk: ')
    cel.setDataCelana(id, id_celana, modelCelana)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataCelana():
    global cel
    print('\nDaftar Celana')
    daftarCelana = cel.getDaftarCelana()
    for user_row in daftarCelana:
        print(user_row)
    print('\n')

def ubahDataCelana():
    global cel
    print('\nUbah Data Celana berdasarkan ID Celana')
    id_celana = input('Masukkan ID Celana: ')
    modelCelana = input('Masukkan Model Celana: ')
    id = input('Masukkan Id Produk: ')
    cel.setUbahDataCelana(id, id_celana, modelCelana)
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataBaju():
    global baj
    print('\nTambah Data Baju')
    id_baju = input('Masukkan ID Baju: ')
    modelBaju = input('Masukkan Model Baju: ')
    id = input('Masukkan Id Produk: ')
    baj.setDataBaju(id, id_baju, modelBaju)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataBaju():
    global baj
    print('\nDaftar Baju')
    daftarBaju = baj.getDaftarBaju()
    for user_row in daftarBaju:
        print(user_row)
    print('\n')

def ubahDataBaju():
    global baj
    print('\nUbah Data Baju berdasarkan ID Baju')
    id_baju = input('Masukkan ID Baju: ')
    modelBaju = input('Masukkan Model Baju: ')
    id = input('Masukkan Id Produk: ')
    baj.setUbahDataBaju(id, id_baju, modelBaju)
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataTas():
    global taS
    print('\nTambah Data Tas')
    id_tas = input('Masukkan ID Tas: ')
    namaTas = input('Masukkan Nama Tas: ')
    id = input('Masukkan Id Produk: ')
    taS.setDataTas(id, id_tas, namaTas)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataTas():
    global taS
    print('\nDaftar Tas')
    daftarTas = taS.getDaftarTas()
    for user_row in daftarTas:
        print(user_row)
    print('\n')

def ubahDataTas():
    global taS
    print('\nUbah Data Tas berdasarkan ID Tas')
    id_tas = input('Masukkan ID Tas: ')
    namaTas = input('Masukkan Nama Tas: ')
    id = input('Masukkan Id Produk: ')
    taS.setUbahDataTas(id, id_tas, namaTas)
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataPesanan():
    global order
    print('\nTambah Data Pesanan')
    id = input('Masukkan ID Pesanan: ')
    statusPesanan = input('Masukkan Status Pesanan: ')
    tanggalPenerimaan = input('Masukkan Tanggal Penerimaan Pesanan: ')
    verifikasi = input('Masukkan Verifikasi Pesanan: ')
    id_kasir = input('Masukkan Id Kasir: ')
    order.setDataPesanan(id_kasir, id, statusPesanan, tanggalPenerimaan, verifikasi)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataPesanan():
    global order
    print('\nDaftar Pesanan')
    daftarOrder = order.getDaftarPesanan()
    for user_row in daftarOrder:
        print(user_row)
    print('\n')

def ubahDataPesanan():
    global order
    print('\nUbah Data Order berdasarkan ID Order')
    id = input('Masukkan ID Pesanan: ')
    statusPesanan = input('Masukkan Status Pesanan: ')
    tanggalPenerimaan = input('Masukkan Tanggal Penerimaan Pesanan: ')
    verifikasi = input('Masukkan Verifikasi Pesanan: ')
    id_kasir = input('Masukkan Id Kasir: ')
    order.setUbahDataPesanan(id_kasir, id, statusPesanan, tanggalPenerimaan, verifikasi)
    print('\n')
    print('Data Berhasil Diubah')

# def tambahDataDetPesanan():
#     global detailOrder
#     print('\nTambah Data Detail Pesanan')
#     id = input('Masukkan ID Detail Pesanan: ')
#     jumlahBaju = input('Masukkan jumlah baju yang dibeli: ')
#     jumlahCelana = input('Masukkan jumlah celana yang dibeli: ')
#     jumlahTas = input('Masukkan jumlah tas yang dibeli: ')
#     jumlahPembelian = jumlahBaju + jumlahCelana + jumlahTas
#     hargaTotalProduk = 
#     detailOrder.setDataDetailPesanan(id, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPembelian, hargaTotalProduk, id_pesanan, id_tas, id_celana, id_baju, id_customer)
#     print('\n')
#     print('Data Berhasil Ditambahkan')

def login(username, password):
    con=sqlite3.connect("sejati.db")
    cur =con.cursor()
    query = 'SELECT username, password FROM user where username=\'%s\' and password=\'%s\' '
    query = query % (username, password)
    cur.execute(query)
    con.commit()
    rows =cur.fetchall()
    accept_Login = True
    if (len(rows)) == 0:
        accept_Login = False

    if accept_Login == False:
        print("Login Gagal")
        print()

    elif username == rows[0][0] and password == rows[0][1]:
        accept_Login = True
        print("Login Sukses")
        print()
        return username
    con.close()

def fiturPemilik():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Pemilik:')
    print('1. Melihat Data User')
    print('2. Menambah Data User')
    print('3. Mengubah Data User')
    print('4. Melihat Data Pemilik')
    print('5. Menambah Data Pemilik')
    print('6. Mengubah Data Pemilik')
    print('7. Melihat Data Admin Gudang')
    print('8. Menambah Data Admin Gudang')
    print('9. Mengubah Data Admin Gudang')
    print('10. Melihat Data Kasir')
    print('11. Menambah Data Kasir')
    print('12. Mengubah Data Kasir')
    print('13. Melihat Data Customer')
    print('14. Menambah Data Customer')
    print('15. Mengubah Data Customer')
    print('16. Melihat Data Celana')
    print('17. Melihat Data Baju')
    print('18. Melihat Data Tas')
    pilihFiturPemilik = input('Masukkan pilihan: ')
    print()
    return pilihFiturPemilik

def fiturAdmin():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Admin Gudang:')
    print('1. Menambah Data User')
    print('2. Mengubah Data User')
    print('3. Melihat Data Admin Gudang')
    print('4. Menambah Data Admin Gudang')
    print('5. Mengubah Data Admin Gudang')
    print('6. Melihat Data Produk')
    print('7. Menambah Data Produk')
    print('8. Mengubah Data Produk')
    print('9. Melihat Data Celana')
    print('10. Menambah Data Celana')
    print('11. Mengubah Data Celana')
    print('12. Melihat Data Baju')
    print('13. Menambah Data Baju')
    print('14. Mengubah Data Baju')
    print('15. Melihat Data Tas')
    print('16. Menambah Data Tas')
    print('17. Mengubah Data Tas')
    pilihFiturAdmin = input('Masukkan pilihan: ')
    print()
    return pilihFiturAdmin

def fiturKasir():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Kasir:')
    print('1. Menambah Data User')
    print('2. Mengubah Data User')
    print('3. Melihat Data Kasir')
    print('4. Menambah Data Kasir')
    print('5. Mengubah Data Kasir')
    print('6. Melihat Data Celana')
    print('7. Melihat Data Baju')
    print('8. Melihat Data Tas')
    print('9. Melihat Data Pesanan')
    print('10. Menambah Data Pesanan')
    print('11. Mengubah Data Pesanan')
    pilihFiturKasir = input('Masukkan pilihan: ')
    print()
    return pilihFiturKasir

def fiturCustomer():
    print(70*"*")
    print('SIAPA (SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION)'.center(70, "*"))
    print(70*"*")
    print('Fitur Customer:')
    print('1. Menambah Data User')
    print('2. Mengubah Data User')
    print('3. Melihat Data Customer')
    print('4. Menambah Data Customer')
    print('5. Mengubah Data Customer')
    print('6. Melihat Data Pesanan')
    print('7. Menambah Data Pesanan')
    print('8. Mengubah Data Pesanan')
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
                login(username, password)
                jalanFiturPemilik = True

                while jalanFiturPemilik:
                    pilihFiturPemilik = fiturPemilik()
                    if pilihFiturPemilik == '1':
                        tampilkanDataUser()
                    elif pilihFiturPemilik == '2':
                        tambahDataUser()
                    elif pilihFiturPemilik == '3':
                        ubahDataUser()
                    elif pilihFiturPemilik == '4':
                        tampilkanDataPemilik()
                    elif pilihFiturPemilik == '5':
                        tambahDataPemilik()
                    elif pilihFiturPemilik == '6':
                        ubahDataPemilik()
                    elif pilihFiturPemilik == '7':
                        tampilkanDataAdmin()
                    elif pilihFiturPemilik == '8':
                        tambahDataAdmin()
                    elif pilihFiturPemilik == '9':
                        ubahDataAdmin()
                    elif pilihFiturPemilik == '10':
                        tampilkanDataKasir()
                    elif pilihFiturPemilik == '11':
                        tambahDataKasir()
                    elif pilihFiturPemilik == '12':
                        ubahDataKasir()
                    elif pilihFiturPemilik == '13':
                        tampilkanDataCustomer()
                    elif pilihFiturPemilik == '14':
                        tambahDataCustomer()
                    elif pilihFiturPemilik == '15':
                        ubahDataCustomer()
                    elif pilihFiturPemilik == '16':
                        tampilkanDataCelana()
                    elif pilihFiturPemilik == '17':
                        tampilkanDataBaju()
                    elif pilihFiturPemilik == '18':
                        tampilkanDataTas()

            elif pilihPemilik == '2':
                tambahDataUser()
            elif pilihPemilik == '3':
                tambahDataPemilik()
    
    elif pilihUser == '2':
        jalanAdmin = True

        while jalanAdmin:
            pilihAdmin= tampilanAdmin()
            if pilihAdmin == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                login(username, password)
                jalanFiturAdmin = True

                while jalanFiturAdmin:
                    pilihFiturAdmin = fiturAdmin()
                    if pilihFiturAdmin == '1':
                        tambahDataUser()
                    elif pilihFiturAdmin == '2':
                        ubahDataUser()
                    elif pilihFiturAdmin == '3':
                        tampilkanSatuDataAdmin()
                    elif pilihFiturAdmin == '4':
                        tambahDataAdmin()
                    elif pilihFiturAdmin == '5':
                        ubahDataAdmin()
                    elif pilihFiturAdmin == '6':
                        tampilkanDataProduk()
                    elif pilihFiturAdmin == '7':
                        tambahDataProduk()
                    elif pilihFiturAdmin == '8':
                        ubahDataProduk()
                    elif pilihFiturAdmin == '9':
                        tampilkanDataCelana()
                    elif pilihFiturAdmin == '10':
                        tambahDataCelana()
                    elif pilihFiturAdmin == '11':
                        ubahDataCelana()
                    elif pilihFiturAdmin == '12':
                        tampilkanDataBaju()
                    elif pilihFiturAdmin == '13':
                        tambahDataBaju()
                    elif pilihFiturAdmin == '14':
                        ubahDataBaju()
                    elif pilihFiturAdmin == '15':
                        tampilkanDataTas()
                    elif pilihFiturAdmin == '16':
                        tambahDataTas()
                    elif pilihFiturAdmin == '17':
                        ubahDataTas()

            elif pilihAdmin == '2':
                tambahDataUser()
            elif pilihAdmin == '3':
                tambahDataAdmin()

    elif pilihUser == '3':
        jalanKasir = True

        while jalanKasir:
            pilihKasir= tampilanKasir()
            if pilihKasir == '1':
                username = input('Username : ')
                password = input('Password : ')
                login(username, password)
                jalanFiturKasir = True

                while jalanFiturKasir:
                    pilihFiturKasir = fiturKasir()
                    if pilihFiturKasir == '1':
                        tambahDataUser()
                    elif pilihFiturKasir == '2':
                        ubahDataUser()
                    elif pilihFiturKasir == '3':
                        tampilkanSatuDataKasir()
                    elif pilihFiturKasir == '4':
                        tambahDataKasir()
                    elif pilihFiturKasir == '5':
                        ubahDataKasir()
                    elif pilihFiturKasir == '6':
                        tampilkanDataCelana()
                    elif pilihFiturKasir == '7':
                        tampilkanDataBaju()
                    elif pilihFiturKasir == '8':
                        tampilkanDataTas()
                    elif pilihFiturKasir == '9':
                        tampilkanDataPesanan()
                    elif pilihFiturKasir == '10':
                        tambahDataPesanan()
                    elif pilihFiturKasir == '11':
                        ubahDataPesanan()

            elif pilihKasir == '2':
                tambahDataUser()
            elif pilihKasir == '3':
                tambahDataKasir()

    elif pilihUser == '4':
        jalanCustomer = True

        while jalanCustomer:
            pilihCustomer= tampilanCustomer()
            if pilihCustomer == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                login(username, password)
                jalanFiturCustomer = True

                while jalanFiturCustomer:
                    pilihFiturCustomer = fiturCustomer()
                    if pilihFiturCustomer == '1':
                        tambahDataCustomer()
                    elif pilihFiturCustomer == '2':
                        ubahDataCustomer()
                    elif pilihFiturCustomer == '3':
                        tampilkanSatuDataCustomer()
                    elif pilihFiturCustomer == '4':
                        tambahDataCustomer()
                    elif pilihFiturCustomer == '5':
                        ubahDataCustomer()
                    elif pilihFiturCustomer == '3':
                        tampilkanSatuDataCustomer()
                    elif pilihFiturCustomer == '4':
                        tambahDataCustomer()
                    elif pilihFiturCustomer == '5':
                        ubahDataCustomer()

            elif pilihCustomer == '2':
                tambahDataUser()
            elif pilihCustomer == '3':
                tambahDataCustomer()
