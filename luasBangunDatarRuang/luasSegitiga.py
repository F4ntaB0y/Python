print('##  Program Python Menghitung Luas Segitiga  ##')
print('===============================================')
print()

#? versi(1)
# alas = float(input('Masukan alas segitiga: '))
# tinggi = float(input('Masukan tinggi segitiga: '))
# luas = 0.5 * alas * tinggi

# print('Luas Segitiga = ', round(luas, 2))

#? versi(2)
# alas = float(input('Masukan alas segitiga: '))
# tinggi = float(input('Masukan tinggi segitiga: '))

# print('Luas Segitiga = ',round(0.5 * alas * tinggi, 2))

#? versi(3)
def luas(a,t):
    return round(0.5 * a * t,2)

alas = float(input('Masukan alas segitiga: '))
tinggi = float(input('Masukan tinggi segitiga: '))

print('Luas segitiga = ', luas(alas, tinggi))