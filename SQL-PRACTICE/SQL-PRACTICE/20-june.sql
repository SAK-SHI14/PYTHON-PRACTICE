CREATE DATABASE university;

USE university;

CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
  course_id INT PRIMARY KEY,
  name VARCHAR(100),
  credits INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE enrollments (
  enrollment_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  enrollment_date DATE,
  grade VARCHAR(2),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE instructors (
  instructor_id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE course_instructors (
  course_id INT,
  instructor_id INT,
  PRIMARY KEY (course_id, instructor_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id),
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

SELECT s.name AS student_name, c.name AS course_name, i.name AS instructor_name, e.enrollment_date
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
JOIN course_instructors ci ON c.course_id = ci.course_id
JOIN instructors i ON ci.instructor_id = i.instructor_id;

SELECT c.name, COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.name
HAVING COUNT(e.enrollment_id) = (
  SELECT COUNT(e2.enrollment_id)
  FROM courses c2
  JOIN enrollments e2 ON c2.course_id = e2.course_id
  GROUP BY c2.name
  ORDER BY COUNT(e2.enrollment_id) DESC
  LIMIT 1
);

SELECT *
FROM enrollments
WHERE DATE_FORMAT(enrollment_date, '%Y-%m') = DATE_FORMAT(CURDATE(), '%Y-%m');

SELECT s.name AS student_name, c.name AS course_name, i.name AS instructor_name, e.enrollment_date
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
JOIN course_instructors ci ON c.course_id = ci.course_id
JOIN instructors i ON ci.instructor_id = i.instructor_id
WHERE DATE_FORMAT(e.enrollment_date, '%Y-%m') = DATE_FORMAT(CURDATE(), '%Y-%m')
AND c.name IN (
  SELECT c2.name
  FROM courses c2
  JOIN enrollments e2 ON c2.course_id = e2.course_id
  GROUP BY c2.name
  HAVING COUNT(e2.enrollment_id) = (
    SELECT COUNT(e3.enrollment_id)
    FROM courses c3
    JOIN enrollments e3 ON c3.course_id = e3.course_id
    GROUP BY c3.name
    ORDER BY COUNT(e3.enrollment_id) DESC
    LIMIT 1
  )
);