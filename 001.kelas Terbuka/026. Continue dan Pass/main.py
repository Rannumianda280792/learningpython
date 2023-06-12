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
        print("ini comment di continue") #aksi 3
        continue # akan memebuat loop loncat ke loop selanjut nya tidak akan di eksekusi aksi 2 
        #akan di cut proses nya ke loop selanjut , dibawah continue tidak akan di eksekusi    
    
    print ("comment diluar continue") #aksi 2
    
