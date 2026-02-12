#Task 1: __str__ and __repr__

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Price: {self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"


b1 = Book("Python Basics", "John", 500)
b2 = Book("OOP Concepts", "Alice", 700)

print(b1)
print([b1, b2])


#Task 2: __eq__

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model


m1 = Mobile("Apple", "iPhone 15", 80000)
m2 = Mobile("Apple", "iPhone 15", 85000)
m3 = Mobile("Samsung", "S24", 70000)

print(m1 == m2)
print(m1 == m3)


#Task 3: __new__ and __init__

class User:
    def __new__(cls, *args, **kwargs):
        print("Object is being created")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print("Object is initialized")


u1 = User("Uday")


#Task 4: __enter__ and __exit__

class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Database Closed")


with DatabaseConnection():
    print("Performing Query...")


#Task 5: __call__

class Calculator:
    def __call__(self, a, b):
        return a + b


obj = Calculator()
print(obj(10, 20))


#Task 6: __getitem__ and __setitem__

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value


cart = ShoppingCart(["Shirt", "Shoes", "Watch"])
print(cart[0])

cart[1] = "New Shoes"
print(cart.items)

#Task 7: __del__

class Session:
    def __del__(self):
        print("Session Ended")


obj = Session()
del obj


#Task 8: __contains__

class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books


library = Library(["Python", "Java", "C++"])
print("Python" in library)


#Task 9: __gt__ and __lt__

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary


e1 = Employee("A", 50000)
e2 = Employee("B", 60000)

print(e1 > e2)
print(e1 < e2)


#Task 10: __iter__ and __next__

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


for i in Counter(1, 5):
    print(i)

#Task 11: __getitem__ and __setitem__