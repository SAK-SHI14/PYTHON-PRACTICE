--Procedure to enroll a student in a course--
CREATE PROCEDURE sp_EnrollStudentInCourse
    @StudentID int,
    @CourseID int,
    @Semester nvarchar(10)
AS
BEGIN
    INSERT INTO Enrollments (StudentID, CourseID, Semester)
    VALUES (@StudentID, @CourseID, @Semester)
END
GO

-- Execute the procedure
EXEC sp_EnrollStudentInCourse 1, 101, 'Fall 2024'

--Procedure to update a student's GPA--
CREATE PROCEDURE sp_UpdateStudentGPA
    @StudentID int,
    @NewGPA decimal(3, 2)
AS
BEGIN
    UPDATE Students
    SET GPA = @NewGPA
    WHERE StudentID = @StudentID
END
GO

-- Execute the procedure
EXEC sp_UpdateStudentGPA 1, 3.50

--FUNCTIONS--
 --Function to calculate a student's GPA--
CREATE FUNCTION fn_CalculateGPA
    (@StudentID int)
RETURNS decimal(3, 2)
AS
BEGIN
    DECLARE @GPA decimal(3, 2)
    SELECT @GPA = AVG(Grade)
    FROM Grades
    WHERE StudentID = @StudentID
    RETURN @GPA
END
GO

-- Use the function in a query
SELECT dbo.fn_CalculateGPA(1) AS GPA

--Function to get a course's description--
CREATE FUNCTION fn_GetCourseDescription
    (@CourseID int)
RETURNS nvarchar(50)
AS
BEGIN
    DECLARE @Description nvarchar(50)
    SELECT @Description = Description
    FROM Courses
    WHERE CourseID = @CourseID
    RETURN @Description
END
GO

-- Use the function in a query
SELECT dbo.fn_GetCourseDescription(101) AS CourseDescription

--CURSOR--
--Cursor to retrieve all students enrolled in a course and print their names--
DECLARE @StudentName nvarchar(50)

DECLARE cur CURSOR FOR
SELECT s.Name
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID = 101

OPEN cur

FETCH NEXT FROM cur INTO @StudentName

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @StudentName
    FETCH NEXT FROM cur INTO @StudentName
END

CLOSE cur
DEALLOCATE cur

--PRE-DEFINED CURSORS--
--Using the @@CURSOR_ROWS system variable to get the number of students enrolled in a course--
DECLARE cur CURSOR FOR
SELECT s.Name
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID = 101

OPEN cur

SELECT @@CURSOR_ROWS AS NumberOfStudents

CLOSE cur
DEALLOCATE cur

--DECLARE cur CURSOR FOR
SELECT *
FROM Employees

OPEN cur

FETCH NEXT FROM cur

WHILE @@FETCH_STATUS = 0
BEGIN
    -- Process the row
    FETCH NEXT FROM cur
END

CLOSE cur
DEALLOCATE cur

--PROCEDURES--
-- Procedure to enroll a student in a course--
CREATE PROCEDURE sp_EnrollStudentInCourse
    @StudentID int,
    @CourseID int,
    @Semester nvarchar(10)
AS
BEGIN
    INSERT INTO Enrollments (StudentID, CourseID, Semester)
    VALUES (@StudentID, @CourseID, @Semester)
END
GO

-- Execute the procedure
EXEC sp_EnrollStudentInCourse 1, 101, 'Fall 2024'

-- Procedure to update a student's GPA--
CREATE PROCEDURE sp_UpdateStudentGPA
    @StudentID int,
    @NewGPA decimal(3, 2)
AS
BEGIN
    UPDATE Students
    SET GPA = @NewGPA
    WHERE StudentID = @StudentID
END
GO

-- Execute the procedure
EXEC sp_UpdateStudentGPA 1, 3.50

--FUNCTIONS--
-- Function to calculate a student's GPA--
CREATE FUNCTION fn_CalculateGPA
    (@StudentID int)
RETURNS decimal(3, 2)
AS
BEGIN
    DECLARE @GPA decimal(3, 2)
    SELECT @GPA = AVG(Grade)
    FROM Grades
    WHERE StudentID = @StudentID
    RETURN @GPA
END
GO

-- Use the function in a query
SELECT dbo.fn_CalculateGPA(1) AS GPA

-- Function to get a course's description--
CREATE FUNCTION fn_GetCourseDescription
    (@CourseID int)
RETURNS nvarchar(50)
AS
BEGIN
    DECLARE @Description nvarchar(50)
    SELECT @Description = Description
    FROM Courses
    WHERE CourseID = @CourseID
    RETURN @Description
END
GO

-- Use the function in a query
SELECT dbo.fn_GetCourseDescription(101) AS CourseDescription

--CURSORS--
--Cursor to retrieve all students enrolled in a course and print their names--
DECLARE @StudentName nvarchar(50)

DECLARE cur CURSOR FOR
SELECT s.Name
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID = 101

OPEN cur

FETCH NEXT FROM cur INTO @StudentName

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @StudentName
    FETCH NEXT FROM cur INTO @StudentName
END

CLOSE cur
DEALLOCATE cur

--Function to get a course's description--
CREATE FUNCTION fn_GetCourseDescription
    (@CourseID int)
RETURNS nvarchar(50)
AS
BEGIN
    DECLARE @Description nvarchar(50)
    SELECT @Description = Description
    FROM Courses
    WHERE CourseID = @CourseID
    RETURN @Description
END
GO

-- Use the function in a query
SELECT dbo.fn_GetCourseDescription(101) AS CourseDescription

--Cursor to retrieve all students enrolled in a course and print their names--
DECLARE @StudentName nvarchar(50)

DECLARE cur CURSOR FOR
SELECT s.Name
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID = 101

OPEN cur

FETCH NEXT FROM cur INTO @StudentName

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @StudentName
    FETCH NEXT FROM cur INTO @StudentName
END

CLOSE cur
DEALLOCATE cur

--Using the @@CURSOR_ROWS system variable to get the number of students enrolled in a course--
DECLARE cur CURSOR FOR
SELECT s.Name
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID = 101

OPEN cur

SELECT @@CURSOR_ROWS AS NumberOfStudents

CLOSE cur
DEALLOCATE cur

--Using the @@FETCH_STATUS system variable to check the status of a cursor fetch operation--
DECLARE cur CURSOR FOR
SELECT s.Name
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE e.CourseID = 101

OPEN cur

FETCH NEXT FROM cur

WHILE @@FETCH_STATUS = 0
BEGIN
    -- Process the row
    FETCH NEXT FROM cur
END

CLOSE cur
DEALLOCATE cur

