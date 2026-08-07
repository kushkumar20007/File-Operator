# 📘 File Operator — Smart Journal Manager

*A Python-based personal journal application using File Handling, OOP, and Exception Handling.*

---

## 🎯 Project Objective

This project is designed to create a **menu-driven journal management system** where users can store and manage their personal notes in a text file.

### ✅ Main Objectives

* Understand **file handling operations** (`read`, `write`, `append`, `create`)
* Learn the difference between **`r`, `w`, `a`, and `x` file modes**
* Perform **input and output operations** using text files
* Handle errors using **exception handling**
* Apply **Object-Oriented Programming (OOP)** concepts
* Build a **menu-driven console application**
* Store entries with **automatic timestamps**

---

## 🌟 Key Features

| Feature            | Description                             |
| ------------------ | --------------------------------------- |
| ✍️ Add Entry       | Save a new journal note                 |
| 📖 View Entries    | Display all saved entries               |
| 🔍 Search Entry    | Search by keyword or date               |
| 🗑️ Delete Entries | Remove all entries safely               |
| ⚠️ Error Handling  | Prevent program crashes                 |
| 🧱 OOP Structure   | Uses a dedicated `JournalManager` class |

---

## 🧱 OOP Structure

```python
class JournalManager:
    def add_entry(self):
        pass

    def view_entries(self):
        pass

    def search_entry(self):
        pass

    def delete_entries(self):
        pass
```

### 📌 Object Used

```python
manager = JournalManager()
```

The **object `manager`** is responsible for calling all journal operations:

```python
manager.add_entry()
manager.view_entries()
manager.search_entry()
manager.delete_entries()
```

This demonstrates the **object creation and method invocation** required in OOP.

---

## 📂 Project Structure

```text
FileOperator/
│
├── journal_manager.py
├── journal.txt
└── README.md
```

---

## ⚙️ Technologies Used

* **Python 3**
* **OOP (Classes & Objects)**
* **File Handling**
* **Exception Handling**
* **datetime module**
* **os module**

---

## 🖥️ Menu Preview

```text
===== SMART JOURNAL MANAGER =====

1 ➜ Add New Entry
2 ➜ View All Entries
3 ➜ Search Entry
4 ➜ Delete All Entries
5 ➜ Exit
```

---

## 📂 File Modes

| Mode | Purpose            |
| ---- | ------------------ |
| `r`  | Read file          |
| `w`  | Write / overwrite  |
| `a`  | Append new content |
| `x`  | Create a new file  |

---

## 🛡️ Exception Handling

```python
try:
    with open(self.filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Journal file not found")

except PermissionError:
    print("Permission denied")
```

---

## 🕒 Sample Output

```text
[2026-08-06 22:10:30]
Today I learned Python OOP and File Handling.
```

---

## ▶️ Run the Program

```bash
python journal_manager.py
```

---

## 🎓 Learning Outcomes

After completing this project, you will be able to:

* Create **classes and objects**
* Use **instance methods**
* Perform **file read/write operations**
* Implement **exception handling**
* Develop **menu-driven applications**
* Organize code using **OOP principles**

---

## 🏁 Conclusion

**Smart Journal Manager** is a simple yet powerful Python project that combines **File Handling, OOP, Exception Handling, and User Interaction** in a structured and practical way. It is suitable for **college practicals, assignments, and GitHub portfolio projects**.

---

## 👨‍💻 Author

**Kush Kumar**

*Python Learner | AI Developer Aspirant | Exploring OOP & File Handling with Python*

---

⭐ **If you found this project useful, give it a star on GitHub!**
