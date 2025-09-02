import sys

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.total_books = 0
        self.total_price = 0
        self.issues = []
        
    def new_book(self, name, price):
        self.total_books += 1
        newBook = {
            "book_id": self.total_books,
            "book_name": name,
            "book_price": price
        }
        self.books.append(newBook)
        self.total_price += price
        
        print(f"New Book Procured:\n ID = {newBook['book_id']}\n Name = {newBook['book_name']}\n Price = {newBook['book_price']}")
        
    def new_user(self, name, user_id):
        newUser = {
            "user_id": user_id,
            "user_name": name
        }
        self.users.append(newUser)
        
        print(f"New User Registered:\n ID = {newUser['user_id']}\n Name = {newUser['user_name']}")
        
    def new_issue(self, book_id, user_id):
        f1 = 0
        f2 = 0
        for i, user in enumerate(self.users):
            if user['user_id'] == user_id:
                f1 = 1
                break
            
        if f1 == 0:
            print("Invalid Book Issue")
            return
            
        for i, book in enumerate(self.books):
            if book['book_id'] == book_id:
                f2 = 1
                issued_book = self.books.pop(i)
                newIssue = {
                    "user_id": user_id,
                    "book_id": issued_book['book_id']
                }
                self.issues.append(newIssue)
                break
                
        if f2 == 0:
            print("Invalid Book Issue")
            return
        else:
            print(f"New Book Issue:\n Book ID = {newIssue['book_id']}\n user ID = {newIssue['user_id']}")
            
    def display_records(self):
        print("Library Records\n===============")
        print("Total Books =", self.total_books)
        print("Total Users =", len(self.users))
        print("Total Price = Rs.", self.total_price)
        print("Total Issues =", len(self.issues), "\n")

def main():
    ob = Library()
    
    while True:
        ch = int(input("Enter:\n 1. Procure New Book\n 2. Register New User\n 3. Issue a Book\n 4. Exit\n"))
        match ch:
            case 1:
                while True:
                    name = input("Enter name of the book: ")
                    price = input("Enter price of the book: ")
                    
                    if name == "" or price == "":
                        break
                    ob.new_book(name, float(price))
                
                print("\nBooks Procured:")
                print(ob.books)
                ob.display_records()      
            case 2:
                while True:
                    name = input("Enter name of the user: ")
                    user_id = input("Enter ID of the user: ")
                    
                    if name == "" or user_id == "":
                        break
                    ob.new_user(name, int(user_id))
                
                print("\nUsers Registered:")
                print(ob.users)
                ob.display_records()
            case 3:
                while True:
                    book_id = input("Enter ID of the book: ")
                    user_id = input("Enter ID of the user: ")
                    
                    if book_id == "" or user_id == "":
                        break
                    ob.new_issue(int(book_id), int(user_id))
                
                print("\nBooks Issued:")
                print(ob.issues)
                ob.display_records()
            case 4:
                print("End of Program")
                sys.exit(0)
            case _:
                print("Wrong Choice!")

main()