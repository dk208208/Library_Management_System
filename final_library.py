from datetime import datetime,timedelta
import time
class library:
   
    purpose = 'To help student to study!'
    remaining_times = {}
    student_book_history = {}
    list_of_books =[]
    details_of_bookid = {}
    list_of_borrower ={}
    count = 2000
    list3=[]
    admin_sign_up_dict = {}

   
    def __init__ (self):
        print('--------------------------------Welcome! to PHYTHON library---------------------------')
       

    def admin_sign_up(self):        
        print("Please Enter Details To Log-In")
        self.username = str(input("Enter Username: "))
        self.password = str(input("Enter Password: "))
        if self.username not in library.admin_sign_up_dict:
            library.admin_sign_up_dict[self.username] = self.password
        else:
            print("Username already used. Please! Try Again.")
        print("Sign-up successfully")
        self.input = str(input("Press>> 1. For sign-in \nPress>> 2. For Home\n           "))
        if self.input == "1":
            self.admin_login()
        else:
            self.home()  
     
    def recall(self):
        self.admin_login()
    def admin_login(self):
        self.username= input("for login, Enter Your Username: ")
        while self.username not in library.admin_sign_up_dict:
            print("Username does not found in database.\n Make sure you have signed up ")
            self.option = input("Press>> 1. for re-enter username.\nPress>> 2. for sign up\n")
            if self.option == "1":
                self.recall()
            elif self.option == "2":
                self.admin_sign_up()
                self.recall()          
        self.password = str(input("Enter your password: "))  
        while self.password != library.admin_sign_up_dict[self.username]:
            self.password = str(input("Invalid password \n Please enter correct password: "))                  
        print("Admin Login is Successful")  
        self.admin_option()
             
    def books_catalogue(self):
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
       
        for p_id, p_info in library.details_of_bookid.items():
            print("\nBook ID:", p_id)
            for key in p_info:
                print(key + ':', p_info[key])
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)        
        self.dash()
     
    def books_catalogues(self):
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
       
        for p_id, p_info in library.details_of_bookid.items():
            print("\nBook ID:", p_id)
            for key in p_info:
                print(key + ':', p_info[key])
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)        
        self.admin_option()
               
    def book_details(self):
        self.book_id = int(input("Enter Book-Id: "))
        if self.book_id in library.details_of_bookid:
            for p_id, p_info in library.details_of_bookid.items():
                print("\nBook ID:", p_id)
            for key in p_info:
                print(key + ':', p_info[key])
        else:
            print('Enter Valid Book-Id. \n Try again')
            self.book_details()
                                   
    def add_books(self):
        library.count += 1
        self.book_id = library.count
        self.dict1 = {}
        self.name = input("Enter The Book Name: ").upper()
        self.dict1['Name']=self.name
        self.book_title = input("Enter The Book Title: ")
        self.dict1['Book Title']=self.book_title
        self.author_name = input("Enter The Author Name: ")
        self.dict1['Author Name']=self.author_name
        self.publish_year = input("Enter Published Year")
        self.dict1['Published Year'] = self.publish_year
        self.total_pages = input("Enter Total Pages: ")
        self.dict1['Total Pages']=self.total_pages
        self.no_of_copies = int(input("Enter Number of Copies: "))
        self.dict1['Number of Copies'] = self.no_of_copies
        self.isbn = input("Enter 13 Digit Unique ISBN")
        self.dict1['ISBN']= self.isbn
       
        library.details_of_bookid[self.book_id] = self.dict1
        print("Book has been added.")
        print(" If you want to add more press key 'M' otherwise press any key ")
        self.input = input().upper()
        if self.input=='M':
            self.add_books()
        else:
            print("Thank u ! \n We have list of books shown below. ")
            for p_id, p_info in library.details_of_bookid.items():
                print("\nBook ID:", p_id)
                for key in p_info:
                    print(key + ':', p_info[key])
        library.count += 1                                        
        self.admin_option()
                 
    def remove_book(self):
        self.booki_d = int(input("Enter Book-Id you want to remove: "))
        if self.booki_d in self.details_of_bookid:
            del self.details_of_bookid[self.booki_d]
            print(f"\n{self.booki_d} has been removed.")
            print("\nAvailable Book's Details Given Below:~~~~~\n ")
            for p_id, p_info in library.details_of_bookid.items():
                print("\nBook ID:", p_id)
                for key in p_info:
                    print(key + ':', p_info[key])
        else:
            print("\nEnter valid Book-ID\n")
            self.admin_option()
        self.admin_option()
       
    def borrower_details(self):
        self.full_name = input("\n Enter the Full Name :   ").upper()
        self.DOB = input("\nEnter the date of birth: ")
        self.contact_no = input("\nEnter the contact number: ")
        self.email = input("\nEnter the Email:     ")
        self.password = input("Create your password: ")
        self.gender = input("\n Gender: ").upper()
        self.dict2 = {}
        self.dict2['Name'] = self.full_name
        self.dict2['Date of Birth'] = self.DOB
        self.dict2['Contact number'] = self.contact_no
        self.dict2['Email'] = self.email
        self.dict2['Password'] = self.password
        self.dict2['Gender'] = self.gender
        self.issued_book = None
        self.dict2['Bookid'] = {}
        student_registeration.login_details[self.email] = self.password
        print(f"Borrower's Username: {self.email}\nBorrower's Password: {student_registeration.login_details[self.email]}")
        library.list_of_borrower[self.email] = self.dict2
        print("\n-----------------------\nYou have added borrower Successfully")
        self.admin_option()

    def borrower_details1(self):
        self.full_name = input("\n Enter the Full Name :   ").upper()
        self.DOB = input("\nEnter the date of birth: ")
        self.contact_no = input("\nEnter the contact number: ")
        self.email = input("\nEnter the Email:     ")
        self.password = input("Create your password: ")
        self.gender = input("\n Gender: ").upper()
        self.dict2 = {}
        self.dict2['Name'] = self.full_name
        self.dict2['Date of Birth'] = self.DOB
        self.dict2['Contact number'] = self.contact_no
        self.dict2['Email'] = self.email
        self.dict2['Password'] = self.password
        self.dict2['Gender'] = self.gender
        self.dict2['Bookid'] = {}
        student_registeration.login_details[self.email] = self.password
        library.list_of_borrower[self.email] = self.dict2
        print("\nStudent registration successful")
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)
        print(".\n.")
        time.sleep(1)    
        self.dash()        

    def add_lend_book(self):
        self.issue_time= datetime.now()
        self.email = input("\nEnter Email: ")
        if self.email in library.list_of_borrower:
            self.lend_bookid = int(input("\nEnter the Book_Id you want to lend: "))
            if self.lend_bookid in library.details_of_bookid:
                library.list_of_borrower[self.email]['Bookid'][self.lend_bookid]= {"Issue Date":None,"Return Time":None}
                self.time1 = time.asctime(time.localtime(time.time()))
                if self.email not in library.remaining_times:
                    library.remaining_times[self.email] = {}
                    library.remaining_times[self.email][self.lend_bookid] = {"Issue Date":None,"Return Time":None,"Remaining Time":None}
                else:
                    library.remaining_times[self.email][self.lend_bookid] = {"Issue Date":None,"Return Time":None,"Remaining Time":None}
                if library.details_of_bookid[self.lend_bookid]['Number of Copies'] > 0 :
                    library.list_of_borrower[self.email]['Bookid'][self.lend_bookid]["Issue Date"] = self.time1
                    library.remaining_times[self.email][self.lend_bookid]["Issue Date"] = self.time1
                    library.details_of_bookid[self.lend_bookid]['Number of Copies'] -= 1
                    print(f"\n{self.lend_bookid} has been lended to {self.email}")
                   
                    self.remaintime()
                    self.timeduration = self.issue_time + timedelta(days=14)
                    self.timediff= self.timeduration-self.remain_time
                    if self.timediff != 0:
                        library.remaining_times[self.email][self.lend_bookid]["Remaining Time"] = self.timediff
                        print("--------------------")
                    else:
                        library.remaining_times[self.email][self.lend_bookid]["Remaining Time"] = "No Time Left"
                else:
                    print("\nBook is out of stock\n")
                    self.admin_option()
            else:
                print("\n!!!Invalid Book-Id!!!")
                self.admin_option()
        else:
            print(f"\n{self.email} is not registered.!!!")
            self.admin_option()
    def st_book_his(self):
        self.st_bk = input("Enter Your Email: \n")
        for i in library.student_book_history[self.st_bk]:
            print(i)
        self.dash()    
       
    def remaintime(self):
        self.remain_time01 = time.asctime(time.localtime(time.time()))
        self.remain_time = datetime.now()      

    def borrower_history_detail(self):
        self.email = input("Enter your email-id: ")
        if self.email in library.list_of_borrower:
            for p_id, p_info in library.list_of_borrower[self.email].items():
                print( p_id,":", p_info)
        else:
            print("enter correct email")
            self.borrower_history_detail()
   
    def books_history(self,email):
        self.email = email
        self.dict3 = {}
        self.bookname = str(input("Enter book name: "))
        self.list3.append(self.bookname)
        self.dict3['Book Name'] = self.list3
        self.lend_books[self.email] = self.dict3        
           
    def return_book(self):
        self.st_email =input("\n Enter student'email")
        self.book_id = int(input("\nEnter Book-Id you want to return: "))
        self.return_time = datetime.now()
        self.returntime = time.asctime(time.localtime(time.time()))
        library.list_of_borrower[self.st_email]['Bookid'][self.book_id]['Return Time'] = self.returntime
        self.timeduration = self.issue_time + timedelta(days=14)
        self.timediff= self.timeduration- self.return_time
        if (self.return_time - self.issue_time >  self.timediff) is False:
            library.details_of_bookid[self.book_id]['Number of Copies'] += 1
            del self.list_of_borrower[self.st_email]['Bookid'][self.book_id]
            print("Book return successful")
            print("The book you have to return given below>>>")
            print(library.list_of_borrower[self.st_email]['Bookid'])
            self.admin_option()
        else:
            print("You have to pay 100 Rs.")
            self.admin_option()

# ============================================================================================================================

class student_registeration(library):
    login_details = {}
   
    def __init__(self):
        print('         --------------------------------Welcome! to library---------------------------')
        self.remain_time = datetime.now()
        self.home()
   
    def home(self):    
        self.input5 = input("\n====================Home========================\n\nPress>> 1. For Admin \nPress>> 2. For Student\n\n================")
        if self.input5 == "1":
            print("------------------------------------Admin portal-----------------------------------------------")
            self.input6 = input("\nPress>> 1. For sign_up \nPress>> 2. For sign_in\nPress>> 0. Home \n--------------")
            if self.input6 == "1":
                self.admin_sign_up()
            elif self.input6 == "2":
                self.admin_login()
            elif  self.input6 == "0":
                self.home()
            else:
                print("Due to incorrect input we are transferring to home\n ")
                self.home()
               
        elif self.input5 =="2":
            print("------------------------------------Student portal-----------------------------------------------")
            input4 = input("\nPress>> 1. For sign_up \nPress>> 2. For sign_in\nPress>> 0. Home\n --------------")
            if input4 == "2":
                self.student_login()
            elif input4 == "1":
                time.sleep(1)
                self.borrower_details1()
                print("\n==>Enter details for sign up.")
            elif input4 == "0":
                self.home()
            else:
                print("\n.\n.\n.????   Invalid---Number   ????\n.\n.\n.  ")
                print("Due to incorrect input we are transferring to home\n ")
                self.home()
        else:
            print("\n.????   Invalid---Number   ????\n.  ")
            self.home()
#         ---------------------------------------sign up---------------------------------------------------

    def student_login(self):
        print("\n==>Enter details for sign_in.\n")
        self.email = input("enter Email: ")
        self.password =input("enter password: ")
        if self.email in self.login_details:
            if  self.login_details[self.email]==self.password:
                print(" Student Login Successfully")
            else:
                print("\n!!!!!!!!email or password does not match!!!!!!")
                self.home()
        else:
            print("\n!!!!!!!!!!email or password does not match!!!!!!!!")
            self.student_login()
        self.dash()

    def dash(self):
        print("--------------------------------------------Student Portal----------------------------------------------")
        print("\nPress>> 1.     Book lists")
        print("\nPress>> 2.     Lend books history ")
        print("\nPress>> 0.     Home")
        self.dash1()
    def st_error(self):
        print("!!!!!  Enter valid input !!!!!!!")
        self.dash1()
    def dash1(self):
        self.input3 = input("\n")
        if self.input3 == "1":
            self.books_catalogue()
            self.dash()
        elif self.input3 == "0":
            self.home()
        elif self.input3 == "2" :
            try:  
                self.in222 = input("------------Email")
                self.remaintime()
                for i in library.remaining_times[self.in222]:
                    print(f"Book-ID: {i}\n")
                    print(library.details_of_bookid[i])
                    print(library.remaining_times[self.in222])
            except:
                print("\nThere is no book you have borrowed\n")
            finally:
                self.dash()
        else:
            self.st_error()
            self.dash()
           
    def admin_option(self):
        print("------------------------------------Admin portal-----------------------------------------------")
        self.admin_portal1()
    def admin_error(self):
        print("!!!!!   Enter valid input  !!!!!!!")
        self.admin_portal1()    
    def admin_portal1(self):
        self.input7 =input("Press>> 1.    Add Book\n \nPress>> 2.    Add Student in borrower list\n \nPress>> 3.    Remove Books\n \nPress>> 4.    Lend Book\n \nPress>> 5.    Return Book\n \nPress>> 6.    Available Book List\n\nPress>> 0.    Home\n      ")
        if self.input7 == "1":
            self.add_books()
        elif self.input7 == "2":
            self.borrower_details()
        elif self.input7 == "3":
            self.remove_book()
        elif self.input7 == "4":
            self.add_lend_book()
        elif self.input7 == "5":
            self.return_book()
        elif self.input7 == "6":
            self.books_catalogues()
        elif self.input7 == "0":
            self.home()
        else:
            self.admin_error()
        self.admin_portal1()    
#  -----------------------------------------COMPLETED-------------------------------------------------------    

scout = student_registeration()
