#71200553_STEFANUS EMMANUEL

nama = ['Ajeng','Stef','Alvani','Julio']
nis = ['0001','0002','0003','0004']
umur = [18,19,19,20]
nama2 = ['Gaia','Kaia','Freya','Widya']
nis2 = ['25100','25101','25102','25103']
umur2 = [14,15,15,16]

def pemetaanList (nama, nis, umur):
    print("======Daftar Siswa======")
    for i in range (0,4):
        print('Nama:', nama[i],'|','NIS:', nis[i],'|', 'Umur:', umur[i])

pemetaanList(nama, nis, umur)
pemetaanList(nama2, nis2, umur2)
