

import sqlite3
import Produk as produk
import Pengeluaran as pengeluaran
import modal as Modal
import Pemesanan as pemesanan
import menu as Menu

database = 'uas2.db'
connection = sqlite3.connect(database)

def tampilkanDataProduk():
    global connection
    print("|idProduk|","|namaProduk|","|jumlahProduk|","|harga|","|warna|","|kategoriKain|","|kategoriGordenJadi|")
    for row in connection.execute('SELECT * FROM produk'):
        print(row)


def tambahDataKategoriGordenJadi():
    global connection
    _idProduk= None
    _namaProduk = input("masukkan nama produk: ")
    _jumlahProduk =int(input ("Masukkan jumlah produk: "))
    _harga = input("Masukkan harga produk: ")
    _warna = input("Masukkan warna: ")
    _kategoriGordenJadi=input ("Masukkan kategori Gorden Jadi: ")
    kategori= produk.KategoriGordenJadi(_idProduk,_namaProduk, _jumlahProduk, _harga, _warna, _kategoriGordenJadi)
    queryStr = f'INSERT INTO produk(namaProduk, jumlahProduk,harga,warna,kategoriGordenJadi ) VALUES ("{kategori._getNamaProduk()}", "{kategori._getJumlahProduk()}","{kategori._getHarga()}","{kategori._getWarna()}","{kategori._getKategoriGordenJadi()}")'
    connection.execute(queryStr)
    connection.commit()

def tambahDataKategoriKain():
    global connection
    _idProduk= None
    _namaProduk = input("masukkan nama produk: ")
    _jumlahProduk =int(input ("Masukkan jumlah produk: "))
    _harga = input("Masukkan harga produk: ")
    _warna = input("Masukkan warna: ")
    _kategoriKain=input ("Masukkan kategori Gorden Jadi: ")
    kategori= produk.KategoriKain(_idProduk,_namaProduk, _jumlahProduk, _harga, _warna, _kategoriKain)
    queryStr = f'INSERT INTO produk(namaProduk, jumlahProduk,harga,warna,kategoriKain ) VALUES ("{kategori._getNamaProduk()}", "{kategori._getJumlahProduk()}","{kategori._getHarga()}","{kategori._getWarna()}","{kategori._getKategoriKain()}")'
    connection.execute(queryStr)
    connection.commit()

def ubahDataProdukGordenJadi():
    global connection
    _idProduk =input("Masukkan id produk yang akan diubah: ")
    _kategoriGordenJadi =input ("Masukkan kategori: ")
    print("=====Masukkan data baru=====")
    _namaProduk = input("masukkan nama produk: ")
    _jumlahProduk =int(input ("Masukkan jumlah produk: "))
    _harga = input("Masukkan harga produk: ")
    _warna = input("Masukkan warna: ")
    produk1 = produk.KategoriGordenJadi(_idProduk,_namaProduk, _jumlahProduk, _harga, _warna, _kategoriGordenJadi)
    connection.execute('UPDATE produk SET namaProduk=?, jumlahProduk=?, harga=?, warna=? WHERE kategoriGordenJadi=? and idProduk=?', (produk1._getNamaProduk(), produk1._getJumlahProduk(), produk1._getHarga(), produk1._getWarna(), produk1._getKategoriGordenJadi(), produk1._getIdProduk())) 
    connection.commit()

def ubahDataProdukKain():
    global connection
    _idProduk =input("Masukkan id produk yang akan diubah: ")
    _kategoriKain =input ("Masukkan kategori: ")
    print("=====Masukkan data baru=====")
    _namaProduk = input("masukkan nama produk: ")
    _jumlahProduk =int(input ("Masukkan jumlah produk: "))
    _harga = input("Masukkan harga produk: ")
    _warna = input("Masukkan warna: ")
    produk1 = produk.KategoriKain(_idProduk,_namaProduk, _jumlahProduk, _harga, _warna, _kategoriKain)
    connection.execute('UPDATE produk SET namaProduk=?, jumlahProduk=?, harga=?, warna=? WHERE kategoriKain=? and idProduk=?', (produk1._getNamaProduk(), produk1._getJumlahProduk(), produk1._getHarga(), produk1._getWarna(), produk1._getKategoriKain(), produk1._getIdProduk())) 
    connection.commit()

def deleteProdukKategoriGordenJadi():
    global connection
    _idProduk = input("Masukkan id produk yang akan di hapus: ")
    _kategoriGordenJadi = input("Masukkan kategori gorden yang akan dihapus: ")
    query ='DELETE FROM produk WHERE idProduk=? and kategoriGordenJadi=?'
    cur = connection.cursor()
    cur.execute(query,(_idProduk,_kategoriGordenJadi,))
    connection.commit()

def deleteProdukKategoriKain():
    global connection
    _idProduk = input("Masukkan id produk yang akan di hapus: ")
    _kategoriKain = input("Masukkan kategori kain yang akan dihapus: ")
    query ='DELETE FROM produk WHERE idProduk=? and kategoriKain=?'
    cur = connection.cursor()
    cur.execute(query,(_idProduk,_kategoriKain,))
    connection.commit()

def tampilkanDataPengeluaran():
    global connection
    print("|idPengeluaran|","|jumlahPengeluaran|","|keteranganPengeluaran|","|tanggalPengeluaran|")
    for row in connection.execute('SELECT * FROM pengeluaran'):
        print(row)


def tambahDataPengeluaran():
    global connection
    __idPengeluaran = None
    __tanggalPengeluaran = input("masukkan tanggal pengeluaran: ")
    __jumlahPengeluaran =input ("Masukkan jumlah pengeluaran: ")
    __keteranganPengeluaran = input("Masukkan keterangan pengeluaran: ")
    pengeluaran1 = pengeluaran.Pengeluaran( __idPengeluaran, __jumlahPengeluaran, __keteranganPengeluaran, __tanggalPengeluaran)
    # connection.execute(f'INSERT INTO pengeluaran values (?,?)', ( pengeluaran1.getTanggalPengeluaran(), pengeluaran1.getJumlahPengeluaran()))
    # connection.commit()
    queryStr = f'INSERT INTO pengeluaran(jumlahPengeluaran, keteranganPengeluaran, tanggalPengeluaran) VALUES ("{pengeluaran1.__getJumlahPengeluaran()}", "{pengeluaran1.__getKeteranganPengeluaran()}","{pengeluaran1.__getTanggalPengeluaran()}")'
    connection.execute(queryStr)
    connection.commit()

def ubahDataPengeluaran():
    global connection
    __idPengeluaran =input("Masukkan id pengeluaran yang akan diubah: ")
    print("=====Masukkan data baru=====")
    __tanggalPengeluaran = input("masukkan tanggal pengeluaran: ")
    __jumlahPengeluaran =input ("Masukkan jumlah pengeluaran: ")
    __keteranganPengeluaran = input("Masukkan keterangan pengeluaran: ")
    pengeluaran1 = pengeluaran.Pengeluaran(__idPengeluaran, __jumlahPengeluaran, __keteranganPengeluaran, __tanggalPengeluaran)
    connection.execute('UPDATE pengeluaran SET jumlahPengeluaran=?, keteranganPengeluaran=?, tanggalPengeluaran=? WHERE idPengeluaran=?', (pengeluaran1.__getJumlahPengeluaran(), pengeluaran1.__getKeteranganPengeluaran(), pengeluaran1.__getTanggalPengeluaran(), pengeluaran1.__getIdpengeluaran())) 
    connection.commit()

def deletePengeluaran():
    global connection
    __idPengeluaran = input ("Masukkan id pengeluaran yang akan dihapus: ")
    query = 'DELETE FROM pengeluaran WHERE idPengeluaran=?'
    cur = connection.cursor()
    cur.execute(query,(__idPengeluaran,))
    connection.commit()

def tampilkanModal():
    global connection
    print("|idModal|","|jumlahModal|","|tanggalModal|")
    for row in connection.execute('SELECT * FROM modal'):
        print(row)

def tambahModal():
    global connection
    __idModal= None
    __tanggalModal = input("masukkan tanggal Modal: ")
    __jumlahModal =input ("Masukkan jumlah Modal: ")
    modal1 = Modal.modal(__idModal,__tanggalModal, __jumlahModal)
    queryStr = f'INSERT INTO modal(tanggalModal, jumlahModal ) VALUES ("{modal1.__getTanggalModal()}", "{modal1.__getJumlahModal()}")'
    connection.execute(queryStr)
    connection.commit()

def ubahModal():
    global connection
    __idModal =input("Masukkan id modal yang akan diubah: ")
    print("=====Masukkan data baru=====")
    __tanggalModal = input("masukkan tanggal modal: ")
    __jumlahModal =input ("Masukkan jumlah modal: ")
    modal1 = Modal.modal(__idModal, __tanggalModal, __jumlahModal)
    connection.execute('UPDATE pengeluaran SET tanggalPengeluaran=?, jumlahPengeluaran=? WHERE idModal=?', (modal1.__getIdModal(), modal1.__getTanggalModal(), modal1.__getJumlahModal())) 
    connection.commit()

def deleteModal():
    global connection
    __idModal = input ("Masukkan id modal yang akan dihapus: ")
    query = 'DELETE FROM modal WHERE idModal=?'
    cur = connection.cursor()
    cur.execute(query,(__idModal,))
    connection.commit()

def tambahPemesanan():
    global connection
    _idPemesanan = None
    _tanggalPemesanan = input("masukkan tanggal pemesanan:")
    _namaPembeli = input("masukkan nama pembeli:")
    _noHpPembeli = input("masukan nomor hp: ")
    _alamatPemasangan = input("masukkan alamat pemasangan gorden:")
    _status =input("status pemesanan:")
    _idProduk2=int(input("id produk yang akan di beli: "))
    _jumlahPemesanan = int(input("masukkan jumlah barang yang dipesan: "))
    pemesanan1 = pemesanan.Pemesanan(_idPemesanan, _tanggalPemesanan, _namaPembeli, _noHpPembeli, _alamatPemasangan, _status, _idProduk2, _jumlahPemesanan)
    queryStr = f'INSERT INTO pemesanan(tanggalPemesanan, namaPembeli, noHpPembeli, alamatPemasangan, status, idProduk, jumlahPemesanan ) VALUES ("{pemesanan1._getTanggalPemesanan()}", "{pemesanan1._getNamaPembeli()}", "{pemesanan1._getNoHpPembeli()}","{pemesanan1._getAlamatPemasangan()}","{pemesanan1._getStatus()}","{pemesanan1._getIdProduk()}","{pemesanan1._getJumlahPemesanan()}")'
    connection.execute(queryStr)
    connection.commit()
    for row in connection.execute('SELECT * FROM  produk '):
        _idProduk =_idProduk2
        _namaProduk = row[1]
        _jumlahProduk = row[2]-_jumlahPemesanan
        _harga = row[3]
        _warna = row[4]
        _kategoriKain = row[5]
    if (_jumlahPemesanan <= _jumlahProduk) :
        produk1 = produk.KategoriKain(_idProduk, _namaProduk, _jumlahProduk, _harga, _warna, _kategoriKain)
        connection.execute('UPDATE produk SET namaProduk=?, jumlahProduk=?, harga=?, warna=? WHERE kategoriKain=? and idProduk=?', (produk1._getNamaProduk(), produk1._getJumlahProduk(), produk1._getHarga(), produk1._getWarna(), produk1._getKategoriKain(), produk1._getIdProduk())) 
        connection.commit()
        print("_"*40)
        bayar = _jumlahPemesanan * _harga
        print ("Total Harga : " , bayar)
    else :
        print("stok tidak mencukupi")






    

