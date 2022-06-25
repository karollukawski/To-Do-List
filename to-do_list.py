def show_tasks():
    print()

def add_task():
    print()

def delete_task():
    print()


while True:
    print ()
    print ("0. Show all tasks")
    print ("1. Add a task")
    print ("2. Delete a task")
    print ("3. Exit")

    choice = int(input ("Choose option:"))

    if choice == 0:
        show_tasks()
    if choice == 1:
        add_task()
    if choice == 2:
        delete_task()
    if choice == 3: 
        break
    else:
        break