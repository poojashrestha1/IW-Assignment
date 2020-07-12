'''Create a console application for an IT Academy with the
following features:
a) The academy program should have a fixed course of study.
b) If a new student is interested in the academy program the student can
inquiry about the course of study.
c) Student Registration with Rs. 20000 (deposit). Students are allowed to
pay in two installments with Rs. 10000 each.
d) Display all the student’s information from the academy with their payments
and remaining payments.
e) Update the student information if needed.
f) Delete the student information if he/she left the program.
g) Return the deposit amount (Rs. 20000) to the students after the
successful completion of the course and check the balance.
Remember it should be a full feature CONSOLE APP. You can store
the course of study and the student’s detail in your preferred file
format (.csv, .txt, etc).
Ignore the permissions for now. Anyone who runs the script is allowed to
access all the features. Develop the app with OOP Approach.'''

import csv
import sys
import os.path

class Course:

    def c_info():
        print("\n\nC programming is a general-purpose, procedural, imperative computer programming language developed in 1972 by Dennis M. Ritchie at the Bell Telephone Laboratories to develop the UNIX operating system. \nCis the most widely used computer language. \n \nThe course is 10 hours long! \n")

    def cplusplus_info():
        print("\n\nC++ is a cross-platform language that can be used to create high-performance applications. \nC++ was developed by Bjarne Stroustrup, as an extension to the C language. \nC++ gives programmers a high level of control over system resources and memory. \n\nThe course is 20 hours long! \n")

    def python_info():
        print("\n\nPython is an interpreted, high-level, general-purpose programming language. \nCreated by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. \n\nThe course is 25 hours long! \n")




class Student(Course):

    courses_available = ['c', 'C', 'C++', 'PYTHON', 'Python', 'python', 'c++']
    c = ['c', 'C']
    cplusplus = ['c++', 'C++']
    python = ['Python', 'python', 'PYTHON']
    agree = ['Yes', 'yes', 'YES']


    def student_info(self):


        name = input("\nName: ")
        address = input("Address: ")
        try:
            phone_number = int(input("Phone number: "))
        except ValueError:
            print("\nError.\n")
            self.main_menu()
        '''lines = list()

        with open('student_details.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row[2])
        if phone_number in lines: 
            print("\nAlready registered\n") #using the phone number as a primary ID
            self.main_menu()'''

        course = input("Course: ")
        if course in self.courses_available:
            pass
        else:
            print("\nInvalid Input. Please try again.\n")
            exit()
        print("\nYou need to deposit Rs. 20,000 for registration process. \nYou can pay in two installments as well. \n")
        payment_amount = input("Type 1 for Full pay \nType 2 for Installment: ")
        if payment_amount == '1':
            print("\nYou have decided to deposit Rs. 20,000.\n")
            payment_amount = 20000
            remaining_amount = 0

        elif payment_amount == '2':
            print("\nYou have decided to deposit Rs. 10,000. \n")
            payment_amount = 10000
            remaining_amount = 10000
        status = 'On progess'
        new_student = (name, address, phone_number, course, payment_amount, remaining_amount, status)
        return new_student
        self.main_menu()


    def display_info(self): 

        with open('student_details.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',', escapechar=' ', quoting = csv.QUOTE_NONE)
            for row in reader:
                print("\nName: ", row[0]) 
                print("Address: ", row[1]) 
                print("Phone number: ", row[2]) 
                print("Course: ", row[3])
                print("Paid: Rs.", row[4]) 
                print("Due: Rs.", row[5])
                print("Status: ", row[6])
        
        self.main_menu()

        

    def search_student(self, number): 
        with open('student_details.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if number == row[2]:
                    print("\nName: ", row[0]) 
                    print("Address: ", row[1]) 
                    print("Phone number: ", row[2]) 
                    print("Course: ", row[3])
                    print("Paid: Rs.", row[4]) 
                    print("Due: Rs.", row[5])
                    print("Status: ", row[6])
        
        self.main_menu()



    def delete_info(self, number): 
        
        lines = list()

        with open('student_details.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == number:
                        lines.remove(row)

        with open('student_details.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        print("\nDeleted")
        print('\nRemaining data: \n')
        self.display_info()


         
    def update_info(self, number, row, column, value): 
                
        r = csv.reader(open('student_details.csv')) # Here your csv file
        lines = list(r)
        row = int(row)
        column = int(column)
        
        if column == 4:
            value = int(value)
            lines[row][column] = value
            lines[row][column+1] = 20000 - value
        elif column == 6:
            lines[row][column] = "Graduated"
            lines[row][column-1] = "Refunded"
            lines[row][column-2] = "Refunded"

            with open('student_details.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

            self.search_student(number)
    
        else:
            lines[row][column] = value

        with open('student_details.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)




    def choices(self):        

        lines = list()

        with open('student_details.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row[2])
        
        choice = int(input("Enter choice: "))
        if(choice == 0):
            print("\nWe have C, C++ and Python.")
            selected = input("Which course would you like to know about? : ")
            if selected in self.c:
                Course.c_info()
            elif selected in self.cplusplus:
                Course.cplusplus_info()
            elif selected in self.python:
                Course.python_info()
            else:
                print(f"{selected} course is not available.")
                
            print("\nDo you want to register?")
            
            register = input("Please 'Yes' or 'No': ")
            
            if register in self.agree:
                new_student = self.student_info()
                with open('student_details.csv','a') as file:
                    writer = csv.writer(file)
                    writer.writerow(new_student)

                    print("Registration Successful")
                    self.main_menu()
            else:
                print("Sorry! Seems like you are not interested")
                exit()

            
        if(choice == 1):  
            new_student = self.student_info()
            with open('student_details.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow(new_student)
                print("Registration Successful") 


        elif(choice == 2):
            return self.display_info()


        elif(choice == 3): 

            num = input("Enter the phone number: ")
            if num in lines:
                return self.search_student(num)
            else:
                print("The record doesn't exist")


        elif(choice == 4): 

            num = input("Enter the phone number: ")
            if num in lines:
                return self.delete_info(num)
            else:
                print("The record doesn't exist")


        elif(choice == 5):
            print("\nIf provided option of main menu, please select 'No' if you want to update any data.")
            print("\nOur data are as follows: ")
            self.display_info()
            print("\nThe range starts from 0")
            
            number = input("\nEnter the phone number: ")
            if number in lines:
                row = input("Enter row you want to change:")
                col = input("Enter the column number you want to change \n0 Name \n1 Address \n2 Phone number \n3 Course \n4 Paid Amount \n5 Remaining Amount \n6 Course Status \n\nYour Input = ")
                val = input("Enter value to change: ")
                self.update_info(number,row, col, val)
                self.search_student(number)
                print("Updated.")
            else:
                print("Record doesn't exist.")
                self.main_menu()



    def beginning(self):
        print("\nPlease select: ") 
        print('\n0.See course details \n1.Register \n2.Display Details \n3.Search Details \n4.Delete Details \n5.Update Details \n') 
        self.choices()



    def main_menu(self):
        print("\nDo you want to go to the main menu? ")
        answer = input("Type 'yes' or 'no': ")
        if answer in self.agree:
            self.beginning()    
        else:
            print("\nThank you.")                   
                    
                
    

student_list = []
studentobj = Student()

print("\n\nWelcome to the IT Academy! \n\nThe courses avaiable are: C, C++ and Python.")

studentobj.beginning()
