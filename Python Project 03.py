#Python Project 03
dataNama = []
i = True

while(i == True) :
    nama = input("Masukkan nama : ")
    dataNama.append(nama)

    lanjut = input("Input Nama Lagi ? (y/n) ")

    if(lanjut=='y') :
            i = True
            
    elif(lanjut=='n') :
            i = False

    else :
            print('Input Salah')
            break

print()
dataNama.sort()

for x in range(len(dataNama)) :
    print(dataNama[x], '(', len(dataNama[x]), 'karakter )')





    
