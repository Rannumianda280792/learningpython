#operasi logika Boolean

# not, or, and, xor

print("=====not=====") # not kebalikan nilai yang telah di tetapkan
a=True
c= not a
print('nilai a = ', a)
print('-----not')
print('nilai c = ', c)

print("=====OR=====") # jika salah satu nilai true maka akan menghasilkan true
a=False
b=False
c= a or b 
print(a,'OR',b, '= ',c)

a=True
b=False
c= a or b
print(a,'OR',b, ' = ', c)

a=False
b=True
c= a or b
print(a,'OR',b, ' = ', c)

a=True
b=True
c= a or b
print(a,'OR',b, '  = ',  c)

print("=====AND=====") # jika duah buah nilai true , maka hasil nya true
a=False
b=False
c= a and b 
print(a,'AND',b, '= ',c)

a=True
b=False
c= a and b
print(a,'AND',b, ' = ', c)

a=False
b=True
c= a and b
print(a,'AND',b, ' = ', c)

a=True
b=True
c= a and b
print(a,'AND',b, '  = ',  c)

print("=====XOR=====") #jika nilai true jika salah satu nya true, sisa nya akan false
a=False
b=False
c= a ^ b 
print(a,'XOR',b, '= ',c)

a=True
b=False
c= a ^ b
print(a,'XOR',b, ' = ', c)

a=False
b=True
c= a ^ b
print(a,'XOR',b, ' = ', c)

a=True
b=True
c= a ^ b
print(a,'XOR',b, '  = ',  c)
