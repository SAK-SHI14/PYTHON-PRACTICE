-- Create a database
CREATE DATABASE mydb;

-- Use the database
USE mydb;

-- Create a table
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  phone VARCHAR(20),
  address VARCHAR(100)
);

-- Insert some data into the table
INSERT INTO customers (id, name, email, phone, address)
VALUES
  (1, 'John Doe', 'john@example.com', '123-456-7890', '123 Main St'),
  (2, 'Jane Smith', 'jane@example.com', '098-765-4321', '456 Elm St'),
  (3, 'Bob Johnson', 'bob@example.com', '555-123-4567', '789 Oak St');

-- Drop a table
DROP TABLE customers;

-- Create a new table with a different structure
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  phone VARCHAR(20),
  address VARCHAR(100),
  country VARCHAR(50) DEFAULT 'USA'
);

-- Alter a table to add a column
ALTER TABLE customers
ADD COLUMN city VARCHAR(50);

-- Alter a table to delete a column
ALTER TABLE customers
DROP COLUMN phone;

-- Alter a table to rename a column
ALTER TABLE customers
RENAME COLUMN address TO location;

-- Alter a table to modify the data type of a column
ALTER TABLE customers
MODIFY COLUMN id VARCHAR(10);

-- Add a constraint to a column
ALTER TABLE customers
ADD CONSTRAINT chk_country CHECK (country IN ('USA', 'Canada', 'Mexico'));

-- Insert data into the table with the new structure
INSERT INTO customers (id, name, email, location, country)
VALUES
  ('C001', 'John Doe', 'john@example.com', '123 Main St', 'USA'),
  ('C002', 'Jane Smith', 'jane@example.com', '456 Elm St', 'Canada'),
  ('C003', 'Bob Johnson', 'bob@example.com', '789 Oak St', 'Mexico');

-- Update a row in the table
UPDATE customers
SET location = '456 Elm St'
WHERE id = 'C002';

-- Delete a row from the table
DELETE FROM customers
WHERE id = 'C003';

-- Truncate the table
TRUNCATE TABLE customers;

-- Create a new table with a foreign key constraint
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id VARCHAR(10),
  order_date DATE,
  total DECIMAL(10, 2),
  FOREIGN KEY (customer_id) REFERENCES customers (id)
);

-- Insert data into the orders table
INSERT INTO orders (id, customer_id, order_date, total)
VALUES
  (1, 'C001', '2022-01-01', 100.00),
  (2, 'C002', '2022-01-15', 50.00),
  (3, 'C003', '2022-02-01', 200.00);

-- Update a row in the orders table
UPDATE orders
SET total = 120.00
WHERE id = 1;

-- Delete a row from the orders table
DELETE FROM orders
WHERE id = 2;



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
QUESTIONS


-- 0)Make a new table employee with specified column id, name, position and salary.
CREATE TABLE employee (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  position VARCHAR(255),
  salary DECIMAL(10, 2)
);

-----------------------------------------------------------------------------------------------
-- 1)insert query adds a new row to the employees table with specific values for id, name, position, and salary.
INSERT INTO employee (id, name, position, salary)
VALUES (1, 'John Doe', 'Software Engineer', 80000.00);

-----------------------------------------------------------------------------------------------
-- 2)update query updates the salary of the employee with id = 1.
UPDATE employee
SET salary = 90000.00
WHERE id = 1;

-----------------------------------------------------------------------------------------------
-- 3)delete query deletes the row from employees where id = 1.
DELETE FROM employee
WHERE id = 1;

-----------------------------------------------------------------------------------------------
-- 4)create a query that creates a table called students.
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

-----------------------------------------------------------------------------------------------
-- 5)create another table courses and set up a foreign key constraint in the students table.
	The foreign key constraint ensures that the course_id in students must refer to a valid course_id in the courses table.
CREATE TABLE courses (
  id INT PRIMARY KEY,
  course_name VARCHAR(255)
);

CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  course_id INT,
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

-----------------------------------------------------------------------------------------------
-- 6)Alter the students table to add the foreign key constraint.
ALTER TABLE students
ADD CONSTRAINT fk_course_id
FOREIGN KEY (course_id) REFERENCES courses(id);

-----------------------------------------------------------------------------------------------

-- 7)insert some data into the students table while respecting the constraints.
INSERT INTO courses (id, course_name)
VALUES (1, 'Computer Science');

INSERT INTO students (id, name, email, course_id)
VALUES (1, 'Alice Johnson', 'alice@example.com', 1);

-----------------------------------------------------------------------------------------------
-- 8)create a SELECT query that retrieves products based on numeric and date conditions.
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  price DECIMAL(10, 2),
  created_at DATE
);

SELECT *
FROM products
WHERE price > 100.00 AND created_at > '2020-01-01';

-----------------------------------------------------------------------------------------------
-- 9)update a record and set the last_updated column to the current datetime.
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  price DECIMAL(10, 2),
  created_at DATE,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

UPDATE products
SET price = 150.00
WHERE id = 1;

-----------------------------------------------------------------------------------------------
-- 10)delete products with stock below a certain threshold.
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  price DECIMAL(10, 2),
  stock INT
);

DELETE FROM products
WHERE stock < 10;
