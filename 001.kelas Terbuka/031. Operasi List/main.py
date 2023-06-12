#operasi

data_angka=[1,1,5,4,8,5,5,6,7,2,6,2,5,7,9,6,5,1,4,4]

print (f"data angka = \n{data_angka}")

#Count data
jumlah_angka_4=data_angka.count(4)
jumlah_angka_3=data_angka.count(3)
print (f"jumlah data angka 4 = {jumlah_angka_4}") #jumlah data angka 4 = 3
print (f"jumlah data angka 3 = {jumlah_angka_3}") #jumlah data angka 3 = 0

#ambil data posisi

data=['saras','rannu','shanum','mianda']

index_rannu=data.index('rannu')
index_saras=data.index('saras')
print (f"data = \n{data}") 
print (f"index_rannu = {index_rannu}") #index_rannu = 1
print (f"index_saras = {index_saras}")#index_saras = 0

#mengurutkan data list
print (f"data angka sebelum di sort = \n{data_angka}")
# [1, 1, 5, 4, 8, 5, 5, 6, 7, 2, 6, 2, 5, 7, 9, 6, 5, 1, 4, 4]

data_angka.sort() # angka terkecil sampai terbesar

print (f"data angka setelah di Sort = {data_angka}")
#[1, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9]

print (f"data =\n{data}")
#['saras', 'rannu', 'shanum', 'mianda']
data.sort()
print (f"data Sort = {data}")
#['mianda', 'rannu', 'saras', 'shanum']

#balik list nya (besar ke kecil) wajib di sort terlebih dulu
data_angka.reverse() 
data.reverse()
print (f"data angka di reverse =\n {data_angka}") 
#[9, 8, 7, 7, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 2, 2, 1, 1, 1]
print (f"data di reverse = \n {data}")
#['shanum', 'saras', 'rannu', 'mianda']
