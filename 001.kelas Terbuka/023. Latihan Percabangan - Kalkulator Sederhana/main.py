#  latihan 

#kalkulator sederhana
print (40*"=")
print ("kalkulator sederhana")
print (40*"="+"\n")

angka_1= float(input ("silahkan masukan bilangan Pertama = "))
operator= input ("silahakan pilih (+,-,x,/)         = ")
angka_2= float(input ("silahkan masukan bilangan kedua   = "))    

if operator=="+" :
    #hasil= angka_1 +angka_2  
    print (f"hasil dari {angka_1} + {angka_2} = {angka_1+ angka_2}")
    print (40*"-")
    
elif operator=="-" :
    #hasil= angka_1 +angka_2  
    print (f"hasil dari {angka_1} - {angka_2} = {angka_1- angka_2}")
    print (40*"-")
    
elif operator=="x" or operator== "*" or operator=="X":
    #hasil= angka_1 +angka_2  
    print (f"hasil dari {angka_1} * {angka_2} = {angka_1* angka_2}")
    print (40*"-")
    
elif operator=="/" :
    #hasil= angka_1 +angka_2  
    print (f"hasil dari {angka_1} / {angka_2} = {angka_1 / angka_2}")
    print (40*"-")
else :
    print (f"Inputan anda salah silahkan ulangi")
    print ("terimakasih banyak")

print ("akhir dari program")
