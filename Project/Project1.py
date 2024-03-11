#create a CLT TO DO application. User should able to add task, view task, mark the task as completed and remove the task 
#Choose task: 
# 1. Add task
# 2. View task
# 3. Remove task
Choose = int(input("Enter your choice:"))

match Choose:
    case 1:
        print("Add task")
    case 2:
        print("View task")
    case 3:
        print("Remove Task")
    case _:
        print("Exist")
while Choose == 1:
    print("Enter a tsak ")
    break