print('##  Program Python Cek Angka Prima  ##')
print('======================================')
print()

#* Penjelasan Bilangan Prima
"""
Bilangan prima adalah bilangan yang hanya memiliki dua faktor(1 dan dirinya sendiri),
2 adalah satu-satunya bilangan prima genap,
0 dan 1 bukan bilangan prima.
"""

# #* versi(1)
# x = int(input('Input satu angka bulat: '))

# angka_prima = True

# #? 0 atau 1 bukan bilangan prima,
# # 0 bukan prima karena bisa dibagi dengan semua bilangan,
# # 1 karena hanya bisa dibagi dengan 1.
# if ((x == 0) or (x == 1)):
#     angka_prima = False
# else:
#     #? Memeriksa apakah angka memiliki pembagi selain 1 dan dirinya sendiri
#     for i in range(2, (x // 2)):
#             angka_prima = False
#             break
# if angka_prima:
#     print(x, 'adalah angka prima')
# else:
#     print(x, 'bukan angka prima karena bisa dibagi', i)

"""
#* BUG DI VERSI 1
#! Name Error jika dimasaukan 1 atau 0
#! Jika memasukan 4 ke x hasilnya prima pdhl 4 bukan prima
"""

#* versi(2) memperbaiki bug di versi sebelumnya
x = int(input('Input satu angka bulat: '))

#? bilangan prima dimulai dari 2
if x < 2:
    print(x, 'bukan angka prima')

#? mengecek angka
else:
    angka_prima = True 

    #? faktor bilangan tidak mungkin lebih besar dari akar kuadratnya.
    for i in range(2, int(x**0.5) + 1): #! harus dikonversi ke int jika tidak akan error
        if x % i == 0:  
            angka_prima = False
            print(x, 'bukan angka prima, karena bisa dibagi', i)  # Cetak pembagi pertama yang ditemukan
            break  

    # Jika tidak ditemukan pembagi, berarti x adalah bilangan prima
    if angka_prima:
        print(x, 'adalah angka prima')
