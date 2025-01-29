print('## Program Python Segitiga Bintang Terbalik ##')
print('============================================')
print()

tinggiSegitiga = int(input('Masukan tinggi segitiga: '))
print()

#? dua perulangan
# for i in range(tinggiSegitiga):
#     for j in range(tinggiSegitiga - i):
#         print(' *', end="")
#     print()

#? satu perulangan
for i in range(tinggiSegitiga):
    print(' *' * (tinggiSegitiga - i))
