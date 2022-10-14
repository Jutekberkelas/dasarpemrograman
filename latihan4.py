#input nama barang
#input harga baranngbaran#deskriptif
#membuat variabel nama barang
#membuat variabel harga barang
#membuat variabel persen harga
#menghitung harga barang
#harga barang * persen /100
#print harga barang beserta nama barang

nama_barang = input("masukkan nama baranng:")
harga_barang1 = int(input("masukkan harga barang:"))
nama_barang = input("masukkan nama barang:")
harga_barang2 = int(input("masukkan harga barang:"))
nama_barang = input("masukkan nama barang:")
harga_barang3 = int(input("masukkan harga barang:"))

persen = 10
total = harga_barang1+harga_barang2+harga_barang3
hargapersen = int(total*10/100)
print('harga barang setelah di persenkan:', hargapersen)
print('total harga keuntungan:', total+hargapersen)
