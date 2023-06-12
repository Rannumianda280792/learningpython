#while loop

# while kondisi
#     aksi ini
#     aksi itu
# akhir dari program

angka_1=0
while angka_1<5:
    angka_1+=1
    print(f"saya bisa - {angka_1}")
print("akhir dari program ini...")

#ini program latihan
angka= 0
cetak= input("mau cetak tulisan apa ? ")
tanya=True

while  tanya==True:
    angka+=1
    print (f"cetak ke: {angka}")
    print(cetak)
    tanya= bool (int((input("ingin ulangi ? (1/0) : "))))
    print (40*"=")
    
    if tanya==False:
        print("anda keluar dari program ini...")
    

print(f"\njumlah yang tercetak = {angka}")

