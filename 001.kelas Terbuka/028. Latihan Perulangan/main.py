# #latihan percabangan

# print ("pakai For")
# sisi=10
# count=0
# for i in range (sisi):
#     count+=1
#     print ("*"*count)
# print ("akhir For\n")

# print ("pakai While")
# count=0
# while True:
#     count+=1
#     print ("*"*count)
#     if count > sisi:
#         break
# print ("akhir while\n")
# sisi=10
# print ("pakai While cetak ganjil")
# count=0
# while True: 
#     count+=1
#     if (count % 2) :  # ini sama seperti count % 2 == 1, ini hasil nya adalah ganjil , otomatis hasil bagi sisa 1 akan di cetak
#         #print (count%2)
#         print ("*"*count)
#     else:
#         continue
    
#     if count > 10:
#         break
# print ("akhir while\n")

# print ("pakai While cetak segitiga sama kaki")
# sisi=10
# count=0
# while True: 
#     count+=1
#     if (count % 2) :  # ini sama seperti count % 2 == 1, ini hasil nya adalah ganjil , otomatis hasil bagi sisa 1 akan di cetak
#         #print (count%2)
#         spasi="*"*count
#         print(spasi.center(sisi+1))
        
#     else:
#         continue
    
    
#     if count > sisi:
#         break
    
count=0
sisi=10
spasi=int(sisi/2) # ini untuk menentukan jumlah spasi
while True:
    count+=1
    if count%2 == 1: # cetak apabila countnya berjumlah ganjil
        print(" "*spasi,"+"*count)
        spasi-=1 #mengurangi spasi setiap looping 
    else: continue #jika genap tidak akan di cetak akan looping selanjutnya
    
    if count > sisi: # apabila ini count nya sudah melebihi jumlah sisi maka stop 
        break
    
#print(13*"=")

spasi = 0
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        count -= 1
        spasi += 1
    if count < 1:
        break
    else:
        count -= 1
        continue