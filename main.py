class Book:
    def __init__(self, isbn, title, author, type_, publication_year, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.type = type_
        self.publication_year = publication_year
        self.price = price
        self.stock = 10  # default stock for paper books
        self.filetype = "PDF" if self.type == "ebook" else None

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def get_publication_year(self):
        return self.publication_year

    def is_outdated(self, threshold_year):
        return self.publication_year < threshold_year

    def buy(self, quantity, email, address):
        if self.type == "paper":
            if self.stock < quantity:
                raise Exception("Quantum book store: Not enough stock.")
            self.stock -= quantity
            DeliveryService.send("shipping", address)
            return self.price * quantity

        elif self.type == "ebook":
            DeliveryService.send("email", email)
            return self.price * quantity

        elif self.type == "showcase":
            raise Exception("Quantum book store: This book is not for sale.")

        else:
            raise Exception("Quantum book store: Unknown book type.")


class DeliveryService:
    @staticmethod
    def send(method, target):
        if method == "shipping":
            print(f"Quantum book store: Shipping book to {target}")
        elif method == "email":
            print(f"Quantum book store: Sending eBook to {target}")
        else:
            print(f"Quantum book store: Unknown delivery method to {target}")


class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_outdated_books(self, threshold_year):
        removed_books = []
        self.books = [book for book in self.books if not (
            book.is_outdated(threshold_year) and removed_books.append(book)
        )]
        return removed_books

    def buy_book(self, isbn, quantity, email, address):
        for book in self.books:
            if book.get_isbn() == isbn:
                return book.buy(quantity, email, address)
        raise Exception(f"Quantum book store: Book with ISBN {isbn} not found.")


class QuantumBookstoreFullTest:
    @staticmethod
    def run():
        try:
            inventory = Inventory()

            # Add a paper book
            paper_book = Book("ISBN123", "The Paper Trail", "John Doe", "paper", 2016, 100)
            inventory.add_book(paper_book)

            # Add an eBook
            ebook = Book("ISBN456", "Digital Depths", "Alice Smith", "ebook", 2025, 50)
            inventory.add_book(ebook)

            # Add a showcase book (not for sale)
            showcase = Book("ISBN789", "Timeless Demo", "Mark Twain", "showcase", 1962, 200)
            inventory.add_book(showcase)

            # Remove outdated books (before 2010)
            removed = inventory.remove_outdated_books(2010)
            for book in removed:
                print(f"Quantum book store: Removed outdated book: {book.get_title()} ({book.get_publication_year()})")

            # Buy a paper book
            price1 = inventory.buy_book("ISBN123", 2, "client@email.com", "Giza")
            print(f"Quantum book store: Amount paid for paper book: {price1}")

            # Buy an eBook
            price2 = inventory.buy_book("ISBN456", 1, "client@email.com", "Giza")
            print(f"Quantum book store: Amount paid for eBook: {price2}")

            # Try to buy a showcase book (will raise error)
            inventory.buy_book("ISBN789", 1, "client@email.com", "Alhram")

        except Exception as e:
            print(e)


# Run the test
if __name__ == "__main__":
    QuantumBookstoreFullTest.run()

