#Create a phonebook using python dictionary named 'phonebook' with at least 5 key-value pairs. Each key should represent person's name and each value should represent phone numbers.
phonebook = {
    'Rijan' : 9866283218,
    'Ram' : 9818488364,
    'Sita' : 9840173379,
    'Sunaina' : 9875035745,
    'Laxman' : 9874034006,
}
#1. Print the phonebook
print(phonebook)
#2. Add new item to the phonebook
phonebook['Hari'] = 980456678
print(phonebook)
#3. Update the phonebook of one of the person
u = phonebook.update({'Sita': 9880173379})
#4. Print the phonebook
print(phonebook)
#5. Print the values of phonebook using for loop
for key, value in phonebook.items():
    print(f"{key} = {value}")
