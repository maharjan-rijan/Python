#If customer by a product and if total price is greater than 1000, than give10% discount other. Print the
#discount value and the total amount to be paid.
amount = int(input('Enter the amount in number = '))
discount = 0

if (amount > 1000):
    discount = amount*10/100
print("Discount = ", discount)
print("Total amount to be paid = ", int(amount - discount))