class detailPesanan():
    def __init__(self, _id_DetPesanan, _id_pesanan, _tanggalPesanan, _jumlahBaju, _jumlahCelana, _jumlahTas, _id_tas, _id_celana, _id_baju, _id_user):
        self._id_DetPesanan = _id_DetPesanan
        self._id_pesanan = _id_pesanan
        self._tanggalPesanan = _tanggalPesanan
        self._jumlahBaju = _jumlahBaju
        self._jumlahCelana = _jumlahCelana
        self._jumlahTas = _jumlahTas
        self._id_tas = _id_tas
        self._id_celana = _id_celana
        self._id_baju = _id_baju
        self._id_user = _id_user
    
    def _getIdDetPesanan(self):
        return self._id_DetPesanan
    
    def _setIdDetPesanan(self, _id_DetPesanan):
        self._id_DetPesanan = _id_DetPesanan

    def _getIdPesanan(self):
        return self._id_pesanan

    def _getTglPesanan(self):
        return self._tanggalPesanan
    
    def _setTglPesanan(self, _tanggalPesanan):
        self._tanggalPesanan = _tanggalPesanan

    def _getJumlahBaju(self):
        return self._jumlahBaju
    
    def _setJumlahBaju(self, _jumlahBaju):
        self._jumlahBaju = _jumlahBaju

    def _getJumlahCelana(self):
        return self._jumlahCelana
    
    def _setJumlahCelana(self, _jumlahCelana):
        self._jumlahCelana = _jumlahCelana
    
    def _getJumlahTas(self):
        return self._jumlahTas
    
    def _setJumlahTas(self, _jumlahTas):
        self._jumlahTas = _jumlahTas

    def _getIdTas(self):
        return self._id_tas
    
    def _setIdTas(self, _id_tas):
        self._id_tas = _id_tas

    def _getIdCelana(self):
        return self._id_celana
    
    def _setIdCelana(self, _id_celana):
        self._id_celana = _id_celana

    def _getIdBaju(self):
        return self._id_baju

    def _setIdBaju(self, _id_baju):
        self._id_baju = _id_baju

    def _getIdUser(self):
        return self._id_user