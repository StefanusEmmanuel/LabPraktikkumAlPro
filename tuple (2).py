def hitung_pengeluaran(x):
    total = 0
    for i in x:
        total+=(int(input('Masukkan pengeluaran anda pada bulan'+' '+i+': Rp.')))
        print('Total pengeluaran anda tahun ini adalah: Rp.', total)
bulan = ('Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember')
hitung_pengeluaran(bulan)
