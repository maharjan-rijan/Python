#Write a program to get a number from user and check if a given number is odd or even. If the number is even, 
# Print "The number is even" otherwise "The number is odd"
number = int(input('Enter any number = '))
if(number%2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")