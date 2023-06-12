#pengenalan Fungsi dengan argument defult
import os
#template fungsi
'''Def nama_fungsi(Argument=""):
    badan_fungsi
    
    Return
'''
def say_hello(nama, pesan="ok"):
    print (f"hallo apa kabar {nama} ? {pesan}")
    
say_hello("rannu","hallo") #jika tidak di inputkan argument maka akan tercetak defult yang berada dalam fungsi
#hallo apa kabar rannu ? hallo
say_hello("mianda") #hallo apa kabar mianda ? ok


def fungsi_kuadrat(input_angka,bilangan_pangkat=2):
    hasil_fungsi = input_angka**bilangan_pangkat
    return hasil_fungsi


#os.system("cls")
nilai_input=3
print(f"pangkat dari {nilai_input} **2 adalah {fungsi_kuadrat(nilai_input)}") #pangkat dari 3 **2 adalah 9

hasil= fungsi_kuadrat(bilangan_pangkat=4,input_angka=4) #dapat menentukan nilai dari argument itu sendiri
print(f"hasil pangkat adalah {hasil}")
#hasil pangkat adalah 256



def tambah(input1=1,input2=2,input3=3,input4=4):
    hasil_fungsi_tambah = input1+input2+input3+input4
    return hasil_fungsi_tambah

hasil_tambah=tambah()
print (f"hasil tambah {hasil_tambah}") #hasil tambah 10 mengunakan seluruh defult argument

hasil_tambah=tambah(input2=6)
print (f"hasil tambah {hasil_tambah}") #hasil tambah 14 mengunakan defult argument yang di ganti hanya input2

