print('##  Program Python Cek Kata Palindrom  ##')
print('=========================================')
print()

x = input('Masukan kata/kalimat: ')
palindrom = True
panjang_x = len(x)

for i in range(panjang_x // 2):
    if(x[i] != x[panjang_x-i-1]):
        palindrom = False
        break

if palindrom:
    print(x, 'adalah palindrome!')
else:
    print(x, 'bukan palindrome!')