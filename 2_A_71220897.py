print('===== Selamat datang di Toko Andi Tersenyum, selamat belanaja =====')
a = int(input('Total belanja :RP.'))

b1 = int(a*2/100)
b2 = int(a*5/100)
b3 = int(a*10/100)

if a >= 100000 and a <= 500000 :
    print('Biaya yang harus dibayar setelah diskon adalah:', a-b1)
elif a >= 500000 and a <= 1000000:
    print('Biaya yang harus dibayar setelah diskon adalah:', a-b2)
elif a >= 1000000 :
    print('Biaya yang harus dibayar setelah diskon adalah:', a-b3)
else :
    print('Tidak ada diskon! Maka yang Anda Bayarkan adalah: Rp.', a)