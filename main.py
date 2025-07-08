class Book:
    def __init__(self, isbn, title, type_, publication_year, price):
        self.isbn = isbn
        self.title = title
        self.type = type_
        self.publication_year = publication_year
        self.price = price
        self.stock = 10  # Default stock for paper books

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def get_title(self):
        return self.title

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
            print(f"Shipping book to {target}")
        elif method == "email":
            print(f"Sending eBook to {target}")


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


# ------------------ Test Cases ------------------

def run_test_cases():
    try:
        inventory = Inventory()

        # Add paper book
        paper_book = Book("ISBN123", "dummyname", "paper", 2016, 100)
        inventory.add_book(paper_book)

        # Add ebook
        ebook = Book("ISBN456", "dummyaswell", "ebook", 2025, 50)
        inventory.add_book(ebook)

        # Add showcase book
        showcase_book = Book("ISBN789", "helloWorld", "showcase", 1962, 200)
        inventory.add_book(showcase_book)

        inventory.remove_outdated_books(2010)

        # Buy paper book
        paper_price = inventory.buy_book("ISBN123", 2, "aya.ahmed8760@gmail.com", "6 October")
        print(f"Amount paid for paper book: {paper_price}")

        # Buy ebook
        ebook_price = inventory.buy_book("ISBN456", 1, "aya.ahmed8760@gmail.com", "6 October")
        print(f"Amount paid for eBook: {ebook_price}")

        # Buy showcase book (will raise an exception)
        inventory.buy_book("ISBN789", 1, "aya.ahmed8760@gmail.com", "Alhram")

    except Exception as e:
        print(e)


# Run the main program
if __name__ == "__main__":
    run_test_cases()
