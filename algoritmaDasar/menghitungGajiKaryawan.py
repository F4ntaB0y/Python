print('##  Program Python Menghitung Gaji Karyawan  ##')
print('===============================================')
print()

#* proses input
nama = input("Nama karyawan: ")
golongan = input("Golongan: ")
jamKerja = int(input("Jumlah jam kerja: "))

print()

#* menentukan Gaji golonan/jam
if golongan == 'A':
    upahPerJam = 5000
elif golongan == 'B':
    upahPerJam = 7000
elif golongan == 'C':
    upahPerJam = 7000
elif golongan == 'D':
    upahPerJam = 7000
else:
    print("Golongan tidak valid")

totalGaji = jamKerja * upahPerJam

#* cek apakah jam kerja lebih dari 48 jam
if(jamKerja - 48) > 0:
    totalGaji = totalGaji + ((jamKerja - 48) * 4000)

#* cetak output
print(nama, "Menerima upah Rp.", totalGaji,'Per minggu')
