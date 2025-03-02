#* Mengimpor modul re untuk bekerja dengan ekspresi reguler (regex)
import re

#* Menampilkan judul program
print('##  Program Python Cek Kata Palindrom  ##')
print('=========================================')
print()

#* Menerima input dan memersihkannya
x = input('Masukan kata/kalimat: ')
x_clean = re.sub(r'[^a-zA-Z0-9]', '', x.lower()) # Hapus simbol, spasi, dan ubah ke huruf kecil

#* Inisialisasi variabel
palindrom = True # Asumsi awal bahwa input adalah palindrom
panjang_x = len(x) # Menghitung panjang string

#* Mengecek apakah input adalah palindrom
#* versi(1)
# for i in range(panjang_x // 2): # Looping setengah panjang string
#     if(x[i] != x[panjang_x-i-1]): # Bandingkan karakter depan dan
#         palindrom = False # Jika berbeda, bukan palindrom
#         break # Hentikan loop jika bukan palindrom
# 
# #* Menampilkan hasil
# if palindrom:
#     print(x, 'adalah palindrome!')
# else:
#     print(x, 'bukan palindrome!')

#* veris(2)
# Mengecek apakah input yang telah dibersihkan adalah palindrom
if x_clean == x_clean[::-1]:  # Membandingkan string dengan versi terbaliknya
    print(x, 'adalah palindrome!')
else:
    print(x, 'bukan palindrome!')
