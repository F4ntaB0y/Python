print('##  Program Python Deret Angka Ganjil/Genap  ##')
print('========================================')
print()

#! Input versi(1)(2)
# jumlahDeret = int(input('Masukan jumlah deret: ')) 

#? versi(1) genap
# for i in range(1 ,jumlahDeret + 1):
#     print(i * 2, end=' ')

#? versi(2) ganjil
# for i in range(1 ,jumlahDeret + 1):
#     print((i * 2) - 1, end=' ')

#! Input versi(1.1)(1.2)
awal = int(input('Masukan angka awal: '))
akhir = int(input('Masukan angka akhir: '))

# #? versi(1.1) genap dengan range
# for i in range(awal, akhir + 1):
#     if(i % 2 == 0): #Genap: habis dibagi 2
#         print(i, end=' ')

#? versi(2.1) ganjil dengan range
for i in range(awal, akhir + 1):
    if(i % 2 != 0): #Ganjil: tidak habis dibagi 2
        print(i, end=' ')
