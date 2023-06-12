# Operator Dalam Bentuk Method

## Merubah Case dari String

# Merubah Semua ke Upper Case

salam= "bro"
print ("normal="+ salam)
salam=salam.upper()
print ("Uper Case= "+salam)

# Merubah Semua ke Lowwer Case
alay='Aq SangAt KeCe HabIzZzZ'
alay=alay.lower()
print ("Lowwer Case= "+alay)

## pengecekan dengan IsX Method
salam= "sist"
apakah_lowwer =salam.islower() # Cek Seluruh kata berhuruf kecil
print (salam + " is Lowwer " + str(apakah_lowwer)) #hasil dalam bentuk Boolean maka dilakukan Format Casting Method
apakah_upper =salam.isupper() # Cek Seluruh kata berhuruf besar
print (salam + " is upper " + str(apakah_upper)) #hasil dalam bentuk Boolean maka dilakukan Format Casting Method

isnum= '100'
apakah_num =isnum.isnumeric()
print (isnum+ " is num "+ str(apakah_num))
# isalpha () <----- untuk mengecek semua nya huruf
# isnum () <----- untuk mengecek huruf dan angka
# isdecimal() <----- untuk mengecek angka saja
# isspec () <----- untuk mengecek tab, spasi, newlines
# istittle () <----- semua dimulai dengan huruf besar

judul = "Belajar Python Di Kelas Terbuka" #semua diawal kata besar
cek_judul=judul.istitle() #hasil boolean
print (judul+ " is title = " + str(cek_judul))

## ngecek komponen startwith() dan endwith() 
cek_start= "Mengejar matahari".startswith('Mengejar')
print ('start= ' + str(cek_start))

cek_end= "Mengejar matahari".endswith('matahari')
print ('end= ' + str(cek_end))

#komponen  join () dan Split()
pisah= ['aku', 'sayang', 'kamu'] # ini list
print (pisah)
gabungan = ",".join(pisah)
print (gabungan)

gabungan = " ".join(pisah)
print (gabungan)

gabungan = " hm ".join(pisah)
print (gabungan)

gabungan ="aku sayang kamu"
print (gabungan.split(" ")) #menjadikan data list kembali kebalikan dengan join

#alokasi karakter rjust(), ljust(), Center()
print (5*"=" + "data" + "="*5)

kanan = "1234".rjust(10) #rata kanan untuk space 10 karakter
print ("'" + kanan + "'")

kiri = "1234".ljust(10) #rata kiri untuk space 10 karakter
print ("'" + kiri + "'")

tengah = "1234".center(10,'-') #rata tengah untuk space 10 karakter
print ("'" + tengah + "'")

#kebalikannya -> strip()
tengah = tengah.strip('-') #menghilangkan tanda -
print ("'" + tengah + "'")

kanan = kanan.strip() #menghiangkan rata kanan
print ("'" + kanan + "'")

kiri = kiri.strip() #menghiangkan rata kiri
print ("'" + kiri + "'")