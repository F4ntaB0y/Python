print('##  Program Python Menentukan Nama Bulan  ##')
print('============================================')
print()

#* versi(1)
# x = int(input('Input angka bulan (1-12): '))

# if x == 1:
#     print('Januari')
# elif x == 2:
#     print('Februari')
# elif x == 3:
#     print('Maret')
# elif x == 4:
#     print('April')
# elif x == 5:
#     print('Mei')
# elif x == 6:
#     print('Juni')
# elif x == 7:
#     print('Juli')
# elif x == 8:
#     print('Agustus')
# elif x == 9:
#     print('September')
# elif x == 10:
#     print('Oktober')
# elif x == 11:
#     print('November')
# elif x == 12:
#     print('Desember')
# else:
#     print('Pilihan tidak tersedia')

#* versi(2)
# x = int(input('Input angka bulan (1-12): '))

# match x:
#     case 1:
#         print('Januari')
#     case 2:
#         print('Februari')
#     case 3:
#         print('Maret')
#     case 4:
#         print('April')
#     case 5:
#         print('Mei')
#     case 6:
#         print('Juni')
#     case 7:
#         print('Juli')
#     case 8:
#         print('Agustus')
#     case 9:
#         print('September')
#     case 10:
#         print('Oktober')
#     case 11:
#         print('November')
#     case 12:
#         print('Desember')
#     case _:
#         print('Pilihan tidak tersedia')

#* versi(3)
# x = int(input('Input angka bulan (1-12): '))

# match x:
#     case 1:
#         bulan = 'Januari'
#     case 2:
#         bulan = 'Februari'
#     case 3:
#         bulan = 'Maret'
#     case 4:
#         bulan = 'April'
#     case 5:
#         bulan = 'Mei'
#     case 6:
#         bulan = 'Juni'
#     case 7:
#         bulan = 'Juli'
#     case 8:
#         bulan = 'Agustus'
#     case 9:
#         bulan = 'September'
#     case 10:
#         bulan = 'Oktober'
#     case 11:
#         bulan = 'November'
#     case 12:
#         bulan = 'Desember'
#     case _:
#         print('Pilihan tidak tersedia')

# if (x >= 1) and (x <= 12):
#     print('Bulan ke-',x,' adalah ',bulan,sep="")