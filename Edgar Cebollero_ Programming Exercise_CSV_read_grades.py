#An instructor teaches a class in which each student takes three exams. The instructor would like to store this information
#in a file named grades.csv for later use. Create a program that allows an instructor to input how many students they
#want to enter. Then enter each student’s first name and last name as strings and the student’s three exam grades as
#integers. Use the csv module to write each record into the grades.csv file and have a header of First Name, Last Name,
#Exam 1, Exam 2 and Exam3. Each student should be a record in the grades.csv file.
#Once the file is created, create a separate program to read the grades.csv file and display the data in tabular format.
#Implement the with keyword. You may need to refer back to Chapter 5 for formatting.
#Each of these 2 programs should be separate functions so you have at least two functions for this assignment, but you can have more.

#imports csv and filename
import csv

def read_grades_from_csv():
    filename = "grades.csv"

#Opens the file using the 'with' keyword
    with open(filename, mode="r", newline="") as file:
        reader = csv.reader(file)

#Reads all lines from the file inserted
        rows = list(reader)

#Prints the table header
        print("\nStudent Grades")
        print("-" * 60)

#Prints the column headers
        print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")
        print("-" * 60)

#Skips the header row when printing data
        for row in rows[1:]:
            first_name, last_name, exam1, exam2, exam3 = row
            print(f"{first_name:<15}{last_name:<15}{exam1:<10}{exam2:<10}{exam3:<10}")

#Runs the function
if __name__ == "__main__":
    read_grades_from_csv()