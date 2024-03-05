#Create a python program that check if a given number is divisible by 3 and 5. If it is divisible by both, print "The number is divisible by both 3 and 5" otherwise print "The number is divisible by both 3 and 5"
numb = int(input('Enter any number = '))
if(numb%3 == 0 and numb%5==0):
    print (f"The number {numb} is divisible by both 3 and 5.")
else:
     print (f"The number {numb} is not divisible by both 3 and 5.")