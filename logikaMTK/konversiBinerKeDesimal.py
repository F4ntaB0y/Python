print('##  Program Python Konversi Biner ke Desimal  ##')
print('================================================')
print()

#* versi(1)
angka_biner = int(input('Input angka biner: '))
print('Angka desimal dari biner', angka_biner, end='')

# Inisialisasi variabel untuk menyimpan hasil konversi
angka_desimal = 0  # Menyimpan hasil akhir dalam bentuk desimal
i = 1  # Nilai tempat (1, 2, 4, 8, ... sesuai dengan basis 2)

# Proses konversi biner ke desimal
while (angka_biner != 0):
    digit = angka_biner % 10  # Mengambil digit terakhir dari angka biner
    angka_desimal = angka_desimal + (digit * i)  # Mengalikan digit dengan nilai tempatnya
    i = i * 2  # Mengupdate nilai tempat (basis 2)
    angka_biner = angka_biner // 10  # Menghapus digit terakhir yang sudah diproses

# Menampilkan hasil konversi dalam format desimal
print(' =', angka_desimal)

#* versi(2) cara singkat dengan function bin()
angka_biner = input('Input angka biner: ')

# Mengonversi angka biner ke desimal menggunakan fungsi bawaan int()
# Parameter kedua pada int() adalah basis bilangan (dalam hal ini basis 2)
angka_desimal = int(angka_biner, 2)

print('Angka desimal dari biner', angka_biner, '=', angka_desimal)
