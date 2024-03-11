# Find sum of even numbers from 1 to 10 using while loop.
#2+4+6+8+10
i = 0
sum = 0
while i <= 10:
    if i%2 == 0:
        sum = sum + i
    i = i+1
print(f"Sum = {sum}")