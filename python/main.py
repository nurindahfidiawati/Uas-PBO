
import sqlite3
import modal as Modal
import Pemesanan as pemesanan
database = 'uas2.db'
connection = sqlite3.connect(database)



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

def tambahPembelian():
    global connection
    _idPemesanan = None
    _tanggalPemesanan = input("masukkan tanggal pembelian:")
    _namaPembeli = input("masukkan nama pembeli:")
    _noHpPembeli = input("masukan nomor hp: ")
    _alamatPemasangan = input("masukkan alamat pemasangan gorden:")
    _status = None
    _idProduk2=int(input("id produk yang akan di beli: "))
    _jumlahPemesanan = int(input("masukkan jumlah barang yang dibeli: "))
    pemesanan1 = pemesanan.Beli(_idPemesanan, _tanggalPemesanan, _namaPembeli, _noHpPembeli, _alamatPemasangan, _status, _idProduk2,_jumlahPemesanan)
    queryStr = f'INSERT INTO pemesanan(tanggalPemesanan, namaPembeli, noHpPembeli, alamatPemasangan, status, idProduk, jumlahPemesanan ) VALUES ("{pemesanan1._getTanggalPemesanan()}", "{pemesanan1._getNamaPembeli()}", "{pemesanan1._getNoHpPembeli()}","{pemesanan1._getAlamatPemasangan()}","{pemesanan1._getStatus()}","{pemesanan1._getIdProduk()}","{pemesanan1._getJumlahPemesanan()}")'
    connection.execute(queryStr)
    connection.commit()
    for row in connection.execute('SELECT * FROM  produk '):
        _idProduk = _idProduk2
        _namaProduk = row[1]
        _jumlahProduk = row[2]-_jumlahPemesanan
        _harga = row[3]
        _warna = row[4]
        _kategoriGordenJadi = row[6]
    if (_jumlahPemesanan <= _jumlahProduk) :
        produk1 = produk.KategoriGordenJadi(_idProduk, _namaProduk, _jumlahProduk, _harga, _warna, _kategoriGordenJadi)
        connection.execute('UPDATE produk SET namaProduk=?, jumlahProduk=?, harga=?, warna=? WHERE kategoriGordenJadi=? and idProduk=?', (produk1._getNamaProduk(), produk1._getJumlahProduk(), produk1._getHarga(), produk1._getWarna(), produk1._getKategoriGordenJadi(), produk1._getIdProduk())) 
        connection.commit()
        print("_"*40)
        bayar = _jumlahPemesanan * _harga
        print ("Total Harga : ", bayar)
    else :
        print("stok tidak mencukupi")

def tampilkanPemesanan():
    global connection
    for row in connection.execute('SELECT * FROM pemesanan JOIN produk on produk.idProduk = pemesanan.idProduk'):
        print(row)    
       
def tampilkanPembelian():
    global connection
    for row in connection.execute('SELECT * FROM pemesanan JOIN produk on produk.idProduk = pemesanan.idProduk WHERE status = "selesai" '):
        print(row)  

def ubahPemesanan():
    global connection
    _idPemesana =input("Masukkan id pemesanan yang akan diubah: ")
    print("=====Masukkan data baru=====")
    _statuus =input("status pemesanan:")
    pemesanan1 = pemesanan.Pemesanan(_idPemesana, "nul", "nul", "nul","nul", _statuus, 0,"nul")
    connection.execute('UPDATE pemesanan SET status=? WHERE idPemesanan=?', (pemesanan1._getStatus())) 
    connection.commit()

def tampilkanOmset():
    print("________________Rincian Omset________________")
    for row in connection.execute('SELECT s.jumlahPemesanan * p.harga AS TotalHarga FROM produk p JOIN pemesanan s ON p.idProduk = s.idProduk'):
        print ("Rp.",row[0])
    

while True:
    print("============Pilihan Menu============")
    print("""
        1. Menu Produk
        2. Menu Pemesanan
        3. Menu Modal
        4. Menu Keuangan
        5. Keluar
    """)
    pilihan = int(input('Pilihan: '))
    if pilihan == 1:
        while True:
            print("__________Menu Produk__________")
            print("""
            1. Menampilkan data produk
            2. Menambahkan data produk gorden 
            3. Menambahkan data produk kain
            4. Mengubah data produk gorden
            5. Mengubah data produk kain
            6. Menghapus data produk gorden
            7. Menghapus data produk kain
            8. Keluar
            """)
            pilihan = int(input('Pilihan: '))

            if (pilihan == 1):
                tampilkanDataProduk()
            elif(pilihan == 2):
                tambahDataKategoriGordenJadi()
            elif(pilihan == 3):
                tambahDataKategoriKain()
            elif(pilihan == 4):
                ubahDataProdukGordenJadi()
            elif(pilihan == 5):
                ubahDataProdukKain()
            elif(pilihan == 6):
                deleteProdukKategoriGordenJadi()
            elif(pilihan == 7):
                deleteProdukKategoriKain()
            elif(pilihan == 8):
                break
            else:
                print("Menu tidak tersedia")
    
    elif pilihan == 2:
        while True:
            print("__________Menu Pemesanan__________")
            print("""
            1. Menambahkan data pemesanan
            2. Menambahkan data pembelian
            3. Menampilkan data pemesanan
            4. Menampilkan data pembelian
            5. Mengubah data pemesanan
            6. Keluar
            """)
            pilihan = int(input('Pilihan: '))

            if (pilihan == 1):
                tambahPemesanan()
            elif (pilihan == 2):
                tambahPembelian()
            elif (pilihan == 3):
                tampilkanPemesanan()
            elif (pilihan == 4):
                tampilkanPembelian()
            elif (pilihan == 5):
                ubahPemesanan()
            elif (pilihan == 6):
                break
            else:
                print("Menu tidak tersedia")
    
    elif pilihan == 3:
        while True:
            print("__________Menu Modal__________")
            print("""
            
            1. Menambahkan data modal
            2. Mengubah data modal
            3. Menampilkan data modal
            4. Menghapus modal
            5. Keluar
                """)
            pilihan = int(input('Pilihan: '))

            if (pilihan == 1):
                tambahModal()
            elif(pilihan == 2):
                ubahModal()
            elif(pilihan == 3):
                tampilkanModal()
            elif (pilihan == 4):
                deleteModal()
            elif (pilihan == 5):
                break
            else:
                print("Menu tidak tersedia")
    
    elif pilihan == 4:
        while True:
            print("__________Menu Keuangan__________")
            print("""
            1. Menambahkan data pengeluaran
            2. Mengubah data pengeluaran
            3. Melihat data pengeluaran
            4. Menghapus pengeluaran
            5. Menampilkan omset
            6. Keluar
                """)
            pilihan = int(input('Pilihan: '))

            if (pilihan == 1):
                tambahDataPengeluaran()
            elif (pilihan == 2):
                ubahDataPengeluaran()
            elif (pilihan == 3):
                tampilkanDataPengeluaran()
            elif (pilihan ==4):
                deletePengeluaran()
            elif (pilihan == 5):
                tampilkanOmset()
            elif (pilihan == 6):
                break
            else:
                print("Menu tidak tersedia")
    elif pilihan == 5:
        break
    else:
        print("Menu tidak tersedia")




    

