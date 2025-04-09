from datetime import datetime
def save_note():
    note = input("Write your note: ").strip()
    if note == "":
        print("No Note, Please try again!")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp}\n{note}\n" + "_"*60 + "\n"

    with open("journal.text", "a") as file:
        file.write(entry)
    print("Your note has been saved")

def view_note():
    try:
        with open("journal.text", "r") as file:
            content = file.read()

        if content.strip() == "":
            print("No note found yet")
        else:
            print("\nAll Notes:\n")
            print(content)
    except FileNotFoundError:
        print(" No note found yet please write note first.")

while True: 
    print("List Note")
    print("1. Add note")
    print("2. View note")
    print("3. Exit")

    choice = input("Enter your choice").strip()
    if choice == "1":
        save_note()
    elif choice == "2":
        view_note()
    elif choice == "3":
        print("Bye")
        break
    else: 
        print("choice 1 to 3 please")



            




