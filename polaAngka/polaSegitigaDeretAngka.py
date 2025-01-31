print('##  Program Python Segitiga Deret Angka  ##')
print('===========================================')
print()

tinggiSegitiga = int(input('Masukan tinggi segitiga: '))
print()

#? versi (1)
# k = 1
# for i in range(tinggiSegitiga):
#     for j in range(i + 1):
#         print(k, ' ', end='', sep='')
#         k = k + 1
#     print()

#? versi (2) rata kanan
k = 1
for i in range(1,tinggiSegitiga): # Jumlah baris
    for j in range(i): # Isi baris
        print(f'{k:>2} ', end='', sep='')
        # f'{k:>2} ' -> Format angka agar rata kanan dengan lebar minimal 2 karakter
        # end='' -> Mencegah pindah baris setelah mencetak angka, agar tetap dalam satu baris
        # sep='' -> Tidak ada pemisah tambahan antara elemen (default untuk print)
        k = k + 1 # Menambah  nilai k
    print() # Pindah baris