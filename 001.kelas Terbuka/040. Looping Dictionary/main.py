#lopping Dictionary

keluarga = {
    'rm':'rannu mianda',
    'so': 'saraswati oksiana',
    'masm':'medina aesha shanum mianda'
}

for family in keluarga:
    print(family) #ini hanya mengambil key nya saja
    '''rm
       so
       masm '''

#operator mengambil item/ iterable
key= keluarga.keys() #untuk mengambil key nya saja
print(key) # ini adalah itereble dict_keys(['rm', 'so', 'masm'])

for key in keluarga.keys():
    print(f"{keluarga[key]}")
    #rannu mianda
    #saraswati oksiana
    #medina aesha shanum mianda
    
values=keluarga.values() #untuk mengambil value
print(values) # dict_values(['rannu mianda', 'saraswati oksiana', 'medina aesha shanum mianda'])

for value in keluarga.values():
    print(f"{value}")
    #rannu mianda
    #saraswati oksiana
    #medina aesha shanum mianda
    
item=keluarga.items() #untuk mengambil kay dan value
print(item) # dict_items([('rm', 'rannu mianda'), ('so', 'saraswati oksiana'), ('masm', 'medina aesha shanum mianda')])

for items in item:
    print(items)
    #('rm', 'rannu mianda')
    #('so', 'saraswati oksiana')
    #('masm', 'medina aesha shanum mianda')

#bisa mengambil key dan value sama dengan jika di list fungsi numarate()
for key,value in item:
    print (f"keys : {key} value : {value}")
    '''keys : rm value : rannu mianda
       keys : so value : saraswati oksiana
       keys : masm value : medina aesha shanum mianda'''