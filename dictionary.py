user = int(input("Jumlah pegawai:"))
nama = []
gaji = []
for i in range (user):
    user1 = str(input("Nama:"))
    nama.append(user1)
    user2 = int(input("gaji"))
    gaji.append(user2)

zipped = zip(nama,gaji)
result = dict(zipped)
x = sum(result.values())
rata=x/(len(result.values()))
print(rata)
for i in range(len(result.values())):
    if gaji[i] > rata:
        print(nama[i], gaji [i])
      
