# Copy() dan POP Dictionary

keluarga = {
    'rm':'rannu mianda',
    'so': 'saraswati oksiana',
    'masm':'medina aesha shanum mianda'
}

Familys=keluarga.copy() # melakukan copy dictionary 

print(f" ini dictionary keluarga: {keluarga}\n")
#ini dictionary keluarga: {'rm': 'rannu mianda', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda'}

print(f" ini dictionary Familys: {Familys}\n") 
# ini dictionary Familys: {'rm': 'rannu mianda', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda'}

#kita mencoba ganti  list yang ada di dictionary Family
Familys['rm']="rannumiandatanpaspasi"
Familys['gg']="tidak tahu"
print(f" ini dictionary keluarga: {keluarga}\n")
# ini dictionary keluarga: {'rm': 'rannu mianda', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda'}
print(f" ini dictionary Familys: {Familys}\n") 
#ini dictionary Familys: {'rm': 'rannumiandatanpaspasi', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda', 'gg': 'tidak tahu'}

quit_list_on_keys=Familys.pop('rm') #mengeluarkan list berdasarkan key saja 
print(f"list dictionaries yang dikeluarkan...: {quit_list_on_keys}")
#list dictionaries yang dikeluarkan...: rannumiandatanpaspasi
print(f"ini dictionary Familys: {Familys}\n")
#ini dictionary Familys: {'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda', 'gg': 'tidak tahu'} 

quit_list_on_last=Familys.popitem() #list terkahir yang dikeluarkan 
print(f"list dictionaries akhir yang dikeluarkan...: {quit_list_on_last}")
#list dictionaries akhir yang dikeluarkan...: ('gg', 'tidak tahu')
print(f"ini dictionary Familys: {Familys}\n")
#ini dictionary Familys: {'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda'}



