#Pyhton Project 10
buah = {'apel' : 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

def jumlaheBuah() :
    jumlah = int(input('Berapa Kg (dalam satuan KiloGram) : '))
    hargane = buah.get(jenengBuah, 0)*jumlah
    return hargane

print('Daftar Buah : ')
for a,b in buah.items() :
    print ('- ' ,a, ' : ' , b)

totale =[]
lanjutTidak = True

while (lanjutTidak == True) :
    jenengBuah = input('\nNama buah yang akan anda beli apa : ').lower()

    if (jenengBuah not in buah.keys ()) :
        print ('Maaf buah yang anda masukkan tidak invalid dengan daftar buah yang ada ' )
        continue
    else :
        try :
            hargane = jumlaheBuah ()
            totale.append(hargane)

            pilihan = input('Mau beli buah yang lain atau tidak mumpung ada promo (y/n) ? ').lower()
            if (pilihan == 'y') :
                lanjutTidak = True
            elif (pilihan == 'n'):
                lanjutTidak = False

            else :
                print ('Inputan Tidak Valid')
                break
        except TypeError :
            print ('input error, hanya tersedia input (y/n), silahkan masukan y atau n')
            continue
        except ValueError :
            print ('\nInputan Invalid Coba Lagi di Ulangi Siapa tau bisa ^_^')
            continue
print ('=================================')
print ('Total Harga Buah yang di beli : ' , sum(totale))
                
            
                
