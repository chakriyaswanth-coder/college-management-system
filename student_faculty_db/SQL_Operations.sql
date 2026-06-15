CREATE DATABASE college_db;

USE college_db;

CREATE TABLE students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50),
    marks FLOAT
);

CREATE TABLE faculty(
    faculty_id INT PRIMARY KEY AUTO_INCREMENT,
    faculty_name VARCHAR(100),
    subject VARCHAR(50),
    mobile_number VARCHAR(15),
    salary DECIMAL(10,2)
);

SHOW TABLES;