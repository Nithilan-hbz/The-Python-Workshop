import os

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.read().splitlines()
    return tasks

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)

def view_tasks(tasks):
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to remove: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
    else:
        print("Invalid task number.")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks, filename)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
