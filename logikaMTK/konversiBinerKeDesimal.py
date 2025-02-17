print('##  Program Python Konversi Biner ke Desimal  ##')
print('================================================')
print()

#* versi(1)
# angkaBiner = int(input('Masukan angka biner: '))
# angkaDesimal = 0 # wadah untuk menyimpan angka desimal setelah di hitung
# i = 1 # Wadah pola nilai setelah dikali (basis 2)

# #? Proses konversi biner ke desimal
# while (angkaBiner != 0):
#     digit = angkaBiner % 10  # Mengambil digit terakhir dari angka biner
#     angkaDesimal = angkaDesimal + (digit * i)  # Mengalikan digit dengan nilai tempatnya
#     i = i * 2  # Mengupdate nilai wadaah (basis 2)
#     angkaBiner = angkaBiner // 10  # Menghapus digit terakhir yang sudah diproses

# print('Angka desimalnya:', angkaDesimal)

#* versi(2) cara singkat dengan function bin()
# angkaBiner = input('Masukan angka biner: ')

# #? Mengonversi angka biner ke desimal menggunakan fungsi bawaan int()
# angkaDesimal = int(angkaBiner, 2) #! Parameter 2 pada int() memeberitahu Python bahwa input adalah bilangan biner dan perlu dikoncersi ke desimal

# print('Angka desimal dari biner', angkaBiner, '=', angkaDesimal)
