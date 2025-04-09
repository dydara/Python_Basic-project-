import json
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        title = input("📝 Task title: ").strip()
        due_date = input("📅 Due date (YYYY-MM-DD): ").strip()

        # Validate date format
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
            return

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "due_date": due_date,
            "status": "pending"
        }

        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task '{title}' added successfully!")

# 🔹 Main menu loop
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n📋 Task Manager")
        print("1. Add Task")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            print("👋 Goodbye! Keep crushing your tasks.")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1 or 2.")
