'''write a library class with no_of_books and Books(list) as two instance variable.
write a program to create a library from this library class and show how can you print all books
add a books and get number of books using different method.'''

class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.Books = []
    
    def add_book(self, book):
        self.Books.append(book)
        self.noOfBooks +=1

    def show_Book(self):
        for i in self.Books:
            print(i)

    def check(self):
        if self.noOfBooks == len(self.Books):
            print("number of books are correct  ")
        else:
            print("number of books are not correct")

obj1 = Library()
obj1.add_book("History")
obj1.add_book("maths")
obj1.add_book("science")
obj1.add_book("physics")

obj1.show_Book()
obj1.check()
print(obj1.noOfBooks)


        