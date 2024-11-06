print("Welcome to the To-Do List Manager!")

Task_list = []

def display_menu():
    print("\n1. Add new task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Save tasks")
    print("5. Mark task as complete")
    print("6. Load saved tasks")
    print("7. Exit")

def Add_Task():
    New_task = input("Enter a new task: ")
    Task_list.append(New_task)   
    print("Task added.")

def View_Task():
    if not Task_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(Task_list):
            print(f"{index + 1}. {task}")

def delete_Task():
    if not Task_list:
        print("No tasks found.")
        return
    View_Task()
    try:
        delete_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= delete_index < len(Task_list):
            deleted_item = Task_list.pop(delete_index)
            print(f"'{deleted_item}' was deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def save_Task():
    if not Task_list:
        print("No tasks to save.")
        return
    with open("file.txt", "w") as f:
        for ind, task in enumerate(Task_list):
            f.write(f"{ind + 1}. {task}\n")
    print("Tasks saved successfully.")

def load_save_Task():
    try:
        with open("file.txt", "r") as f:
            Task_list.clear()
            for line in f:
                Task_list.append(line.strip())
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found.")

def Mark_complete():
    if not Task_list:
        print("No tasks found.")
        return
    View_Task()
    try:
        task_complete = int(input("Choose a task number to mark as complete: ")) - 1
        if 0 <= task_complete < len(Task_list):
            Task_list[task_complete] += " ✔"
            print(f"Task {task_complete + 1} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    display_menu()
    try:
        user_input = int(input("Choose an option: "))
        if user_input == 1:
            Add_Task()
        elif user_input == 2:
            View_Task()
        elif user_input == 3:
            delete_Task()
        elif user_input == 4:
            save_Task()
        elif user_input == 5:
            Mark_complete()
        elif user_input == 6:
            load_save_Task()
        elif user_input == 7:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 7.")
    except ValueError:
        print("Invalid input. Please enter a number.")
