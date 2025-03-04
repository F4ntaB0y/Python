# Menampilkan judul program
print('##  Program Python Diskon Potongan Harga  ##')
print('============================================')
print()

# Meminta pengguna memasukkan total belanja
totalBelanja = int(input("Total Belanja: Rp."))

# Menentukan diskon berdasarkan total belanja
if (totalBelanja >= 10000) and (totalBelanja < 500000):  
    # Jika total belanja antara Rp10.000 hingga kurang dari Rp500.000, diskon 10%
    hargaAkhir = totalBelanja - (0.1 * totalBelanja)
    print('Selamat, anda mendapat diskon 10%')
elif (totalBelanja >= 500000) and (totalBelanja < 1000000):  
    # Jika total belanja antara Rp500.000 hingga kurang dari Rp1.000.000, diskon 20%
    hargaAkhir = totalBelanja - (0.2 * totalBelanja)
    print('Selamat, anda mendapat diskon 20%')
elif (totalBelanja >= 1000000):  
    # Jika total belanja Rp1.000.000 atau lebih, diskon 30%
    hargaAkhir = totalBelanja - (0.3 * totalBelanja)
    print('Selamat, anda mendapat diskon 30%')
else:  
    # Jika total belanja kurang dari Rp10.000, tidak ada diskon
    hargaAkhir = totalBelanja

# Menampilkan total pembayaran setelah diskon
print("Total bayar: Rp.", round(hargaAkhir, 2))
