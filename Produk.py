class Produk:
    def __init__(self, _id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok):
        self._id = _id
        self._jenisProduk = _jenisProduk
        self._merk = _merk
        self._deskripsi = _deskripsi
        self._warna = _warna
        self._ukuran = _ukuran
        self._jenisBahan = _jenisBahan
        self._harga = _harga
        self._stok = _stok
    
    def _getId(self):
        return self._id
    
    def _setId(self, _id):
        self._id = _id

    def _getJenisProduk(self):
        return self._jenisProduk
    
    def _setJenisProduk(self, _jenisProduk):
        self._jenisProduk = _jenisProduk
    
    def _getMerk(self):
        return self._merk
    
    def _setMerk(self, _merk):
        self._merk = _merk
    
    def _getDeskripsi(self):
        return self._deskripsi
    
    def _setDeskripsi(self, _deskripsi):
        self._deskripsi = _deskripsi

    def _getWarna(self):
        return self._warna
    
    def _setWarna(self, _warna):
        self._warna = _warna
    
    def _getUkuran(self):
        return self._ukuran

    def _setUkuran(self, _ukuran):
        self._ukuran = _ukuran
    
    def _getJenisBahan(self):
        return self._jenisBahan

    def _setJenisBahan(self, _jenisBahan):
        self._jenisBahan = _jenisBahan
    
    def _getHarga(self):
        return self._harga

    def _setHarga(self, _harga):
        self._harga = _harga
    
    def _getStok(self):
        return self._stok

    def _setStok(self, _stok):
        self._stok = _stok

class Celana(Produk):
    def __init__(self, _id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _modelCelana):
        super().__init__(_id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok)
        self._jenisProduk = _jenisProduk
        self._modelCelana = _modelCelana

    def _getJenisProduk(self):
        return "CELANA"

    def _getModelCelana(self):
        return self._modelCelana
    
    def _setModelCelana(self, _modelCelana):
        self._modelCelana = _modelCelana

class Baju(Produk):
    def __init__(self, _id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _modelBaju):
        super().__init__(_id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok)
        self._jenisProduk = _jenisProduk
        self._modelBaju = _modelBaju

    def _getJenisProduk(self):
        return "BAJU"

    def _getModelBaju(self):
        return self._modelBaju
    
    def _setModelBaju(self, _modelBaju):
        self._modelBaju = _modelBaju

class Tas(Produk):
    def __init__(self, _id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok, _namaTas):
        super().__init__(_id, _jenisProduk, _merk, _deskripsi, _warna, _ukuran, _jenisBahan, _harga, _stok)
        self._jenisProduk = _jenisProduk
        self._namaTas = _namaTas

    def _getJenisProduk(self):
        return "TAS"

    def _getNamaTas(self):
        return self._namaTas
    
    def _setNamaTas(self, _namaTas):
        self._namaTas = _namaTas