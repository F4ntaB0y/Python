print('## Program Python Persegi Panjang Bintang ##')
print('============================================')
print()

tinggi = int(input("Masukan tinggi persegi: "))
lebar = int(input("Masukan lebar persegi : "))
print()

#? dua perulangan
# for i in range(tinggi):
#     for i in range(lebar):
#         print(' *', end='')
#     print()

#? satu perulangan
for i in range(tinggi):
        print(' *' * lebar)
