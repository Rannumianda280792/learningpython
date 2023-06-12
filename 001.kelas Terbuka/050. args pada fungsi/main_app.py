# *args pada Fungsi
import os
# *args merupakan singkatan dari argument.
# kegunaan nya adalah mempermudah sebuah fungsi menerima parameter inputan/arguments seberapa banyak apapun 
# tidak tergantung pada jumlah parameter/argument yang di tulis kan. 
# argument atau input bersifat: data tuple ()
# *args dapat di ganti apa saja misal nya *data, *mahasiswa, *family dan yang lain nya. asalakan ada tanda * (bintang) didepan nya

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

# penggunaan *arg sangat memudahkan hal tersebut, mengambil parameter sebanyak apapun tidak ada masalah 
#contoh fungsi dengan *args

def fungsi (*args) : # argument akan di ambil dalam bentuk tupple ()
    print(args) #(160, 67, 29)  
    tinggi= args[0]
    berat= args[1]
    umur= args[2]
    print (f" tinggi = {tinggi}, berat = {berat}, umur = {umur}")
    #tinggi = 160, berat = 67, umur = 29

fungsi(160,67,29)

def tambah(*data):
    print(data) # data berbentuk jenis tuple 
    
    output=0
    for angka in data:
        output += angka
    return output
print(f"hasil dari tambah : {tambah(1,33,4,3)}")

