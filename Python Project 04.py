#Python Project 04
sayur = ['bayam', 'kangkung', 'wortel', 'selada']


def tambahSayur() :
    sayurBaru = input("Masukkan nama sayur yang diinginkan : ")
    sayur.append(sayurBaru)
    return sayur

def hapusSayur() :
    sayurHapus = input("Masukkan nama sayur yang ingin dihapus : ")
    sayur.remove(sayurHapus)
    return sayur

def readSayur() :
    print(sayur)


print("Apa yang program bisa lakukan untukmu : ")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")
print("0. Keluar")

while True :
    print()
    opsi = input("Pilihan Anda : ")

    if(opsi=='A' or opsi=='a') :
        tambahSayur()
            
    elif(opsi=='B' or opsi=='b') :
        hapusSayur()

    elif(opsi=='C' or opsi=='c') :
        readSayur()

    elif(opsi=='0') :
        break
    
    else :
        print('Inputan Invalid')
        continue

