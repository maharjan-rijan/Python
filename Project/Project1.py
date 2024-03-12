#create a CLT TO DO application. User should able to add task, view task, mark the task as completed and remove the task 
#Choose task: 
# 1. Add task
# 2. View task
# 3. Remove task

todolist=[]
while True:
    print("TODO list:")
    print("Enter 1 to add list: ")
    print("Enter 2 to complete added list: ")
    print("Enter 3 to display list: ")
    print("Enter 4 to remove list: ")
    print("Enter 5 to exit list: ")
    choice=int(input("enter choice: "))
    if choice==1:
        x = input("Enter task: ")
        todolist.append(x)
        print(f"{x} successfully added")
    elif choice == 2:
        x = input("Enter task to complete: ")
        if x in todolist:
            todolist.remove(x)
            print(f"{x} successfully completed")
        else:
            print(f"{x} task not found")
    elif choice==3:
            print(todolist[x])
    elif choice==4:
        x = input("Enter task to complete: ")
        if x in todolist:
            todolist.remove(x)
            print(f"{x} successfully removed")
        else:
            print(f"{x} not found to remove")
    elif choice==5:
        print("list completed ready to exist: ")
        break
    else:
        print("Invalid choice")