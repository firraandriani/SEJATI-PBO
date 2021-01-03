import sqlite3

class User:
    def __init__(self, _id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role):
        self._id_user = _id_user
        self._username = _username
        self._password = _password
        self._namaLengkap = _namaLengkap
        self._tanggalLahir = _tanggalLahir
        self._status = _status
        self._role = _role
    
    def _getIdUser(self):
        return self._id_user
    
    def _setIdUser(self, _id_user):
        self._id_user = _id_user

    def _getUsername(self):
        return self._username
    
    def _setUsername(self, _username):
        self._username = _username
    
    def _getPassword(self):
        return self._password
    
    def _setPassword(self, _password):
        self._password = _password
    
    def _getNamaLengkap(self):
        return self._namaLengkap
    
    def _setNamaLengkap(self, _namaLengkap):
        self._namaLengkap = _namaLengkap

    def _getTanggalLahir(self):
        return self._tanggalLahir
    
    def _setTanggalLahir(self, _tanggalLahir):
        self._tanggalLahir = _tanggalLahir
    
    def _getStatus(self):
        return self._status

    def _setStatus(self, _status):
        self._status = _status
    
    def _getRole(self):
        return self._role

    def _setRole(self, _role):
        self._role = _role

class Pemilik(User):
    def __init__(self, _id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role):
        super().__init__(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role)
        self._role = _role

    def _getRole(self):
        return "PEMILIK"

class Admin(User):
    def __init__(self, _id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _bagian, _jamKerja):
        super().__init__(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role)
        self._role = _role
        self._bagian = _bagian
        self._jamKerja = _jamKerja
    
    def _getRole(self):
        return "ADMIN GUDANG"
    
    def _getBagian(self):
        return self._bagian
    
    def _setBagian(self, _bagian):
        self._bagian = _bagian
    
    def _getJamKerja(self):
        return self._jamKerja
    
    def _setJamKerja(self, _jamKerja):
        self._jamKerja = _jamKerja

class Kasir(User):
    def __init__(self, _id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _jamKerja, _nomorHandphone):
        super().__init__(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role)
        self._role = _role
        self._jamKerja = _jamKerja
        self._nomorHandphone = _nomorHandphone
    
    def _getRole(self):
        return "KASIR"
    
    def _getJamKerja(self):
        return self._jamKerja
    
    def _setJamKerja(self, _jamKerja):
        self._jamKerja = _jamKerja

    def _getNomorHandphone(self):
        return self._nomorHandphone
    
    def _setNomorHandphone(self, _nomorHandphone):
        self._nomorHandphone = _nomorHandphone

class Customer(User):
    def __init__(self, _id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role, _nomorHandphone, _alamatRumah):
        super().__init__(_id_user, _username, _password, _namaLengkap, _tanggalLahir, _status, _role)
        self._role = _role
        self._nomorHandphone = _nomorHandphone
        self._alamatRumah = _alamatRumah
    
    def _getRole(self):
        return "CUSTOMER"

    def _getNomorHandphone(self):
        return self._nomorHandphone
    
    def _setNomorHandphone(self, _nomorHandphone):
        self._nomorHandphone = _nomorHandphone
    
    def _getAlamatRumah(self):
        return self._alamatRumah
    
    def _setAlamatRumah(self, _alamatRumah):
        self._alamatRumah = _alamatRumah

class Login(User):

    @staticmethod
    def login(username, password):
        con = sqlite3.connect("sejatiUAS.db")
        cur = con.cursor()
        query = 'SELECT username, password FROM user WHERE username=\'%s\' and password=\'%s\''
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