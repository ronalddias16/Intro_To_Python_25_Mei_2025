x=3
y=3

#besar dari
hasil = (x>y)
print(f"Apakah nilai {x} besar dari {y} adalah {hasil}")
#besar dari sama dengan
hasil = (x>=y)
print(f"Apakah nilai {x} sama dengan dari {y} adalah {hasil}")

kondisi = True
hasil = kondisi != False # ! not ini adalah kondisi yang dibalikkan
print(f"Apa yang akan terjadi dari kondisi diatas:{hasil}")

x="1"
y=1
hasil = x == y
print(f"hasil dari {x} apakah sama dengan {y} adalah {hasil}")

print("=======if=======")
nilai_raport = 50
if nilai_raport <= 100:
    print("selamat kamu lulus")
print("program terus berlanjut")
nilai_raport = 50
if nilai_raport >= 100:
    print("selamat kamu lulus")
else:
    print("kamu tidak lulus")
      

