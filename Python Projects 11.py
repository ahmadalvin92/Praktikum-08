#Pyhton Project 11
buah = {'apel' : 5000,
        'jeruk' : 8500,
        'mangga' : 7800,
        'duku' : 6500}

def jumlaheBuah(jenengBuah) :
    jumlah = int(input('Berapa Kg (dalam satuan KiloGram) : '))
    hargane = buah.get(jenengBuah, 0)*jumlah
    return hargane

def tukuBuah(buahDict) :
    print('Daftar Buah : ')

    for a,b in buah.items() :
        print ('- ' ,a, ' : ' , b)

    totale =[]
    lanjutTidak = True

    while (lanjutTidak == True) :
        jenengBuah = input('\nNama buah yang akan anda beli apa : ').lower()

        if (jenengBuah not in buahDict.keys ()) :
            print ('Maaf buah yang anda masukkan tidak invalid dengan daftar buah yang ada ' )
            continue
        else :
            try :
                hargane = jumlaheBuah (jenengBuah)
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
                print ('Tuhkan salah input an nya, kan cuman ada (y/n), jangan yang lain')
                continue
            except ValueError :
                print ('\nInputan Invalid Coba Lagi di Ulangi Siapa tau bisa ^_^')
                continue
    print ('=================================')
    print ('Total Harga Buah yang di beli : ' , sum(totale))

def nambahBuah(buahDict) :
    jenengBuahBaru = input('Masukkan nama buah : ').lower()

    while True :
        try :
            if(jenengBuahBaru in buahDict.keys() ):
                print (' Buah ', jenengBuahBaru, 'buah sudah di dalam data. Sekarang masukkan harga buah berapa ? ')
                hargaBuahBaru = int(input('\nMasukkan harga buah dalam bentuk satuan angka : '))

                dictBuahBaru = {namaBuahBaru : hargaBuahBaru}
                buahDict.update(dictBuahBaru)

                print('Data Buah : ')

                for a,b in buah.items() :
                      print ('- ' ,a, '(harga  : ' , b, ')')
            else :
                hargaBuahBaru = int(input('\nMasukkan Harga dalam bantuk satuan angka : '))
                buah[jenengBuahBaru] = hargaBuahBaru

                print('Data Buah : ')
                
                for a,b in buah.items() :
                      print ('- ' ,a, '(harga  : ' , b, ')')
            break
        except ValueError :
            print ('\nInputan Invalid Coba Lagi di Ulangi Siapa tau bisa ^_^')
            continue
print ('Daftar menu : ')
print('a. Tambah data buah')
print('b. Beli buah')
print('97. Keluar')

while True :
    pilihanDaftarMenu = input('\nPilihan Menu : ').lower()

    if(pilihanDaftarMenu == 'a') :
        nambahBuah(buah)
    elif(pilihanDaftarMenu == 'b') :
        tukuBuah(buah)
    elif(pilihanDaftarMenu == '97') :
        break
    else :
        print('Tuhkan ada yang salah input an, coba lagi deh, SEMANGATTTT')
        continue

                


                
                
            
                
