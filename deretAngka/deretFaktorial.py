print('##  Program Python Deret Faktorial  ##')
print('======================================')
print()

# Meminta pengguna untuk memasukkan sebuah angka
angka = int(input('Masukan angka: '))  # Konversi input menjadi integer

# Menampilkan format awal hasil faktorial
print(angka, '! = ', sep='', end='')

# Inisialisasi variabel hasil dengan nilai 1 (karena faktorial melibatkan perkalian)
hasil = 1

# Perulangan untuk menghitung faktorial
for i in range(1, angka + 1):  #Loop dari 1 hingga angka yang dimasukkan
    hasil = hasil * i  #Mengalikan hasil dengan nilai i saat ini
    print(i, end='')  #Menampilkan angka yang dikalikan

    #Menampilkan simbol perkalian kecuali untuk angka terakhir
    if(i != angka):
        print(' * ', end='')

#Menampilkan hasil akhir faktorial
print(' = ', hasil)
