print('##  Program Python Menghitung Luas Lingkaran  ##')
print('================================================')
print()

#? versi(1)
# r = float(input('Masukan jari-jari lingkaran: '))
# luas = 3.14 * r * r

# print('Luas lingkaran = ', round(luas, 2))

#? versi(2)
# r = float(input("Masukan jari-jari lingkaran: "))

# print('Luas Lingkaran: ', round(3.14 * r * r, 2))

#? versi(3)
def luasLingkaran(jariJari):
    return round(3.14 * jariJari * jariJari, 2)

r = float(input('Masukan jari-jari lingkaran: '))

print('Luas Lingkaran = ', luasLingkaran(r))