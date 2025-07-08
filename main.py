from quantum_bookstore import Book, Inventory

class QuantumBookstoreFullTest:
    @staticmethod
    def run():
        try:
            inventory = Inventory()

            # Add paper book
            paper_book = Book("ISBN123", "The Paper Trail", "John Doe", "paper", 2016, 100)
            inventory.add_book(paper_book)

            # Add ebook
            ebook = Book("ISBN456", "Digital Depths", "Alice Smith", "ebook", 2025, 50)
            inventory.add_book(ebook)

            # Add showcase book
            showcase_book = Book("ISBN789", "Timeless Demo", "Mark Twain", "showcase", 1962, 200)
            inventory.add_book(showcase_book)

            # Remove outdated books
            removed_books = inventory.remove_outdated_books(2010)
            for book in removed_books:
                print(f"Quantum book store: Removed outdated book: {book.get_title()} ({book.get_publication_year()})")

            # Buy paper book
            paper_price = inventory.buy_book("ISBN123", 2, "customer@email.com", "Giza")
            print(f"Quantum book store: Amount paid for paper book: {paper_price}")

            # Buy ebook
            ebook_price = inventory.buy_book("ISBN456", 1, "customer@email.com", "Giza")
            print(f"Quantum book store: Amount paid for eBook: {ebook_price}")

            # Attempt to buy showcase book
            inventory.buy_book("ISBN789", 1, "customer@email.com", "Alhram")

        except Exception as e:
            print(e)

# Run the test
if __name__ == "__main__":
    QuantumBookstoreFullTest.run()
