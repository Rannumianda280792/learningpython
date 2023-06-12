# *kwargs pada Fungsi
import os
# **kwargs merupakan singkatan dari keyward argument.
# kegunaan nya  sama dengan *args  adalah mempermudah sebuah fungsi menerima parameter inputan/arguments seberapa banyak apapun yang di kirim dari luar fungsi 
# tidak tergantung pada jumlah parameter/argument yang di tulis kan. 
# perbedaan nya **kwargs argument atau input bersifat: data dictionary :{ 'key' : 'value')
# **kwargs dapat di ganti apa saja misal nya **data, **mahasiswa, **family dan yang lain nya. asalakan ada tanda * (bintang) didepan nya double

#contoh fungsi biasa: 
def fungsi (tinggi='non', berat='non', umur='non') : 
    # pakai fungsi dalam defult agar nanti di inputkan tidak ada error apabila tidak sesuai 3 parameter tersebut
    print (f" tinggi = {tinggi}, berat = {berat}, umur = {umur}")
    #tinggi = 160, berat = 67, umur = 29
os.system("cls") #bersih kan layar diterminal bila program dalam keadaan Run
fungsi(160,67,29) #parmater kiriman ke fungsi berjumlah 3 karena di fungsi menerima 3 argument
#kalau parameter kirim 4 paramater ke fungsi maka akan Error karena sudah di batasi 3 argument saja
#fungsi (160,67,54,34)
#ini akan Error  
#seperti ini pesan nya :TypeError: fungsi() takes from 0 to 3 positional arguments but 4 were given 

#contoh fungsi dengan *kwargs

def fungsi (**kwargs) : # argument akan di ambil dalam bentuk dictionary {}  
    print (f"cek format kwargs : {kwargs}")
    tinggi= kwargs['tinggi']
    berat= kwargs['berat']
    umur= kwargs['umur']
    print (f" tinggi = {tinggi}, berat = {berat}, umur = {umur}")
    #tinggi = 160, berat = 67, umur = 29

fungsi(tinggi=160, berat= 67,umur= 29) # perhatikan!! parameter pengirim harus memberi format jelas ke fungsi
# setalah nya akan di ambil dalam bentuk key 

def kalkulator(*argdata:float,**kwdata:float)->float:
    print(argdata) # data berbentuk jenis tuple ()
    print (kwdata) # data berbentuk dictionary {}
    if kwdata['option']=="tambah":
        output=0
        for angka in argdata:
            output += angka
    
    elif kwdata['option']=='kali':
        output=1
        for angka in argdata:
            output *= angka
    return output
hasil_tambah = kalkulator(1,2,3,4, option ='tambah')
hasil_kali = kalkulator(1,2,3,4, option ='kali')
print(f"hasil dari penambahan = {hasil_tambah}") #hasil dari penambahan = 10
print(f"hasil dari perkalian = {hasil_kali}") #hasil dari perkalian = 24


def biodata (*bio, **dicdata):
    nama=dicdata['nama']
    umur=bio[0]
    berat=bio[1]
    return nama,umur,berat

hasil=biodata(30,43,nama="rannu")
print(f"nama {hasil[0]}, berat badan {hasil[2]} kg dan umur = {hasil[1]} tahun") 
#nama rannu, berat badan 43 kg dan umur = 30 tahun