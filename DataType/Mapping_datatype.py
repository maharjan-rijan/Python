# Dictonary DataType
phonebook = {
    'Rijan' : 9866283218,
    'Rachit' : 9800574663,
    'Sunaina': 9877854335
}
phonebook1 = dict(name="Rijan Maharjan", age = 20)
# m = phonebook['Rijan']
# print(m)
# g = phonebook.get('Sunaina')
# print(g)
# print(type(phonebook))
# print(phonebook)
# print(phonebook.keys())
#Loop
# for x in phonebook:
    #for keys and value
    # print(f"{x} = {phonebook.get(x)}")
    #for value
    # print(phonebook.get(x))
    
for key, value in phonebook.items():
    print(f"{key} = {value}")
print(phonebook1)
