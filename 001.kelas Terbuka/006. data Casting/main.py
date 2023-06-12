#bleajar casting
#merubah satu tipe ke tipe lainnya (convert)
#tipe Data: int,float, str, boolean

print("======Integer======")
data_integer=0
print("data : ", data_integer,"type : ", type(data_integer) )
data_float=float(data_integer)
data_string= str(data_integer)
data_boolean= bool(data_integer) # akan false jika int=0
print("data : ", data_float,"type : ", type(data_float) )
print("data : ", data_string,"type : ", type(data_string) )
print("data : ", data_boolean,"type : ", type(data_boolean) )

print("======float======")
data_float=4.6
print("data : ", data_float,"type : ", type(data_float) )
data_integer=int(data_float)
data_string= str(data_float) #akan membulatkan ke Bawah
data_boolean= bool(data_float) # akan false jika float=0
print("data : ", data_integer,"type : ", type(data_integer) )
print("data : ", data_string,"type : ", type(data_string) )
print("data : ", data_boolean,"type : ", type(data_boolean) )


print("======Boolean======")
data_boolean=True
print("data : ", data_boolean,"type : ", type(data_boolean) )
data_integer=int(data_boolean)
data_string= str(data_boolean)
data_float= float(data_boolean) 
print("data : ", data_integer,"type : ", type(data_integer) )
print("data : ", data_string,"type : ", type(data_string) )
print("data : ", data_float,"type : ", type(data_float) )

print("======String======")
data_string=""
print("data : ", data_string,"type : ", type(data_string) )
#data_integer=int(data_string) #string harus angka
data_boolean= bool(data_string) # akan false jika string kosong
#data_float= float(data_string) #string harus angka
print("data : ", data_integer,"type : ", type(data_integer) )
print("data : ", data_boolean,"type : ", type(data_boolean) )
print("data : ", data_float,"type : ", type(data_float) )