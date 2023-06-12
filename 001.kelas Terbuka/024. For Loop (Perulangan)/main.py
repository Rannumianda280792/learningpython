#looping (perulangan)


#looping dalam bentuk list
angka_list=[2,4,6,7,9] 

print (f"jumlah angka pada list adalah {angka_list}\n")
for i in angka_list: #untuk i dalam angkalist arti nya di dalam seuruh list di tampilkan sesaui jumlah seluruh list
    print (f"list ke- {angka_list.index( i )} = {i}")

print ("akhir program ke-1")
print (20*"=")
#ini di dalam range 

angka_range_1= range(5)

print (f"jumlah angka pada  {angka_range_1}\n")
for i in angka_range_1 :
    print (f"i sekarang -> {i}")#akan menampilkan range dimulai dari  0 s/d 4 (0,1,2,3,4)
    
print ("akhir program ke-2")
print (20*"=")

#range dapat diatur dengan kemauan sendiri
angka_range_2= range(1,6)

print (f"jumlah angka pada {angka_range_2}\n")
for x in angka_range_2 :
    print (f"x sekarang -> {x}")#akan menampilkan range dimulai dari  1 s/d 5 (1,2,3,4,5)
    
print ("akhir program ke-3")
print (20*"=")

#looping dalam bentung string
data_str="saya bisa" 

for huruf in data_str :
    print (f"index ke- {data_str.index(huruf)} huruf = {huruf}")
print ("akhir program ke-4")
print (20*"=")
