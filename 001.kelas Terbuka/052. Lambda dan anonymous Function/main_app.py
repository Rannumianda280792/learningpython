# lambda Function
# kegunaan nya untuk membuat sebuah fungsi menjadi lebih simple dan ringkas
# harus mempunyai nilai paramaeter dan Return
# output = lambda argument/input/parameter : experesion/nilai Return
# dapat mengunakan lebih dari 1 parameter ( lambda angka,pow: angka**pow)
# penggunaan lambda di saran  hanya untuk sebuah fungsi yang ringkas 

# fungsi biasa
def f_kuadrat (angka,pangkat):
    return angka**pangkat

print( f"hasil fungsi pangkat biasa adalah : {f_kuadrat(3,2)} ") #hasil fungsi pangkat biasa adalah : 9 

# fungsi lambda
# format lambda -> output = lambda argument/input/parameter : experesion/nilai Return
kuadrat= lambda angka:angka**2 
#kaudrat as output ,
#lambda as function,
#angka as input/argument/parameter, 
#angka**2 as experssion atau nilai return
print( f"hasil fungsi kuadrat lambda adalah : {kuadrat(3)} ") #hasil fungsi kuadrat lambda adalah : 9 

pangkat = lambda num,pow : num**pow # dapat mengunakan lebih dari 1 parameter
print( f"hasil fungsi pangkat lambda adalah : {pangkat(3,2)} ") #hasil fungsi pangkat lambda adalah : 9 

# terihat jelas kegunaan dari lambda di dalam sort dan filter

# sorting untuk list biasa
data_list=['otong','dudung','ucup']
data_list.sort()
print(f"data sorted list : {data_list}") #data sorted list : ['dudung', 'otong', 'ucup']

#apabila sorting berdasarkan jumlah panjang nama
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama) # fungsi sort sebenar nya ada paramater kategori dalam sorting yaitu key 
print(f"data sorted list by panjang : {data_list}") #data sorted list by panjang : ['ucup', 'otong', 'dudung']
# agak sedikit panjang pemanggilan fungsi nya maka alternatif baik pakai lambda

#sorting pakai lambda berdasarkan panjang nama
data_list=['otong','dudung','ucup']
data_list.sort (key=lambda nama:len (nama))
print(f"data sorted list by Lambda panjang : {data_list}")

#filter
data_angka=[1,2,3,4,5,6,7,8,9,10]

def kurang_dari(angka):
    return angka<5
#filter(function, iterable)
data_angka_baru= list(filter(kurang_dari,data_angka))
data_angka_baru= list(filter(lambda x:x<5,data_angka))
print(data_angka_baru)

#bilangan Genap
data_genap= list(filter(lambda x:x%2==0,data_angka))
print(data_genap)

#bilangan Ganjil 
data_ganjil= list(filter(lambda x:x%2!=0,data_angka))
print(data_ganjil)

#bilangan 3
data_3= list(filter(lambda x:x%3==0,data_angka))
print(data_3)

data_input=lambda x,w:x+w
print(data_input('rannu',' mianda'))

a = (lambda x: x*2) 
print(a(5)) #ini di akan di kirim ke nilai X lambda
# bisa seperti ini
a = (lambda x: x*2) (5) #nilai 5 adalah sebagai parameters x yang di dikrim ke lambda
print(a) 

#anonymous function
#lambda termasuk kedalam anonymous function karena tidak memiliki nama
# salah satu motede teknik currying

def pangkat(angka,n):
    hasil=angka**n
    return hasil
data_hasil=pangkat(5,2)
print(f'fungsi biasa: {data_hasil}')

#penggunaan currying:
# 1.fungsi yang telah dibuat tidak bersifat fix 
# 2. fungsinya dapat di sign kedalam variabel

def pangkat(n):
    return lambda angka:angka**n #lambda adalah termasuk fungsi anonymous karena tidak memiliki nama

pangkat2=pangkat(2) #ini yang dinamakan fungsi currying yang bisa di simpan dalam variabel
print(f'pangkat 2 : {pangkat2(5)}') #25 dan dapat digunakan fungsi pangkat2 kembali dengan parameter
print(f'pangkat 4**2 : {pangkat2(4)}') #16 

pangkat3=pangkat(3)(9) #bisa di proses seperti ini langsung
print(pangkat3) #729