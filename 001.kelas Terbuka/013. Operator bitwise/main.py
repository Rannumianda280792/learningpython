#operator bitwise operasi biner

a=9
b=5

# bitwise OR (|)
c= a | b
print ('\n==========OR==========')
print ('nilai : ', a,', Binary: ', format(a,'08b')) #'0' untuk merubah kosong jadi nol, '8' untuk jumlah bilangan biner, b untuk biner
print ('nilai : ', b,', Binary: ', format(b,'08b'))
print ('-------------------------------(|)')
print ('nilai : ', c,', Binary: ', format(c,'08b'))

# bitwise AND (&)
c= a & b
print ('\n==========AND==========')
print ('nilai : ', a,', Binary: ', format(a,'08b')) #'0' untuk merubah kosong jadi nol, '8' untuk jumlah bilangan biner, b untuk biner
print ('nilai : ', b,', Binary: ', format(b,'08b'))
print ('-------------------------------(&)')
print ('nilai : ', c,', Binary: ', format(c,'08b'))

# bitwise XOR (^)
c= a ^ b
print ('\n==========XOR==========')
print ('nilai : ', a,', Binary: ', format(a,'08b')) #'0' untuk merubah kosong jadi nol, '8' untuk jumlah bilangan biner, b untuk biner
print ('nilai : ', b,', Binary: ', format(b,'08b'))
print ('-------------------------------(^)')
print ('nilai : ', c,', Binary: ', format(c,'08b'))

# bitwise NOT ()
c= ~a #tanda tilda
print ('\n==========NOT==========')
print ('nilai : ', a,', Binary: ', format(a,'08b')) #'0' untuk merubah kosong jadi nol, '8' untuk jumlah bilangan biner, b untuk biner
print ('-------------------------------(~)')
print ('nilai : ', c,', Binary: ', format(c,'08b'))
print ('-------------------------------(^)') #trick untuk flip nilai a dengan cara XOR
d=0b0000001001 #biner a
e=0b1111111111
print ('nilai : ', e^d,', Binary: ', format(e^d,'08b'))

# bitwise Shift Right (>>)
c= a >> 2
print ('\n==========>>==========')
print ('nilai : ', a,', Binary: ', format(a,'08b')) #'0' untuk merubah kosong jadi nol, '8' untuk jumlah bilangan biner, b untuk biner
print ('-------------------------------(>>)')
print ('nilai : ', c,', Binary: ', format(c,'08b'))

# bitwise Shift LEFT(<<)
c= a << 2
print ('\n==========<<==========')
print ('nilai : ', a,', Binary: ', format(a,'08b')) #'0' untuk merubah kosong jadi nol, '8' untuk jumlah bilangan biner, b untuk biner
print ('-------------------------------(<<)')
print ('nilai : ', c,', Binary: ', format(c,'08b'))