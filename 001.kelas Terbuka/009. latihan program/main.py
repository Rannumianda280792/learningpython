#latihan program konversi satuan temperatur

#program celcius konversi ke satuan lain

print("\nKONVERSI TEMPERATURE SUHU\n")

celcius=float(input("Masukan Suhu dalam Celcius : "))
print("Suhu adalah ", celcius, "Celcius")

#celcius ke Reamur
Reamur=(4/5) * celcius
print(" 1. suhu dalam Reamur adalah ", Reamur, "Reamur")

#celcius ke fahrenhit
fahrenhit= (9/5)*celcius+32
print(" 2. suhu dalam Fahrenhit adalah ", fahrenhit, "fahrenhit")

#celcius ke Kelvin
kelvin= celcius +273
print(" 3. suhu dalam Kelvin adalah ", kelvin, "Kelvin")

#tugas Fahrainhit to Kelvin
print("\nKONVERSI Fahrenhit to kelvin \n")

fahrenhit=float(input("berikan nilai Fahrenhit : "))
print("suhu adalah : ",fahrenhit, "Fahrenhit")

celcius= 5/9 * (fahrenhit-32) #konversi dahulu ke celcius
kelvin= celcius +273 # hitung nilai kelvin di Celcius
print("suhu",fahrenhit,"fahrenhit = ", kelvin, "Kelvin")
