class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def verify_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Название должно быть строкой")
        if len(title) < 1 or len(title) > 100:
            raise ValueError("Название должно быть от 1 до 100 символов")

    def verify_author(self, author):
        if not isinstance(author, str):
            raise ValueError("Автор должен быть строкой")
        if len(author) < 3 or len(author) > 50:
            raise ValueError("Автор должен быть от 3 до 50 символов")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.verify_title(title)
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.verify_author(author)
        self.__author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __hash__(self):
        return hash((self.title, self.author))

# Пример использования
book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Brave New World", "Aldous Huxley")

# Сравнение книг
print(book1 == book2)  # True
print(book1 == book3)  # False

# Использование книги как ключ в словаре
book_dict = {book1: "Dystopian fiction"}
print(book_dict[book2])  # "Dystopian fiction", т.к. book1 и book2 считаются одинаковыми
