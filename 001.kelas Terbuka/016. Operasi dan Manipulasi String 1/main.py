# Operasi Dan Manipulasi String

# 1. menyambungkan String (concatenate)
nama_depan ="Ucup"
nama_tengah="D"
nama_akhir="Fame"

nama_lengkap=nama_depan+" "+nama_tengah+"'"+nama_akhir #untuk menggabungkan string gunakan plus (+)
print (nama_lengkap) 

# 2. menghitung panjang dari string (len)
print ("jumlah string dari "+(nama_lengkap)+" adalah" , int(len(nama_lengkap))) #untuk menggabungkan string dan angka (int,float) gunakan koma(,)

# 3. operator untuk String

#mengecek apakah ada komponen char atau string di dalam string
d='d'
status = d in nama_lengkap 
print (d + "ada di " +nama_lengkap + "= " + str (status) ) # harus di rubah ke string TypeError: can only concatenate str (not "bool") to str

D='D'
status = D in nama_lengkap 
print (D + "ada di " +nama_lengkap + "= " + str (status) ) # harus di rubah ke string TypeError: can only concatenate str (not "bool") to str


d='d'
status = d  not in nama_lengkap 
print (d + " tidak ada di " +nama_lengkap + "= " + str (status) ) # harus di rubah ke string TypeError: can only concatenate str (not "bool") to str

#mengulang String
print ('wkwk'*10)
print (15*'wkwk')

#indexing
print ('index ke [0] ' + nama_lengkap[0])
print ('index ke [6] ' + nama_lengkap[6])
print ('index ke [-1] ' + nama_lengkap[-1]) # diambil dari belkang string
print ('index ke [-2] ' + nama_lengkap[-2]) # diambil dari belkang string
print ('index ke [0:3] ' + nama_lengkap[0:4]) # BILA mengambil lebih dari 1 string maka tambahkan satu di index terakhir
print ('index ke [3:7] ' + nama_lengkap[3:8]) # BILA mengambil lebih dari 1 string maka tambahkan satu di index terakhir
print ('index ke [0,2,4,6,8,10] ' + nama_lengkap[0:11:2]) # mengambil string index kelipatan 2

#item paling kecil
print ('paling kecil : ' + min (nama_lengkap))

#item paling besar
print ('paling besar : ' + max (nama_lengkap)) 

ascii_code=ord(" ") # untuk mengambil nilai dari unicode ascii
print ('ASCII dari spasi adalah ' + str(ascii_code))
data=117
print ('char untuk ASCII 117 adalah ' + chr(data))

# 4. operator dalam bentuk method
data="otong surotong pararotong"
jumlah= data.count ("o")
print ("jumlah o pada " + data + " adalah " +str(jumlah))

