tasks = []

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to delete a task
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully!")
    else:
        print("Invalid task number. Please try again.")

# Function to mark a task as completed
def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number. Please try again.")

# Function to display tasks
def display_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. [{status}] {task['task']}")

# Main function
def main():
    while True:
        print("\n---- To-Do List ----")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            index = int(input("Enter the number of the task to delete: ")) - 1
            delete_task(index)
        elif choice == "3":
            index = int(input("Enter the number of the task to mark as completed: ")) - 1
            mark_completed(index)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

# Entry point of the program
if __name__ == "__main__":
    main()
