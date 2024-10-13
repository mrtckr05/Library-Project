import sqlite3
import os
os.chdir("D:\\vscode-works\\PYTHON\\sqlite3")
print(os.getcwd())

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def create_tab():
    cursor.execute("CREATE TABLE IF NOT EXISTS my_library (Name TEXT, Author TEXT, Publisher TEXT, Page_Number INT)")
    con.commit()

create_tab()

def add_book(book_name, book_author, book_publisher, book_page_number):     
    cursor.execute("INSERT INTO my_library VALUES(?,?,?,?)",(book_name,book_author,book_publisher,book_page_number))
    con.commit()

print("Would you like to add a new book in your library ? ")
would_you = input("Yes or No Y/N: ")
if would_you == 'Y':
    book_name = input("Please write your name of the book: ")
    book_author = input("Please write your author of the book: ")
    book_publisher = input("Please write your publisher of the book: ")
    book_page_number = int(input("Please write your page number of the book: ")) 
    add_book(book_name, book_author, book_publisher, book_page_number)
elif would_you == 'N':
    pass


con.close()