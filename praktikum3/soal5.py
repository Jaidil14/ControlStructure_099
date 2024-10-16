#program untuk menampilkan piramida angka yang jumlah barisnya sesuai dengan input dari user

#membuat variabel untuk menyimpan input dari user
n = int(input("Masukkan nilai n: "))
#inisialisasi nilai awal untuk variabel i
i = 1

while i <= n: #terus mencetak i selama tidak melebihi n
    print((str(i)+ ' ') * i) #menampilkan nilai i dengan dipisah oleh spasi dalam satu baris kemudian dikalikan dengan i
    i += 1 #menambahkan 1 ke ke i setiap perulangan untuk melanjutkan ke angka berikutnya