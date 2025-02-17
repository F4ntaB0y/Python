print('##  Program Python Konversi Biner ke Desimal  ##')
print('================================================')
print()

#* versi(1)
angka_biner = int(input('Masukan angka biner: '))
print('Angka desimal dari biner', angka_biner, end='')

angka_desimal = 0
i = 1 # Wadah pola nilai

#? Proses konversi biner ke desimal
while (angka_biner != 0):
    digit = angka_biner % 10  # Mengambil digit terakhir dari angka biner
    angka_desimal = angka_desimal + (digit * i)  # Mengalikan digit dengan nilai tempatnya
    i = i * 2  # Mengupdate nilai tempat (basis 2)
    angka_biner = angka_biner // 10  # Menghapus digit terakhir yang sudah diproses

print(' =', angka_desimal)

#* versi(2) cara singkat dengan function bin()
# # Meminta pengguna untuk memasukkan angka biner dalam bentuk string
# angka_biner = input('Masukan angka biner: ')

# # Mengonversi angka biner ke desimal menggunakan fungsi bawaan int()
# # Parameter kedua pada int() adalah basis bilangan (dalam hal ini basis 2)
# angka_desimal = int(angka_biner, 2)

# # Menampilkan hasil konversi dari biner ke desimal
# print('Angka desimal dari biner', angka_biner, '=', angka_desimal)
