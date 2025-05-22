# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
#  Ezra Feyissa, 05/21/2025, Assignment05 script
# ------------------------------------------------------------------------------------------ #

#setup section 

import json as js


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
#csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
# file = open(FILE_NAME, "r")
# for row in file.readlines():
#     # Transform the data from the file
#     student_data = row.split(',')
#     student_data = [student_data[0], student_data[1], student_data[2].strip()]
#     # Load it into our collection (list of lists)
#     students.append(student_data)
# file.close()

try:

    file = open(FILE_NAME, 'r')
    students = js.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exit before running this script!\n")
    print("Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("--Technical Error Message --")
    print(e, e.__doc__, type(e), sep = '\n')
finally:
    if file.closed == False:
        file.close()



# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain number.")
            student_last_name = input("What is the student's last name?")
        except student_last_name.isalpha():
                raise ValueError("The last name should not contain number.")

        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName":course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            message = '{} {} is enrolled in {}'
            print(message.format(student ['FirstName'] , student['LastName'],student ['CourseName']))
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            js.dump(students, file)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep = "\n")
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
        # for student in students:
        #     csv_data = f"{student[0]},{student[1]},{student[2]}\n"
        #     file.dump(students)
        # file.close()
            print("The following data was saved to file!")
            print("-" * 50)
            for student in students:
                message = '{} {} is enrolled in {}'
                print(message.format(student ['FirstName'] , student['LastName'],student ['CourseName']))
            continue

    # Stop the loop
    elif menu_choice == "4":
        print("Program Ended")
        break  # out of the loop
else:
    print("Please only choose option 1, 2, 3, or 4")


