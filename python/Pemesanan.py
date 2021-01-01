
class Pemesanan:
    def __init__(self, _idPemesanan, _tanggalPemesanan, _namaPembeli, _noHpPembeli, _alamatPemasangan, _status,_idProduk,_jumlahPemesanan):
        self._idPemesanan = _idPemesanan
        self._tanggalPemesanan = _tanggalPemesanan
        self._namaPembeli = _namaPembeli
        self._noHpPembeli = _noHpPembeli
        self._alamatPemasangan = _alamatPemasangan
        self._status = _status
        self._idProduk = _idProduk
        self._jumlahPemesanan = _jumlahPemesanan
        
    def _getIdPemesanan(self):
        return self._idPemesanan
    
    def _setIdPemesanan(self,_idPemesanan):
        self._idPemesanan = _idPemesanan
    
    def _getTanggalPemesanan(self):
        return self._tanggalPemesanan
    
    def _setTanggalPemesanan(self,_tanggalPemesanan):
        self._tanggalPemesanan = _tanggalPemesanan
    
    def _getNamaPembeli(self):
        return self._namaPembeli
    
    def _setNamaPembeli(self,_namaPembeli):
        self._namaPembeli = _namaPembeli
    
    def _getNoHpPembeli(self):
        return self._noHpPembeli
    
    def _setNoHpPembeli(self,_noHpPembeli):
        self._noHpPembeli = _noHpPembeli

    def _getAlamatPemasangan(self):
        return self._alamatPemasangan
    
    def _setAlamatPemasangan(self,_alamatPemasangan):
        self._alamatPemasangan = _alamatPemasangan
    
    def _getStatus(self):
        return self._status
    
    def _setStatus(self,_status):
        self._status = _status

    def _getIdProduk (self):
        return self._idProduk

    def _setJumlahPemesanan(self,_jumlahPemesanan):
        self._jumlahPemesanan = _jumlahPemesanan

    def _getJumlahPemesanan (self):
        return self._jumlahPemesanan

class Beli(Pemesanan):
    def __init__(self,_idPembelian, _tanggal, _namaPembeli, _noHpPembeli, _alamatPemasangan, _status,_idProduk,_jumlahBarang):
        super().__init__(_idPembelian, _tanggal, _namaPembeli, _noHpPembeli, _alamatPemasangan, _status,_idProduk,_jumlahBarang)
        self._status = _status

    def _getStatus(self):
        return "selesai"   
