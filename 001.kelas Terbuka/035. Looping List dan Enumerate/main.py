# loop list

kumpulan_angka=[3,7,4,5]

#for loop
print ("For Loop")
for angka in kumpulan_angka:
    print (f"list : {angka}")
    #list : 3
    #list : 7
    #list : 4
    #list : 5
    
peserta=["rannu","mianda","saras"]

for nama in peserta:
    print (f"nama : {nama}")
    #nama : rannu
    #nama : mianda
    #nama : saras

#for dan range
print ("\nFor Loop and Range")
kumpulan_angka=[8,4,2,6]

panjang=len(kumpulan_angka)
for i in range(panjang):
    print (f"Angka adalah {kumpulan_angka[i]}")
    #Angka adalah 8
    #Angka adalah 4
    #Angka adalah 2
    #Angka adalah 6
    
#while loop   
print ("\nwhile Loop")
kumpulan_angka=[8,4,2,6]

panjang=len(kumpulan_angka)
i=0
while i < panjang:
    print (f"Angka adalah {kumpulan_angka[i]}")
    i+=1
    
# for comprehension
print ("\nfor comprehension")
data_list= [1,35,"rannu","mianda"]
[print(f"data : {i}") for i in data_list]
#data : 1
#data : 35
#data : rannu
#data : mianda

angka=[8,4,2,6]
angka_kuadrat=[i**2 for i in angka]
print(angka_kuadrat) #[64, 16, 4, 36]

# for enumarate
# untuk mengambil index dan data list
for index, data in enumerate(data_list,1): 
    print(f"index ke- {index}, data: {data}")
    '''index ke- 0, data: 1
       index ke- 1, data: 35
       index ke- 2, data: rannu
       index ke- 3, data: mianda'''