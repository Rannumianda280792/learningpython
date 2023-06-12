# Date and Time

import datetime as dt

hari_ini= dt.date.today() # method untuk menampilkan Hari ini atau Saat ini
print (f"tanggal sekarang adalah {hari_ini}")
print (f"hari ini adalah hari {hari_ini:%A}")
hari = dt.datetime(1992,7,28) #method untuk menampilkan datetime sesaui dengan inputan 
print (hari.strftime("%A")+"\n")
print (10*"="+" Data Lahir "+"="*10)
tanggal=int (input("tanggal lahir \t: "))
bulan=int (input("bulan lahir \t: "))
tahun=int (input("tahun lahir \t: "))
tanggal_lahir= dt.datetime(tahun,bulan,tanggal)
print (f"tanggal Lahir adalah {tanggal_lahir}")
print (f"hari Lahir adalah  {tanggal_lahir:%A}")
umur = hari_ini.year - tanggal_lahir.year
bulan_lahir = hari_ini.month - tanggal_lahir.month
print (f"Umur anda adalah {umur} tahun, {bulan_lahir} Bulan")