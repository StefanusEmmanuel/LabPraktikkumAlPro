#71200553_STEFANUS EMMANUEL

#Berikut adalah beberapa istilah generasi berdasarkan tahun kelahirannya:

#1900-1943, 2016-2021 belum memiliki nama generasi
#1944-1964 adalah generasi baby boomer 
#kelahiran 1965-1979 adalah generasi x
#kelahiran 1980-1994 adalah generasi y(milennials)
#1995-2021 adalah Generasi Z
#Buat program dimana user diminta untuk menuliskan nama dan tahun kelahirannya, kemudian cetak nama dan generasinya seperti pada contoh output berikut.

#input : Nama, Tahun Kelahiran
#proses: Mencari nama generasi berdasarkan tahun kelahiran menggunakan if/else
#output: Nama generasi berdasarkan tahun kelahiran

nama = input("Nama anda adalah")
tahun = int(input("Masukkan Tahun kelahiran anda!"))

if tahun >=1944 and tahun <= 1964:
    print("Anda", nama, "masuk dalam generasi baby boomer")

elif tahun >= 1965 and tahun<= 1979:
    print("Anda", nama, "masuk dalam generasi x")
elif  tahun >= 1980 and tahun <= 1994:
    print("Anda",nama,"masuk dalam generasi y (milennials)")

elif tahun >= 1995 and tahun<= 2015:
    print("Anda", nama,"masuk dalam generasi z")

else:
    print("Nama generasi anda belum memiliki nama generasi/diluar range yang tersedia")
 