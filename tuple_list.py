import sys
fruit_list = ["Apple","Banana","Orange"] #List is mutiable data type which can changeable and can modify
fruit_tuple = ("Apple","Banana","Orange","Banana","Pineapple") #List is unmutiable data type which cannot change and cannot modify

print("List Memory Size",sys.getsizeof(fruit_list))
print("List Memory Size",sys.getsizeof(fruit_tuple))

count_Apple = fruit_tuple.count('Apple')
print(count_Apple)
print(fruit_tuple.count('Banana'))

index_fruit = fruit_tuple.index('Banana')
print(index_fruit)
