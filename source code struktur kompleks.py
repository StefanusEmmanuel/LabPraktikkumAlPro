#Buatlah Program untuk menampilkan deret seperti dibawah diinputkan secara dinamis

#05 06 07 08
#09 10 11 12
#13 14 15 16
#17 18 19 20

#input = user memasukkan tinggi dan lebar
#proses =  membuat program seperti deret seperti contoh output
#output =  deret tertampil



x=int(input('Tinggi: '))
y=int(input('Lebar: '))
a=1
b=0
d=2
c=1
f=1
for x in range(1,x+1):
    if x % 2 !=0:
        for i in range(a,(y*c)+1):
            if i >=10:
                print(i,end='')
            if i <10:
                print('0{}'.format(i),end='')
        a=(y*d)+1
        c+=2
        print()
    if x % 2 == 0:
        b+=2
        e=(y*f)+1
        for i in range(e,(y*b)+1):
            if i >=10:
                print(i,end='')
            if i <10:
                print('0{}'.format(i),end='')
        f+=2
        d+=2
        print()