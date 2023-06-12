# width and multiline

#data
data_nama= "Rannu"
data_umur= 30
data_tinggi=190
data_sepatu=45

#string Standart
data_string=f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Sepatu = {data_sepatu}"
print(5*"="+"Data String "+"="*5)
print(data_string)

#string Multiline dengan mengunakan enter, newline, \n
data_string=f"Nama = {data_nama} \nUmur = {data_umur} \nTinggi = {data_tinggi} \nSepatu = {data_sepatu}"
print("\n"+5*"="+"Data String "+"="*5)
print(data_string)

#string Multiline dengan kutip tripels """xxxxxxx"""
data_string=f"""Nama   = {data_nama} 
Umur   = {data_umur} 
Tinggi = {data_tinggi} 
Sepatu = {data_sepatu} """
print(5*"="+"Data String "+"="*5)
print(data_string)


#mengatur lebar
data_nama = "Rannu Mianda"
data_string=f"""Nama   = {data_nama:>12}  
Umur   = {data_umur:>4} 
Tinggi = {data_tinggi:>8} 
Sepatu = {data_sepatu:>12}""" #mengatur lebar rata kanan dengan ukuran yang di inginkan

print(5*"="+"Data String "+"="*5)
print(data_string)