#oprasi Dictionary

list_dict = {
    'rm':'rannu mianda',
    'so': 'saraswati oksiana',
    'masm':'medina aesha shanum mianda'
}

# panjang data pada dictionary
lendict=len(list_dict)
print (f"jumlah data pada dictionary adalah {lendict}")
#jumlah data pada dictionary adalah 3

#mengecek key exist ada atau tidak
key="rm"
checkkey= key in list_dict
print (f"{key} didalam list_dict adalah {checkkey}")
#rm didalam list_dict adalah True

#mengakses value(read) dengan get
print (f"{list_dict['masm']}") #medina aesha shanum mianda
#print (f"{list_dict['rms']}") #ini akan ditampilkan pesan Error
#untuk mengantisipasi pesan error pada dictionary sebaiknya pakai get
print (f"{list_dict.get('rm')}") #rannu mianda
print (list_dict.get('rms','tidak ditemukan')) # None akan menampilkan pesan none, 
#kita juga dapat mengganti pesan none dengan pesan yang kita inginkan

#mengupdate data pada dictionary
list_dict['rm'] = 'rannu miandas'
print (list_dict) #akan di update
#{'rm': 'rannu miandas', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda'}
list_dict['ft']= 'fransesco totti'
print (list_dict) #akan di tambahkan
#{'rm': 'rannu miandas', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda', 'ft': 'fransesco totti'}

list_dict.update({'rm':'rannu mianda'})
print (list_dict) #akan di update
#{'rm': 'rannu mianda', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda', 'ft': 'fransesco totti'}

list_dict.update({'lm':'leo messi'}) #jika tidak ada maka di add saja tidak perlu ragu ada atau tidak nya di dalam list
print (list_dict) 
#{'rm': 'rannu mianda', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda', 'ft': 'fransesco totti', 'lm': 'leo messi'}

#menghapus dictionary
del list_dict['lm']
del list_dict['ft']
print (list_dict)
#{'rm': 'rannu mianda', 'so': 'saraswati oksiana', 'masm': 'medina aesha shanum mianda'}