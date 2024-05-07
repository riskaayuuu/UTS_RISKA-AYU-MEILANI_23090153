tahun = int(input('Masukkan Tahun:'))
if (tahun % 400 == 0) :
    print('Tahun',tahun, 'merupakan TAHUN KABISAT')
elif (tahun%4 == 0) and (tahun%100 ):
    print('Tahun',tahun, 'termasuk TAHUN KABISAT')    
else:
    print('Tahun',tahun, 'BUKAN TAHUN KABISAT')     
