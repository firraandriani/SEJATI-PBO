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
    def setDataAdmin(self, id_user, username, password, namaLengkap, tanggalLahir, status, role, id_admin, bagian, jamKerja):
        self.setDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        id_user = self.getDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        self.query = 'INSERT INTO admin (id_admin, bagian, jamKerja, id_user) \ values (%d, \'%s\', \'%s\', %d)' 
        self.query = self.query % (id_admin, bagian, jamKerja, id_user[0][0])
        self.executeQuery(self.query)
    
    def getDaftarAdmin(self):
        self.query = 'SELECT t1.id_admin, t1.bagian, t1.jamKerja, t2.id_user \ FROM admin t1 \ join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Pemilik(User):
    def setDataPemilik(self, id_user, username, password, namaLengkap, tanggalLahir, status, role, id_pemilik):
        self.setDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        id_user = self.getDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        self.query = 'INSERT INTO pemilik (id_pemilik, id_user) \ values (%d, %d)' 
        self.query = self.query % (id_pemilik, id_user[0][0])
        self.executeQuery(self.query)
    
    def getDaftarPemilik(self):
        self.query = 'SELECT t1.id_pemilik, t2.id_user \ FROM pemilik t1 \ join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Customer(User):
    def setDataCustomer(self, id_user, username, password, namaLengkap, tanggalLahir, status, role, id_customer, nomorHandphone, alamatRumah):
        self.setDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        id_user = self.getDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        self.query = 'INSERT INTO customer (id_customer, nomorHandphone, alamatRumah, id_user) \ values (%d, \'%s\', \'%s\', %d)' 
        self.query = self.query % (id_customer, nomorHandphone, alamatRumah, id_user[0][0])
        self.executeQuery(self.query)
    
    def getDaftarCustomer(self):
        self.query = 'SELECT t1.id_customer, t1.nomorHandphone, t1.alamatRumah, t2.id_user \ FROM customer t1 \ join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Kasir(User):
    def setDataKasir(self, id_user, username, password, namaLengkap, tanggalLahir, status, role, id_kasir, jamKerja, nomorHandphone):
        self.setDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        id_user = self.getDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
        self.query = 'INSERT INTO kasir (id_kasir, jamKerja, nomorHandphone, id_user) \ values (%d, \'%s\', \'%s\', %d)' 
        self.query = self.query % (id_kasir, jamKerja, nomorHandphone, id_user[0][0])
        self.executeQuery(self.query)
    
    def getDaftarKasir(self):
        self.query = 'SELECT t1.id_kasir, t1.jamKerja, t1.nomorHandphone, t2.id_user \ FROM kasir t1 \ join user t2 on t1.id_user=t2.id_user' 
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
        self.query = 'INSERT INTO produk (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok) \ VALUES (%d, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\' %d, %d)' 
        self.query = self.query % (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        self.executeQuery(self.query)
    
    def getDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok):
        self.query = 'SELECT id FROM produk \ where id=%d and jenisProduk=\'%s\' and merk=\'%s\' and deskripsi=\'%s\' and warna=\'%s\' and ukuran=\'%s\' and jenisBahan=\'%s\' and harga=%d and stok=%d ' 
        self.query = self.query % (id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        id = self.executeQuery(self.query, retVal=True)
        return id

class Celana(Produk):
    def setDataCelana(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, id_celana, modelCelana):
        self.setDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        id = self.getDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        self.query = 'INSERT INTO celana (id_celana, modelCelana, id) \ values (%d, \'%s\', %d)' 
        self.query = self.query % (id_celana, modelCelana, id[0][0])
        self.executeQuery(self.query)
    
    def getDaftarCelana(self):
        self.query = 'SELECT t1.id_celana, t1.modelCelana, t2.id \ FROM celana t1 \ join produk t2 on t1.id=t2.id' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Baju(Produk):
    def setDataBaju(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, id_baju, modelBaju):
        self.setDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        id = self.getDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        self.query = 'INSERT INTO celana (id_baju, modelBaju, id) \ values (%d, \'%s\', %d)' 
        self.query = self.query % (id_baju, modelBaju, id[0][0])
        self.executeQuery(self.query)
    
    def getDaftarBaju(self):
        self.query = 'SELECT t1.id_baju, t1.modelBaju, t2.id \ FROM baju t1 \ join produk t2 on t1.id=t2.id' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Tas(Produk):
    def setDataTas(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, id_tas, namaTas):
        self.setDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        id = self.getDataProduk(self, id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok)
        self.query = 'INSERT INTO tas (id_tas, namaTas, id) \ values (%d, \'%s\', %d)' 
        self.query = self.query % (id_tas, namaTas, id[0][0])
        self.executeQuery(self.query)
    
    def getDaftarTas(self):
        self.query = 'SELECT t1.id_tas, t1.namaTas, t2.id \ FROM baju t1 \ join produk t2 on t1.id=t2.id' 
        daftar = self.executeQuery(self.query, True)
        return daftar

class Pesanan(Kasir):
    def setDataPesanan(self, id_kasir, jamKerja, nomorHandphone, id_user, id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi):
        self.setDataCustomer(id_kasir, jamKerja, nomorHandphone, id_user)
        id_kasir = self.getDaftarCustomer(id_kasir, jamKerja, nomorHandphone, id_user)
        self.query = 'INSERT INTO pesanan (id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir) \ values (%d, \'%s\', \'%s\', \'%s\', %d)' 
        self.query = self.query % (id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir[0][0])
        self.executeQuery(self.query)

    def getDaftarPesanan(self):
        self.query = 'SELECT t1.id, t1.tanggalPesanan, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t2.id_kasir \ FROM pesanan t1 \ join kasir t2 on t1.id_kasir=t2.id_kasir' 
        daftar = self.executeQuery(self.query, True)
        return daftar

# class DetailPesanan(Pesanan, Tas, Celana, Baju, Customer):
#     def setDataDetailPesanan(self, id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir, id_tas, namaTas, id, id_celana, modelCelana, id, id_baju, modelBaju, id, id_customer, nomorHandphone, alamatRumah, id_user):
#         self.setDataPesanan(id_kasir, jamKerja, nomorHandphone, id_user, id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi)
#         id = self.getDaftarPesanan(id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir)
#         self.setDataTas(id, jenisProduk, merk, deskripsi, warna, ukuran, jenisBahan, harga, stok, id_tas, namaTas)
#         self.query = 'INSERT INTO pesanan (id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir) \ values (%d, \'%s\', \'%s\', \'%s\', %d)' 
#         self.query = self.query % (id, tanggalPesanan, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir[0][0])
#         self.executeQuery(self.query)

#     def getDaftarPesanan(self):
#         self.query = 'SELECT t1.id, t1.tanggalPesanan, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t2.id_kasir \ FROM pesanan t1 \ join kasir t2 on t1.id_kasir=t2.id_kasir' 
#         daftar = self.executeQuery(self.query, True)
#         return daftar

pengguna = User()
jalan = True
def tampilkanPilihan():
    print('******************************')
    print('SIAPA')
    print('SISTEM INFORMASI PENJUALAN ZAHRA COLLECTION')
    print('******************************')
    print('Pilih Menu')
    print('1. Tampilkan Daftar User')
    print('2. Tambah Data User')
    print('3. Ubah Data User berdasarkan ID User')
    pilihan = input('Masukkan pilihan: ')
    return pilihan

def tampilkanDataUser():
    global pengguna
    print('\nDaftar User')
    daftarPengguna = pengguna.getDataUser()
    for user_row in daftarPengguna:
        print(user_row)
    print('\n')

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

while jalan:
    pilihan = tampilkanPilihan()
    if pilihan == '1':
        tampilkanDataUser()
    elif pilihan == '2':
        tambahDataUser()
    elif pilihan == '3':
        ubahDataUser()