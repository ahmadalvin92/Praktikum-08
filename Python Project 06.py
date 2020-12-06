#Project Project 06
def sortStringByChar(data) :
    
    data.sort(reverse=True)
    return data


data = ['apel', 'rambutan', 'jeruk']
dataSorted = sortStringByChar(data)

print("Data baru : ", dataSorted)


