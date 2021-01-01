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
    
    def getDataRowUser(self):
        self.query = 'SELECT id_user FROM user ORDER BY id_user DESC LIMIT 1'
        id_user = self.executeQuery(self.query, retVal=True)
        return id_user

    def _deleteDataUser(self, id_user):
        self.query = 'DELETE FROM user WHERE id_user = %s'
        self.query = self.query % (id_user)
        self.executeQuery(self.query)

class Admin(User):
    def setDataAdmin(self, id_admin, bagian, jamKerja, id_user):
        self.query = 'INSERT INTO admin (id_admin, bagian, jamKerja, id_user) values (%s, \'%s\', \'%s\', %s)' 
        self.query = self.query % (id_admin, bagian, jamKerja, id_user)
        self.executeQuery(self.query)
    
    def setUbahDataAdmin(self, id_user, id_admin, bagian, jamKerja):
        self.query = 'UPDATE admin set id_admin = %s, bagian = \'%s\', jamKerja = \'%s\', id_user = %s WHERE id_admin = %s'
        self.query = self.query % (id_admin, bagian, jamKerja, id_user, id_admin)
        self.executeQuery(self.query)

    def getDaftarAdmin(self):
        self.query = 'SELECT t1.id_admin, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.bagian, t1.jamKerja FROM admin t1 join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar
    
    def getDataAdmin(self, username):
        self.query = 'SELECT t1.id_admin, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.bagian, t1.jamKerja FROM admin t1 join user t2 on t1.id_user=t2.id_user WHERE username = \'%s\'' 
        self.query = self.query % (username)
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataRowAdmin(self):
        self.query = 'SELECT id_admin FROM admin ORDER BY id_admin DESC LIMIT 1'
        id_user = self.executeQuery(self.query, retVal=True)
        return id_user

    def _deleteDataAdmin(self, id_admin):
        self.query = 'DELETE FROM admin WHERE id_admin = %s'
        self.query = self.query % (id_admin)
        self.executeQuery(self.query)

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

    def getDataRowPenilik(self):
        self.query = 'SELECT id_pemilik FROM pemilik ORDER BY id_pemilik DESC LIMIT 1'
        id_user = self.executeQuery(self.query, retVal=True)
        return id_user

    def _deleteDataPemilik(self, id_pemilik):
        self.query = 'DELETE FROM pemilik WHERE id_pemilik = %s'
        self.query = self.query % (id_pemilik)
        self.executeQuery(self.query)

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

    def getDataCustomer(self, username):
        self.query = 'SELECT t1.id_customer, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.nomorHandphone, t1.alamatRumah FROM customer t1 join user t2 on t1.id_user=t2.id_user WHERE username = \'%s\'' 
        self.query = self.query % (username)
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataRowCustomer(self):
        self.query = 'SELECT id_customer FROM customer ORDER BY id_customer DESC LIMIT 1'
        id_user = self.executeQuery(self.query, retVal=True)
        return id_user

    def _deleteDataCustomer(self, id_customer):
        self.query = 'DELETE FROM customer WHERE id_customer = %s'
        self.query = self.query % (id_customer)
        self.executeQuery(self.query)

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
        self.query = 'SELECT t1.id_kasir, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.jamKerja, t1.nomorHandphone FROM kasir t1 join user t2 on t1.id_user=t2.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataKasir(self, username):
        self.query = 'SELECT t1.id_kasir, t2.id_user, t2.username, t2.password, t2.namaLengkap, t2.tanggalLahir, t2.status, t2.role, t1.jamKerja, t1.nomorHandphone FROM kasir t1 join user t2 on t1.id_user=t2.id_user WHERE username = \'%s\'' 
        self.query = self.query % (username)
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataRowKasir(self):
        self.query = 'SELECT id_kasir FROM kasir ORDER BY id_kasir DESC LIMIT 1'
        id_user = self.executeQuery(self.query, retVal=True)
        return id_user

    def _deleteDataKasir(self, id_kasir):
        self.query = 'DELETE FROM kasir WHERE id_kasir = %s'
        self.query = self.query % (id_kasir)
        self.executeQuery(self.query)

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

    def _deleteDataProduk(self, id):
        self.query = 'DELETE FROM produk WHERE id = %s'
        self.query = self.query % (id)
        self.executeQuery(self.query)

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

    def _deleteDataCelana(self, id_celana):
        self.query = 'DELETE FROM celana WHERE id_celana = %s'
        self.query = self.query % (id_celana)
        self.executeQuery(self.query)

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

    def _deleteDataBaju(self, id_baju):
        self.query = 'DELETE FROM baju WHERE id_baju = %s'
        self.query = self.query % (id_baju)
        self.executeQuery(self.query)

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

    def _deleteDataTas(self, id_tas):
        self.query = 'DELETE FROM tas WHERE id_tas = %s'
        self.query = self.query % (id_tas)
        self.executeQuery(self.query)

class Pesanan(Kasir, User):
    def setDataPesanan(self, id_kasir, id, statusPesanan, tanggalPenerimaan, verifikasi):
        self.query = 'INSERT INTO pesanan (id, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir) values (%s, \'%s\', \'%s\', \'%s\', %s)' 
        self.query = self.query % (id, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir)
        self.executeQuery(self.query)
    
    def setUbahDataPesanan(self, id_kasir, id, statusPesanan, tanggalPenerimaan, verifikasi):
        self.query = 'UPDATE pesanan set id = %s, statusPesanan = \'%s\', tanggalPenerimaan = \'%s\', verifikasi = \'%s\', id_kasir = %s WHERE id = %s'
        self.query = self.query % (id, statusPesanan, tanggalPenerimaan, verifikasi, id_kasir, id)
        self.executeQuery(self.query)

    def getDaftarPesanan(self):
        self.query = 'SELECT t1.id, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t2.id_kasir, t3.namaLengkap, t2.nomorHandphone FROM pesanan t1 INNER JOIN kasir t2 ON t1.id_kasir=t2.id_kasir INNER JOIN user t3 ON t2.id_user=t3.id_user' 
        daftar = self.executeQuery(self.query, True)
        return daftar
    
    def getDataPesanan(self, id):
        self.query = 'SELECT t1.id, t1.statusPesanan, t1.tanggalPenerimaan, t1.verifikasi, t3.namaLengkap, t2.nomorHandphone FROM pesanan t1 join kasir t2 on t1.id_kasir=t2.id_kasir join user t3 on t2.id_user=t3.id_user WHERE id = %s'
        self.query = self.query % (id)
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataRowPesanan(self):
        self.query = 'SELECT id FROM pesanan ORDER BY id DESC LIMIT 1'
        id = self.executeQuery(self.query, retVal=True)
        return id

class DetailPesanan(Pesanan, Tas, Celana, Baju, Customer):
    def getTotalHargaBaju(self, id_baju):
        self.query = 'SELECT t2.harga FROM baju t1 INNER JOIN produk t2 ON t2.id = t1.id WHERE t1.id_baju = %s'
        self.query = self.query % (id_baju)
        hargaBaju = self.executeQuery(self.query, True) 
        return hargaBaju[0][0]
    
    def getTotalHargaCelana(self, id_celana):
        self.query = 'SELECT t2.harga FROM celana t1 INNER JOIN produk t2 ON t2.id = t1.id WHERE t1.id_celana = %s'
        self.query = self.query % (id_celana)
        hargaCelana = self.executeQuery(self.query, True) 
        return hargaCelana[0][0]
    
    def getTotalHargaTas(self, id_tas):
        self.query = 'SELECT t2.harga FROM tas t1 INNER JOIN produk t2 ON t2.id = t1.id WHERE t1.id_tas = %s'
        self.query = self.query % (id_tas)
        hargaTas = self.executeQuery(self.query, True) 
        return hargaTas[0][0]

    def setDataDetailPesanan(self, id, tanggalPesanan, jumlahBaju, jumlahCelana, jumlahTas, id_pesanan, id_tas, id_celana, id_baju, id_customer):
        totHarBaju = self.getTotalHargaBaju(id_baju)
        totalHarBaju = int(jumlahBaju) * int(totHarBaju)
        totHarCelana = self.getTotalHargaCelana(id_celana)
        totalHarCelana = int(jumlahCelana) * int(totHarCelana)
        totHarTas = self.getTotalHargaTas(id_tas)
        totalHarTas = int(jumlahTas) * int(totHarTas)
        jumlahPembelian = int(jumlahBaju) + int(jumlahCelana) + int(jumlahTas)
        hargaTotalProduk = totalHarBaju + totalHarCelana + totalHarTas
        self.query = "INSERT INTO detailPesanan (id, tanggalPesanan, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPembelian, hargaTotalProduk, id_pesanan, id_tas, id_celana, id_baju, id_customer) values ({0}, '{1}', {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14})".format(id, tanggalPesanan, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPembelian, hargaTotalProduk, id_pesanan, id_tas, id_celana, id_baju, id_customer)
        self.executeQuery(self.query)
    
    def setUbahDataDetailPesanan(self, id, tanggalPesanan, jumlahBaju, jumlahCelana, jumlahTas, id_pesanan, id_tas, id_celana, id_baju, id_customer):
        totHarBaju = self.getTotalHargaBaju(id_baju)
        totalHarBaju = int(jumlahBaju) * int(totHarBaju)
        totHarCelana = self.getTotalHargaCelana(id_celana)
        totalHarCelana = int(jumlahCelana) * int(totHarCelana)
        totHarTas = self.getTotalHargaTas(id_tas)
        totalHarTas = int(jumlahTas) * int(totHarTas)
        jumlahPembelian = int(jumlahBaju) + int(jumlahCelana) + int(jumlahTas)
        hargaTotalProduk = totalHarBaju + totalHarCelana + totalHarTas
        self.query = 'UPDATE detailPesanan set id = %s, tanggalPesanan = \'%s\', jumlahBaju = %s, totalHarBaju = %s, jumlahCelana = %s, totalHarCelana = %s, jumlahTas = %s, totalHarTas = %s, jumlahPembelian = %s, hargaTotalProduk = %s, id_pesanan = %s, id_tas = %s, id_celana = %s, id_baju = %s, id_customer = %s WHERE id = %s' 
        self.query = self.query % (id, tanggalPesanan, jumlahBaju, totalHarBaju, jumlahCelana, totalHarCelana, jumlahTas, totalHarTas, jumlahPembelian, hargaTotalProduk, id_pesanan, id_tas, id_celana, id_baju, id_customer, id)
        self.executeQuery(self.query)

    def getDataSatuDetPesanan(self, id):
        self.query = 'SELECT detailPesanan.id_customer, user1.namaLengkap, customer.nomorHandphone, customer.alamatRumah, detailPesanan.id, detailPesanan.tanggalPesanan, detailPesanan.id_celana, produk.jenisProduk, celana.modelCelana, produk.merk, produk.deskripsi, produk.warna, produk.ukuran, produk.jenisBahan, produk.harga, detailPesanan.jumlahCelana, detailPesanan.totalHarCelana, detailPesanan.id_baju, produk1.jenisProduk, baju.modelBaju, produk1.merk, produk1.deskripsi, produk1.warna, produk1.ukuran, produk1.jenisBahan, produk1.harga, detailPesanan.jumlahBaju, detailPesanan.totalHarBaju, detailPesanan.id_tas, produk2.jenisProduk, tas.namaTas, produk2.merk, produk2.deskripsi, produk2.warna, produk2.ukuran, produk2.jenisBahan, produk2.harga, detailPesanan.jumlahTas, detailPesanan.totalHarTas, detailPesanan.id_pesanan, pesanan.statusPesanan, pesanan.tanggalPenerimaan, pesanan.verifikasi, user.namaLengkap, kasir.nomorHandphone, detailPesanan.jumlahPembelian, detailPesanan.hargaTotalProduk FROM detailPesanan INNER JOIN pesanan ON detailPesanan.id_pesanan = pesanan.id INNER JOIN kasir ON pesanan.id_kasir = kasir.id_kasir INNER JOIN user ON user.id_user = kasir.id_user INNER JOIN customer ON detailPesanan.id_customer = customer.id_customer INNER JOIN user user1 ON customer.id_user = user1.id_user INNER JOIN celana ON detailPesanan.id_celana = celana.id_celana INNER JOIN produk ON celana.id = produk.id INNER JOIN baju ON detailPesanan.id_baju = baju.id_baju INNER JOIN produk produk1 ON produk1.id = baju.id INNER JOIN tas ON tas.id_tas = detailPesanan.id_tas INNER JOIN produk produk2 ON tas.id = produk2.id WHERE detailPesanan.id = %s'
        self.query = self.query % (id)
        daftar = self.executeQuery(self.query, True)
        return daftar
    
    def getDataSatuDetPesananPemilik(self, tanggalPesanan):
        self.query = 'SELECT detailPesanan.id_customer, user1.namaLengkap, customer.nomorHandphone, customer.alamatRumah, detailPesanan.id, detailPesanan.tanggalPesanan, detailPesanan.id_celana, produk.jenisProduk, celana.modelCelana, produk.merk, produk.deskripsi, produk.warna, produk.ukuran, produk.jenisBahan, produk.harga, detailPesanan.jumlahCelana, detailPesanan.totalHarCelana, detailPesanan.id_baju, produk1.jenisProduk, baju.modelBaju, produk1.merk, produk1.deskripsi, produk1.warna, produk1.ukuran, produk1.jenisBahan, produk1.harga, detailPesanan.jumlahBaju, detailPesanan.totalHarBaju, detailPesanan.id_tas, produk2.jenisProduk, tas.namaTas, produk2.merk, produk2.deskripsi, produk2.warna, produk2.ukuran, produk2.jenisBahan, produk2.harga, detailPesanan.jumlahTas, detailPesanan.totalHarTas, detailPesanan.id_pesanan, pesanan.statusPesanan, pesanan.tanggalPenerimaan, pesanan.verifikasi, user.namaLengkap, kasir.nomorHandphone, detailPesanan.jumlahPembelian, detailPesanan.hargaTotalProduk FROM detailPesanan INNER JOIN pesanan ON detailPesanan.id_pesanan = pesanan.id INNER JOIN kasir ON pesanan.id_kasir = kasir.id_kasir INNER JOIN user ON user.id_user = kasir.id_user INNER JOIN customer ON detailPesanan.id_customer = customer.id_customer INNER JOIN user user1 ON customer.id_user = user1.id_user INNER JOIN celana ON detailPesanan.id_celana = celana.id_celana INNER JOIN produk ON celana.id = produk.id INNER JOIN baju ON detailPesanan.id_baju = baju.id_baju INNER JOIN produk produk1 ON produk1.id = baju.id INNER JOIN tas ON tas.id_tas = detailPesanan.id_tas INNER JOIN produk produk2 ON tas.id = produk2.id WHERE detailPesanan.tanggalPesanan = \'%s\''
        self.query = self.query % (tanggalPesanan)
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataSatuDetPesananCus(self, username):
        self.query = 'SELECT detailPesanan.id_customer, user1.namaLengkap, customer.nomorHandphone, customer.alamatRumah, detailPesanan.id, detailPesanan.tanggalPesanan, detailPesanan.id_celana, produk.jenisProduk, celana.modelCelana, produk.merk, produk.deskripsi, produk.warna, produk.ukuran, produk.jenisBahan, produk.harga, detailPesanan.jumlahCelana, detailPesanan.totalHarCelana, detailPesanan.id_baju, produk1.jenisProduk, baju.modelBaju, produk1.merk, produk1.deskripsi, produk1.warna, produk1.ukuran, produk1.jenisBahan, produk1.harga, detailPesanan.jumlahBaju, detailPesanan.totalHarBaju, detailPesanan.id_tas, produk2.jenisProduk, tas.namaTas, produk2.merk, produk2.deskripsi, produk2.warna, produk2.ukuran, produk2.jenisBahan, produk2.harga, detailPesanan.jumlahTas, detailPesanan.totalHarTas, detailPesanan.id_pesanan, pesanan.statusPesanan, pesanan.tanggalPenerimaan, pesanan.verifikasi, user.namaLengkap, kasir.nomorHandphone, detailPesanan.jumlahPembelian, detailPesanan.hargaTotalProduk FROM detailPesanan INNER JOIN pesanan ON detailPesanan.id_pesanan = pesanan.id INNER JOIN kasir ON pesanan.id_kasir = kasir.id_kasir INNER JOIN user ON user.id_user = kasir.id_user INNER JOIN customer ON detailPesanan.id_customer = customer.id_customer INNER JOIN user user1 ON customer.id_user = user1.id_user INNER JOIN celana ON detailPesanan.id_celana = celana.id_celana INNER JOIN produk ON celana.id = produk.id INNER JOIN baju ON detailPesanan.id_baju = baju.id_baju INNER JOIN produk produk1 ON produk1.id = baju.id INNER JOIN tas ON tas.id_tas = detailPesanan.id_tas INNER JOIN produk produk2 ON tas.id = produk2.id WHERE user1.username = \'%s\''
        self.query = self.query % (username)
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataDetPesanan(self):
        self.query = 'SELECT detailPesanan.id_customer, user1.namaLengkap, customer.nomorHandphone, customer.alamatRumah, detailPesanan.id, detailPesanan.tanggalPesanan, detailPesanan.id_celana, produk.jenisProduk, celana.modelCelana, produk.merk, produk.deskripsi, produk.warna, produk.ukuran, produk.jenisBahan, produk.harga, detailPesanan.jumlahCelana, detailPesanan.totalHarCelana, detailPesanan.id_baju, produk1.jenisProduk, baju.modelBaju, produk1.merk, produk1.deskripsi, produk1.warna, produk1.ukuran, produk1.jenisBahan, produk1.harga, detailPesanan.jumlahBaju, detailPesanan.totalHarBaju, detailPesanan.id_tas, produk2.jenisProduk, tas.namaTas, produk2.merk, produk2.deskripsi, produk2.warna, produk2.ukuran, produk2.jenisBahan, produk2.harga, detailPesanan.jumlahTas, detailPesanan.totalHarTas, detailPesanan.id_pesanan, pesanan.statusPesanan, pesanan.tanggalPenerimaan, pesanan.verifikasi, user.namaLengkap, kasir.nomorHandphone, detailPesanan.jumlahPembelian, detailPesanan.hargaTotalProduk FROM detailPesanan INNER JOIN pesanan ON detailPesanan.id_pesanan = pesanan.id INNER JOIN kasir ON pesanan.id_kasir = kasir.id_kasir INNER JOIN user ON user.id_user = kasir.id_user INNER JOIN customer ON detailPesanan.id_customer = customer.id_customer INNER JOIN user user1 ON customer.id_user = user1.id_user INNER JOIN celana ON detailPesanan.id_celana = celana.id_celana INNER JOIN produk ON celana.id = produk.id INNER JOIN baju ON detailPesanan.id_baju = baju.id_baju INNER JOIN produk produk1 ON produk1.id = baju.id INNER JOIN tas ON tas.id_tas = detailPesanan.id_tas INNER JOIN produk produk2 ON tas.id = produk2.id'
        daftar = self.executeQuery(self.query, True)
        return daftar

    def getDataRowDetPesanan(self):
        self.query = 'SELECT id FROM detailPesanan ORDER BY id DESC LIMIT 1'
        id = self.executeQuery(self.query, retVal=True)
        return id

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
    print('2. Melihet Data ID User Terakhir')
    print('3. Membuat Data User')
    print('4. Melihat Data ID Pemilik Terakhir')
    print('5. Membuat Data Pemilik')
    print('6. LOGOUT')
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
    print('2. Melihet Data ID User Terakhir')
    print('3. Membuat Data User')
    print('4. Melihat Data ID Admin Gudang Terakhir')
    print('5. Membuat Data Admin Gudang')
    print('6. LOGOUT')
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
    print('2. Melihet Data ID User Terakhir')
    print('3. Membuat Data User')
    print('4. Melihat Data ID Kasir Terakhir')
    print('5. Membuat Data Kasir')
    print('6. LOGOUT')
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
    print('2. Melihet Data ID User Terakhir')
    print('3. Membuat Data User')
    print('4. Melihat Data ID Kasir Terakhir')
    print('5. Membuat Data Customer')
    print('6. LOGOUT')
    pilihCustomer = input('Masukkan pilihan: ')
    print()
    return pilihCustomer

def lihatIDUser():
    global pengguna
    print('\nDaftar User')
    daftarPengguna = pengguna.getDataRowUser()
    for user_row in daftarPengguna:
        print()
        print("ID User:", user_row[0])
        print()

def tambahDataUser():
    global pengguna
    print('\nTambah data User')
    id_user = input('Masukkan ID User: ')
    username = input('Masukkan Username: ')
    password = input('Masukkan Password: ')
    namaLengkap = input('Masukkan Nama Lengkap: ')
    tanggalLahir = input('Masukkan Tanggal Lahir(y-m-d): ')
    status = input('Masukkan Status(Aktif, Tidak Aktif): ')
    role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    pengguna.setDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataUser():
    global pengguna
    print('Daftar User'.center(132, "-"))
    print('''
------------------------------------------------------------------------------------------------------------------------------------
|  ID User  |    Username    |  Password  |          Nama Lengkap          | Tanggal Lahir |    Status    |          Role          |
------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = pengguna.getDataUser()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(11-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(16-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(12-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(32-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(15-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(14-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(24-1-len(isi6)):
            print(' ', end='')
        print('|')
    print('------------------------------------------------------------------------------------------------------------------------------------')
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
    role = input('Masukkan role(PEMILIK, ADMIN GUDANG, CUSTOMER, KASIR): ')
    pengguna.setUbahDataUser(id_user, username, password, namaLengkap, tanggalLahir, status, role)
    print('\n')
    print('Data Berhasil Diubah')

def hapusDataUser():
    global pengguna
    print('\nData User Yang Akan Dihapus')
    id_user = input('Masukkan ID User: ')
    pengguna._deleteDataUser(id_user)
    print('Data berhasil Dihapus')

def lihatIDPemilik():
    global owner
    print('\nDaftar Pemilik')
    daftarPemilik = owner.getDaftarPemilik()
    for user_row in daftarPemilik:
        print()
        print("ID Pemilik:", user_row[0])
        print()

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
    print('Daftar Pemilik'.center(145, "-"))
    print('''
-------------------------------------------------------------------------------------------------------------------------------------------------
| ID Pemilik |  ID User  |    Username    |  Password  |          Nama Lengkap          | Tanggal Lahir |    Status    |          Role          |
-------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = owner.getDaftarPemilik()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(12-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(11-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(32-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(14-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(24-1-len(isi7)):
            print(' ', end='')
        print('|')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n')

def ubahDataPemilik():
    global owner
    print('\nUbah data Pemilik berdasarkan ID Pemilik')
    id_pemilik = input('Masukkan ID Pemilik: ')
    id_user = input('Masukkan ID User: ')
    owner.setUbahDataPemilik(id_user, id_pemilik)
    print('\n')
    print('Data Berhasil Diubah')

def hapusDataPemilik():
    global owner
    print('\nData Pemilik Yang Akan Dihapus')
    id_pemilik = input('Masukkan ID Pemilik: ')
    owner._deleteDataPemilik(id_pemilik)
    print('Data berhasil Dihapus')

def lihatIDAdmin():
    global adm
    print('\nDaftar Admin Gudang')
    daftarAdmin = adm.getDataRowAdmin()
    for user_row in daftarAdmin:
        print()
        print("ID Admin:", user_row[0])
        print()

def tambahDataAdmin():
    global adm
    print('\nTambah Data Admin Gudang')
    id_admin = input('Masukkan ID Admin Gudang: ')
    bagian = input('Masukkan Bagian Admin Gudang: ')
    jamKerja = input('Masukkan Jam Kerja Admin Gudang: ')
    id_user = input('Masukkan ID User: ')
    adm.setDataAdmin(id_admin, bagian, jamKerja, id_user)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataAdmin():
    global adm
    print('Daftar Admin Gudang'.center(179, "-"))
    print('''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID Admin  |  ID User  |    Username    |  Password  |        Nama Lengkap        | Tanggal Lahir |    Status    |       Role       |    Bagian    |          Jam Kerja         |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = adm.getDaftarAdmin()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(12-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(11-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(28-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(14-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(18-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[8])
        print('| '+isi8, end='')
        for x in range(14-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[9])
        print('| '+isi9, end='')
        for x in range(28-1-len(isi9)):
            print(' ', end='')
        print('|')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
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
    daftarAdmin = adm.getDataAdmin(username)
    for user_row in daftarAdmin:
        print()
        print("ID Admin Gudang:", user_row[0])
        print("ID User:", user_row[1])
        print("Username:", user_row[2])
        print("Password:", user_row[3])
        print("Nama Lengkap:", user_row[4])
        print("Tanggal Lahir:", user_row[5])
        print("Status:", user_row[6])
        print("Role:", user_row[7])
        print("Bagian Admin Gudang:", user_row[8])
        print("Jam Kerja Admin Gudang:", user_row[9])
        print()

def hapusDataAdmin():
    global adm
    print('\nData Admin Gudang Yang Akan Dihapus')
    id_admin = input('Masukkan ID Admin Gudang: ')
    adm._deleteDataAdmin(id_admin)
    print('Data berhasil Dihapus')

def lihatIDKasir():
    global casher
    print('\nDaftar Kasir')
    daftarKasir = casher.getDataRowKasir()
    for user_row in daftarKasir:
        print()
        print("ID Kasir:", user_row[0])
        print()

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
    print('Daftar Kasir'.center(178, "-"))
    print('''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID Kasir  |  ID User  |    Username    |  Password  |      Nama Lengkap      | Tanggal Lahir |   Status   |       Role       |          Jam Kerja         |  Nomor Handphone  |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = casher.getDaftarKasir()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(12-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(11-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(24-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(12-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(18-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[8])
        print('| '+isi8, end='')
        for x in range(28-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[9])
        print('| '+isi9, end='')
        for x in range(19-1-len(isi9)):
            print(' ', end='')
        print('|')
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
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
        print()
        print("ID Kasir: ", user_row[0])
        print("ID User: ", user_row[1])
        print("Username: ", user_row[2])
        print("Password: ", user_row[3])
        print("Nama Lengkap: ", user_row[4])
        print("Tanggal Lahir: ", user_row[5])
        print("Status: ", user_row[6])
        print("Role: ", user_row[7])
        print("Jam Kerja: ", user_row[8])
        print("Nomor Handphone: ", user_row[9])
        print()

def hapusDataKasir():
    global casher
    print('\nData Kasir Yang Akan Dihapus')
    id_kasir = input('Masukkan ID Kasir: ')
    casher._deleteDataKasir(id_kasir)
    print('Data berhasil Dihapus')

def lihatIDCustomer():
    global pelanggan
    print('\nDaftar Customer')
    daftarCustomer = pelanggan.getDataRowCustomer()
    for user_row in daftarCustomer:
        print()
        print("ID Customer:", user_row[0])
        print()

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
    print('Daftar Customer'.center(181, "-"))
    print('''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| ID Customer |  ID User  |    Username    |  Password  |    Nama Lengkap    | Tanggal Lahir |   Status   |    Role    |  Nomor Handphone  |              Alamat Rumah              |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = pelanggan.getDaftarCustomer()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(13-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(11-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(16-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(12-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(20-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(12-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(12-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[8])
        print('| '+isi8, end='')
        for x in range(19-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[9])
        print('| '+isi9, end='')
        for x in range(38-1-len(isi9)):
            print(' ', end='')
        print('|')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
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
    daftarCustomer = pelanggan.getDataCustomer(username)
    for user_row in daftarCustomer:
        print()
        print("ID Customer: ", user_row[0])
        print("ID User: ", user_row[1])
        print("Username: ", user_row[2])
        print("Password: ", user_row[3])
        print("Nama Lengkap: ", user_row[4])
        print("Tanggal Lahir: ", user_row[5])
        print("Status: ", user_row[6])
        print("Role: ", user_row[7])
        print("Nomor Handphone: ", user_row[8])
        print("Alamat Rumah: ", user_row[9])
        print()

def hapusDataCustomer():
    global pelanggan
    print('\nData Customer Yang Akan Dihapus')
    id_customer = input('Masukkan ID Customer: ')
    pelanggan._deleteDataCustomer(id_customer)
    print('Data berhasil Dihapus')

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
    print('Daftar Produk'.center(158, "-"))
    print('''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
| ID Prod | Jenis Prod |  Merk  |                              Deskripsi                              | Warna |     Ukuran    | Jenis Bahan |  Harga  | Stok |
--------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = prod.getDataProduk()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(9-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(12-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(8-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(69-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(7-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(15-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(13-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(9-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[8])
        print('| '+isi8, end='')
        for x in range(6-1-len(isi8)):
            print(' ', end='')
        print('|')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------')
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

def hapusDataProduk():
    global prod
    print('\nData Produk Yang Akan Dihapus')
    id = input('Masukkan ID Produk: ')
    prod._deleteDataProduk(id)
    print('Data berhasil Dihapus')

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
    print('Daftar Produk Celana'.center(180, "-"))
    print('''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| ID Celana | ID Prod | Jenis Prod |  Merk  |                              Deskripsi                              | Warna |     Ukuran    | Jenis Bahan | Harga | Stok | Model Cel |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = cel.getDaftarCelana()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(11-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(9-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(12-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(8-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(69-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(7-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(15-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(13-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[8])
        print('| '+isi8, end='')
        for x in range(7-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[9])
        print('| '+isi9, end='')
        for x in range(6-1-len(isi9)):
            print(' ', end='')
        isi10 = str(user_row[10])
        print('| '+isi10, end='')
        for x in range(11-1-len(isi10)):
            print(' ', end='')
        print('|')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
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

def hapusDataCelana():
    global cel
    print('\nData Celana Yang Akan Dihapus')
    id_celana = input('Masukkan ID Celana: ')
    cel._deleteDataCelana(id_celana)
    print('Data berhasil Dihapus')

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
    print('Daftar Produk Baju'.center(181, "-"))
    print('''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID Baju  | ID Prod | Jenis Prod |  Merk  |                              Deskripsi                              | Warna |     Ukuran    | Jenis Bahan | Harga | Stok | Model Baju |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = baj.getDaftarBaju()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(11-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(9-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(12-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(8-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(69-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(7-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(15-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(13-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[8])
        print('| '+isi8, end='')
        for x in range(7-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[9])
        print('| '+isi9, end='')
        for x in range(6-1-len(isi9)):
            print(' ', end='')
        isi10 = str(user_row[10])
        print('| '+isi10, end='')
        for x in range(12-1-len(isi10)):
            print(' ', end='')
        print('|')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
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

def hapusDataBaju():
    global baj
    print('\nData Baju Yang Akan Dihapus')
    id_baju = input('Masukkan ID Baju: ')
    baj._deleteDataBaju(id_baju)
    print('Data berhasil Dihapus')

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
    print('Daftar Produk Tas'.center(181, "-"))
    print('''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|  ID  Tas  | ID Prod | Jenis Prod |  Merk  |                              Deskripsi                              | Warna |     Ukuran    | Jenis Bahan | Harga | Stok | Model  Tas |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = taS.getDaftarTas()
    for user_row in daftarPengguna:
        isi = str(user_row[0])
        print('| '+isi, end='')
        for x in range(11-1-len(isi)):
            print(' ', end='')
        isi1 = str(user_row[1])
        print('| '+isi1, end='')
        for x in range(9-1-len(isi1)):
            print(' ', end='')
        isi2 = str(user_row[2])
        print('| '+isi2, end='')
        for x in range(12-1-len(isi2)):
            print(' ', end='')
        isi3 = str(user_row[3])
        print('| '+isi3, end='')
        for x in range(8-1-len(isi3)):
            print(' ', end='')
        isi4 = str(user_row[4])
        print('| '+isi4, end='')
        for x in range(69-1-len(isi4)):
            print(' ', end='')
        isi5 = str(user_row[5])
        print('| '+isi5, end='')
        for x in range(7-1-len(isi5)):
            print(' ', end='')
        isi6 = str(user_row[6])
        print('| '+isi6, end='')
        for x in range(15-1-len(isi6)):
            print(' ', end='')
        isi7 = str(user_row[7])
        print('| '+isi7, end='')
        for x in range(13-1-len(isi7)):
            print(' ', end='')
        isi8 = str(user_row[8])
        print('| '+isi8, end='')
        for x in range(7-1-len(isi8)):
            print(' ', end='')
        isi9 = str(user_row[9])
        print('| '+isi9, end='')
        for x in range(6-1-len(isi9)):
            print(' ', end='')
        isi10 = str(user_row[10])
        print('| '+isi10, end='')
        for x in range(12-1-len(isi10)):
            print(' ', end='')
        print('|')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
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

def hapusDataTas():
    global taS
    print('\nData Tas Yang Akan Dihapus')
    id_tas = input('Masukkan ID Tas: ')
    taS._deleteDataTas(id_tas)
    print('Data berhasil Dihapus')

def lihatIDPesanan():
    global order
    print('\nDaftar Pesanan')
    daftarOrder = order.getDataRowPesanan()
    for user_row in daftarOrder:
        print()
        print("ID Order:", user_row[0])
        print()

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
    print('Daftar Pesanan'.center(125, "-"))
    print('''
-----------------------------------------------------------------------------------------------------------------------------
| ID Pesanan | Status Pesanan | Tgl Penerimaan |  Verifikasi  | ID Kasir |          Nama Lengkap          | Nomor Handphone |
-----------------------------------------------------------------------------------------------------------------------------''')
    daftarPengguna = order.getDaftarPesanan()
    for user_row in daftarPengguna:
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

def lihatIDDetPesanan():
    global detailOrder
    print('\nDaftar Detail Pesanan')
    daftarDetOrder = detailOrder.getDataRowDetPesanan()
    for user_row in daftarDetOrder:
        print()
        print("ID Detail Order:", user_row[0])
        print()

def tampilkanSatuDataPesanan():
    global order
    print('\nDaftar Pesanan')
    id = input('Masukkan ID Pesanan: ')
    daftarOrder = order.getDataPesanan(id)
    for user_row in daftarOrder:
        print()
        print("ID Pesanan: ", user_row[0])
        print("Status Pesanan: ", user_row[1])
        print("Tanggal Penerimaan: ", user_row[2])
        print("Verifikasi: ", user_row[3])
        print("Nama Lengkap: ", user_row[4])
        print("Nomor Handphone: ", user_row[5])
        print()

def ubahDataDetPesanan():
    global detailOrder
    print('\nUbah Data Detail Pesanan berdasarkan ID')
    id = input('Masukkan ID Detail Pesanan: ')
    tanggalPesanan = input('Masukkan Tanggal Pesanan: ')
    jumlahBaju = input('Masukkan jumlah baju yang dibeli: ')
    jumlahCelana = input('Masukkan jumlah celana yang dibeli: ')
    jumlahTas = input('Masukkan jumlah tas yang dibeli: ')
    id_pesanan = input('Masukkan ID Pesanan: ')
    id_tas = input('Masukkan ID Tas: ')
    id_celana = input('Masukkan ID Celana: ')
    id_baju = input('Masukkan ID Baju: ')
    id_customer = input('Masukkan ID Customer: ')
    detailOrder.setUbahDataDetailPesanan(id, tanggalPesanan, jumlahBaju, jumlahCelana, jumlahTas, id_pesanan, id_tas, id_celana, id_baju, id_customer)
    print('\n')
    print('Data Berhasil Diubah')

def tambahDataDetPesanan():
    global detailOrder
    print('\nTambah Data Detail Pesanan')
    id = int(input('Masukkan ID Detail Pesanan: '))
    tanggalPesanan = str(input('Masukkan Tanggal Pesanan: '))
    jumlahBaju = int(input('Masukkan jumlah baju yang dibeli: '))
    jumlahCelana = int(input('Masukkan jumlah celana yang dibeli: '))
    jumlahTas = int(input('Masukkan jumlah tas yang dibeli: '))
    id_pesanan = input('Masukkan ID Pesanan: ')
    id_tas = input('Masukkan ID Tas: ')
    id_celana = input('Masukkan ID Celana: ')
    id_baju = input('Masukkan ID Baju: ')
    id_customer = input('Masukkan ID Customer: ')
    detailOrder.setDataDetailPesanan(id, tanggalPesanan, jumlahBaju, jumlahCelana, jumlahTas, id_pesanan, id_tas, id_celana, id_baju, id_customer)
    print('\n')
    print('Data Berhasil Ditambahkan')

def tampilkanDataDetPesanan():
    global detailOrder
    print('\nDaftar Detail Pesanan')
    daftarDetOrder = detailOrder.getDataDetPesanan()
    for user_row in daftarDetOrder:
        print(user_row)
    print('\n')

def tampilkanDataDetPesananPemilik():
    global detailOrder
    print('\nDaftar Detail Pesanan')
    tanggalPesanan = input('Masukkan Tanggal Pesanan Pesanan: ')
    daftarDetOrder = detailOrder.getDataSatuDetPesananPemilik(tanggalPesanan)
    for user_row in daftarDetOrder:
        print(user_row)
    print('\n')

def tampilkanSatuDataDetPesananCus():
    global detailOrder
    print('\nData Riwayat Detail Pesanan')
    username = input('Masukkan username: ')
    daftarDet = detailOrder.getDataSatuDetPesananCus(username)
    for user_row in daftarDet:
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

def tampilkanSatuDataDetPesanan():
    global detailOrder
    print('\nData Detail Pesanan')
    id = input('Masukkan ID Detail Pesanan: ')
    daftarDet = detailOrder.getDataSatuDetPesanan(id)
    for user_row in daftarDet:
        # print(user_row)
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
        return accept_Login
        
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
    print('4. Menghapus Data User')
    print('5. Melihat Data Pemilik')
    print('6. Menambah Data Pemilik')
    print('7. Mengubah Data Pemilik')
    print('8. Menghapus Data Pemilik')
    print('9. Melihat Data Admin Gudang')
    print('10. Menambah Data Admin Gudang')
    print('11. Mengubah Data Admin Gudang')
    print('12. Menghapus Data Admin Gudang')
    print('13. Melihat Data Kasir')
    print('14. Menambah Data Kasir')
    print('15. Mengubah Data Kasir')
    print('16. Menghapus Data Kasir')
    print('17. Melihat Data Customer')
    print('18. Menambah Data Customer')
    print('19. Mengubah Data Customer')
    print('20. Menghapus Data Customer')
    print('21. Melihat Data Celana')
    print('22. Melihat Data Baju')
    print('23. Melihat Data Tas')
    print('24. Melihat Rekap Pesanan')
    print('25. LOGOUT')
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
    print('9. Menghapus Data Produk')
    print('10. Melihat Data Celana')
    print('11. Menambah Data Celana')
    print('12. Mengubah Data Celana')
    print('13. Menghapus Data Celana')
    print('14. Melihat Data Baju')
    print('15. Menambah Data Baju')
    print('16. Mengubah Data Baju')
    print('17. Menghapus Data Baju')
    print('18. Melihat Data Tas')
    print('19. Menambah Data Tas')
    print('20. Mengubah Data Tas')
    print('21. Menghapus Data Tas')
    print('22. LOGOUT')
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
    print('12. LOGOUT')
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
    print('6. Melihat Data Celana')
    print('7. Melihat Data Baju')
    print('8. Melihat Data Tas')
    print('9. Melihat Data ID Pesanan Terakhir')
    print('10. Melihat Data Pesanan')
    print('11. Menambah Data Pesanan')
    print('12. Mengubah Data Pesanan')
    print('13. Melihat Data ID Detail Pesanan Terakhir')
    print('14. Menambah Data Detail Pesanan')
    print('15. Mengubah Data Detail Pesanan')
    print('16. Melihat Data Detail Pesanan')
    print('17. Melihat Riwayat Pesanan')
    print('18. LOGOUT')

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
                accept_Login = login(username, password)
                if accept_Login == False:
                    break

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
                        hapusDataUser()
                    elif pilihFiturPemilik == '5':
                        tampilkanDataPemilik()
                    elif pilihFiturPemilik == '6':
                        tambahDataPemilik()
                    elif pilihFiturPemilik == '7':
                        ubahDataPemilik()
                    elif pilihFiturPemilik == '8':
                        hapusDataPemilik()
                    elif pilihFiturPemilik == '9':
                        tampilkanDataAdmin()
                    elif pilihFiturPemilik == '10':
                        tambahDataAdmin()
                    elif pilihFiturPemilik == '11':
                        ubahDataAdmin()
                    elif pilihFiturPemilik == '12':
                        hapusDataAdmin()
                    elif pilihFiturPemilik == '13':
                        tampilkanDataKasir()
                    elif pilihFiturPemilik == '14':
                        tambahDataKasir()
                    elif pilihFiturPemilik == '15':
                        ubahDataKasir()
                    elif pilihFiturPemilik == '16':
                        hapusDataKasir()
                    elif pilihFiturPemilik == '17':
                        tampilkanDataCustomer()
                    elif pilihFiturPemilik == '18':
                        tambahDataCustomer()
                    elif pilihFiturPemilik == '19':
                        ubahDataCustomer()
                    elif pilihFiturPemilik == '20':
                        hapusDataCustomer()
                    elif pilihFiturPemilik == '21':
                        tampilkanDataCelana()
                    elif pilihFiturPemilik == '22':
                        tampilkanDataBaju()
                    elif pilihFiturPemilik == '23':
                        tampilkanDataTas()
                    elif pilihFiturPemilik == '24':
                        tampilkanDataDetPesananPemilik()
                    elif pilihFiturPemilik== '25':
                        exit()

            elif pilihPemilik == '2':
                lihatIDUser()
            elif pilihPemilik == '3':
                tambahDataUser()
            elif pilihPemilik == '4':
                lihatIDPemilik()
            elif pilihPemilik == '5':
                tambahDataPemilik()
            elif pilihPemilik == '6':
                exit()
    
    elif pilihUser == '2':
        jalanAdmin = True

        while jalanAdmin:
            pilihAdmin= tampilanAdmin()
            if pilihAdmin == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                accept_Login = login(username, password)
                if accept_Login == False:
                    break

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
                        hapusDataProduk()
                    elif pilihFiturAdmin == '10':
                        tampilkanDataCelana()
                    elif pilihFiturAdmin == '11':
                        tambahDataCelana()
                    elif pilihFiturAdmin == '12':
                        ubahDataCelana()
                    elif pilihFiturAdmin == '13':
                        hapusDataCelana()
                    elif pilihFiturAdmin == '14':
                        tampilkanDataBaju()
                    elif pilihFiturAdmin == '15':
                        tambahDataBaju()
                    elif pilihFiturAdmin == '16':
                        ubahDataBaju()
                    elif pilihFiturAdmin == '17':
                        hapusDataBaju()
                    elif pilihFiturAdmin == '18':
                        tampilkanDataTas()
                    elif pilihFiturAdmin == '19':
                        tambahDataTas()
                    elif pilihFiturAdmin == '20':
                        ubahDataTas()
                    elif pilihFiturAdmin == '21':
                        hapusDataTas()
                    elif pilihFiturAdmin == '22':
                        exit()

            elif pilihAdmin == '2':
                lihatIDUser()
            elif pilihAdmin == '3':
                tambahDataUser()
            elif pilihAdmin == '4':
                lihatIDAdmin()
            elif pilihAdmin == '5':
                tambahDataAdmin()
            elif pilihAdmin== '6':
                exit()

    elif pilihUser == '3':
        jalanKasir = True

        while jalanKasir:
            pilihKasir= tampilanKasir()
            if pilihKasir == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                accept_Login = login(username, password)
                if accept_Login == False:
                    break

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
                    elif pilihFiturKasir == '12':
                        exit()

            elif pilihKasir == '2':
                lihatIDUser()
            elif pilihKasir == '3':
                tambahDataUser()
            elif pilihKasir == '4':
                lihatIDKasir()
            elif pilihKasir == '5':
                tambahDataKasir()
            elif pilihKasir == '6':
                exit()

    elif pilihUser == '4':
        jalanCustomer = True

        while jalanCustomer:
            pilihCustomer= tampilanCustomer()
            if pilihCustomer == '1':
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                accept_Login = login(username, password)
                if accept_Login == False:
                    break

                jalanFiturCustomer = True

                while jalanFiturCustomer:
                    pilihFiturCustomer = fiturCustomer()
                    if pilihFiturCustomer == '1':
                        tambahDataUser()
                    elif pilihFiturCustomer == '2':
                        ubahDataUser()
                    elif pilihFiturCustomer == '3':
                        tampilkanSatuDataCustomer()
                    elif pilihFiturCustomer == '4':
                        tambahDataCustomer()
                    elif pilihFiturCustomer == '5':
                        ubahDataCustomer()
                    elif pilihFiturCustomer == '6':
                        tampilkanDataCelana()
                    elif pilihFiturCustomer == '7':
                        tampilkanDataBaju()
                    elif pilihFiturCustomer == '8':
                        tampilkanDataTas()
                    elif pilihFiturCustomer == '9':
                        lihatIDPesanan()
                    elif pilihFiturCustomer == '10':
                        tampilkanSatuDataPesanan()
                    elif pilihFiturCustomer == '11':
                        tambahDataPesanan()
                    elif pilihFiturCustomer == '12':
                        ubahDataPesanan()
                    elif pilihFiturCustomer == '13':
                        lihatIDDetPesanan()
                    elif pilihFiturCustomer == '14':
                        tambahDataDetPesanan()
                    elif pilihFiturCustomer == '15':
                        ubahDataDetPesanan()
                    elif pilihFiturCustomer == '16':
                        tampilkanSatuDataDetPesanan()
                    elif pilihFiturCustomer == '17':
                        tampilkanSatuDataDetPesananCus()
                    elif pilihFiturCustomer == '18':
                        exit()

            elif pilihCustomer == '2':
                lihatIDUser()
            elif pilihCustomer == '3':
                tambahDataUser()
            elif pilihCustomer == '4':
                lihatIDCustomer()
            elif pilihCustomer == '5':
                tambahDataCustomer()
            elif pilihCustomer == '6':
                exit()
