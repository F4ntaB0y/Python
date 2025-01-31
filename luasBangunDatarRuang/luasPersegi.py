print('##  Program Python Menghitung Luas Persegi  ##')
print('==============================================')
print()

#? versi (1)
# sisiPersegi = float(input('Masukan panjang sisi persegi: '))
# luas = sisiPersegi * sisiPersegi
# print('Luas Persegi = ',round(luas,2)) # round(luas,2) berfungsi untuk membulatkan nilai variabel luas dengan 2 tempat desimal

#? versi (2)
# sisiPersegi = float(input('Masukan panjang sisi persegi: '))
# print('Luas Persegi = ', round(sisiPersegi * sisiPersegi, 2))

#? versi (3)
def hitungLuasPersegi(sisiPersegi):
    return round(sisiPersegi * sisiPersegi, 2)

sisiPersegi = float(input('Masukan Luas Persegi: '))
print('Luas Persegi = ', hitungLuasPersegi(sisiPersegi))
