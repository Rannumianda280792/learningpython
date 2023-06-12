# list


#kumpulan data number
data_angka=[1,2,3]
print (f"{data_angka}")

#kumpulan data string
data_string=["rannu","saras","shanum"]
print (f"{data_string}")

#kumpulan data boolean
data_boolean=[True,False,True]
print (f"{data_boolean}")

#kumpulan data campuran
data_campuran=[1, "rannu",True]
print (f"{data_campuran}")

## alternative membuat data list
data_range=range(0,10,2) # range (start, Stop, Step) cetak dari 0 sampai sebelum 10 angka genap
print (f"{data_range}")#tidak bisa langsung di print jika ingin dibentuk dengan list
data_list=list(data_range) #pakai fungsi list
print (f"{data_list}")

#membuat list dalam bentuk for loop, list compartion
list_pake_for=[i**2 for i in range(0,10)] # <variable-target> = [<kembalian> for <item> in <iterable>] 
"""variable-target: variable untuk menampung list yang telah dibuat
kembalian: nilai yang akan dikembalikan sebagai elemen list. Dapat berupa nilai tetap, variable, maupun ekspresi untuk memproses nilai item
item: penampung nilai dari iterable pada tiap iterasi, nilai ini dapat digunakan sebagai ekspresi dalam kembalian
iterable: variable yang berisi kumpulan nilai (list, string, tuple, dll)"""
print (f"{list_pake_for}")

#membuat list pake for pake if
list_pake_for_if = [x for x in range(1,10) if x not in list_pake_for] #filter yang tidak ada di list_pake_for
print (f"{list_pake_for_if}")

list_pake_for_if = [x for x in range(1,10) if x %2 ==0 ]# list genap
print (f"{list_pake_for_if}")

list_pake_for_if = [x for x in range(1,10) if x %2 !=0 ] #list ganjil
print (f"{list_pake_for_if}")

list_pake_for_if = [x for x in range(1,10) if x !=2 and x !=4 ] #list yang tidak di cetak angka 2 dan 4
print (f"{list_pake_for_if}")
