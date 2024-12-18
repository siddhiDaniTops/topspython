# student_management_system.py - Main Menu



def main_menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Counsellor Menu")
        print("2. Faculty Menu")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Counsellor.menu()
            elif choice == 2:
                Faculty.menu()
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main_menu()

# business_logic.py - All Business Logic

import re
import json

students_data = {}  # Nested dictionary to store student information
log_file = "transaction_log.txt"

# Logging utility
def log_transaction(action, details):
    with open(log_file, "a") as log:
        log.write(f"{action}: {details}\n")

# Counsellor-related operations
class Counsellor:
    @staticmethod
    def add_student():
        print("\n--- Add Student ---")
        while True:
            first_name = input("Enter a First Name: ").strip()
            if first_name.isalpha():
                break
            print("Invalid input! First name must contain only letters.")

        while True:
            last_name = input("Enter a Last Name: ").strip()
            if last_name.isalpha():
                break
            print("Invalid input! Last name must contain only letters.")

        while True:
            contact = input("Enter a Contact Number: ").strip()
            if contact.isdigit() and len(contact) == 10:
                break
            print("Invalid contact number! Must be 10 digits.")

        while True:
            student_id = input("Enter a Serial Number: ").strip()
            if student_id.isdigit():
                break
            print("Invalid Serial Number! It must be numeric.")

        print("\n--- Enter Course Details ---")
        courses = {}
        while True:
            subject = input("Enter a Subject: ").strip()
            try:
                marks = int(input(f"Enter Marks for {subject}: ").strip())
                fees = int(input(f"Enter Fees for {subject}: ").strip())
                courses[subject] = {"marks": marks, "fees": fees}
                add_more = input("Add another course? (Y/N): ").strip().upper()
                if add_more != 'Y':
                    break
            except ValueError:
                print("Invalid input! Marks and fees must be numbers.")

        students_data[student_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "contact": contact,
            "courses": courses
        }
        log_transaction("Added Student", f"ID: {student_id}, Name: {first_name} {last_name}")
        print(f"\nStudent {first_name} {last_name} added successfully!\n")

    @staticmethod
    def remove_student():
        print("\n--- Remove Student ---")
        student_id = input("Enter Student ID to remove: ").strip()
        if student_id in students_data:
            confirm = input(f"Are you sure you want to delete student ID {student_id}? (Y/N): ").strip().upper()
            if confirm == "Y":
                del students_data[student_id]
                log_transaction("Removed Student", f"ID: {student_id}")
                print("Student removed successfully!\n")
            else:
                print("Operation cancelled.\n")
        else:
            print("Student does not exist.\n")

    @staticmethod
    def view_all_students():
        print("\n--- All Students ---")
        if not students_data:
            print("No students available.\n")
        else:
            print(json.dumps(students_data, indent=4))
        print()

    @staticmethod
    def view_specific_student():
        print("\n--- View Specific Student ---")
        student_id = input("Enter Student ID: ").strip()
        if student_id in students_data:
            info = students_data[student_id]
            print(json.dumps({student_id: info}, indent=4))
        else:
            print("Student does not exist.\n")

    @staticmethod
    def menu():
        while True:
            print("\n--- Counsellor Menu ---")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. View All Students")
            print("4. View Specific Student")
            print("5. Back to Main Menu")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    Counsellor.add_student()
                elif choice == 2:
                    Counsellor.remove_student()
                elif choice == 3:
                    Counsellor.view_all_students()
                elif choice == 4:
                    Counsellor.view_specific_student()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

# Faculty-related operations
class Faculty:
    @staticmethod
    def add_marks():
        print("\n--- Add Marks ---")
        student_id = input("Enter Student ID: ").strip()
        if student_id in students_data:
            while True:
                subject = input("Enter Subject: ").strip()
                try:
                    marks = int(input(f"Enter Marks for {subject}: ").strip())
                    students_data[student_id]["courses"].setdefault(subject, {})["marks"] = marks
                    log_transaction("Added Marks", f"ID: {student_id}, Subject: {subject}, Marks: {marks}")
                    print("Marks added successfully!\n")
                    break
                except ValueError:
                    print("Invalid input! Marks must be a number.")
        else:
            print("Student does not exist.\n")

    @staticmethod
    def view_students():
        print("\n--- View Students ---")
        if not students_data:
            print("No students available.\n")
        else:
            print(json.dumps(students_data, indent=4))
        print()

    @staticmethod
    def menu():
        while True:
            print("\n--- Faculty Menu ---")
            print("1. Add Marks")
            print("2. View Students")
            print("3. Back to Main Menu")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    Faculty.add_marks()
                elif choice == 2:
                    Faculty.view_students()
                elif choice == 3:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")
