# 📘 File Operator — Smart Journal Manager

*A Python project that turns simple text files into a personal digital diary.*

---

## 🌟 Why This Project Is Different?

Most file-handling projects only **read and write text**.
This project is designed like a **mini real-world application** that demonstrates:

* 🧠 **Object-Oriented Programming (OOP)**
* 📂 **File management**
* ⚠️ **Exception handling**
* 🔎 **Search functionality**
* 🗑️ **Safe deletion system**
* 🕒 **Automatic timestamps**

Think of it as a **personal journal + file operator** combined into one Python program.

---

# 🚀 Project Snapshot

| Feature           | Description                                  |
| ----------------- | -------------------------------------------- |
| ✍️ Add Entry      | Save a new journal note                      |
| 📖 View Entries   | Read all saved notes                         |
| 🔍 Search         | Find notes by keyword or date                |
| 🗑️ Delete        | Remove the journal safely                    |
| ⚠️ Error Handling | Prevent crashes from invalid file operations |
| 🧱 OOP Design     | All operations managed through a class       |

---

# 🧭 Folder Layout

```text
FileOperator/
│
├── journal_manager.py
├── journal.txt
└── README.md
```

---

# ⚙️ Technologies Used

```python
Python 3.x
os module
datetime module
Exception Handling
OOP (Classes & Objects)
Text File Handling
```

---

# 🧱 Program Architecture

```text
        ┌────────────────────┐
        │   Main Menu (UI)   │
        └─────────┬──────────┘
                  │
        ┌─────────▼──────────┐
        │   JournalManager   │
        └─────────┬──────────┘
                  │
     ┌────────────┼────────────┐
     │            │            │
     ▼            ▼            ▼
 Add Entry   View/Search   Delete File
```

---

# 🖥️ Menu Preview

```text
===== SMART JOURNAL MANAGER =====

1 ➜ Add New Entry
2 ➜ View All Entries
3 ➜ Search Entry
4 ➜ Delete All Entries
5 ➜ Exit

Choose an option:
```

---

# 📌 Core Methods

## ✍️ Add Entry

```python
def add_entry(self):
```

* Opens the file in **append mode (`a`)**
* Adds the current **date & time**
* Saves the user’s note permanently

---

## 📖 View Entries

```python
def view_entries(self):
```

* Opens the file in **read mode (`r`)**
* Displays all journal content
* Handles missing file errors gracefully

---

## 🔍 Search Entry

```python
def search_entry(self):
```

* Searches line by line
* Works with **keywords** or **dates**
* Shows only matching results

---

## 🗑️ Delete Entries

```python
def delete_entries(self):
```

* Asks for **user confirmation**
* Deletes `journal.txt`
* Prevents accidental data loss

---

# 📂 File Modes Explained

| Mode | Purpose                               |
| ---- | ------------------------------------- |
| `r`  | Read existing file                    |
| `w`  | Create/overwrite file                 |
| `a`  | Append new content                    |
| `x`  | Create file only if it does not exist |

### Example

```python
with open("journal.txt", "a") as file:
    file.write(entry)
```

---

# 🛡️ Exception Handling

This project demonstrates professional error handling:

```python
try:
    with open(self.filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Journal file not found")

except PermissionError:
    print("Permission denied")
```

### ✔️ Handles

* `FileNotFoundError`
* `PermissionError`
* Invalid user input
* Unexpected runtime errors

---

# 🕒 Sample Journal Output

```text
[2026-08-06 21:30:12]
Today I learned Python file handling.

[2026-08-06 21:45:03]
Implemented OOP and exception handling successfully.
```

---

# ▶️ How To Run

### Step 1 — Open VS Code

Open the project folder.

### Step 2 — Run the program

```bash
python journal_manager.py
```

---

# 🧪 Example Session

```text
Choose an option: 1

Write your journal entry:
Learning Python is becoming interesting!

✔ Entry added successfully.
```

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

* ✅ Creating and using **classes**
* ✅ Working with **instance methods**
* ✅ Reading and writing **text files**
* ✅ Using different **file modes**
* ✅ Implementing **menu-driven applications**
* ✅ Writing **robust exception-safe code**

---

# 💡 Future Improvements

You can upgrade this project by adding:

* 🔐 Password protection
* 🌙 Dark-mode terminal UI
* 📅 Date-wise filtering
* 📤 Export to PDF
* 🗃️ Multiple journal files
* 🖼️ GUI using **Tkinter**

---

# 🏁 Conclusion

**Smart Journal Manager** is more than a beginner file-handling program.
It combines **Python OOP, file operations, exception handling, and a user-friendly menu system** into a structured mini application.

This project is ideal for:

* 🎓 **College practicals**
* 💻 **Python assignments**
* 📚 **OOP demonstrations**
* 🧪 **File handling practice**
* 🚀 **GitHub portfolio projects**

---

# 👨‍💻 Author

**Kush Kumar**

*Python Learner | AI Developer Aspirant | Exploring OOP & File Handling with Python*

---

⭐ *If you found this project useful, consider giving it a star on GitHub!*
