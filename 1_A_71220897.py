a = input('Masukan nama mahasiswa : ')
b = str(input('Masukan NIM-nya : '))

tahun = int(b[2:4])
akt = int(b[0:2])

if tahun >= 20 and tahun <=22 and akt == 71 :
    print(f'{a} merupakan mahasiswa informatika angkatan 20 hingga 22')
else :
    print(f'{a} bukan mahasiswa informatika angkatan 20 hingga 22')