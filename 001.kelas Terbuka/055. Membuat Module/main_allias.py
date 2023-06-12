from matematika import kali as K 
from matematika import tambah as add
from matematika import pangkat as P
# alias memberi nama kepada module atau fungsi nya
# tidak dapat di gunakan apabila seperti ini:
# from matematika as matem
# yang benar adalah import matematika as matem tanpa from


print(f"hasil tambah dari module matematika {add(1,3,4,5)}")

print(f"hasil kali dari module matematika {K(1,3,4,5)}")

pangkat_3= P(3)

print(f"hasil pangkat dari module matematika {pangkat_3(3)}")
