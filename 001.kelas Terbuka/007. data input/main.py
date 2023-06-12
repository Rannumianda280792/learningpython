#input dari User


data=input("masukan data : ") #data pasti di input pasti berbentuk string
print("data :" , data, type((data)))

#jika ingin mengambil Int, maka lakukan casting
angka= int(input("masukan angka :"))
print("angka :" , angka, type((angka)))
angka= float(input("masukan angka :"))
print("angka :" , angka, type((angka)))

#bagaimana dengan boolean , lakukan casting kedalam int 
biner= bool(int(input("masukan biner = ")))
print("biner :" , biner, type((biner)))