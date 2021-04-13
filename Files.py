
print('SELAMAT DATANG DI SMA BELAJAR GIAT!'.center(70,'='))

chc = 0
while(chc!=3):
    print('1. Tambah data')
    print('2. Lihat Data Mahasiswa')
    print('3. Exit')
    try:
        chc = int(input('Masukan nomor yang diinginkan : '))
        assert 0 < chc < 4
    except AssertionError:
        print('Invalid Input')

    if chc == 1:
        print('MENU TAMBAH DATA'.center(25,'='))
        kelas = input('Masukan kelas : ')
        try:
            n = int(input('Masukan jumlah Mahasiswa : '))
        except ValueError:
            print('Invalid Input')
        s = ''
        for i in range(n):
            nama = input('Masukan Nama Mahasiswa : ')
            try: 
                nilai = int(input('Masukan Nilai Mahasiswa : '))
            except ValueError:
                print('Invalid Input')
            s = s + str(kelas) + '\t' + str(nama) + "\t" + str(nilai) + '\n'
        f = open("db.txt", "w")
        f.write(s)
        f.close()
    elif chc == 2:
        print('LIHAT DATA MAHASISWA'.center(25,'='))
        f = open("db.txt", "r")
        for i in f.readlines():
            print('Kelas\tNama\tNilai')
            print(i)
        f.close()
    elif chc == 3:
        print('Berhasil Logout')
        break
