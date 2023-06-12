
#alternatif 1
import sains.matematika # folder ini  berisi module matematika
#fungsi tambah, kali , dan pangkat ada di module matematika
#untuk running nya harus menuliskan nama pakeges.nama module. nama function 
print(f"hasil tambah dari module matematika {sains.matematika.tambah(1,3,4,5)}") 
#hasil tambah dari module matematika 13
print(f"hasil kali dari module matematika {sains.matematika.kali(1,3,4,5)}")
#hasil kali dari module matematika 60
pangkat_3= sains.matematika.pangkat(3)
print(f"hasil pangkat dari module matematika {pangkat_3(3)}")
# hasil pangkat dari module matematika 27
#alternatif 2
from sains import fisika
#arti nya dari akses pakages sains untuk module fisika
#cara penggunaan :
print(f"hasil dari module fisika {fisika.gaya(1,3)}") #tidak perlu menuliskan pakages sains 
#hasil dari module fisika 3

#alternative 3
from sains.fisika import gaya as force
#cara penggunaan :
print(f"hasil dari module fisika {force(1,5)}") #tidak perlu menuliskan module fisika cukup nama alias
#hasil dari module fisika 5 
