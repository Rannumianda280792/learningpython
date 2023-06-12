#key and nesting dictionary
import datetime
mahasiswa1={
    'nama':'Rannu Mianda',
    'nim' :'103510479',
    'sks_lulus': 130,
    'beasiswa' : True,
    'lahir' : datetime.datetime(1992,7,28)      
}
mahasiswa2={
    'nama':'saraswati oksiana',
    'nim' :'093538459',
    'sks_lulus': 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(1991,10,24)      
}
mahasiswa3={
    'nama':'shanum mianda',
    'nim' :'193510263',
    'sks_lulus': 134,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2019,9,29)      
}

#nesting dictionaries
data_mahasiswa={
    'MHS1' : mahasiswa1,
    'MHS2' :mahasiswa2,
    'MHS3' :mahasiswa3
}
print (f"{'KEY':<9} {'nama':<20} {'sks':<4} {'beasiswa':<6} {'lahir':<10}" )
print ("="*50)

for mahasiswa in data_mahasiswa: #cek ditutorial looping dictionary,
# ini hanya ambil KEY nya saja di tampung di Variabel mahasiswa   
    #print (mahasiswa) 
    #MHS1
    #MHS2
    #MHS3
    
    KEY =mahasiswa#buat variabel baru untuk tampung key dari mahasiswa
    #NIM= data_mahasiswa[mahasiswa]['nim'] # begini juga tidak ada masalah hanya Refactoring saja
    NIM= data_mahasiswa[KEY]['nim'] # untuk mengambil nilai dari nim di setiap KEY
    NAMA=data_mahasiswa[KEY]['nama'] # untuk mengambil nilai dari nama di setiap KEY
    SKS=data_mahasiswa[KEY]['sks_lulus'] ## untuk mengambil nilai dari SKS di setiap KEY
    BS=data_mahasiswa[KEY]['beasiswa'] # untuk mengambil nilai dari basiswa di setiap KEY
    LAHIR=data_mahasiswa[KEY]['lahir'].strftime("%x") # untuk mengambil nilai dari lahir di setiap KEY
    
    print (f"{NIM:<9} {NAMA:<20} {SKS:<4} {BS:^6} {LAHIR:<10}") # BS^6 agar line CENTER 
    '''KEY       nama       sks  beasiswa lahir     
==================================================
103510479 Rannu Mianda      130    1     07/28/92 
093538459 saraswatioksiana  130    0     10/24/91 
193510263 shanum mianda     134    1     09/29/19 '''