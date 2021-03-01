# STEFANUS EMMANUEL
# 71200553
# GruP A
# Universitas Kristen Duta Wacana

# Modular Programing (fungsi)

"""
Seorang streamer youtube bingung menghitung gaji bulanan dia dan bonus yang 
dia dapat. gaji dia adalah jumlah jam yg dia dapat perbulan di kali 14 dollar,
dan bonus dia 1 star = 0,02 dollar. hitunglah gaji bulanan dia dan star bonus 
dia kemudian jumlah kan. program ini di gunakan untuk streamer youtube saja 
dengan password youtube_gaming.
input : jumlah jam perbulan (whr) , jumlah star/bonus
proses : gaji = jam*(14*14000)
            bonus = (star*0.02)*14000
output : Gaji yang di dapat adalah Rp ......
            Bonus yang di dapat adalah Rp .....
            Jumlah total dari Gaji dan Bonus adalah Rp.....
"""

def gaji(jam):
    total_1 = jam*(14*14000)
    return total_1

def bonus(star):
    total_2 = (star*0.02)*14000
    return total_2

a =  str("youtube_gaming")
passw = input("Masukkan password anda : ")
if passw == a:
    jam = int(input("Masukkan jumlah jam perbulan(whr): "))
    print(f"gaji yang di dapat adalah RP {gaji(jam)}")
    star = int(input("Masukkan jumlah star/bonus anda : "))
    print(f"Bonus yang didapat adalah Rp {bonus(star)}")
    jumlah_total = gaji(jam) + bonus(star)
    print(f"Jumlah total dari gaji dan bonus adalah Rp {jumlah_total}")

else : 
    print("Password yang anda masukkan kurang tepat!")