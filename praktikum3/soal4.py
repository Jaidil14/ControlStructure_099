#program untuk menampilkan deret bilangan ganjil dengan nilai n sebagai limit deretnya

#membuat variabel untuk menyimpan input dari user
n = int(input("Masukkan limit deret bilangan ganjil: "))

print ("Deret angka ganjil: ") #menampilkan teks
for odd in range(1,n,2): #terus mencetak angka dari 1 sampai n dengan kelipatan 2 
    print(odd, end=' ') #menampilkan perulangan dalam satu baris dan dipisahkan oleh spasi
    

   