#Python Project 08
buah = {'apel' : 5000,
           'jeruk' : 8500,
           'mangga' : 7800,
           'duku' : 6500}

def rerataHargaBuah(buah) :
    zigma = 0
    jumlah = 0
    
    for x,y in buah.items() :
        zigma += y
        jumlah += 1

    rerata = zigma / jumlah
    return rerata

def ratarataHargaBuah(buah) :
    harga = list(buah.values())
    rata = sum(harga) / len(harga)
    return rata

a = rerataHargaBuah(buah)
b = ratarataHargaBuah(buah)

print(a)
print(b)
