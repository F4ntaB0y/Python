print('##  Program Python Belah Ketupat Bintang  ##')
print('============================================')
print()

lebarBelahKetupat = int(input('Masukan lebar belah ketupat: '))
print()

#? enam perulangan
# for i in range(lebarBelahKetupat):
#     for j in range(lebarBelahKetupat - i):
#         print(' ', end='')

#     for k in range(i + 1):
#         print(' *',end='')
#     print()

# for i in range(1, lebarBelahKetupat): # !Set agar perulangan mulai dari 1
#     for j in range(i + 1):
#         print(' ', end='')

#     for k in range(lebarBelahKetupat - i):
#         print(' *', end='')
#     print()

#? dua perulangan
for i in range(lebarBelahKetupat):
    print(' ' * (lebarBelahKetupat - i), end='')
    print(' *' * (i + 1))

for i in range(1, lebarBelahKetupat):
    print(' ' * (i + 1), end='')
    print(' *' * (lebarBelahKetupat - i))
