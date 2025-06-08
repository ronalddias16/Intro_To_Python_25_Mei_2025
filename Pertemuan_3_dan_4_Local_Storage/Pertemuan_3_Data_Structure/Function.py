employee =[
    {
        "nama":"Ronaldo",
        "pekerjaan":"Design Engineer",
        "gaji":"100000"
    },
    {   
        "nama":"Dias",
        "pekerjaan":"Design UI/UX",
    },
    {   
        "nama":"Endo",
        "pekerjaan":"Football Player",
    }
]

print("======Daftar Pekerja=======")
    #functional void
def detail_pekerja(nama, pekerjaan, gaji=None):
    print(f"Nama:{nama}")
    print(f"Pekerjaan:{pekerjaan}")
    print(f"Gaji:{gaji}")
    print(f"Pekerja yang rajin")
#cara panggil
detail_pekerja(employee[0]['nama'],employee[0]['pekerjaan'],employee[0]['gaji'])
detail_pekerja(employee[1]['nama'],employee[1]['pekerjaan'])
detail_pekerja(employee[2]['nama'],employee[2]['pekerjaan'])

def penjumlahan(a,b):
    return a+b
hasil_penjumlahan = penjumlahan(10,12)
print(f"hasil dari penjumlahan:{hasil_penjumlahan}")