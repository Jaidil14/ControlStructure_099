#program untuk evaluasi performa siswa

#membuat variabel untuk menyimpan input user
value = (input) ("Masukkan nilai untuk melihat performa siswa: ")
#kondisi pertama
if int(value) >= 90 : #jika nilai yang dimasukkan >= 90
    print ("Excellent performance") #teks akan ditampilkan
#kondisi kedua
elif int(value) >= 80 :
    print ("Very Good performance")
#kondisi ketiga
elif int(value) >= 70 :
    print ("Good performance")
#kondisi keempat
elif int(value) >= 60 :
    print ("Average performance")
#kondisi kelima
else :
    print ("Poor performance") #teks yang akan ditampilkan jika input tidak memenuhi semua kondisi if dan elif di atas

