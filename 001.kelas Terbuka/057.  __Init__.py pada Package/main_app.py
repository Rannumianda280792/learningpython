#halaman Main Program
#fungsi dari __init__  adalah digunakan untuk pemanggilan module secara langsung di dalam Packege/folder setelah di import dan 
#dapat digunakan di halaman utama 
#di eksekusi saat kita import pakckege
import sains
#pada import tidak perlu lagi menuliskan module dalam packege seperti sebelum nya
# import sains.matematika
# peran __init__ untuk menempelkan/menyambungkan pakages sains ke module matematika dan module fisika
# dan dapat mengakses file di dalam subfolder/pakages 

#ini hasil dari file __init__ from . import matematika
nilai_tambah = sains.matematika.tambah(123,45,3)
print (f'nilai_tambah = {nilai_tambah}')

#ini hasil dari file __init__ from . import fisika
nilai_fisika = sains.fisika.gaya(10,9.8)
print (f'nilai_fisika = {nilai_fisika}')

#ini hasil dari file __init__ from .matematika import kali
nilai_kali=sains.kali(3,6,5,3)
print (f'nilai_kali = {nilai_kali}')

#ini subfolder/subpackege, cara akses nya:
#import terlebih dulu subfolder di __init__ yang ada di folder utama
# import . hitungan
# lalu bikin lagi file __init__ di subfolder nya 
# from. import kurang
nilai_kurang = sains.hitungan.kurang.pengurangan(2,10)
#folder utama 'sains' mempunyai sub folder 'hitungan' yang
# mempunyai module 'kurang' dan diambil fungsi/member 'pengurangan'
#di akses dengan file __init__ yang ada di subfolder hitungan
print (f'nilai_kurang = {nilai_kurang}')

#sama dengan diatas hanya di taruh pada sub __init__ seperti berikut
#from .bagi import pembagian as mid
nilai_bagi= sains.hitungan.mid(100,2)
print (f'nilai_bagi = {nilai_bagi}')
