#* Menampilkan judul program
print('##  Program Python Cek Kata Palindrom  ##')
print('=========================================')
print()

#* Menerima input dari pengguna
x = input('Masukan kata/kalimat: ')

#* Inisialisasi variabel
palindrom = True # Asumsi awal bahwa input adalah palindrom
panjang_x = len(x) # Menghitung panjang string

#* Mengecek apakah input adalah palindrom
for i in range(panjang_x // 2): # Looping setengah panjang string
    if(x[i] != x[panjang_x-i-1]): # Bandingkan karakter depan dan
        palindrom = False # Jika berbeda, bukan palindrom
        break # Hentikan loop jika bukan palindrom

#* Menampilkan hasil
if palindrom:
    print(x, 'adalah palindrome!')
else:
    print(x, 'bukan palindrome!')
