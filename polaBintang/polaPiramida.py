print('## Program Python Segitiga Bintang ##')
print('============================================')
print()

tinggiPiramida = int(input('Masukan tinggi piramaida: '))
print()

# ?dua perulangan
# for i in range(tinggiPiramida):
#     for j in range(tinggiPiramida-i):
#         print(' ', end='')
    
#     for k in range(i+1):
#         print(' *', end='')
#     print()

# ?satu perulangan
for i in range(tinggiPiramida):
    print(' ' * (tinggiPiramida - i),end='')
    print(' *' * (i + 1))