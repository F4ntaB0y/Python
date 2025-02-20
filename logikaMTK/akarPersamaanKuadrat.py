import math  # Mengimpor modul math untuk operasi matematika seperti akar kuadrat

# Menampilkan judul program
print('##  Program Python Mencari Akar Persamaan Kuadrat  ##')
print('=====================================================')
print()

# Menampilkan format umum persamaan kuadrat
print('Format persamaan: ax^2 + bx + c = 0')

# Meminta pengguna untuk memasukkan nilai a, b, dan c
# Konversi input menjadi integer
a = int(input('Input nilai a: '))
b = int(input('Input nilai b: '))
c = int(input('Input nilai c: '))
print()

# Menghitung diskriminan dengan rumus D = b^2 - 4ac
D = (b*b)-(4*a*c)
print('Diskriminan =',D,end='')

# Mengecek jenis akar berdasarkan nilai diskriminan
if (D > 0):  # Jika D > 0, akar real dan berbeda
    print(' (akar real dan berbeda)');
    # Menghitung akar persamaan menggunakan rumus kuadratik
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    # Menampilkan akar dengan pembulatan dua desimal
    print('x1 =',round(x1,2))
    print('x2 =',round(x2,2))
elif (D == 0):  # Jika D = 0, akar real dan sama
    print(' (akar real dan sama)');
    x1 = (-b + math.sqrt(D)) / (2*a)  # Karena D = 0, kedua akar bernilai sama
    x2 = x1

    print('x1 = ',round(x1,2))
    print('x2 = ',round(x2,2))
else:  # Jika D < 0, akar bersifat imajiner
    print(' (akar tidak real / imajiner)');
