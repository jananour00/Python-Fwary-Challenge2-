
# 📚 Quantum Bookstore System

A simple command-line **Bookstore Inventory Management System** written in **Python**, simulating various book types such as paper books, eBooks, and showcase items.

This project is a Python adaptation of a Java-based bookstore system, featuring class-based design, purchase processing, outdated book filtering, and delivery simulation.

---

## 🚀 Features

- Add books to an inventory system
- Buy books by ISBN with validation
- Remove outdated books based on publication year
- Simulate delivery via email or shipping
- Exception handling for unsupported or invalid operations

---

## 🛠️ Requirements

- Python 3.6 or higher
- No external libraries required

---

## 🔄 How It Works

- Books are created with ISBN, title, type, publication year, and price.
- Book types:
  - **Paper books**: Require stock and simulate shipping
  - **eBooks**: Delivered via email
  - **Showcase books**: Not available for sale
- Outdated books can be removed if published before a threshold year.
- Attempting invalid actions raises descriptive exceptions.

---

## 🧪 Sample Output

Shipping book to 6 October
Amount paid for paper book: 200
Sending eBook to example@email.com
Amount paid for eBook: 50
Quantum book store: This book is not for sale.


## 📤 GitHub Upload Instructions

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/bookstore-project.git
git branch -M main
git push -u origin main
