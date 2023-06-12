#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assigment

a=5 # adalah assigment
print ("nilai a adalah", a)
a += 1 #ini arti nya a= a+1
print ("nilai a+=1, nilai a menjadi ", a )
a -= 2 #ini arti nya a= a-2
print ("nilai a-=2, nilai a menjadi ", a )
a *= 5 #ini arti nya a= a*2
print ("nilai a*=5, nilai a menjadi ", a )
a /= 2 #ini arti nya a= a/2
print ("nilai a/=2, nilai a menjadi ", a )

# modulus dan floor devition
b=10
print ("\nnilai b adalah", b)
b %=3 # ini arti nya  b= b % 3 
print ("nilai b%=3, nilai b menjadi ", b )
b=10
print ("nilai b adalah", b)
b //= 3 #ini arti nya b= b // 3 operator left devision (pebulatan ke bawah) 
print ("nilai b//=3, nilai b menjadi ", b )

#operasi pangkat
a=5
a **= 3 # ini arti nya  a= a ** 3   
print ("nilai a**=3, nilai a menjadi ", a )

#operasi Bitwaise
# OR
c=False
print ("nilai c adalah", c)
c|=True # ini arti nya c= false or true
print ("nilai c|=true, nilai c menjadi ", c )
c=False
print ("nilai c adalah", c)
c&=False # ini arti nya c= false or false 
print ("nilai c|=false, nilai c menjadi ", c )
# And
c=False
print ("nilai c adalah", c)
c&=True # ini arti nya c= false or true
print ("nilai c&=true, nilai c menjadi ", c )
c=True 
print ("nilai c adalah", c)
c&= True # ini arti nya c= false or false 
print ("nilai c&=true, nilai c menjadi ", c )

# XOR
c=True
print ("nilai c adalah", c)
c^=True 
print ("nilai c^=true, nilai c menjadi ", c )
c=False  
print ("nilai c adalah", c)
c^= True 
print ("nilai c^=true, nilai c menjadi ", c )

#geser geser
d=0b0100
print ("\nnilai d = ", format (d,'04b'))
d >>= 2
print ("nilai d>>=2 , nilai d menjadi ", format(d,'04b') )
d <<= 2
print ("nilai d<<=2 , nilai d menjadi ", format(d,'04b') )