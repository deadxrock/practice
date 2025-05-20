# Базовий клас для бібліотечних елементів
from seaborn import load_dataset


class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.is_borrowed = False

    def borrow_item(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.item_id}, Title: {self.title}, Status: {status}")

# Похідний клас Книга
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Book - ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

# Похідний клас Журнал
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number, publication_date):
        super().__init__(item_id, title)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Magazine - ID: {self.item_id}, Title: {self.title}, "
              f"Issue: {self.issue_number}, Date: {self.publication_date}, Status: {status}")

# Клас Читача
class Reader:
    def __init__(self, reader_id, name):
        self.reader_id = reader_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item: LibraryItem):
        if item.is_borrowed:
            print(f"Item '{item.title}' is already borrowed.")
            return False
        if item.borrow_item():
            self.borrowed_items.append(item)
            print(f"Item '{item.title}' successfully borrowed by {self.name}.")
            return True
        return False

    def return_item(self, item: LibraryItem):
        if item in self.borrowed_items:
            if item.return_item():
                self.borrowed_items.remove(item)
                print(f"Item '{item.title}' successfully returned by {self.name}.")
                return True
        else:
            print(f"Item '{item.title}' was not borrowed by {self.name}.")
        return False

    def display_info(self):
        print(f"\nReader ID: {self.reader_id}, Name: {self.name}")
        print("Borrowed Items:")
        if not self.borrowed_items:
            print("  No borrowed items.")
        for item in self.borrowed_items:
            item.display_info()
if __name__ == "__main__":
    # Створення елементів
    book = Book(1, "1984", "George Orwell")
    magazine = Magazine(2, "Science Today", "202", "2024-05")

    # Створення читача
    reader = Reader(1001, "Ira Rost")
    reader.borrow_item(book)
    reader.borrow_item(magazine)

    # Відображення
    reader.display_info()
