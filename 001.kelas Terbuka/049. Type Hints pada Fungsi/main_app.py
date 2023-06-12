# type hints pada Fungsi

#type hints berguna untuk memberitahu kepada pengguna type data mengintruksi ke parameter dan return
#tidak ada pengaruh apa2 terhadap code dijalan kan bila tidak cocok dengan intruksi hints dan inputan akan tetap error (tidak ada pesan khusus)

def sepuluh_pangkat(arguments:int)->int: # memberitahu kepada user bahwa  value argument type data integer dan return dengan type integer
    #bila di hover/tahan pada fungsi sepuluh_pangkat maka akan tampil :
    # (function) sepuluh_pangkat(arguments: int) -> int 
    # ini menandakan input harus int dan return -> akan bernilai integer
    '''fungsi mengunakan type hints''' 
    return 10**arguments

print(f"{sepuluh_pangkat(2)}") #100

def display (argument:str):
    '''fungsi mengunakan type hints tanpa return'''
    print(argument)
    #bila di hover/tahan pada fungsi sepuluh_pangkat maka akan tampil :
    # (function) display(argument: str) -> None
    # ini menandakan input harus string dan  nilai return tidak ada (none)

display("rannu") # rannu