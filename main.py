#Done By : Mousa M Salha -Palestine-

class Book:
    def __init__(self, title, publisher, isbn_10, isbn_13, edition, hardcover,year,month,paperback):
        self.title = title
        self.publisher = publisher
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        self.edition = edition
        self.hardcover = hardcover
        self.year = year
        self.month = month
        self.paperback =paperback
        self.num_copies = 1  # Set the number of copies to 1 for each new book

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"ISBN-10: {self.isbn_10}\n" \
               f"ISBN-13: {self.isbn_13}\n" \
               f"Publisher: {self.publisher}\n" \
               f"Edition: {self.edition}\n" \
               f"Hardcover: {self.hardcover}\n" \
               f"Year: {self.year}\n" \
               f"Month: {self.month}\n" \
               f"Paperback: {self.paperback}\n" \
               f"Number of Copies: {self.num_copies}\n"


class Library:
    def __init__(self, file_lms):
        self.file_lms = file_lms
        self.books = []
        self.archived = []

    def read_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('Title'):
                        current_book = Book(title=line.split(':')[1].strip(), publisher=None,
                                            isbn_10=None, isbn_13=None, edition=None, hardcover=None,year=None,month=None,paperback=None)
                    
                    elif line.startswith('ISBN-10'):
                        current_book.isbn_10 = line.split(':')[1].strip()
                    elif line.startswith('ISBN-13'):
                        current_book.isbn_13 = line.split(':')[1].strip()
                    elif line.startswith('Publisher'):
                        current_book.publisher = line.split(':')[1].strip()
                    elif line.startswith('Edition'):
                        current_book.edition = line.split(':')[1].strip()
                    elif line.startswith('Hardcover'):
                        current_book.hardcover = line.split(':')[1].strip()
                    elif line.startswith('Year'):
                        current_book.year = line.split(':')[1].strip()
                    elif line.startswith('Month'):
                        current_book.month = line.split(':')[1].strip()
                    elif line.startswith('Paperback'):
                        current_book.paperback = line.split(':')[1].strip()
                    
                    elif line == '':
                        self.books.append(current_book)
                        current_book = Book(title=None, publisher=None,
                                            isbn_10=None, isbn_13=None, edition=None, hardcover=None,year=None,month=None,paperback=None)

            if len(self.books) == 0:
                print("No books found in the file.")
        
        

        except FileNotFoundError:
            print("File not found or inaccessible.")
            

    def search_book(self,optional, parameter):
        search_list = []
        for book in self.books:
         if optional == 'title':
            if book.title  ==  parameter:
                search_list.append(book)
         elif optional == 'Isbn_13':
            if book.isbn_13  ==  parameter:
                search_list.append(book)
         elif optional == 'publisher':
            if book.publisher  ==  parameter:
                search_list.append(book)
         elif optional == 'isbn_10':
            if book.isbn_10  ==  parameter:
                search_list.append(book)
         elif optional == 'year':
            if book.year  ==  parameter:
                search_list.append(book)
         

        for book in search_list:
         print(book)


        option = input("Do You Want to save this result to file (search.txt) ?")
        if option == 'yes':
         if search_list:
          with open("search.txt", "w") as file:
            for book in search_list:
                file.write(str(book) + "\n")
            print("Search results saved to search.txt")
         else:
          print("No Books found to save the result !")
        else:
           print("the result did not save ")      
    
    def add_book(self, book):
        self.books.append(book)
        print("New book added successfully.")

    def remove_book(self,isbn_13):
        for book in self.books:
            if book.isbn_13 == isbn_13 :
             #self.books.remove(book)
                self.archived.append(book)
                print("book archived successfully")
                return
        print("book not found in the LMS ")

    def delete_book(self,isbn_13):
        for book in self.archived:
            if book.isbn_13 == isbn_13 :
             self.archived.remove(book)
             for book in self.books:
              if book.isbn_13 == isbn_13:
               self.books.remove(book)
             print("book deleted form LMS archive successfully")
             return
        print("book not found in the LMS ")

    def print_archived_books(self):
        if len(self.archived) == 0:
            print("No archived books found.")
        else:
            print("Archived Books:")
            for book in self.archived:
                print(book)

    def write_file(self):
     with open(self.file_lms, 'w') as file:
        for book in self.books:
            file.write('Title: ' + book.title + '\n')
            file.write('ISBN-10: ' + book.isbn_10 + '\n')
            file.write('ISBN-13: ' + book.isbn_13 + '\n')
            file.write('Publisher: ' + book.publisher + '\n')
            file.write('Edition: ' + (book.edition or '') + '\n')
            file.write('Hardcover: ' + (book.hardcover or '') + '\n')
            file.write('Year: ' + (book.year or '') + '\n')
            file.write('Month: ' + (book.month or '') + '\n')
            file.write('Paperback: ' + (book.paperback or '') + '\n')
            file.write('\n')

    def count_books(self):
     num_books = len(self.books)
     return num_books
    
    def count_unique_isbn_13(self):
     isbn_counts = {}
     for book in self.books :
        isbn_13 = book.isbn_13
        if isbn_13 in isbn_counts:
            isbn_counts[isbn_13] += 1
        else:
            isbn_counts[isbn_13] = 1

     num_unique_books = len(isbn_counts)
     print(isbn_counts)
     return num_unique_books
         
    def count_books_archived(self):
     num_books_archived = len(self.archived)
     return num_books_archived
    
    def count_year(self,year) :
        num_years = 0 
        for book in self.books:
            if book.year > year:
                num_years +=1 
        return num_years
    
    def book_dis_publisher(self,publisher):
        dis_publishers = []
        for book in self.books :
            if publisher == book.publisher:
               dis_publishers.append(book)

        for book in dis_publishers:
         print(book)
        
    def search_book_edit(self, isbn_13):
        for book in self.books:
            if book.isbn_13 == isbn_13:
                return book
        return None

    def book_dis_year(self,years):
        dis_years = []
        for book in self.books :
            if years == book.year:
               dis_years.append(book)

        for book in dis_years:
         print(book)

    def edit_book(self, isbn_13):
        book = self.search_book_edit(isbn_13)
        if book is None:
            print("Book not found.")
            return

        # Prompt the user to enter new book information
        print("Enter new book information:")

        title = input("Title: ")
        publisher = input("Publisher: ")
        isbn_10 = input("ISBN-10: ")
        isbn_13 = input("ISBN-13: ")
        edition = input("Edition: ")
        hardcover = input("Hardcover: ")
        year = input("Year: ")
        month = input("Month: ")
        paperback = input("Paperback: ")


        # Display the entered book information
        print("New Book Information:")
        print(f"Title: {title}")
        print(f"Publisher: {publisher}")
        print(f"ISBN-10: {isbn_10}")
        print(f"ISBN-13: {isbn_13}")
        print(f"Edition: {edition}")
        print(f"Year: {year}")
        print(f"Month: {month}")
        print(f"Paperback: {paperback}")
        

        # Prompt the user to confirm the changes
        confirmation = input("Do you want to save these changes? (yes/no): ")
        if confirmation.lower() != 'yes':
            print("Changes not saved.")
            return

        # Update the book attributes
        book.title = title
        book.publisher = publisher
        book.isbn_10 = isbn_10
        book.isbn_13 = isbn_13
        book.edition = edition
        book.hardcover = hardcover
        book.year = year
        book.month = month
        book.paperback = paperback

        # Save the changes to the file
        self.write_file()
        print("Changes saved successfully.")





def count_occurrences(lst, value):
     return lst.count(value)

def print_occurrences(isbn_13, books):
      occurrences = count_occurrences([book.isbn_13 for book in books], isbn_13)
      print(f"The ISBN-13 {isbn_13} appears {occurrences} times in the book library.")





file_lms = input("Enter the file LMS : ")
library = Library(file_lms)
library.read_file(file_lms)



while True:
        print('\U0001F4DA' + "Welcome to the Library Managment System" + '\U0001F4DA')
        print("Menu")
        print("1. Add a new book")
        print("2. Search for a book")
        print("3. Count occurrences of a specific ISBN-13 in LMS")
        print("4. Edit Book ")
        print("5. archive")
        print("6. delete")
        print("7. Generating reports about the books available in the LMS")
        print("8. Exit the Library")
        print()

        choice = input("Enter your choice : ")

        if choice == '1':
            file_name = input("Enter the file name: ")
            library.read_file(file_name)
            print("Books from the file have been added to the library.")
            library.write_file()

        elif choice == '2':
            optional = input("Enter the option you want to search by :: (isbn_13, title,isbn_10,publisher,year) ")
            parameter = input("Enter the parameter of the book to search : ")
            library.search_book(optional,parameter)
            

        elif choice == '3':
            isbn_13 = input("Enter the ISBN-13 to count occurrences: ")
            print_occurrences(isbn_13, library.books)

        elif choice == '4':
            isbn_13 = input("Enter the ISBN-13 of the book to edit: ")
            library.edit_book(isbn_13)

        elif choice == '5':
            isbn_13 = input("Enter the ISBN-13 of the book to remove and archive: ")
            library.remove_book(isbn_13)
            #library.write_file()
            ask = input("Do you want to print the archived books ?")
            if ask == 'yes':
             library.print_archived_books()
            else:
             print("the book not archived ")

        elif choice == '6':
            isbn_13 = input("Enter the ISBN-13 of the book to remove and archive: ")
            confirm = input("Do you want to confirm the removing ? ")
            if confirm =='yes':
            
             library.delete_book(isbn_13)
             library.write_file()
            else :
             print("The book not removed ")



        elif choice == '7':
            print("1.how many books are in the LMS ? ")
            print("2. how many different books are offered in the LMS  ?")
            print("3. the number of books archived in the LMS")
            print("4. how many books in the LMS are newer than a particular year ?")
            print("5. Book distribution by the publisher,")
            print("6. Books distribution by year.")


            option = input("Enter the option to print report : ")
            

            if option == '1':
             num_books = library.count_books()
             print(num_books)
            
            
            elif option == '2': 
             num_unique_books = library.count_unique_isbn_13()
             print(num_unique_books)

            elif option == '3':
                num_books_archived = library.count_books_archived()
                print(num_books_archived) 

            elif option == '4':
                year = input("Enter the Year to get the number of books newer than ")
                num_years = library.count_year(year) 
                print(num_years)

            elif option == '5':
                publisher = input("Enter the publisher to print the book distribution by the publisher ")
                library.book_dis_publisher(publisher) 
                
            elif option == '6':
                years = input("Enter the year to print the book distribution by the year ")
                library.book_dis_year(years)    

        
        elif choice == '8':
            ask = input("Do you want to exit the Library ?")
            if ask == 'yes':
             print("Thank You For using our Library "+'\U0001F600')
             library.write_file()
             break
            else :
             print()

        else:
            print("wrong choice ! Please try again." +'\U0001F614')

#Done By : Mousa M Salha -Palestine-


