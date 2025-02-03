# Program Python Menentukan Ganjil-Genap
print('##  Program Python Menentukan Ganjil-Genap  ##')
print('=====================================================')
print()

#* versi(1)
# Meminta pengguna untuk memasukkan sebuah angka bulat
x = int(input('Input sebuah angka bulat: '))

# Mengecek apakah angka genap atau ganjil
if (x % 2 == 0):  # Jika sisa pembagian angka dengan 2 adalah 0, maka angka genap
    print(x, 'adalah bilangan genap')
else:  # Jika tidak, maka angka ganjil
    print(x, 'adalah bilangan ganjil')

#* versi(2)
# Meminta pengguna untuk memasukkan sebuah angka bulat
x = int(input('Input sebuah angka bulat: '))

# Mengecek apakah angka ganjil atau genap dengan kondisi terbalik
if (x % 2 != 0):  # Jika sisa pembagian angka dengan 2 tidak sama dengan 0, maka angka ganjil
    print(x, 'adalah bilangan ganjil')
else:  # Jika sisa pembagiannya 0, maka angka genap
    print(x, 'adalah bilangan genap')