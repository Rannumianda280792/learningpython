#Deep Copy

data_0=[1,4]
data_1=[2,9]

data_2D=[data_0,data_1]

#mengambil data nested list
data= data_2D[0]
print(f"data = {data}") #data = [1, 4]
data= data_2D[0][1]
print(f"data = {data}") #data = 4
data= data_2D[1][1]
print(f"data = {data}") #data = 9

data_2D_copy = data_2D.copy() #ini hanya berbeda pada address list nya saja namun item/member nya address tetap sama 
print (f"data_asli = {data_2D}") #data_2D = [[1, 4], [2, 9]]
print (f"data_Copy = {data_2D_copy}") #data_2D_copy = [[1, 4], [2, 9]]

data_2D_copy[0][1]=5 #akan merubah ke-2 nya list copy dan asli 

print (f"data_asli = {data_2D}") #data_asli = [[1, 5], [2, 9]]
print (f"data_Copy = {data_2D_copy}") #data_Copy = [[1, 5], [2, 9]]
print (f"data_asli  Addressing = {hex(id(data_2D))}") #Cetak address 0x1ac1aeadec0
print (f"data_copy  Addressing = {hex(id(data_2D_copy))}") #cetak address 0x1ac1aeadec0

#hanya list nya saja berbeda namun member /item list tetap memakai address yang sama

print (f"data_member_asli  Addressing = {hex(id(data_2D[0][1]))}") #Cetak address 0x7ffb0dd4d3a8
print (f"data_member_copy  Addressing = {hex(id(data_2D_copy[0][1]))}") #cetak address 0x7ffb0dd4d3a8

#maka alternative yang harus di pakai untuk mengcopy list adalah dengan cara metode "deepcopy"
from copy import deepcopy

data_2D=[data_0,data_1]
data_2D_deepcopy= deepcopy(data_2D)

#data address list dan item akan berbeda kedua-dua nya

print (f"data_asli  Addressing = {hex(id(data_2D))}") #Cetak address 0x1ceea526f00
print (f"data_deepcopy  Addressing = {hex(id(data_2D_deepcopy))}") #cetak address 0x1ceea4fdec0
print (f"data_member_asli  Addressing        \t= {hex(id(data_2D[1][1]))}") #Cetak address 0x7ffb0dd4d3a8
print (f"data_member_deepcopy  Addressing \t= {hex(id(data_2D_deepcopy[1][1]))}") #cetak address 0x7ffb0dd4d3a8

data_2D[0][0]=32 #akan merubah isi list data_2D dan data_2D_copy namun tidak merubah Deepcopy
data_2D_deepcopy[0][1]=10 #tidak akan merubah isi list data_2D dan data_2D_copy namun merubah Deepcopy

print (f"data_asli = {data_2D}") #data_asli = [[32, 5], [2, 9]]
print (f"data_Copy = {data_2D_copy}") #data_copy = [[32, 5], [2, 9]]]
print (f"data_deepcopy= {data_2D_deepcopy}") #data_deepcopy= [[1, 10], [2, 9]] 