#Write a python program that takes any number between 1 to 7 and print the week day 
#of that week day of that number using match statement.
number = int(input('Enter the amount in number = '))
match number:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Out of Range.")