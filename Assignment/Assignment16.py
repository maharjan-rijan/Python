# Write a python program that ask two number and a arthimatic operation 
# (+, -, *, /) from user can on the basic of the arithmetic operation provided by the 
# user, calculate its value. To calculate and print its value,create function for 
# each operations. Use keyword argument to call the function.

def numberCalculate(num1, num2)->None:
    choice = input("Enter any Operation:")
    if choice == "+":
        sum = num1 + num2
        print(f"The sum is {sum}")
    elif choice == "-":
        difference = num1 - num2
        print(f"The difference is {difference}")
    elif choice == "*":
        multiplication = num1 * num2
        print(f"The multiplication is {multiplication}")
    elif choice == "/":
        division = num1 / num2
        print(f"The division is {division}")
    else:
        print("Arithmetic Operation Cannot performe.")
numberCalculate(num1 = 4, num2 = 6)