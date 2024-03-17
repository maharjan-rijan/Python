#create a CLT TO DO application. User should able to add task, view task, mark the task as completed and remove the task 
#Choose task: 
# 1. Add task
# 2. Make as Completed
# 3. View task
# 4. Remove task
# 5. Exit
#========================================================================================================================#
#initialize empty todos to store todo items
toDoList = [] 
while True:
    print("\nToDo List Manager:")
    print("1. Add Task")
    print("2. Mark as completed")
    print("3. View Tasks")
    print("4. Remove Task")
    print("5. Exit\n")
    
    choice = input("Enter your choice (1-5):")
    
    if choice == '1':
        task_name = input("Enter the task name:")
        task = {
            'task_name' : task_name,
            'is_completed' : False,
        }
        toDoList.append(task)
        print("Task Added Succesfully.")
    elif choice == '2':
        task_index = int(input("Enter Task index:"))
        toDo_item = toDoList[task_index]
        toDo_item['is_completed'] = True
    elif choice == '3':
        if len(toDoList > 0):
            for index, task in enumerate(toDoList):
                print(f"{index+1}.{task['task_name']} - {'Completed ✔️' if task['is_completed'] else 'Not Completed ❌'} ")
        else:
            print("You haven't added task yet.")
    elif choice == '4':
        task_index = int(input("Enter Task index:"))
        if len(toDoList) < task_index:
            print('Invalid task range')
        else:
            toDo_item = toDoList.pop(task_index)
            print("Task Removed Succesfully.")
    elif choice == '5':
        print("Program Exit.")
        break