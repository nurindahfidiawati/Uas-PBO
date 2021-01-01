
class Pengeluaran:
    def __init__(self, __idPengeluaran, __tanggalPengeluaran, __jumlahPengeluaran, __keteranganPengeluaran):
        self.__idPengeluaran = __idPengeluaran
        self.__tanggalPengeluaran = __tanggalPengeluaran
        self.__jumlahPengeluaran = __jumlahPengeluaran
        self.__keteranganPengeluaran = __keteranganPengeluaran
    
    def __getIdpengeluaran(self):
        return self.__idPengeluaran
    
    def __setIdPengeluaran(self, __IdPengeluaran):
        self.__idPengeluaran = __IdPengeluaran

    def __getTanggalPengeluaran(self):
        return self.__tanggalPengeluaran
    
    def __setTanggalPengeluaran(self, __tanggalPengeluaran):
        self.__tanggalPengeluaran = __tanggalPengeluaran
    
    def __getJumlahPengeluaran(self):
        return self.__jumlahPengeluaran

    def __setJumlahPengeluaran(self, __jumlahPengeluaran):
        self.__jumlahPengeluaran = __jumlahPengeluaran
    
    def __getKeteranganPengeluaran(self):
        return self.__keteranganPengeluaran
    
    def __setKeteranganPengeluaran(self, __keteranganPengeluaran):
        self.__keteranganPengeluaran = __keteranganPengeluaran
