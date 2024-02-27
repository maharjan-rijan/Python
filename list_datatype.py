countries = [
    "Nepal","India","China","Japan"
]

print(type(countries))
print(countries[1:])
print(countries[0])

# append method
countries.append("America")
print(countries)

countries.insert(2,"Bhutan")
print(countries)

for country in countries:
    print(country)