#inisialisasi
#teknik program menyediakan memori yang akan dipakai
makanan = ["nasi","sayur","ayam"]

#Read (R)
print(f"List Makanan:{makanan}")

#Read Spesifik
print(f"index of 1:{makanan[1]}")
print(f"index of -1:{makanan[-1]}")

#update (U)
makanan[1] = "daging"
print(f"List makanan setelah diupdate:{makanan}")

#tambah data append (a)
makanan.append("sayur")
print(f"List makanan setelah diupdate:{makanan}")

makanan.remove("nasi")
print(f"List makanan setelah diupdate:{makanan}")

buah = ["semangka","Melon","nanas"]
makanan+=buah
print(f"List makanan setelah di add list:{makanan}")