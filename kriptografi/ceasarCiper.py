print('##  Program Python Caesar Cipher: Implementasi Enkripsi dan Dekripsi  ##')
print('========================================================================')
print()

# Daftar alfabet yang digunakan untuk enkripsi dan dekripsi
abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Meminta pengguna memasukkan angka sebagai kunci cipher
key = int(input('Masukkan cipher key (dalam angka, misal 9): '))

def encode(kalimat, cipherKey):
    """
    Fungsi untuk mengenkripsi atau mendekripsi teks menggunakan metode Caesar Cipher.
    
    Parameter:
    kalimat (str): Kalimat yang akan diproses.
    cipherKey (int): Jumlah pergeseran huruf dalam alfabet.
    
    Return:
    str: Kalimat hasil enkripsi atau dekripsi.
    """
    
    kalimat = kalimat.lower()  # Mengubah semua huruf menjadi huruf kecil
    hasilEncode = ''  # Menyimpan hasil enkripsi atau dekripsi
    
    for karakter in kalimat:
        if karakter in abjad:  # Memeriksa apakah karakter ada dalam daftar alfabet
            indexLama = abjad.index(karakter)  # Mendapatkan posisi huruf saat ini dalam alfabet
            indexBaru = (indexLama + cipherKey) % len(abjad)  # Menggeser posisi sesuai cipherKey
            abjadBaru = abjad[indexBaru]  # Mendapatkan huruf baru setelah pergeseran
            hasilEncode += abjadBaru  # Menambahkan huruf hasil enkripsi ke string hasil
        else:
            hasilEncode += ' '  # Jika karakter bukan huruf (misal spasi), tetap dipertahankan
    
    return hasilEncode  # Mengembalikan hasil enkripsi atau dekripsi

# Meminta input dari pengguna untuk kalimat yang akan dienkripsi
kalimat = input('Masukkan kalimat yang ingin dienkripsi    : ')

# ENKRIPSI
kalimat_hasil = encode(kalimat, key)
print('Hasil enkripsi kalimat :', kalimat_hasil)

# DEKRIPSI (dengan menggunakan kunci negatif)
kalimat_awal = encode(kalimat_hasil, -key)
print('Hasil deskripsi kalimat:', kalimat_awal)
