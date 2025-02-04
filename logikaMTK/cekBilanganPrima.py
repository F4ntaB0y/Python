print('##  Program Python Cek Angka Prima  ##')
print('======================================')
print()

#* versi(1)
# #? Meminta input dari pengguna berupa angka bulat
# x = int(input('Input satu angka bulat: '))

# #? Mengasumsikan bahwa angka tersebut adalah bilangan prima
# angka_prima = True

# #? Jika angka adalah 0 atau 1, maka bukan bilangan prima
# if ((x == 0) or (x == 1)):
#     angka_prima = False
# else:
#     #? Memeriksa apakah angka memiliki pembagi selain 1 dan dirinya sendiri
#     # for i in range(2, (x // 2)):  #! Loop dari 2 hingga x//2 (kurang optimal)
#     for i in range(2, int(x ** 0.5) + 1): #* gunakan agar lebih cepat, karena faktor bilangan tidak mungkin lebih besar dari akar kuadratnya.
#         if ((x % i) == 0):  # Jika habis dibagi i, maka bukan bilangan prima
#             angka_prima = False
#             break  # Hentikan loop jika sudah ditemukan faktor pembagi

# #? Menampilkan hasil apakah angka prima atau bukan
# if angka_prima:
#     print(x, 'adalah angka prima')
# else:
#     print(x, 'bukan angka prima')

#* versi(2)
#? Meminta input dari pengguna berupa angka bulat
#
