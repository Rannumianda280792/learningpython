#operasi List

# index 0(-3)    1(-2)     2(-1)
data=["Rannu", "Shanum", "Saras"]

#mengambil data dari list ini
data_0= data[0]
print(f"data pertama (index-0)= {data_0}")

data_terakhir=data[-1]
print (f"data terakhir adalah= {data_terakhir}")

#mengambil info jumlah data dalam list
panjang_data= len(data)

print(f"panjang data dalam list adalah = {panjang_data} ")

#manipulasi atau merubah data di dalam list
print (f"data sebelum ditambah\n {data}")

data.insert(1,"Mianda")
print(f"data setelah ditambah \n {data} ")

#menambah data di akhir list
data.append("Oksiana")
print(f"data di ditambah lagi =\n {data}")

#menambah list dengan list
data_baru= ["Medina", "Aesha"]
data.extend(data_baru)
print (f"data Gabungan \n {data}")

# Merubah data
# merubah data pada index ke -3
data[3]="Saraswati"
print (f" Data Rubah \n {data}")

# Remove data
data.remove("Aesha") # remove data harus sesuai dengan di dalam list kalau tidak akan Error
print (f" Data Remove \n {data}")

#meremove data paling belakang
data_remove=data.pop()
print (f" Data yang di Remove paling belakang adalah {data_remove}")
print (f" Data Remove yang dibelakang \n {data}")

