import sys  # Library untuk berinteraksi dengan sistem, digunakan untuk flush output ke terminal
import time  # Library untuk menambahkan delay (jeda) dalam mencetak lirik lagu

# Fungsi untuk menampilkan lirik lagu dengan efek mengetik perlahan
def lirikNina():
    # List yang berisi tuple dengan lirik lagu dan waktu jeda per karakter
    lirik = [
        ("Saat engkau teringat", 0.2),
        ("Tengkar kita, manakala", 0.2),
        ("Maaf atas perjalanan yang tidak sempurna", 0.1),
        ("Namun percayalah, untukmu kujual dunia", 0.1),
        ("", 0.3),  # Baris kosong sebagai jeda
        ("Segala hal kuupayakan untuk melindungi", 0.2),
        ("Tunggu aku kembali lagi esok pagi", 0.2),
        ("", 0.3),  # Baris kosong sebagai jeda
        ("Tumbuh lebih baik, cari panggilanmu", 0.1),
        ("Jadi lebih baik dibanding diriku", 0.1),
        ("Dan tertawalah saat ini selepas-lepasnya", 0.1),
        ("Kar'na kelak kau 'kan tersakiti", 0.1)
    ]

    # List berisi waktu jeda antar baris lirik
    delay = [
        0.8, 0.8, 2, 1.4,
        0.1, 6.5, 6.5, 0.5,
        1, 1, 2, 2
    ]

    # Menampilkan judul lagu
    print("\n==Nina - Feast==")
    time.sleep(2)  # Jeda sebelum mulai menampilkan lirik

    # Loop untuk mencetak lirik satu per satu dengan efek mengetik
    for i, (barisLagu, delayKarakter) in enumerate(lirik):
        for karakter in barisLagu:
            print(karakter, end='')  # Mencetak karakter satu per satu tanpa newline
            sys.stdout.flush()  # Memastikan karakter langsung ditampilkan di terminal
            time.sleep(delayKarakter)  # Jeda antar karakter untuk efek mengetik

        time.sleep(delay[i])  # Jeda setelah satu baris selesai dicetak
        print('')  # Pindah ke baris baru setelah mencetak satu baris lirik

    # Menampilkan kredit pembuat kode
    print("\nCode by Aestu")

# Memanggil fungsi untuk menampilkan lirik lagu
lirikNina()
