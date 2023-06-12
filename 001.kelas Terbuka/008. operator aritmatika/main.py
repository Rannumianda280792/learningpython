#operator Aritmatika


#penjumalah + 
a=3
b=5
c=a+b
print(a,"+",b," = ", c)

#pengurangan -
c=a-b
print(a,"-",b," = ", c)

#perkalian *
c=a*b
print(a,"*",b," = ", c)

#pembagian /
c=a/b
print(a,"/",b," = ", c)

#eksponen(pangkat) **
c=a**b
print(a,"**",b," = ", c)

#Modolus (sisa Bagi) %
c=a%b
print(a,"%",b," = ", c)

#floor Devision (pembulatan kebawah) //
c=a // b
print(a,"//",b," = ", c)

#prioritas operasi atau operational precendence
'''
1. () 
2. Eksponen **
3. perkalian dan teman-teman * / % //
4. penjumlahan dan teman-teman + -
'''

x=3
y=2
z=4
hasil = x ** y * z + x / y - y % z // x
print(x ,"**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x,"=", hasil)

hasil=x + y * z
print(x, " + ", y, "*", z, "=", hasil)

# kurung di prioritas pertama
hasil=(x + y) * z
print("(",x, " + ", y,")", "*", z, "=", hasil)