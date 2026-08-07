import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("Write your journal entry: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}] {entry}\n")

            print("Entry added successfully!\n")

        except Exception as e:
            print("Error while adding entry:", e)


    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

                if content.strip() == "":
                    print("Journal is empty.\n")
                else:
                    print("\n----- All Journal Entries -----")
                    print(content)

        except FileNotFoundError:
            print("No journal file found.\n")

        except Exception as e:
            print("Error while reading file:", e)

    def search_entry(self):
        keyword = input("Enter keyword or date to search: ")

        try:
            found = False

            with open(self.filename, "r", encoding="utf-8") as file:
                print("\n----- Search Results -----")

                for line in file:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

            if not found:
                print("No matching entries found.")

        except FileNotFoundError:
            print("Journal file does not exist.\n")

        except Exception as e:
            print("Error while searching:", e)

    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            try:
                if os.path.exists(self.filename):
                    os.remove(self.filename)
                    print("All entries deleted successfully!\n")
                else:
                    print("Journal file does not exist.\n")

            except Exception as e:
                print("Error while deleting file:", e)

        else:
            print("Deletion cancelled.\n")


def main_menu():
    manager = JournalManager()

    while True:
        print("\n===== Personal Journal Manager =====")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            manager.add_entry()

        elif choice == "2":
            manager.view_entries()

        elif choice == "3":
            manager.search_entry()

        elif choice == "4":
            manager.delete_entries()

        elif choice == "5":
            print("Thank you for using Journal Manager!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()