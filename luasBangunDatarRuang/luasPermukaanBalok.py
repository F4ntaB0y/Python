print('##  Program Python Menghitung Luas Balok  ##')
print('============================================')
print()

#? versi(1)
panjang = float(input('Masukan panjang balok: '))
lebar = float(input('Masukan lebar balok: '))
tinggi = float(input('Masukan tinggi balok: '))
luas = 2 * (panjang * lebar) + 2 * (panjang * tinggi) + 2 * (lebar * tinggi)

print('Luas permukaan balok: ', round(luas, 2))

#? versi(2)
# panjang = float(input('Masukan panjang balok: '))
# lebar = float(input('Masukan lebar balok: '))
# tinggi = float(input('Masukan tinggi balok: '))

print('Luas permukaan balok: ', round(2 * (panjang * lebar) + 2 * (panjang * tinggi) + 2 * (lebar * tinggi), 2))

#? versi(3)
def luasPermukaanBalok(p,l,t):
    return round(2 * (p * l) + 2 * (p * t) + 2 * (l * t), 2)
# panjang = float(input('Masukan panjang balok: '))
# lebar = float(input('Masukan lebar balok: '))
# tinggi = float(input('Masukan tinggi balok: '))

print('Luas permukaan balok: ', luasPermukaanBalok(panjang, lebar, tinggi))