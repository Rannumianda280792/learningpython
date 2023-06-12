#list copy

a=["rannu","saras","shanum"]
b=a # ini variabel b memiliki addres yang sama dengan variabel a

print(f"data list a adalah\n{a}")
print(f"data list b adalah\n{b}")

#apapun di yang dirubah akan mempengaruhi ke dua list  nya
b[2]="mianda"
print(f"data list a adalah\n{a}") # ['rannu', 'saras', 'mianda'] akan berubah pula di index ke-2 list a menjadi 'mianda'
print(f"data list b adalah\n{b}") #['rannu', 'saras', 'mianda']

#mengapa demikian?? karena ke-2 nya memiliki address yang sama 
print(f" addres pada list a = {hex(id(a))}") #a = 0x1e860363f00
print(f" addres pada list b = {hex(id(b))}") #b = 0x1e860363f00

#solusi nya seperti apa untuk duplicate list?? menggunakan metode ".copy()"

c=a.copy() #akan tercopy seluruh data di list a ke list c ,akan berbeda addres list a dengan list c

c[2]="aesha" #akan berubah di index-2 namun tidak merubah list a dan b 

print(f"data list a adalah\n{a}") # ['rannu', 'saras', 'mianda']
print(f"data list b adalah\n{b}") # ['rannu', 'saras', 'mianda']
print(f"data list c adalah\n{c}") # ['rannu', 'saras', 'aesha'] 

# address list C berbeda dengan list a dan b , jadi apapun modifikasi di list c tidak merubah apa2 di lis a dan b

print(f" addres pada list a = {hex(id(a))}") #a = 0x1e860363f00
print(f" addres pada list b = {hex(id(b))}") #b = 0x1e860363f00
print(f" addres pada list c = {hex(id(c))}") #c = 0x1e8604ddf00