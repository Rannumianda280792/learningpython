#standart Library Python

import datetime # datetime ini adalah module bawaan Python

waktu_sekarang= datetime.datetime.now()
                #datetime= module yang di import, .datetime = class dalam module datetime, .now()= methode di dalam sebuah class datetime
                
print (f"waktu sekarang adalah {waktu_sekarang}")
print (f"tahun sekarang adalah {datetime.datetime.now().year}")
print (f"hari sekarang adalah {waktu_sekarang.strftime('%A')}")

from collections import Counter 

data= ['a','b','c','a','a','a','c','c']
data_count= Counter(data)
print (f"{data_count}")
print (f"jumlah angka a adalah {data_count['a']}")
print (f"jumlah angka d adalah {data_count['d']}")

import io

file=io.open("file_text.txt","w") # menulis kan isi file
file.write(f"==============\nini isi dari file_text.txt : {str(waktu_sekarang)}\n")
file.write(f"{str(data_count)}\n==============")
file=io.open("file_text.txt","r") #membaca isi file
print (file.read())
file.close()


'''Counter({'a': 4, 'c': 3, 'b': 1})
jumlah angka a adalah 4
jumlah angka d adalah 0
ini adalah teks dari file_text.txt'''
