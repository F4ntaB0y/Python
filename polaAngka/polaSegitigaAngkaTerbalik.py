print('##  Program Python Segitiga Angka Terbalik  ##')
print('==============================================')
print()

tinggiSegitiga = int(input('Masukan tinggi segitiga: '))
print()

# ?versi (1)
# for i in range(1,tinggiSegitiga + 1):
#     for j in range(tinggiSegitiga-i+1):
#         print(i, ' ', end='',sep='')
#     print()

# ?versi (2)
for i in range(1,tinggiSegitiga + 1):
    for j in range(1, tinggiSegitiga - i + 2):
        print(j, ' ', end='', sep='')
    print()

# ?versi (2.1)
for i in range(1,tinggiSegitiga + 1):
    for j in range(tinggiSegitiga):
        print(j + 1,' ', end='', sep='')
    tinggiSegitiga = tinggiSegitiga - 1
    print()