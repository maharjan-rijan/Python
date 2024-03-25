
# Function with input and switch case
num1 = int(input("Input The first number:"))
num2 = int(input("Input The second number:"))
def numberCalculate(num1, num2)->None:
    sum = num1 + num2
    different = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    choice = int(input("Enter any number:"))
    match choice:
        case 1:
            print(f"The sum is {sum}")
        case 2:
            print(f"The difference is {different}")
        case 3:
            print(f"The multiplication is {multiplication}")
        case 4:
            print(f"The division is {division}")
        case _:
            print("Unable to perform Calculation")
numberCalculate(num1, num2)