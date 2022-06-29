from typing import List

choice = -1

tasks = []

def show_tasks():
    task_index = 0
    for task in tasks:
        print("[" + str(task_index) + "] " + task)
        task_index += 1

def add_task():
    task = input("Add task to list: ")
    tasks.append(task)
    print(task)
    print ()
    print ("Task added to list!")

def delete_task():
    task_index = int(input("Give the number of task to delete: "))
    if task_index < 0 or task_index > len(tasks) - 1:
        print ()
        print ("There are no tasks with that index")
        return
    tasks.pop(task_index)
    print ()
    print ("Task deleted from list!")

def save_task_t0_file():
    file = open ("To-Do_List.txt", "w")

while choice != 4:
    print ()
    print ("0. Show all tasks")
    print ("1. Add a task")
    print ("2. Delete a task")
    print ("3. Save changes in the file")
    print ("4. Exit")
    print ()

    choice = int(input("Choose option: "))

    if choice == 0:
        show_tasks()
    if choice == 1:
        add_task()
    if choice == 2:
        delete_task()
    if choice == 3: 
        save_tasks_to_file()
    if choice == 4:
        break