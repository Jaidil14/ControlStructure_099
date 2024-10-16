#program untuk menampilkan deret fibonacci dengan nilai n sebagai limit deretnya

#membuat variabel yang akan menyimpan input dari user
n = int(input("Masukkan nilai limit deret Fibonacci: "))
#inisialisasi awal nilai variabel a dan b
a, b = 0, 1

print("Deret Fibonacci: ")#menampilkan teks

while a <= n: #terus mencetak nilai a selama tidak melebihi n
    print(a, end=' ') #menampilkan nilai a dan nilai berikutnya dalam satu baris dengan dipisahkan oleh spasi
    a, b = b, a + b #mengatur nilai a dan b untuk langkah berikutnya dalam baris
