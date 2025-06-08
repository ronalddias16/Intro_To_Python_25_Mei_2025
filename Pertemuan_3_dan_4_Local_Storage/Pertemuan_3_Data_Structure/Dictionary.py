profile={
    "nama":"Ronaldo",
    "kelas":12,
    "jurusan":["IPA","IPS"] #array 2D
}
print(f"Dictionary Data: {profile}")
print(f"Nama: {profile['nama']}")
print(f"Cara mengambil jurusan IPS: {profile['jurusan'][1]}")

profile['kelas']=10
print(f"Dictionary Data: {profile}")
profile['ketua_kelas']= "Budi"
print(f"Dictionary Data: {profile}")

del profile["ketua_kelas"]
print(f"Dictionary Data: {profile}")