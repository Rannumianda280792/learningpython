#latihahn logika dan komperasi
#soal No.1
#-------0+++++5------8+++++11-----
print('Soal 1-> #-------0+++++5------8+++++11-----')
InputUser=float(input('masukan angka : '))

IsLebihDari_0=(InputUser>0)
print('lebih dari 0  = ' , IsLebihDari_0)
IsKurangDari_5=(InputUser<5)
print('Kurang dari 5 = ' , IsKurangDari_5)
iscorect0_5=IsLebihDari_0 and IsKurangDari_5
print('lebih dari 0 dan kurang dari 5 = ' ,iscorect0_5)

IsLebihDari_8=(InputUser>8)
print('lebih dari 8   = ' , IsLebihDari_8)
IsKurangDari_11=(InputUser<11)
print('Kurang dari 11 = ' , IsKurangDari_11)
iscorect8_11=IsLebihDari_8 and IsKurangDari_11
print('lebih dari 8 dan kurang dari 11 = ' ,iscorect8_11)


print('angka yang anda masukan adalah ', iscorect0_5 or iscorect8_11)

print('\n',10*'=','\n')

#soal No.2
#+++++0----5+++++8----11+++++
print('soal 2 -> +++++0----5+++++8----11+++++')
InputUser=float(input('masukan angka : '))

IskecilDari_0=(InputUser<0)
print('kecil dari 0  = ' , IskecilDari_0)

IsLebihDari_5=(InputUser>5)
print('Lebih dari 5 = ' , IsLebihDari_5)
IskurangDari_8=(InputUser<8)
print('kurang dari 8   = ' , IskurangDari_8)
iscorect5_8=IskurangDari_8 and IsLebihDari_5
print('lebih dari 5 dan kurang dari 8 = ' ,iscorect5_8)

IsLebihDari_11=(InputUser>11)
print('Lebih dari 11 = ' , IsLebihDari_11)



print('angka yang anda masukan adalah ', IskecilDari_0 or iscorect5_8 or IsLebihDari_11)
print('\n')
