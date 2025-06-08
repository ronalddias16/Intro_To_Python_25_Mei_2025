import datetime

nama_pt = "PT.Pertamina"
alamat = "Jl. Kedoya 30 No 1, jAKARTA Timur"
waktu_dibuat = datetime.datetime.now()

#positional argumen
print("=======Posisional Argument=======")
print("\t\t\t{0}\nKepada,\nHRD Manager {1}\n{2}".format(nama_pt,alamat,waktu_dibuat))
print("=======Keyword Argument=======")
print("\t\t\t{0}\nKepada,\nHRD Manager {nama_pt}\n{alamat}".format(nama_pt=nama_pt,alamat=alamat,waktu=waktu_dibuat))
print("=======cara singkat=======")
print(f"\t\t\t{waktu_dibuat}\nKepada,\nHRD Manager {nama_pt}\n{alamat}")