def tambah(*arg) :
    hasil=0
    for plus in arg:
        hasil+=plus
    
    return hasil

def kali(*arg) :
    hasil=1
    for bintang in arg:
        hasil*=bintang
    
    return hasil

def pangkat(n):
    return lambda angka:angka**n

