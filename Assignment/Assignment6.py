#Create a python program that takes two integer number as input and determines the larger one, If they are equal,
#Print"Both are equal" otherwise print one is greater than other
number1 = int(input('Enter first number = '))
number2 = int(input('Enter second number = '))
if(number1 > number2):
    print(f"{number1} is greater than {number2}.")
elif(number2 > number1):
    print(f"{number2} is greater than {number1}.")
else:
    print("Both number are equal.")