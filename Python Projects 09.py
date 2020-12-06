#Python Project 09
buah = {'apel' : 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

def jumlaheBuah() :
    jumlah = int(input('Berapa Kg (dalam satuan KiloGram) : '))

    print ('======================')
    print ( 'Total Harga : ', buah.get(jenengBuah, 0)*jumlah)

print('Daftar Buah : ')
for a,b in buah.items() :
    print ('- ' ,a, ' : ' , b)

while True :
    jenengBuah = input('\nNama buah yang akan anda beli apa : ')

    if (jenengBuah not in buah.keys ()) :
        print ('Maaf buah yang anda masukkan tidak invalid dengan daftar buah yang ada ' )
        continue
    else :
        while True :
            try :
                jumlaheBuah()
                break
            except ValueError :
                continue
        break

