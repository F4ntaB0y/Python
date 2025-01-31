print('##  Program Python Menghitung Luas Belah Ketupat  ##')
print('====================================================')
print()

#? versi(1)
# d1 = float(input('Masukan panjang diagonal 1: '))
# d2 = float(input('Masukan panjang diagonal 2: '))
# luas = 0.5 * d1 * d2

# print('Luas belah ketupat = ', round(luas, 2))

# #? versi(2)
# d1 = float(input('Masukan panjang diagonal 1: '))
# d2 = float(input('Masukan panjang diagonal 2: '))

# print('Luas belah ketupat = ', round(0.5 * d1 * d2, 2))

#? versi(3)
def luasBelahKetupat(D1, D2):
    return round(0.5 * D1 * D2, 2)

d1 = float(input('Masukan panjang diagonal 1: '))
d2 = float(input('Masukan panjang diagonal 2: '))

print('Luas belah ketupat = ', luasBelahKetupat(d1, d2))