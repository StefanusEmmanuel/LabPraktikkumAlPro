#Buatlah Program yang mengubah huruf vokal dalam kalimat (a,i,u,e,o) menjadi e
#contohnya: nama saya stefanus - neme seye stefenes
#input: User akan memasukkan kalimat yang ingin diubah
#proses: Mengubah semua huruf vokal menjadi e
#output: Kalimat yang huruf vokalnya sudah diubah

a = str(input("Masukkan kalimat yang ingin diubah:"))
if a == "a" or "i" or "u" or "e" or "o":
    b = a.replace ("a", "e")
    c = b.replace ("i", "e")
    d = c.replace ("u", "e")
    e = d.replace ("o", "e")

print(e)





    
        
