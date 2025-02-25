print('##  Program Python Menentukan Ganjil-Genap  ##')
print('=====================================================')
print()

#* versi(1)
x = int(input('Input sebuah angka bulat: '))

# Mengecek apakah angka genap atau ganjil
if (x % 2 == 0):
    print(x, 'adalah bilangan genap')
else:  
    print(x, 'adalah bilangan ganjil')

#* versi(2)
x = int(input('Input sebuah angka bulat: '))

# Mengecek apakah angka ganjil atau genap dengan kondisi terbalik
if (x % 2 != 0):  
    print(x, 'adalah bilangan ganjil')
else:  
    print(x, 'adalah bilangan genap')
