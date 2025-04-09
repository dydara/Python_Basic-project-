import os
import json
from datetime import datetime

class ContactBook:
    def __init__(self, folder="data", filename="contacts.json"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.filename = os.path.join(folder, filename)
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, first_name, last_name, phone, email, company=None, telegram=None, whatsapp=None):
        contact = {
            "id": len(self.contacts) + 1,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "company": company,
            "telegram": telegram,
            "whatsapp": whatsapp,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"✅ Contact '{first_name} {last_name}' added successfully!")

    def view_contacts(self):
        print("\n📓 Contact List:")
        print("-" * 60)
        if not self.contacts:
            print("⚠️ No contacts found.")
            return

        for contact in self.contacts:
            first_name = contact.get("first_name", "")
            last_name = contact.get("last_name", "")
            full_name = f"{first_name} {last_name}".strip()

            print(f"{contact['id']}. {full_name} | 📞 {contact['phone']} | ✉️ {contact['email']} | 🕒 Created: {contact['created_at']}")

            if contact.get("company"):
                print(f"   🏢 Company: {contact['company']}")
            if contact.get("telegram"):
                print(f"   🟦 Telegram: {contact['telegram']}")
            if contact.get("whatsapp"):
                print(f"   🟩 WhatsApp: {contact['whatsapp']}")
        print("-" * 60)

    def search_contacts(self, keyword):
        print(f"\n🔍 Search results for: '{keyword}'")
        print("-" * 60)
        found = False
        for contact in self.contacts:
            full_name = f"{contact.get('first_name', '')} {contact.get('last_name', '')}".lower()
            if keyword.lower() in full_name:
                print(f"{contact['id']}. {full_name.title()} | 📞 {contact['phone']} | ✉️ {contact['email']}")
                found = True
        if not found:
            print("⚠️ No contact found with that name.")
        print("-" * 60)

    def delete_contact(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"🗑 Contact '{contact['first_name']} {contact['last_name']}' deleted successfully!")
                return
        print("⚠️ Contact ID not found!")

# Run the app
if __name__ == "__main__":
    cb = ContactBook()

    while True:
        print("\n📇 Contact Book Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ").strip()

        if choice == "1":
            first_name = input("First name: ").strip()
            last_name = input("Last name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            company = input("Company (optional): ").strip()
            telegram = input("Telegram (optional): ").strip()
            whatsapp = input("WhatsApp (optional): ").strip()

            cb.add_contact(first_name, last_name, phone, email, company, telegram, whatsapp)

        elif choice == "2":
            cb.view_contacts()

        elif choice == "3":
            keyword = input("Enter name to search: ").strip()
            cb.search_contacts(keyword)

        elif choice == "4":
            try:
                contact_id = int(input("Enter contact ID to delete: "))
                cb.delete_contact(contact_id)
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == "5":
            print("👋 Goodbye! See you next time.")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")
