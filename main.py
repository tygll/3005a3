from datetime import datetime
import psycopg2
from psycopg2 import Error

# establish connection to PostgreSQL database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            host="YOUR_HOST",
            port="YOUR_PORT",
            database="YOUR_DATABASE"
        )
        return connection
    except Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None

# retrieve and display all records from the students table
def get_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        if students:
            # print each student's data
            for student in students:
                student_id, first_name, last_name, email, enrollment_date = student
                print(f"{student_id}\t{first_name}\t{last_name}\t{email}\t\t{enrollment_date}")
        else:
            print("No students found.")
		
    except Error as e:
        print(f"Error retrieving students: {e}")

# insert a new student record into the students table
def add_student(connection, first_name, last_name, email, enrollment_date):
    # check if the enrollment date is a valid date
    try:
        enrollment_date = datetime.strptime(enrollment_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid enrollment date format. Please use YYYY-MM-DD.")
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student added successfully.")
    except Error as e:
        print(f"Error adding student: {e}")

# update the email address for a student with the specified student_id
def update_student_email(connection, student_id, new_email):
    # Check if the student exists
    if not student_exists(connection, student_id):
        print("Student with the specified ID does not exist.")
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                       (new_email, student_id))
        connection.commit()
        print("Email address updated successfully.")
    except Error as e:
        print(f"Error updating email address: {e}")

# delete the record of the student with the specified student_id
def delete_student(connection, student_id):
    # check if the student exists
    if not student_exists(connection, student_id):
        print("Student with the specified ID does not exist.")
        return
    
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s",
                       (student_id,))
        connection.commit()
        print("Student deleted successfully.")
    except Error as e:
        print(f"Error deleting student: {e}")

# function to check if a student with the specified student_id exists
def student_exists(connection, student_id):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students WHERE student_id = %s",
                       (student_id,))
        count = cursor.fetchone()[0]
        return count > 0
    except Error as e:
        print(f"Error checking student existence: {e}")
        return False

def main():
    # connect to the database
    connection = connect_to_db()
    if connection is None:
        return
    
    while True:
        print("\nChoose an option:")
        print("1. Retrieve all students")
        print("2. Add a new student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAll students:")
            get_all_students(connection)
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            add_student(connection, first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter student ID to update email: ")
            new_email = input("Enter new email: ")
            update_student_email(connection, student_id, new_email)
        elif choice == "4":
            student_id = input("Enter student ID to delete: ")
            delete_student(connection, student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    # close the connection
    connection.close()

if __name__ == "__main__":
    main()
