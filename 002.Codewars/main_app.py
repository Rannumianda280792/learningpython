def fungsi(string):
    ubahjadilist=string.split(",")
    if len(ubahjadilist) >2:
        ubahjadilist.pop(0)
        ubahjadilist.pop()
        gabung=' '.join(ubahjadilist)

    else:
        gabung=print('')

        
    return gabung

hasil=fungsi("2,3,3,4,3")
print (hasil)

