#integer (int)
#ini bilangan.bulat
#contoh0123
x=32767#limit dari integer karakter
print("Ini Contoh Tipe Data Integer:{0}".format(x))
#float (bilangan desimal)
y=3.14
print("Ini Contoh Tipe Data Integer:{0}".format(y))
#kompleks 
z=2+3j
print("Ini Contoh Tipe Data Integer:{0}".format(z))
#tipe data sequence
a=[1,2,3] #list sifat tipe datanya value ya sebisa mungkin tipe dsatanya sama
print("Ini Contoh Tipe Data Integer:{0}".format(a))
b=[4,5,6] # truplet sifat datanya tidak bisa diganti
print("Ini Contoh Tipe Data Integer:{0}".format(b))
c=range (0,5)
print("Ini Contoh Tipe Data Integer:{0}".format(c))
nama = "Ronaldo Adam N"
print("Ini Contoh Tipe Data Integer:{0}".format(nama))
karakter = 'A'
print("Ini Contoh Tipe Data Karakter:{0}".format(karakter))
#set
f={1,2,3}
print("Ini Contoh Tipe Data frozenset:{0}".format(f))


#Tipe data kondisi
#boolean (bool)
#isinya hanya dua True (1) atau False(0)
kondisi_badan= True


#tipe data binary
i=0b1000001
#desimal = int(i)
#print("conversi binary to desimal:{0}".format(desimal))
#char = chr(desimal)
#print("conversi binary to char:{0}".format(char))
print("singkat binary to char:{0}".format(chr(int(i))))
j = bytearray(a)
print("isi binary dalam array variabel a:{0}".format(j))
z = memoryview (j)
print("lokasi view dalam memory (Ram):{0}".format(z))