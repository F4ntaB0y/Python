print('##  Program Python Segitiga Angka  ##')
print('=====================================')
print()

tinggiSegitiga = int(input('Masukan tinggi segitiga: '))
print()

#? versi (1)
# for i in range(1, tinggiSegitiga + 1):
#     for j in range(i):
#         print(i, ' ', end='', sep='')
#     print()

#? versi (1.1)
# k = 1
# for i in range(tinggiSegitiga):
#     for j in range(k):
#         print(k, ' ', end='', sep='')
#     k = k + 1
#     print()

#? versi (2)
for i in range(1, tinggiSegitiga + 1):
    for j in range(1, i + 1):
        print(i, ' ', end='', sep='')
    print()

#? versi (2.1)
# for i in range(1, tinggiSegitiga + 1):
#     for j in range(i):
#         print(j + 1, ' ', end='', sep='')
#         j = j + 1
#     print()