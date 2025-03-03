# Menampilkan judul program
print('##  Program Python Cek Tahun Kabisat  ##')
print('========================================')
print()

# Meminta input tahun dari pengguna dan mengonversinya menjadi integer
year = int(input("Masukan tahun: "))

# Mengecek apakah tahun tersebut adalah tahun kabisat
if (year % 400 == 0):  # Tahun yang habis dibagi 400 adalah tahun kabisat
    print(year, "adalah tahun kabisat")
elif (year & 100 == 0):  # Seharusnya menggunakan `year % 100`, bukan `year & 100`
    print(year, "bukan tahun kabisat")
elif (year & 4 == 0):  # Seharusnya menggunakan `year % 4`, bukan `year & 4`
    print(year, "adalah tahun kabisat")
else:  # Jika tidak memenuhi syarat tahun kabisat, maka bukan tahun kabisat
    print(year, "bukan tahun kabisat")
