
data= "ini adalah string"
print(data)
print(type(data))   

# 1. Cara Membuat String

'''
1. Dengan menggunakan single Quote'...'
2. Dengan menggunakan double Quote "..."
'''
data= 'dengan menggunakan single Quote'
print(data)
data= "dengan menggunakan double Quote"
print(data)

print('"Hallo apa kabar ?"') #akan di tampilkan kutip " sebagai String
print("'Hallo apa kabar ?'")#akan di tampilkan kutip ' sebagai String
print ("ini adalah hari jum'at")

#2. mengunakan tanda \
    
#membuat tanda ' menjadi string
print('mari sholat jum\'at') # digunakan bila terdapat data kutip satu di dalam kalimat single qoute ' '
print('g\'day isn\'t it?')

#backlish
print("D:\\folder\\rannu") #agar backlish dibaca sebagai String maka double backlish

#tab
print("mencoba pakai \t\ttab, kejauhan")

#backspace
print("kalimat \bini \bakan \bdekat")

#newline
print("beris pertama \nbaris kedua") #LF -> Line Feed dipakai unix, macos, linux
print("beris pertama \rbaris kedua") #CR -> cariage Return dipakai commodore, accor
print("baris pertama \r\nbaris kedua") #CRLF -> cariage Return line feed dipakai Windows

# 3. Literals String atau Raw

#hati-hati
print('d:\newfolder') # akan salah path nya

#menggunakan Raw String  menghilangkan semua fungsional dari bacslash dan lain nya, menjadi kan seluruh nya String  
print(r'd:\new folder\d\r\d\rbaris') #seluruhnya akan di baca sebagai String

#multiline literals string
print("""
nama :Rannu
kelas: 3 SD""")

#multiline literals string dan Raw  
print(r"""
nama :Rannu
kelas: 3 SD \new normal
web : www. rannu\nasa""")