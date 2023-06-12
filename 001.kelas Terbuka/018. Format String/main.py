# format String

# Contoh Generic

#string
nama= "Rannu"
format_string= f" Nama : {nama}"
print (format_string)


#boolean
boolean= True
print (f"boolean: {boolean}")

#angka
angka=200.67
format_str= f"Angka : {angka}"
print (format_str)

#bilangan bulat
angka=15
format_str= f"bilangan Bulat : {angka:d}" # d adalah khusus tipe data integer 
print (format_str)

#bilangan ordo ribuan dan jutaan
ribuan=2000
jutaan=2000000
format_str= f"ribuan : {ribuan:,}" # , menambahkan koma untuk pemisah antar nomimal
print(format_str)
format_str= f"jutaan : {jutaan:,}" # , menambahkan koma untuk pemisah antar nomimal
print(format_str)

#bilangan decimal
angkat=2005.54321
format_str= f"angkat : {angkat:.3f}" # .2 mengambil tiga angka dibelakang koma, f untuk tipe data float 
print(format_str)

#menampilkan Leading zero
angkat=2005.54321
format_str= f"angkat : {angkat:09.3f}" # 0 = menambahkan nol di depan, 9 menampilkan hanya 9 digit angka termasuk spasi dan nol, .3 mengambil tiga angka dibelakang koma, f untuk float 
print(format_str)

#menampilkan tanda + dan -
angka_minus=-10
angka_plus= +10.3422
format_minus= f"minus : {angka_minus:d}"
format_plus= f"plus : {angka_plus:+.2f}" #menambahkan tanda + dengan mengambil dua angka belkang koma format float

print(format_minus)
print(format_plus)

#persentase
persentase= 0.045
format_persentase= f"persentase : {persentase:.2%}" 
print(format_persentase)

#melakukan operasi artematika didalam placeholders

harga=1000
jumlah=4
format_str=f" harga {harga} * jumlah barang {jumlah} adalah : {harga*jumlah}"
print(format_str)

#format binary, octal , hexadecimal
angkat=255
format_binary= f" format binary ={bin(angkat)}"
format_octal= f" format octal ={oct(angka)}"
format_hexadecimal= f"format hexadecimal=  {hex(angkat)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)