#Fromkey 
import os
import datetime

#bikin Tamplete dictionary, agar mempermudah data input dengan key ke dictionary
tamplete_mahasiswa={
    'nama':'nama',
    'nim' :'00000000',
    'sks_lulus': 0,
    'lahir' : datetime.datetime(1111,1,11)      
}

os.system('cls')
print(f"{'SELAMAT DATANG':^20}")
print(f"{'MAHASISWA BARU':^20}")
print('='*20)

mahasiswa=dict.fromkeys(tamplete_mahasiswa.keys())
#membuat dictnary baru sesaui dengan kay pada dictionary tamplete_mahasiswa
#print(mahasiswa) #{'nama': None, 'nim': None, 'sks_lulus': None, 'lahir': None}

mahasiswa['nama']=input("Nama Mahasiswa : ") #input data nama sesaui dengan Key
mahasiswa['nim']=input("NIM : ")
mahasiswa['sks_lulus']=int(input("SKS : "))
tahun=int(input("tahun Lahir(YYYY): "))
bulan=int(input("Bulan Lahir(1-12)): "))
tanggal=int(input("Tanggal Lahir(1-12)): "))
mahasiswa['lahir']=datetime.datetime(tahun,bulan,tanggal)
print (mahasiswa)

