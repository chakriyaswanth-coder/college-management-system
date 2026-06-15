# College Management System

A command-line based College Management System developed using Python and MySQL. This project allows users to manage student and faculty records through CRUD (Create, Read, Update, Delete) operations.

## Features

### Student Management

* Add Student
* View Students
* Search Student by ID
* Update Student Marks
* Delete Student

### Faculty Management

* Add Faculty
* View Faculty
* Delete Faculty

## Technologies Used

* Python
* MySQL
* mysql-connector-python

## Database Structure

### students table

| Column     | Type                              |
| ---------- | --------------------------------- |
| student_id | INT (Primary Key, Auto Increment) |
| name       | VARCHAR(100)                      |
| age        | INT                               |
| course     | VARCHAR(100)                      |
| marks      | FLOAT                             |

### faculty table

| Column        | Type                              |
| ------------- | --------------------------------- |
| faculty_id    | INT (Primary Key, Auto Increment) |
| faculty_name  | VARCHAR(100)                      |
| subject       | VARCHAR(100)                      |
| mobile_number | VARCHAR(15)                       |
| salary        | FLOAT                             |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/college-management-system.git
```

2. Install required package:

```bash
pip install mysql-connector-python
```

3. Create a MySQL database:

```sql
CREATE DATABASE college_db;
```

4. Create required tables and update database credentials in the Python file.

5. Run the project:

```bash
python main.py
```

## Sample Menu

```text
===== COLLEGE MANAGEMENT SYSTEM =====
1. Add Student
2. View Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Add Faculty
7. View Faculty
8. Delete Faculty
9. Exit
```

## Author

Developed using Python and MySQL for educational purposes.
