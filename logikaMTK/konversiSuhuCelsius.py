print('##  Program Python Konversi Suhu  ##')
print('====================================')
print()

cels = int(input('Masukan suhu celsius: '))

#* RUMUS KONVERSI SUHU
fahr = (9/5) * cels + 32
kelv = cels + 273.15
ream = (4/5) * cels

print(cels,'derajat Celsius =',fahr,'derajat Fahrenheit')
print(cels,'derajat Celsius =',kelv,'derajat Kelvin')
print(cels,'derajat Celsius =',ream,'derajat Reamur')