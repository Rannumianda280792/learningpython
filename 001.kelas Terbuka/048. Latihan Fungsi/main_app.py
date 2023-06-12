#latihan Fungsi
import os
#program menghitung luas dan keliling persegi panjang 

def header():
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}") 
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    lebar=int(input("inputkan leber persegi : " ))
    panjang=int(input("inputkan panjang persegi : " ))
    return lebar,panjang

def hitung_luas(lebar,panjang):#ini tidak ada argument defult maka wajib di kirim ke fungsi ini
    '''fungsi luas'''
    return panjang*lebar    # jika hanya satu proses di dalam fungsi maka boleh seperti ini

def hitung_keliling(lebar,panjang): #ini tidak ada argument defult maka wajib di kirim ke fungsi ini
    '''fungsi keliling'''
    return 2*(panjang*lebar) # jika hanya satu proses di dalam fungsi maka boleh seperti ini

def display(massage,value): #ini tidak ada argument defult maka wajib di kirim ke fungsi ini
    print (f"{massage} = {value}")

def pilih_options():
    print(f"1.hitung luas persegi panjang")
    print(f"2.hitung keliling persegi panjang")
    print(f"3.hitung luas dan keliling persegi panjang")
    pilihan= int(input("silahkan pilih menu options[1/2/3] :"))
    return pilihan

#program UTAMA
while True:    
    header()
    select_opti=pilih_options()
    lebar,panjang=input_user() 
    # fungsi input_user mempunyai nilai return,
    # kemudian di keluarkan dan tampung di variable luar fungsi atau variabel program utama,
    # agar  memudahkan input value/parameter/argument yang di kirim ke fungsi lainnya / ditampilkan
    if select_opti==1:
        print(f"1.hitung luas persegi panjang")
        luas=hitung_luas(lebar,panjang) #menjadi value/parameter/argument yang di kirim input_user
        display('luas', luas) # value/parameter/argument akan di kirim  ke fungsi Display

    elif select_opti==2:
        print(f"2.hitung keliling persegi panjang")
        keliling=hitung_keliling(lebar,panjang)
        display('keliling', keliling)

    elif select_opti==3:
        print(f"3.hitung luas dan keliling persegi panjang")
        luas=hitung_luas(lebar,panjang)
        keliling=hitung_keliling(lebar,panjang)
        display('luas', luas)
        display('keliling', keliling) 
        
    else:
        print("Input Option Menu salah")
        
    iscontinue= input("apakah akan dilanjutkan [N/Y] : ")
    if iscontinue== 'N' :
        break

print("PROGRAM SELESAI, TERIMAKASIH BANYAK")
