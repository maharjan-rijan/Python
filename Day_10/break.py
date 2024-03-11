# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i = i + 1 

# Numbers = [ 4,67,6,5,8,12,65]
# Search 5 form the above numbers, is the number found prient "Number found" otherwise print "Number not found"
i = [4, 67,6,5,8,12,65 ]
Searching_number = int(input("Enter a number to search:"))
for number in i:
    if number == 5:
        print(f"Number {Searching_number} found")
        break
else:
    print(f"Number {Searching_number} not found")