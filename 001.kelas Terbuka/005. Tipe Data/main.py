# tipe data : angka tanpa koma (integer)
data_integer=10
print("data : ", data_integer)
print("type : ", type(data_integer) )

# tipe data : angka berkoma (Float)
data_float=1.5
print("data : ", data_float)
print("type : ", type(data_float) )

# tipe data : kumpulan karakter (String)
data_string="Shanum"
print("data : ", data_string)
print("type : ", type(data_string) )

# tipe data : biner true or false (boolean)
data_bool=False
print("data : ", data_bool)
print("type : ", type(data_bool) )

#data kompleks
data_komplex=complex(4,3)
print("data : ", data_komplex)
print("type : ", type(data_komplex) )

#tipe data dari bahasa C

from ctypes import c_double
data_c_double= c_double (10.5)
print("data : ", data_c_double)
print("type : ", type(data_c_double) )