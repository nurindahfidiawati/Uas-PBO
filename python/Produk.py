
class Produk:
    def __init__(self,_idProduk, _namaProduk, _jumlahProduk, _harga, _warna):
        self._idProduk= _idProduk
        self._namaProduk = _namaProduk
        self._jumlahProduk = _jumlahProduk
        self._harga = _harga
        self._warna = _warna

    def _getIdProduk(self):
        return self._idProduk
    
    def _setIdProduk(self, _idProduk):
        self._idProduk = _idProduk

    def _getNamaProduk(self):
        return self._namaProduk
    
    def _setNamaProduk(self, _namaProduk):
        self._namaProduk = _namaProduk
    
    def _getJumlahProduk(self):
        return self._jumlahProduk

    def _setJumlahProduk(self, _jumlahProduk):
        self._jumlahProduk = _jumlahProduk

    def _getHarga(self):
        return self._harga
    
    def _setHarga(self, _harga):
        self._harga = _harga
    
    def _getWarna(self):
        return self._warna
    
    def _setWarna(self, _warna):
        self._warna = _warna


class KategoriGordenJadi(Produk):
    def __init__(self,_idProduk, _namaProduk, _jumlahProduk, _harga, _warna, _kategoriGordenJadi):
        super().__init__(_idProduk, _namaProduk, _jumlahProduk, _harga, _warna)
        self._kategoriGordenJadi = _kategoriGordenJadi
    
    def _getKategoriGordenJadi(self):
        return self._kategoriGordenJadi

class KategoriKain(Produk):
    def __init__(self,_idProduk, _namaProduk, _jumlahProduk, _harga, _warna, _kategoriKain):
        super().__init__(_idProduk, _namaProduk, _jumlahProduk, _harga, _warna)
        self._kategoriKain = _kategoriKain
    
    def _getKategoriKain(self):
        return self._kategoriKain 
