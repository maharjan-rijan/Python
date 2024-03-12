#create a CLT TO DO application. User should able to add task, view task, mark the task as completed and remove the task 
#Choose task: 
# 1. Add task
# 2. Make as Completed
# 3. View task
# 4. Remove task
# 5. Exist
#========================================================================================================================#
#initialize empty todos to store todo items
toDoList = [] 
while True:
    print("\nToDo List Manager:")
    print("1. Add Task")
    print("2. Mark as completed")
    print("3. View Tasks")
    print("4. Remove Task")
    print("5. Exist\n")
    
    choice = input("Enter your choice (1-5):")
    
    if choice == '1':
        task_name = input("Enter the task name:")
        task = {
            'task_name' : task_name,
            'is_completed' : False,
        }
        toDoList.append(task)
        print("Task Added Succesfully")