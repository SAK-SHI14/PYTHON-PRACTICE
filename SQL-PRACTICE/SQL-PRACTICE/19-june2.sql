CREATE DATABASE Student_Course;
USE Student_Course;
CREATE TABLE Students (
  Student_ID INT PRIMARY KEY,
  Name VARCHAR(255),
  Email VARCHAR(255),
  Phone_Number VARCHAR(20)
);

CREATE TABLE Courses (
  Course_ID INT PRIMARY KEY,
  Course_Name VARCHAR(255),
  Credits INT,
  Description TEXT
);

CREATE TABLE Enrollment (
  Student_ID INT,
  Course_ID INT,
  Grade DECIMAL(3,2),
  PRIMARY KEY (Student_ID, Course_ID),
  FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
  FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
);

INSERT INTO Students (Student_ID, Name, Email, Phone_Number)
VALUES
  (1, 'John Doe', 'johndoe@example.com', '1234567890'),
  (2, 'Jane Smith', 'janesmith@example.com', '0987654321'),
  (3, 'Bob Johnson', 'bobjohnson@example.com', '5551234567');

INSERT INTO Courses (Course_ID, Course_Name, Credits, Description)
VALUES
  (1, 'Introduction to Programming', 4, 'Basic programming concepts'),
  (2, 'Data Structures', 3, 'Algorithms and data structures'),
  (3, 'Operating Systems', 4, 'Operating system concepts and design');

INSERT INTO Enrollment (Student_ID, Course_ID, Grade)
VALUES
  (1, 1, 3.5),
  (1, 2, 3.8),
  (2, 1, 3.2),
  (2, 3, 3.9),
  (3, 2, 3.1);
  
  -- Get all students
SELECT * FROM Students;

-- Get all courses
SELECT * FROM Courses;

-- Get all enrollments
SELECT * FROM Enrollment;

-- Get a specific student's enrollments
SELECT * FROM Enrollment WHERE Student_ID = 1;

-- Get a specific course's students
SELECT * FROM Enrollment WHERE Course_ID = 1;