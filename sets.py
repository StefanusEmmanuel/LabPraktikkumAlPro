a = int(input("Masukkan jumlah kulikuler yang diikuti anak pertama"))
b = int(input("Masukkan jumlah kulikuler yang diikuti anak kedua"))

bocah = []
bocahh = []
print("Masukkan ekstrakulikuler anak pertama")
for i in range(a):
    eks1 = str(input())
    bocah.append(eks1)
print("Masukkan ekstrakulikuler anak kedua")
for j in range(b):
    eks2 = str(input())
    bocahh.append(eks2)

bocah = set(bocah)
bocahh = set(bocahh)
hasil = bocah.symmetric_difference(bocahh)
print(hasil)
