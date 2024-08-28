# Developer: Steve Baker
# Program: Module 2 Lab - Case Study: if...else and while
# Description: This program will take input for a student's last name, first name, and GPA. 
# The programa will not quit until the use enters "ZZZ" for the last name.

while True:
    # prompt the user to enter a students last name
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")

    # If last name = ZZZ, quit program else move on
    if last_name == 'ZZZ':
        break

    # prompt the user to enter a students first name
    first_name = input("Enter the student's first name: ")

    # prompt the user to enter a students GPA
    gpa = float(input("Enter the student's GPA: "))

    # Compare the level of GPA and match it to the outcome
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")

