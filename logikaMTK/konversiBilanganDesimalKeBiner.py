# Program Python Konversi Desimal ke Biner
print('##  Program Python Konversi Desimal ke Biner  ##')
print('================================================')
print()

#* versi(1)
n = int(input('Input angka desimal: '))

a = [] # List untuk menyimpan hasil konversi biner
i = 0 # berfungsi untuk proses increment perulangan while.

#? Mengonversi angka desimal ke biner menggunakan metode pembagian berulang
while n > 0:
    a.append(n % 2)  # Menyimpan sisa hasil bagi (0 atau 1) ke list a
    n = n // 2  # Membagi angka dengan 2 untuk mendapatkan nilai berikutnya
    i = i + 1  # Menambah indeks 

print('Angka binernya adalah: ', end='')

# Membaca list dari belakang untuk menampilkan angka biner dengan benar
for i in range(i - 1, -1, -1):
    print(a[i], end='')  # Mencetak angka biner sesuai index dana tanpa spasi tambahan

#* versi(2)
# n = int(input('Input angka desimal: '))

# # Mengonversi angka desimal ke biner menggunakan fungsi bawaan bin()
# # Fungsi bin() menghasilkan string dalam format '0b...' sehingga '0b' dihapus dengan replace()
# biner = bin(n).replace("0b", "")

# print('Angka binernya adalah:', biner)

# #? Berikut contoh perbedaan hasil dari bin(x) dan bin(x).replace("0b",""):
# print(bin(211))                   # 0b11010011
# print(bin(211).replace("0b",""))  # 11010011
