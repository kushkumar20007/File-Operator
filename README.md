## Personal Journal Manager (Python OOP Project)

A simple **menu-driven personal journal application** built using **Python**, **Object-Oriented Programming (OOP)**, **file handling**, and **exception handling**.

This project allows users to maintain a personal journal in a text file (`journal.txt`) with timestamped entries.

---

## Features

* Add a new journal entry
* View all journal entries
* Search entries by **keyword** or **date**
* Delete all journal entries with confirmation
* Automatic creation of `journal.txt`
* Timestamp added to every entry
* Handles file-related errors gracefully

---

## Technologies Used

* **Python 3**
* **OOP (Classes & Objects)**
* **File Handling**
* **Exception Handling**
* **Text Files (`.txt`)**

---

## Project Structure

```text
JournalProject/
│
├── journal_manager.py
├── journal.txt        # Auto-created
└── README.md
```

---

## File Handling Modes Used

| Mode | Purpose                                |
| ---- | -------------------------------------- |
| `x`  | Create a new file if it does not exist |
| `a`  | Append new journal entries             |
| `r`  | Read and display/search entries        |
| `w`  | Create an empty journal after deletion |

---

## How to Run

### 1. Open the project folder in **VS Code**

### 2. Open a terminal

```bash
Terminal → New Terminal
```

### 3. Run the program

```bash
python journal_manager.py
```

If `python` does not work:

```bash
python3 journal_manager.py
```

---

## Main Menu

```text
===== PERSONAL JOURNAL MENU =====
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

---

## Example Usage

### Add Entry

```text
Enter your choice (1-5): 1
Write your journal entry: Today I learned Python OOP.
```

### View Entries

```text
===== ALL JOURNAL ENTRIES =====

[2026-07-29 23:50:12]
Today I learned Python OOP.
----------------------------------------
```

---

## OOP Design

### Class: `JournalManager`

| Method                 | Description                 |
| ---------------------- | --------------------------- |
| `create_file()`        | Creates `journal.txt`       |
| `add_entry()`          | Adds a timestamped entry    |
| `view_entries()`       | Displays all entries        |
| `search_entry()`       | Searches by keyword or date |
| `delete_all_entries()` | Deletes all entries safely  |

---

## Exception Handling

The program handles:

* `FileNotFoundError`
* `PermissionError`
* Unexpected exceptions using `Exception as e`

This prevents the application from crashing due to invalid file operations or user input.

---

## Learning Objectives Demonstrated

* Reading and writing text files
* Appending data to files
* Creating files dynamically
* Searching through file contents
* Deleting and recreating files
* Using **classes, objects, constructors, and instance methods**
* Implementing **robust exception handling**

---

## Sample Output File (`journal.txt`)

```text
===== PERSONAL JOURNAL =====

[2026-07-29 23:50:12]
Today I learned Python OOP.
----------------------------------------

[2026-07-30 08:10:45]
Started working on my file handling project.
----------------------------------------
```

---

## Future Improvements

* Edit existing entries
* Store entries in **JSON** format
* Add password protection
* Create a **GUI version using Tkinter**
* Export entries to **PDF**

---

## Author

**Kush Kumar**

* Python Beginner
* Interested in **AI Development**, **Cyber Security**, and **Software Development**

---

## License

This project is created for **educational and learning purposes**. Feel free to modify and improve it for your own practice.

---

### Save this file as:

```text
README.md
```

Place it in the same folder as `journal_manager.py` and it will automatically be recognised by **GitHub** and **VS Code** as the project documentation.
