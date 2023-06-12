#control Flow continue, pass


#pass berfungsi sebagai Dummy  dan tidak akan di eksekusi

# angka=0

# while angka<5 :
#     angka=angka+1
#     if angka==3:
#         pass  #tidak ada pengaruh apa dan tidak akan di eksekusi
#     print (angka)

#continue

angka=0

while angka<5:
    angka+=1
    print (f"baris ke- {angka}") #aksi 1
    if angka==3:
        print("ini comment di break") #aksi 3
        break # akan mamaksa loop berhenti eksekusi    
    
    print ("comment diluar break") #aksi 2
    
print ("ini akhir dari program")

data_int=int(input("hitung sampai = "))
angka_1=0

while True:
    angka_1+=1
    print (f"baris ke- {angka_1}") #aksi 1
    if angka_1==data_int:
        print("ini comment break") #aksi 3
        break # akan mamaksa loop berhenti eksekusi    
    
    print ("comment diluar break") #aksi 2
    
print ("Program selesai")