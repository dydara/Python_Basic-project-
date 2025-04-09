from datetime import datetime

def add_note():
    note = input("📝 Write your note: ").strip()

    if note == "":
        print("⚠️ Note is empty. Try again.")
        return

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Combine note with time
    entry = f"{timestamp}\n{note}\n" + "-"*40 + "\n"

    # Save to a text file
    with open("journal.txt", "a") as file:
        file.write(entry)

    print("✅ Your note has been saved!\n")
