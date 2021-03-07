#71200553_STEFANUS EMMANUEL LEFRAND WUISANG

i = 0
while i == 0:
    print("Selamat Datang di Nike Department Store. Berikut list Sneaker tersedia semua warna.")
    print(" 1. Nike Air Jordan 1")
    print(" 2. Nike Air Jordan 4")
    print(" 3. Nike Air Jordan 5")
    print(" 4. Nike Air Uptempo")
    print(" 5. Nike Air Force 1")
    print(" 6. Nike Air Max 90")
    print(" 7. Exit")
    choice = int(input("Masukkan Nama Sneaker yang anda inginkan"))
    if choice == 1:
        colorway = str(input("Masukkan Colorway yang anda inginkan"))
        print(" Nike Air Jordan 1", colorway)
    elif choice == 2:
        colorway = str(input("Masukkan colorway yang anda inginkan"))
        print(" Nike Air Jordan 4", colorway)
    elif choice == 3:
        colorway = str(input(" Masukkan colorway yang anda inginkan"))
        print("Nike Air Jordan 5", colorway)
    elif choice == 4:
        colorway = str(input("Masukkan Colorway yang anda inginkan"))
        print("Nike Air Uptempo", colorway)
    elif choice == 5:
        colorway = str(input("Masukkan colorway yang anda inginkan"))
        print("Nike Air Force 1", colorway)
    elif choice == 6:
        colorway = str(input("Masukkan colorway yang anda inginkan"))
        print("Nike Air Max 90", colorway)
    elif choice == 7:
        i=1
    else:
        print("Sneaker yang anda cari tidak ada di List, Mohon diulang untuk pemesannya")
        
        
        

                 
