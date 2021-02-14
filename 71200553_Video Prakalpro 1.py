#71200553_STEFANUS EMMANUEL
#SOAL : Hitung jumlah uang yang harus dibayarkan dari pinjaman $20.000 dengan tingkat bunga 5% pertahun untuk masa pinjaman 5 tahun 5 Tahun

#Input: Uang Pinjaman $20.000, Bunga 5% per Tahun, 5 Tahun masa pinjaman
#Proses: Mencarijumlah yang harus dibayarkan selama 5 tahun (Menggunakan rumus uangpinjaman*bunga/100)
#Output: Jumlah uang yang harus dibayarkan untuk masa pinjaman 5 tahun

A = int(input("Masukkan Jumlah uang pinjaman$"))
B = int(input("Masukkan tingkat bunga dalam %"))
C = int(input("Masukkan Masa Pinjaman (Dalam Tahun)"))

bunga = A*B/100
jumlah = bunga*C

print("Jumlah uang yang harus dibayarkan adalah $",jumlah)