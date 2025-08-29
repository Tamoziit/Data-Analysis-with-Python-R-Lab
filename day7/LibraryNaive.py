import sys

class Library:
    def __init__(self):
        self.total_books = 0
        self.total_users = 0
        self.total_price = 0
        self.total_issues = 0
        
    def new_book(self, name, price):
        self.total_books += 1
        self.total_price += price
        print(f"New Book procured:\n Name = {name}\n Price = {price}")
        
    def new_user(self, name, user_id):
        self.total_users += 1
        print(f"New User registered:\n Name = {name}\n ID = {user_id}")
        
    def issue_book(self, book_id, user_id):
        if (book_id > 0 and book_id <= self.total_books) and (user_id > 0 and user_id <= self.total_users):
            self.total_books -= 1
            self.total_issues += 1
            print(f"New Book Issue:\n Book ID = {book_id}\n user ID = {user_id}")
        else:
            print("Invalid Book Issue")
            
    def display_records(self):
        print("Library Records\n===============")
        print("Total Books =", self.total_books)
        print("Total Users =", self.total_users)
        print("Total Price = Rs.", self.total_price)
        print("Total Issues =", self.total_issues, "\n")
        
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
                    
                ob.display_records()      
            case 2:
                while True:
                    name = input("Enter name of the user: ")
                    user_id = input("Enter ID of the user: ")
                    
                    if name == "" or user_id == "":
                        break
                    ob.new_user(name, int(user_id))
                    
                ob.display_records()
            case 3:
                while True:
                    book_id = input("Enter ID of the book: ")
                    user_id = input("Enter ID of the user: ")
                    
                    if book_id == "" or user_id == "":
                        break
                    ob.issue_book(int(book_id), int(user_id))
                    
                ob.display_records()
            case 4:
                print("End of Program")
                sys.exit(0)
            case _:
                print("Wrong Choice!")

main()