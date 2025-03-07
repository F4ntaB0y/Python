print('##  Program Python Menentukan Ganjil-Genap  ##')
print('=====================================================')
print()

#* versi(1)
x = int(input('Masukan sebuah angka bulat: '))

# # Mengecek apakah angka genap atau ganjil
if(x % 2 == 0):
     print(x, 'adalah angka genap')
 else:
     print(x, 'adalah angka ganjil')

#* versi(2)
 x = int(input('Masukan angka bulat'))

 # Mengecek apakah angka ganjil atau genap dengan kondisi terbalik
 if(x % 2 != 0):
     print(x, 'adalah angka ganjil')
 else:
     print(x, 'adalah angka genap')
