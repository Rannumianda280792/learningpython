#pengenalan Fungsi dengan Return atau kembalian
import os
#template fungsi
'''Def nama_fungsi(Argument/parameter/input):
    badan_fungsi
    
    Return
'''
def fungsi_kuadrat(input_angka):
    hasil_fungsi = input_angka**2
    return hasil_fungsi


os.system("cls")
nilai_1=5
print(f"pangkat dari {nilai_1}**2 adalah {fungsi_kuadrat(nilai_1)}") 
#pangkat dari 5**2 adalah 25


def tambah(angka_1, angka2):
    hasil = angka_1+angka2
    return hasil

hasil_tambah=tambah(5,6)
print (f"hasil tambah {hasil_tambah}") #hasil tambah 11

def kalkulator (angka1,angka_2) :
    penambahan=tambah(angka1,angka_2)
    kurang = angka1-angka_2
    kali = angka1*angka_2
    bagi= angka1/angka_2
    return kali,penambahan,kurang,bagi # return juga tidak ada batasan

input1=32
input2=4
a,b,c,d = kalkulator (input1,input2) # jumlah tampung nilai return harus sama
print (f"{input1} X {input2} = {a}") #32 X 4 = 128
print (f"{input1} + {input2} = {b}") #32 + 4 = 36
print (f"{input1} - {input2} = {c}") #32 - 4 = 28
print (f"{input1} / {input2} = {d}") #32 / 4 = 8.0