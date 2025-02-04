print('##  Program Python Cek Angka Prima  ##')
print('======================================')
print()

#* Penjelasan Bilangan Prima
"""
Bilangan prima adalah bilangan yang hanya memiliki dua faktor(1 dan dirinya sendiri),
2 adalah satu-satunya bilangan prima genap,
0 dan 1 bukan bilangan prima.
"""

#* versi(1)
x = int(input('Input satu angka bulat: '))

angka_prima = True

#? 0 atau 1 bukan bilangan prima,
# 0 bukan prima karena bisa dibagi dengan semua bilangan,
# 1 karena hanya bisa dibagi dengan 1.
if ((x == 0) or (x == 1)):
    angka_prima = False
else:
    #? Memeriksa apakah angka memiliki pembagi selain 1 dan dirinya sendiri
    for i in range(2, (x // 2)):
    # for i in range(2, int(x ** 0.5) + 1): #* Alternativ loop(lebih efisien), karena faktor bilangan tidak mungkin lebih besar dari akar kuadratnya.
        if ((x % i) == 0): 
            angka_prima = False
            break
if angka_prima:
    print(x, 'adalah angka prima')
else:
    print(x, 'bukan angka prima')

#* versi(2)
# #? Meminta input dari pengguna berupa angka bulat
# x = int(input('Input satu angka bulat: '))

# #? Mengasumsikan bahwa angka tersebut adalah bilangan prima
# angka_prima = True

# #? Jika angka adalah 0 atau 1, maka bukan bilangan prima
# if (x == 0) or (x == 1):
#     angka_prima = False
# else:
#     #? Loop untuk memeriksa apakah angka memiliki pembagi selain 1 dan dirinya sendiri
#     # for i in range(2, (x // 2)):  #! Loop dari 2 hingga x//2 (tidak optimal)
#     for i in range(2, int(x ** 0.5) + 1): #* gunakan agar lebih cepat:
#         if (x % i) == 0:  # Jika x habis dibagi i, maka bukan bilangan prima
#             angka_prima = False
#             break  # Hentikan loop setelah menemukan pembagi

# #? Menampilkan hasil apakah angka prima atau bukan
# if angka_prima:
#     print(x, 'adalah angka prima')
# else:
#     print(x, 'bukan angka prima, karena bisa dibagi', i)  # Menampilkan pembagi pertama yang ditemukan
