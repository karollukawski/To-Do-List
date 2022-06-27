from typing import List

choice = -1

tasks = []

def show_tasks():
    tasks.append("Do shopping")
    tasks.append("Clean the desk")
    print(tasks)

def add_task():
    print()

def delete_task():
    print()


while choice != 4:
    print ()
    print ("0. Show all tasks")
    print ("1. Add a task")
    print ("2. Delete a task")
    print ("3. Save changes in the file")
    print ("4. Exit")

    choice = int(input ("Choose option: "))

    if choice == 0:
        show_tasks()
    if choice == 1:
        add_task()
    if choice == 2:
        delete_task()
    if choice == 3: 
        print()
    if choice == 4:
        break