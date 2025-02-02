print('##  Program Python Menghitung Faktorial  ##')
print('===========================================')
print()

angka = int(input('Masukan Angka: '))

#? versi(1) menggunakan rekursif
# def faktorial(input):
#     #* if pertama
#     # if(input < 1):
#     #     return 1
#     # return input * faktorial(input - 1)

#     #* if kedua
#     if(input > 1):
#         return input * faktorial(input - 1)
#     else:
#         return 1

# print(angka, '! = ', faktorial(angka), sep='')\

#? versi(2) menggunakan fungsi biasa
def faktorial(input):
    hasil = 1
    for i in range(1, angka + 1):
        hasil = hasil * i
    return hasil

print(angka,'! = ', faktorial(angka), sep='')