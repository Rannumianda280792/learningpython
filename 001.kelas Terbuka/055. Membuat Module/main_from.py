
from matematika import kali, tambah, pangkat
#arti nya dari module matematika diambil fungsi kali, tambah dan pangkat
#jadi kita tidak lagi menuliskan "matematika.kali(13,4,2)" menjadi
# seperti dibawah ini matematika dihilangkan saja
#from matematika import * 
#ini memanggil fungsi atau isi module seluruh nya
#tapi ini tidak direkomendasi kan karena akan ada duplikasi atau ambigu 
#developer yang akan melakukan pekerjaan nya 

print(f"hasil tambah dari module matematika {tambah(1,3,4,5)}")

print(f"hasil kali dari module matematika {kali(1,3,4,5)}")

pangkat_3= pangkat(3)

print(f"hasil pangkat dari module matematika {pangkat_3(3)}")
