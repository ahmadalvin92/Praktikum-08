#Python Project 05
def kuadrat(bil) :
    
    bilSquare = []
    
    for i in range(len(bil)) :
        
        a = bil[i] * bil[i]
        bilSquare.append(a)
        
    return bilSquare


dataBil = [2, 4, 5, 6]

hasil = kuadrat(dataBil)

print(hasil)

