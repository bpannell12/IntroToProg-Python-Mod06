# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   Bryan Pannell, 5/22/2024, Developed Script
# ------------------------------------------------------------------------------------------ #
import json

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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ''    # Holds the choice made by the user.

# Define classes
class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This function reads the file data and extracts it into memory
        Parameters are:
            file_name: string for the file_name where the data is stored
            student_data: list of the student data to extract
            Return: student_data: list of the student data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="There was a problem with reading the file.", error=e)
        finally:
            if file.closed is False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function writes the data to the file
                Parameters are:
                    file_name: string for the file_name where the data is stored
                    student_data: list of the student data to save to the file
                Return: None
        """
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
            print("The following student registration data was saved to the file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            message = "There was a problem with saving data to the file.\n"
            message += "Please check that the file is open and being used by another program."
            IO.output_error_messages(message=message, error=e)
            if file.closed is False:
                file.close()
        finally:
            if file.closed is False:
                file.close()

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """This function writes the data to the file
            Parameters are:
                message: string to be displayed in the error message
                error: the error type
                Return: None
                """
        print(message, end="\n")
        if error is not None:
            print("-- An Error has Occurred --")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """This function displays the menu.
        Parameters are: the string for the menu"""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """This function returns the user's menu selection
           Parameters are:
                None
            Return: str choice - the user's selection from the menu
        """
        choice = "0"

        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """This function displays the data set
           Parameters are:
                student_data: list of dictionary data made up of the student data entered to display
            Return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets user input for the student's first name and last name, with a course name
            Parameters are:
                student_data: list of dictionary data made up of the student data entered to display
            Return: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="An error occurred because of an invalid entry data type.", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a technical error.", error=e)
        return student_data

# Main body
# Read and extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Display the menu and gather the user's menu selection
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Collect user input - menu option 1
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Display current data - menu option 2
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to the JSON file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop and end the script
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only enter a valid menu option.")

print("Program Ended")


