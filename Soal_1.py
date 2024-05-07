def penjumlahan(a,b):
    return a + b

def pengurangan(a,b):
    return a - b

def modulus(angka):
    if angka % 2 == 0:
        return 'Genap'
    else:
        return 'Ganjil'

def operasi_bilangan():
   a = int(input('Masukkan bilangan pertama: '))
   b = int(input('Masukkan bilangan kedua: ')) 

hasil_penjumlahan = penjumlahan(a, b)
print(f"Hasil penjumlahan {a} + {b} = {hasil_penjumlahan}")  
hasil_pengurangan = pengurangan(a, b)
print(f"Hasil pengurangan {a} - {b} = {hasil_pengurangan}")        
hasil_modulus_a = modulus(a)
print(f"Modulus {a} adalah {hasil_modulus_a}")
hasil_modulus_b = modulus(b)
print(f"Modulus {b} adalah {hasil_modulus_b}")


(operasi_bilangan)       
          





