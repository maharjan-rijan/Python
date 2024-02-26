# Sequence DateType 
greeting = "Hello BernHardt"
# indexing 
print(greeting[0])
# Printing value using loop
for x in greeting:
    print(x)
# Length of string
greeting_length = len(greeting)

# Slicing
# Slicing with step
print(greeting[0:11:4])
# Starting String from certain position
print(greeting[6:greeting_length])
# Print String length
print(greeting_length)
# Reverse
print(greeting[::-1])
# Using Slice function
Slicing = slice(0, 11)
print(greeting[Slicing])