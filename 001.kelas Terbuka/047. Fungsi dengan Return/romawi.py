# Fungsi untuk mengubah angka menjadi huruf Romawi
def angka_ke_romawi(angka):
    # Daftar angka dan huruf Romawi yang akan digunakan
    romawi = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    # Inisialisasi variabel untuk menyimpan hasil konversi
    hasil = ""

    # Perulangan untuk setiap angka dari daftar di atas, dari yang terbesar ke terkecil
    for key in sorted(romawi.keys(), reverse=True):
        # Selama angka masih lebih besar dari key, tambahkan huruf Romawi ke hasil
        while angka >= key:
            hasil += romawi[key]
           # print (romawi[key],hasil)
            print (f"{angka} > {key} = " )
            angka =angka- key
            print (f"{angka} dari list kurang dari {key}, cetak romawi {hasil}")
    
    return hasil

# Contoh penggunaan fungsi
print(angka_ke_romawi(67))    # Menghasilkan "III"
#print(angka_ke_romawi(75))    # Menghasilkan "IX"
#print(angka_ke_romawi(58))   # Menghasilkan "LVIII"
#print(angka_ke_romawi(1994)) # Menghasilkan "MCMXCIV"