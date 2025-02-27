print('##  Program Python Diskon Potongan Harga  ##')
print('============================================')
print()

totalBelanja = int(input("Total Belanja: Rp."))

if (totalBelanja >= 10000) and (totalBelanja < 500000):
    hargaAkhir = totalBelanja - (0.1 * totalBelanja)
    print('Selamat, anda mendapat diskon 10%')
elif (totalBelanja >= 500000) and (totalBelanja < 1000000):
    hargaAkhir = totalBelanja - (0.2 * totalBelanja)
    print('Selamat, anda mendapat diskon 20%')
elif (totalBelanja >= 1000000):
    hargaAkhir = totalBelanja - (0.3 * totalBelanja)
    print('Selamat, anda mendapat diskon 30%')
else:
    hargaAkhir = totalBelanja

print("Total bayar: Rp.", round(hargaAkhir, 2))