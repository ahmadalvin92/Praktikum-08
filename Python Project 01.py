#Python Project 01
while True :
    try :
        n = int(input("Berapa banyak data yang anda inginkan? (ketikan dalam angka) : "))
        break
    except ValueError :
        print("Input Salah")
        continue

data = []

i = 0

while (i < n) :
    try :
        bil = int(input("Masukkan bilangan bulat yang anda inginkan : "))
        data.append(bil)
        i+= 1

    except ValueError :
        print("Input salah")
        
data.sort(reverse = True)
print(data)
