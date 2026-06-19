def todo_list():
    tasks = []
    print("--- Welcome to your To-Do List ---")
    
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Added: '{task}'")
            
        elif choice == '2':
            print("\nYour Tasks:")
            if not tasks:
                print("Your list is currently empty.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    todo_list()
