#list -> array, mengambil data dengan index

data_list=['rannu','saras','shanum']

print(f"data list: %s" % data_list[1] +" type : ",type(data_list)) #data list: saras type :  <class 'list'>

#dictionary-> associative Array, mengambil data dengan identification
#identification -> key
data_dictionary={
    'key':'value',
    'rn': 'rannu',
    'sr': 'saras',
    'sh': 'shanum',
    'nmb':3,    
    'list': data_list
}
print (f"data dictionary[rn]: {data_dictionary['rn']}") #data dictionary[rn]: rannu
print (f"data dictionary[nmb]: {data_dictionary['nmb']}") #data dictionary[nmb]:3
print (f"data dictionary[list]: {data_dictionary['list']}") #data dictionary[list]: ['rannu', 'saras', 'shanum']
