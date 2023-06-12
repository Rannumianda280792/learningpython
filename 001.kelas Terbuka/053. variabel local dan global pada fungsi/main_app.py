# variabel Global dan local scope
nama_global = 'Rannu' #varibel global yang bida di akses pada fungsi, loop dan if statment 

def fungsi(): #varibel global untuk fungsi
    print(f" fungsi menampilkan {nama_global}") # fungsi menampilkan Rannu
    
fungsi()

#varibel global untuk loop
for i in range(0,5):
    print(f" loop ke- {i} - nama {nama_global}") 
    ''' loop ke- 0 - nama Rannu
        loop ke- 1 - nama Rannu
        loop ke- 2 - nama Rannu
        loop ke- 3 - nama Rannu
        loop ke- 4 - nama Rannu'''

if True:
    print(f" if menampilkan {nama_global}") #if menampilkan Rannu



#local scope
def local():
    nama_local='ucup'

local()
#print(nama_local) # tidak bisa di akses karena variabel dalam fungsi (local) di dalam fungsi name 'nama_local' is not defined.

#contoh penggunaan varibel global
# contoh 1
def say_hello():
    print(f"hallo {nama}")

nama="mianda" #deklarasi kan varibel global sebelum pemanggilan fungsi 
say_hello()
# nama="mianda" # name 'nama' is not defined

#contoh 2: merubah nilai variable global
angka=0
nama_personil='mianda Shanum'
def ubah_angka(nilai_baru,nama):
    global angka # untuk merubah varibel global maka kita akses dengen sintak Global
    global nama_personil
    nama_personil=nama
    angka=nilai_baru

print(f"sebelum {angka,nama_personil}") #sebelum (0, 'mianda Shanum')
ubah_angka(10,'shanum mianda')
print(f"setelah {angka,nama_personil}") #setelah (10, 'mianda Shanum')

# contoh 3 untuk for dan if bisa mengakses varibel local dan merubah nya

angka=0
for i in range(0,5):
    angka+=i
    angka_dummy=0
#angka_dummy bisa di akses di luar for padahal dia local varibel

print(f"{angka} dan {angka_dummy}") #10 dan 0

if True:
    angka=10
    angka_dummy=10
#angka_dummy bisa di akses di luar if padahal dia local varibel   
print(f"{angka} dan {angka_dummy}") # 10 dan 10

#kesimpulan nya global varibel dan local varibel berlaku pada function saja
