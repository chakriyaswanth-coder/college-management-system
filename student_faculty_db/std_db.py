import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0904",
    database="college_db"
)

cursor = conn.cursor()

print("Connected Successfully")


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    query = """
    INSERT INTO students(name,age,course,marks)
    VALUES(%s,%s,%s,%s)
    """

    values = (name, age, course, marks)

    cursor.execute(query, values)
    conn.commit()

    print("Student Added Successfully")

def view_students():
    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    print("\nStudents List")
    print("-" * 50)

    for row in data:
        print(row)

def search_student():
    sid = int(input("Enter Student ID: "))

    query = """
    SELECT * FROM students
    WHERE student_id=%s
    """

    cursor.execute(query, (sid,))
    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print("Student Not Found")

def update_student():
    sid = int(input("Enter Student ID: "))
    marks = float(input("Enter New Marks: "))

    query = """
    UPDATE students
    SET marks=%s
    WHERE student_id=%s
    """

    cursor.execute(query, (marks, sid))
    conn.commit()

    print("Updated Successfully")

def delete_student():
    sid = int(input("Enter Student ID: "))

    query = """
    DELETE FROM students
    WHERE student_id=%s
    """

    cursor.execute(query, (sid,))
    conn.commit()

    print("Deleted Successfully")

def add_faculty():
    name = input("Faculty Name: ")
    subject = input("Subject: ")
    mobile = input("Mobile Number: ")
    salary = float(input("Salary: "))

    query = """
    INSERT INTO faculty(
        faculty_name,
        subject,
        mobile_number,
        salary
    )
    VALUES(%s,%s,%s,%s)
    """

    values = (name, subject, mobile, salary)

    cursor.execute(query, values)
    conn.commit()

    print("Faculty Added Successfully")

def view_faculty():
    cursor.execute("SELECT * FROM faculty")

    data = cursor.fetchall()

    print("\nFaculty List")
    print("-" * 50)

    for row in data:
        print(row)

def delete_faculty():
    fid = int(input("Enter Faculty ID: "))

    query = """
    DELETE FROM faculty
    WHERE faculty_id=%s
    """

    cursor.execute(query, (fid,))
    conn.commit()

    print("Faculty Deleted")

while True:

    print("\n")
    print("===== COLLEGE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Add Faculty")
    print("7. View Faculty")
    print("8. Delete Faculty")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        add_faculty()

    elif choice == "7":
        view_faculty()

    elif choice == "8":
        delete_faculty()

    elif choice == "9":
        print("Thank You")
        break

    else:
        print("Invalid Choice")