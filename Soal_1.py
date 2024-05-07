def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def modulus(angka):
    if angka % 2 == 0:
        return 'Genap'
    else:
        return 'Ganjil'

bilangan_pertama = int(input('Masukkan bilangan pertama:'))
bilangan_kedua = int(input('Masukkan bilangan kedua:'))

print('Hasil penjumlahan dari bilangan tersebut adalah ', penjumlahan(bilangan_pertama,bilangan_kedua))
print('Hasil pengurangan dari bilangan tersebut adalah ', pengurangan(bilangan_pertama,bilangan_kedua))
print('Hasil modulus dari bilangan tersebut adalah ', modulus(bilangan_pertama))
print('Hasil modulus dari bilangan tersebut adalah ', modulus(bilangan_kedua))




