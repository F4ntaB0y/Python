print('## Program Python Piramida Bintang Terbalik ##')
print('============================================')
print()

tinggiPiramida = int(input('Masukan tinggi piramaida: '))
print()

#? dua perulangan
# for i in range(tinggiPiramida):
#     for j in range(i + 1):
#         print(' ', end='')
    
#     for k in range(tinggiPiramida-i):
#         print(' *', end='')
#     print()

#? satu perulangan
for i in range(tinggiPiramida):
    print(' ' * (i + 1), end='')
    print(' *' * (tinggiPiramida - i))
