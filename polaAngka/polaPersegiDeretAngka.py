print('##  Program Python Persegi Deret Angka ##')
print('=========================================')
print()

besarPersegi = int(input('Masukan besar persegi: '))
print()

#? versi (1)
# k = 1 #variabel penyimpanan
# for i in range(1, besarPersegi + 1): #looping baris 
#     for j in range(1, besarPersegi + 1): #looping kolom
#         print( k ,' ', end='', sep='') #end untuk akhir looping, sep untuk jarak setiap argumen
#         k = k + 1 #perbarui variabel penyimpanan
#     print()

#? versi (2)
k = 1
for i in range(1, besarPersegi + 1):
    for i in range(1, besarPersegi + 1):
        print(f'{k:>3} ', end='',sep='') #* fString untuk format rata kanan(just for aesthetic), jika satuan tidak perlu, jika puluhan gunakan :>2, jika ratusan :>3, dan seterusnya.
        k = k + 1
    print()
