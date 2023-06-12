#pengenalan Fungsi dengan Argument
import os
#template fungsi
'''Def nama_fungsi(Argument/parameter/input):
    badan_fungsi
'''
def hello_world(nama):
    print (f" Hello Dunia!, apa kabar mu {nama}")
    # Hello Dunia!, apa kabar mu Rannu
    #Hello Dunia!, apa kabar mu Shanum
    
os.system("cls")
hello_world("Rannu")
hello_world("Shanum")

def tambah(angka_1, angka2):
    hasil = angka_1+angka2
    print (f" {angka_1}+{angka2} = {hasil}")
    # 2+3 = 5
tambah(2,3)

def list_peserta(masyarakat):
    peserta_goro=masyarakat.copy() #sebaiknya lakukan copy list untuk menghindari duplikat
    peserta_goro[1]="dodo" # tidak akan merubah list di luar fungsi
    for absensi in peserta_goro:
        print(f"terimakasih bapak, {absensi}")
        '''terimakasih bapak, didit
        terimakasih bapak, Rio
        terimakasih bapak, bisma'''
        
anggota_goro=["didit","Rio", "bisma"]
list_peserta(anggota_goro)
