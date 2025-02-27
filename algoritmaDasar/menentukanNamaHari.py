print('##  Program Python Menentukan Nama Hari  ##')
print('===========================================')
print()

x = int(input("Masukan angka hari (1-7): "))

if(x == 1):
    print("Senin")
elif(x == 2):
    print("Selasa")
elif(x == 3):
    print("Rabu")
elif(x == 4):
    print("Kamis")
elif(x == 5):
    print("Jumat")
elif(x == 6):
    print("Sabtu")
elif(x == 7):
    print("Minggu")
else:
    print("Pilihan tidak tersedia")