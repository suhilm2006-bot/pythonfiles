from collections import deque

tasks = deque()


def add_task():
    task = input("Enter task: ")
    print("Task added.")
    
def execute_task():
    
    if not tasks:
        print("No tasks available.")
    else:
        task = tasks.popleft()
        print("Executing:",task)
        
def view_tasks():
    
    if not tasks:
        print("No tasks.")
        
    else:
        print("Pending tasks:")
        
        for task in tasks:
            print("-",task)
            
while True:
    
    print("\n--- TASK SCHEDULER ---")
    print("1. Add Task")
    print("2. Execute Task")
    print("3. View Task")
    print("4. exit ")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_task()
        
    elif choice == "2":
        execute_task()
        

    elif choice == "3":
        view_tasks()

    elif choice == "4":
        break