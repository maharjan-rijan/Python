# Continue to ask for input until the user enters number greater than 20
while True:
    number = int(input("Enter a number:"))
    if number > 20:
        print("You have entered valid input.✅")
        break
    else:
      print("Invalid input.❎")
    