# 📚 Quantum Bookstore System

A simple command-line **Bookstore Inventory Management System** written in **Python**, simulating various book types such as paper books, eBooks, and showcase items.

---

## 🚀 Features

- Add books to inventory with ISBN, title, author, type, year, and price.
- Remove outdated books based on a threshold year.
- Buy books by ISBN and quantity:
  - Paper books reduce stock and simulate shipping.
  - eBooks simulate email delivery.
  - Showcase books are not for sale and raise exceptions.

---

## 🧱 Book Types

- `paper`: Sold from stock and shipped to an address.
- `ebook`: Sent to an email address.
- `showcase`: Not for sale.

---

## 📦 Sample Output

```yaml
Quantum book store: Removed outdated book: Timeless Demo (1962)
Quantum book store: Shipping book to Giza
Quantum book store: Amount paid for paper book: 200
Quantum book store: Sending eBook to client@email.com
Quantum book store: Amount paid for eBook: 50
Quantum book store: This book is not for sale.
