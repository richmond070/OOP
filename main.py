class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount ):
        self.balance += amount


a1 = BankAccount('Mike', 200)

a2 = BankAccount('Jude', 500)

a1.display()
a2.display()


class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(self.title)
        print(f"ISBN is {self.isbn}")
        print(f"Number of copies : {self.copies}")
        print(f"Prices : {self.price}")
        print('.' * 50)



book1 = Book('957-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', "XYZ", 500, 300, 5)

book1.display()
book2.display()
book3.display()


#check if their are available copies

def in_stock(self):
    return True if self.copies > 0 else False

#count the number of copies left

def sell(self):
    if self.in_stock():
        self.copies -= 1
    else:
        print('The book is out of stock')


books =[book1, book2, book3]

for book in books:
    book.display()

jack_books = [book.title for book in books if book.author == "jack"]

print (jack_books)


@property
def price(self):
    return self.price


@price.setter
def price(self, new_price):
    if 50 <= new_price <= 1000:
        self.price = new_price
    else:
        raise ValueError('price cannot be less than 10 or more than 500')