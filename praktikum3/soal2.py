#program untuk mencari dan menampilkan angka terbesar dari input user

#membuat tiga buah variabel yang akan menyimpan input dari user
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

#kondisi pertama
if a > b and a > c: #jika a > b dan c
    angkaTerbesar = a #variabel a akan menjadi angka terbesar, disimpan di variabel 'angkaTerbesar'
#kondisi kedua
elif b > a and b > c:
    angkaTerbesar = b
#kondisi ketiga
else :
    angkaTerbesar = c

#menampilkan variabel yang memiliki nilai terbesar dengan memanggil variabel yang menyimpannya (angkaTerbesar)
print ("Angka terbesar: ", angkaTerbesar)