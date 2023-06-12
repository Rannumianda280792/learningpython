#Latihan List buku

no=0
list_buku=[]
while True:
    no+=1
    print (f"No. {no}")
    judul= input ("Judul Buku \t: ")
    penulis=input ("Penulis Buku \t: ")

    buku_baru=[judul,penulis] 
    print("================================")
    list_buku.append(buku_baru) #menambahkan list di akhir

    for index,buku in enumerate(list_buku): # untuk mendapatkan nilai index dan data
        
        print(f"No.{index+1}|{buku[0]}|{buku[1]} ")

    confirm=input("tambahkan lagi buku [y/n]: ")
    if confirm !='y':
        break
