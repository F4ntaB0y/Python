print('##  Program Python Menghitung Luas Trapesium  ##')
print('================================================')
print()

#?versi(1)
sisiAtas = float(input('Masukan panjang sisi sejajar atas: '))
sisiBawah = float(input('Masukan panjang sisi sejajar bawah: '))
tinggi = float(input('Masukan panjang sisi sejajar atas: '))
luas = 0.5 * (sisiAtas + sisiBawah) * tinggi

print('Luas Trapesium = ', round(luas, 2))

#?versi(2)
# sisiAtas = float(input('Masukan panjang sisi sejajar atas: '))
# sisiBawah = float(input('Masukan panjang sisi sejajar bawah: '))
# tinggi = float(input('Masukan panjang sisi sejajar atas: '))

print('Luas Trapesium = ', round(0.5 * (sisiAtas + sisiBawah) * tinggi, 2))

#?versi(3)
def luasTrapesium(sa, sb, t):
    return round(0.5 * (sisiAtas + sisiBawah) * tinggi, 2)

# sisiAtas = float(input('Masukan panjang sisi sejajar atas: '))
# sisiBawah = float(input('Masukan panjang sisi sejajar bawah: '))
# tinggi = float(input('Masukan panjang sisi sejajar atas: '))

print('Luas Trapesium = ', luasTrapesium(sisiAtas, sisiBawah, tinggi))