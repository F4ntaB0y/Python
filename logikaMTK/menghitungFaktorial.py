print('##  Program Python Menghitung Faktorial  ##')
print('===========================================')
print()

angka = int(input('Masukan angka: '))

#? versi(1)
# hasil = 1
# for i in range(1, angka + 1):
#     hasil = hasil * i
# print(angka, '! = ', hasil, sep='')

#? versi(1.1)
# hasil = 1
# for i in range(2, angka + 1): #perulangan di mulai dari 2 karena hasil sudah bernilai 1
    # hasil = hasil * i
# print(angka, '! = ', hasil, sep='')

#? versi(2) menggunakan fungsi bawaan
# import math
# print(f'{angka}! = {math.factorial(angka)}')

#? versi(3) menggunakan def fungsi
def faktorial(n):
    if(n == 0 or n == 1): #! basis kasus untuk mencegah tekursi tak terbatas
        return 1
    return(n * faktorial(n - 1)) # menggunakan rekursif, memanggil dirinya sendiri lalu dikalikan dengan n, n dikurangi sampai habis 
print(f'{angka}! = {faktorial(angka)}')
