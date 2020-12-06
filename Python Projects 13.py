#Python Project 13
nilaiMahasiswa = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80 },
                  {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90 },
                  {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50 },
                  {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30 },
                  {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40 }]
def nilaiAkhirTinggi(nilaiList) :
    mid = []
    uas = []
    nilaiAkhir = []
    tertinggi = {}

    for i in nilaiList :
        k = (i['mid'] + (2 * i['uas'])) / 3
        nilaiAkhir.append(k)

    tertinggi = nilaiAkhir.index(max(nilaiAkhir))

    data = {'nim' : nilaiList[tertinggi] ['nim'],
              'nama' : nilaiList[tertinggi] ['nama']}
    return data

a = nilaiAkhirTinggi(nilaiMahasiswa)
print ('Mahasiswa dengan mendapatkan nilai tertinggi yaitu : ', a['nama'], 'dengan Nim', a['nim'])
