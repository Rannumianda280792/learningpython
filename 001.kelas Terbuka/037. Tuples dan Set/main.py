#tupels dan set

data_list=[32,5,3,2] #contoh data list

print (f"data_list = {data_list}")#data_list = [32, 5, 3, 2]


data_list[1]=4
data_list.remove(32) #remove
data_list.append(32) #tambah di belankang
data_list.sort()
print (f"data_list = {data_list}") #[2, 3, 4, 32]

#data Tuples tidak dapat di modifikasi dan manipulasi, berguna untuk data yang bersifat konstants
data_tuples=(3,2,42,2)
#data_tuples[1]=4
#data_tuples.remove(3)
#data_tuples.sort()
print (f"data_tuples = {data_tuples}") #data_tuples = (3, 2, 42, 2) hanya bisa menampilkan data saja

data_set={2,5,4,66} # sebuah himpunan yang tidak memiliki index
# print(data_set[1]) #akan Error set tidak mengenal index ,TypeError: 'set' object is not subscriptable
#data_set[1]=1 tidak bisa mengubah item di dalam data set
data_set.remove(2)
data_set.add(10) #append tidak berfungsi pada data set/himpunan
data_set.update({8,7}) #Tidak bisa menerima nilai duplikat
print (f"data_set = {data_set}") #{66, 4, 5, 7, 8, 10}