import time
class Library:
    books = []
    no_of_books = 0
    file_path = ''
    def __init__(self,file_name):
        self.file_path = file_name
    def add_book(self,b_name,writer,user_name):
        if b_name in self.books:
            print('Book already exists')
        else:
            current_time = time.strftime('%H : %M : %S')
            self.books.append(b_name)
            self.no_of_books += 1
            with open(self.file_path,'a') as file:
                file.write('Book added\n')
                file.write(f'Book name : {b_name}    Writer : {writer}    Add by : {user_name}   Time : {current_time}\n\n')
                print('Book added successfully')
                file.close()
    
    def show_available_books(self):
        if(len(self.books) != 0):
            print(f'Total no of books : {self.no_of_books}')
            print('Books available are : ',self.books)
        else:
            print('Library is empty')

    def issue_book(self,b_name,writer,user_name):
        if b_name in self.books:
            current_time = time.strftime('%H : %M : %S')
            self.books.remove(b_name)
            self.no_of_books -= 1
            with open(self.file_path,'a') as file:
                file.write('Book issued\n')
                file.write(f'Book name : \'{b_name}\'    Writer : {writer}    Issued by : {user_name}   Time : {current_time}\n\n')
                print('Book issued successfully')
                file.close()
        else:
            print(f'Book name : \'{b_name}\' doesn\'t exists')

central_library = Library('central.txt')
diploma_library = Library('diploma.txt')

print('Welcome to library management system'.center(50))
library_choice = 1
while(library_choice != 0):
    print('Select library account')
    print('[1] -> Diploma Library\n[2] -> Central Library')
    library_choice = int(input('Your choice : '))
    match library_choice:
        
        case 1:
            print('Diploma library selected')
            op = 1
            while(op != 0):
                print('[1] -> Add book','[2] -> Show Available books','[3] -> Issue book','[4] -> Back <-',sep='\n')
                op = int(input('Your choice : '))
                match op:
                    case 1:
                        b_name = input('Enter book name : ').strip()
                        writer = input('Enter Writer name : ').strip()
                        user_name = input('Enter Your name : ').strip()
                        diploma_library.add_book(b_name,writer,user_name)
                    case 2:
                        diploma_library.show_available_books()
                    case 3:
                        b_name = input('Enter book name : ').strip()
                        writer = input('Enter Writer name : ').strip()
                        user_name = input('Enter Your name : ').strip()
                        diploma_library.issue_book(b_name,writer,user_name)
                    case 4:
                        op = 0

                    case _:
                        print('Invalid input')
        case 2:
            print('Central library selected')
            op = 1
            while(op != 0):
                print('[1] -> Add book','[2] -> Show Available books','[3] -> Issue book','[4] -> Back <-',sep='\n')
                op = int(input('Your choice : '))
                match op:
                    case 1:
                        b_name = input('Enter book name : ').strip()
                        writer = input('Enter Writer name : ').strip()
                        user_name = input('Enter Your name : ').strip()
                        central_library.add_book(b_name,writer,user_name)
                    case 2:
                        central_library.show_available_books()
                    case 3:
                        b_name = input('Enter book name : ').strip()
                        writer = input('Enter Writer name : ').strip()
                        user_name = input('Enter Your name : ').strip()
                        central_library.issue_book(b_name,writer,user_name)    

                    case 4:
                        op = 0        
                    case _:
                        print('Invalid input')
        case _:
            print('Invalid input')
                





