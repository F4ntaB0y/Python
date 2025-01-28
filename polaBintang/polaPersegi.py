print('## Program Python Persegi Bintang ##')
print('====================================')
print()

besarPersegi = int(input('Masukan Angka: '))
print()

# ?dua Perulangan
# for i in range(besarPersegi):
#     for j in range(besarPersegi):
#         print(' *', end='')
#     print()

# ?satu Perulangan
for i in range(besarPersegi):
    print('* ' * besarPersegi)
