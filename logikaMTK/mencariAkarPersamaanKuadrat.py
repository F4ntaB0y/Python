import math  # Mengimpor modul math untuk menggunakan fungsi sqrt()

print('##  Program Python Mencari Akar Persamaan Kuadrat  ##')
print('=====================================================')
print()
print('Format persamaan: ax^2 + bx + c = 0')

# Meminta pengguna untuk memasukkan nilai koefisien a, b, dan c
a = int(input('Input nilai a: '))
b = int(input('Input nilai b: '))
c = int(input('Input nilai c: '))
print()

# Menghitung diskriminan D = b^2 - 4ac
D = (b * b) - (4 * a * c)
print('Diskriminan =', D, end='')

# Menentukan jenis akar berdasarkan nilai diskriminan
if D > 0:
    print(' (akar real dan berbeda)')  # Jika D > 0, akar real dan berbeda
    x1 = (-b + math.sqrt(D)) / (2 * a)  # Menghitung akar pertama
    x2 = (-b - math.sqrt(D)) / (2 * a)  # Menghitung akar kedua

    print('x1 =', round(x1, 2))  # Menampilkan hasil x1 dengan 2 desimal
    print('x2 =', round(x2, 2))  # Menampilkan hasil x2 dengan 2 desimal

elif D == 0:
    print(' (akar real dan sama)')  # Jika D = 0, akar real dan sama
    x1 = (-b + math.sqrt(D)) / (2 * a)  # Menghitung satu akar (karena sama)
    x2 = x1  # x2 sama dengan x1

    print('x1 =', round(x1, 2))
    print('x2 =', round(x2, 2))

else:
    print(' (akar tidak real / imajiner)')  # Jika D < 0, akar imajiner
