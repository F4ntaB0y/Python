print('##  Program Python Menghitung Luas Persegi Panjang  ##')
print('======================================================')
print()

#? versi (1)
# panjang = float(input('Masukan panjang persegi: '))
# lebar = float(input('Masukan lebar persegi  : '))

# luas = panjang * lebar
# print('Luas Persegi Panjang   :',round(luas,2))

#? versi (2)
# panjang = float(input('Masukan panjang persegi: '))
# lebar = float(input('Masukan lebar persegi  : '))

# print('Luas Persegi panjang    =', round(panjang * lebar, 2))

#? versi (3)
def hitungLuasPersegiPanjang(p,l):
    return round(p * l, 2)

panjang = float(input('Masukan panjang persegi: '))
lebar   = float(input('Masukan lebar persegi  : '))
print('Luas persegi panjang   = ', hitungLuasPersegiPanjang(panjang,lebar))