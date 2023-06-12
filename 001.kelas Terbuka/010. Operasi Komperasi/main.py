# Operasi Komparasi

#setiap Hasil dari komperasi adalah Boolean (true or False)

# <, >, <=, >=, ==, != , is, is not

a=4
b=7

# lebih Besar dari >
print("======lebih besar dari (>) =======")
hasil= a > 3
print(a,'>',3,'=', hasil) #true
hasil=b > 3
print(b,'>',3,'=', hasil) #false
hasil=b > 2
print(b,'>',2,'=', hasil) #false

# lebih kecil dari <
print("======lebih kecil dari (<) =======")
hasil= a < 3
print(a,'<',3,'=', hasil)
hasil=b < 3
print(b,'<',3,'=', hasil)
hasil=b < 2
print(b,'<',2,'=', hasil)

# lebih Besar sama dengan dari >=
print("======lebih besar sama dengan dari (>=) =======")
hasil= a >= 3
print(a,'>=',3,'=', hasil)
hasil=b >= 3
print(b,'>=',3,'=', hasil)
hasil=b >= 2
print(b,'>=',2,'=', hasil)

# lebih kecil sama dengan dari dari <=
print("======lebih kecil sama dengan dari (<=) =======")
hasil= a <= 3
print(a,'<=',3,'=', hasil)
hasil=b <= 3
print(b,'<=',3,'=', hasil)
hasil=b <= 2
print(b,'<=',2,'=', hasil)

#sama dengan == (pembadingan serupa)
print("======sama dengan dari (==) =======")
hasil= a == 4
print(a,'==',4,'=', hasil)
hasil= b == 4
print(b,'==',4,'=', hasil)

# tidak sama dengan != (pembadingan tidak serupa)
print("====== sama dengan dari (!=) =======")
hasil= a != 4
print(a,'==',4,'=', hasil)
hasil= b != 4
print(b,'==',4,'=', hasil)

# komparasi dengan is dan is not tidak dapat dilakukan dengan cara 
# membandingan dengan sintak Literal (tidak ada variabel, Objek atau tidak disimpan di memory)
#contoh nya : a is 4 ini adalah salah 
# a is b ini adalah benear
#komparasif ini akan banyak digunakan di Object Orientid Program (OOP)

# "is" sebagai komparasi object indentity 
print("====== object identity (is) =======")
x= 5
y= 5
print("nilai x = ", x,"type = ",type(x), "id = ", hex(id(x)) ) # nilai x  adalah object identity karena mempunyai address penyimpanan
print("nilai y = ", y,"type = ",type(y), "id = ", hex(id(y)) ) # nilai y  adalah object identity karena mempunyai address penyimpanan
hasil= x is y
print(x,'is',y,'=', hasil)

x= 5
y= 6
print("nilai x = ", x,"type = ",type(x), "id = ", hex(id(x)) ) # nilai x  adalah object identity karena mempunyai address penyimpanan
print("nilai y = ", y,"type = ",type(y), "id = ", hex(id(y)) ) # nilai y  adalah object identity karena mempunyai address penyimpanan
hasil= x is y
print(x,'is',y,'=', hasil)

print("====== object identity (is not) =======")
x= 5
y= 5
print("nilai x = ", x,"type = ",type(x), "id = ", hex(id(x)) ) # nilai x  adalah object identity karena mempunyai address penyimpanan
print("nilai y = ", y,"type = ",type(y), "id = ", hex(id(y)) ) # nilai y  adalah object identity karena mempunyai address penyimpanan
hasil= x is not y
print(x,'is not',y,'=', hasil)

x= 5
y= 6
print("nilai x = ", x,"type = ",type(x), "id = ", hex(id(x)) ) # nilai x  adalah object identity karena mempunyai address penyimpanan
print("nilai y = ", y,"type = ",type(y), "id = ", hex(id(y)) ) # nilai y  adalah object identity karena mempunyai address penyimpanan
hasil= x is not y
print(x,'is not',y,'=', hasil)
