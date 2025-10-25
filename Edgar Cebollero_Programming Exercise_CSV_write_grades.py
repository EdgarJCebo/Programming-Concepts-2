#An instructor teaches a class in which each student takes three exams. The instructor would like to store this information
#in a file named grades.csv for later use. Create a program that allows an instructor to input how many students they
#want to enter. Then enter each student’s first name and last name as strings and the student’s three exam grades as
#integers. Use the csv module to write each record into the grades.csv file and have a header of First Name, Last Name,
#Exam 1, Exam 2 and Exam3. Each student should be a record in the grades.csv file.
#Once the file is created, create a separate program to read the grades.csv file and display the data in tabular format.
#Implement the with keyword. You may need to refer back to Chapter 5 for formatting.
#Each of these 2 programs should be separate functions so you have at least two functions for this assignment, but you can have more.

#csv import and filename
import csv

def write_grades_to_csv():
    filename = "grades.csv"

#Opens the file using the 'with' keyword
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

#Writes the header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

#Asks how many students to enter
        num_students = int(input("How many students would you like to enter? "))

#Loop for each student
        for i in range(num_students):
            print(f"\nEntering data for Student {i + 1}:")
            first_name = input("Please enter first name: ")
            last_name = input("Please enter last name: ")

#Gets the three exam grades as integers
            exam1 = int(input("Please enter grade for Exam 1: "))
            exam2 = int(input("Please enter grade for Exam 2: "))
            exam3 = int(input("Please enter grade for Exam 3: "))

#Writes the record to the file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"\nAll data has been written to {filename} successfully.")

#Runs the function
if __name__ == "__main__":
    write_grades_to_csv()