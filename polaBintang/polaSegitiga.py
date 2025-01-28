print('## Program Python Segitiga Bintang ##')
print('============================================')
print()

tinggiSegitiga = int(input('Masukan tinggi segitiga: '))
print()

# ?dua perulangan
for i in range(tinggiSegitiga):
    for j in range(i ):
        print(' *', end='')
    print()

# ?satu perulangan
# for i in range(tinggiSegitiga + 1):
#     print(' *' * i)