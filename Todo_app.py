from datetime import datetime
import json
import os

class TodoList:
    def __init__(self, folder="data", filename="tasks.json"):
        # Create folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        self.filename = os.path.join(folder, filename)
        self.tasks = []
        self.load_tasks()

    def save_tasks(self):
        # Save all tasks to JSON file
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        # Load tasks from file if it exists
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def add_task(self, description):
        # Add a new task to the list
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task '{description}' added successfully!")

    def view_tasks(self):
        # Show all tasks or a message if none
        print("\n📌 Your To-Do List:")
        print("-" * 60)
        if not self.tasks:
            print("⚠️ No tasks available.")
        else:
            for task in self.tasks:
                status = "✔" if task['completed'] else "❌"
                print(f"{task['id']}. [{status}] {task['description']} (Created: {task['created_at']})")
        print("-" * 60)

    def mark_completed(self, task_id):
        # Mark a task as completed
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"✅ Task '{task['description']}' marked as completed!")
                return
        print("⚠️ Task ID not found!")

    def delete_task(self, task_id):
        # Delete a task by ID
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"🗑 Task '{task['description']}' deleted successfully!")
                return
        print("⚠️ Task ID not found!")

# -------------------------------
# 📋 Main App Loop
# -------------------------------

if __name__ == "__main__":
    todo = TodoList()

    while True:
        print("\n📋 To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo.mark_completed(task_id)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "5":
            print("👋 Exiting To-Do List. See you next time!")
            break

        else:
            print("⚠️ Invalid choice. Please enter 1–5.")
