class pesanan:
    def __init__(self, _id_pesanan, _statusPesanan, _tanggalPenerimaan, _verifikasi, _id_user):
        self._id_pesanan = _id_pesanan
        self._statusPesanan = _statusPesanan
        self._tanggalPenerimaan = _tanggalPenerimaan
        self._verifikasi = _verifikasi
        self._id_user = _id_user
    
    def _getIdPesanan(self):
        return self._id_pesanan
    
    def _setIdPesanan(self, _id_pesanan):
        self._id_pesanan = _id_pesanan

    def _getStatusPesanan(self):
        return self._statusPesanan
    
    def _setStatusPesanan(self, _statusPesanan):
        self._statusPesanan = _statusPesanan
    
    def _getTglPenerimaan(self):
        return self._tanggalPenerimaan
    
    def _setTglPenerimaan(self, _tanggalPenerimaan):
        self._tanggalPenerimaan = _tanggalPenerimaan
    
    def _getVerifikasi(self):
        return self._verifikasi
    
    def _setVerfikasi(self, _verifikasi):
        self._verifikasi = _verifikasi

    def _getIdUser(self):
        return self._id_user