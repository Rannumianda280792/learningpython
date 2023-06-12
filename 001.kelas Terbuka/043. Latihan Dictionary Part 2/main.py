#Fromkey 
import os #untuk membersihkan terminal dengan coding 
import datetime
import string # memberikan nilai berbentuk string yang diacak
import random # memberikan nilai acak 


#bikin Tamplete dictionary, agar mempermudah data input dengan key ke dictionary
tamplete_mahasiswa={
    'nama':'nama',
    'nim' :'00000000',
    'sks_lulus': 0,
    'lahir' : datetime.datetime(1111,1,11)      
}

data_mahasiswa={} #variabel penampung untuk data dictionary nested 

while True:
    os.system('cls')#bersihkan layar secara otomatis
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'MAHASISWA BARU':^20}")
    print('='*20)

    mahasiswa=dict.fromkeys(tamplete_mahasiswa.keys())
    #membuat dictnary baru sesaui dengan kay pada dictionary tamplete_mahasiswa
    #print(mahasiswa) #{'nama': None, 'nim': None, 'sks_lulus': None, 'lahir': None}

    mahasiswa['nama']=input("Nama Mahasiswa : ") #input data nama sesaui dengan Key
    mahasiswa['nim']=input("NIM Mahasiswa : ") #input data NIM sesaui dengan Key
    mahasiswa['sks_lulus']=int(input("SKS : ")) #input data SKS sesaui dengan Key
    tahun=int(input("tahun Lahir(YYYY): ")) #input data Tahun sesaui dengan Key
    bulan=int(input("Bulan Lahir(1-12)): ")) #input data bulan sesaui dengan Key
    tanggal=int(input("Tanggal Lahir(1-12)): "))#input data tanggal sesaui dengan Key
    mahasiswa['lahir']=datetime.datetime(tahun,bulan,tanggal)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) 
    #ini untuk mengambil secara acak dalam bentuk string disimpan dalam key 
    # sebagai pembeda dengan data lain agar nanti tidak di timpa oleh data berikut nya
    
    data_mahasiswa.update({KEY:mahasiswa})# tampung ke data_mahasiswa sebagai nested dictionary
    
    print (f"{'KEY':<10} {'NIM':<10} {'nama':<20} {'sks':<4} {'lahir':<10}" )
    print ("-"*60)
    
    for mahasiswa in data_mahasiswa: 
        # ini hanya ambil KEY nya saja di tampung di Variabel mahasiswa   
        KEY =mahasiswa#buat variabel baru untuk tampung key dari mahasiswa
        #NIM= data_mahasiswa[mahasiswa]['nim'] # begini juga tidak ada masalah hanya Refactoring saja
        NIM= data_mahasiswa[KEY]['nim'] # untuk mengambil nilai dari nim di setiap KEY
        NAMA=data_mahasiswa[KEY]['nama'] # untuk mengambil nilai dari nama di setiap KEY
        SKS=data_mahasiswa[KEY]['sks_lulus'] ## untuk mengambil nilai dari SKS di setiap KEY
        LAHIR=data_mahasiswa[KEY]['lahir'].strftime("%x")
        #untuk mengambil nilai dari lahir di setiap KEY dengan format 1992/7/28
    
        print (f"{KEY:<10} {NIM:<10} {NAMA:<20} {SKS:<4} {LAHIR:<10}")  # cetak seluruh inputan
    print("\n")
    is_not=input("ingin input data kembali :[Y/N] ")
    if is_not == 'n' or is_not=='N':
        break
print ("Program Berakhir, Terimakasih banyak")
