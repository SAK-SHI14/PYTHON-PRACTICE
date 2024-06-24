CREATE DATABASE mydatabase;
USE mydatabase;
-- COMMIT example
START TRANSACTION;
INSERT INTO products (name, price) VALUES ('Product 1', 10.99);
COMMIT;

-- ROLLBACK example
START TRANSACTION;
INSERT INTO products (name, price) VALUES ('Product 2', 9.99);
ROLLBACK;

-- SAVEPOINT example
START TRANSACTION;
INSERT INTO products (name, price) VALUES ('Product 3', 12.99);
SAVEPOINT sp1;
INSERT INTO products (name, price) VALUES ('Product 4', 11.99);
ROLLBACK TO SAVEPOINT sp1;
COMMIT;
DELIMITER //

--SQL TRIGGERS--
--LOG CHANGES TRIGGER--
CREATE TRIGGER log_changes
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    INSERT INTO log_table (table_name, row_id, column_name, old_value, new_value)
    VALUES ('products', OLD.id, 'name', OLD.name, NEW.name);
END//

--LOG DELETED TRIGGER--
CREATE TRIGGER log_deleted
AFTER DELETE ON products
FOR EACH ROW
BEGIN
    INSERT INTO log_table (table_name, row_id, column_name, old_value, new_value)
    VALUES ('products', OLD.id, 'name', OLD.name, NULL);
END//

--BEFORE INSERT TRIGGER--
CREATE TRIGGER before_insert
BEFORE INSERT ON products
FOR EACH ROW
BEGIN
    SET NEW.created_at = NOW();
END//

--AFTER INSERT TRIGGER--
CREATE TRIGGER after_insert
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    INSERT INTO log_table (table_name, row_id, column_name, old_value, new_value)
    VALUES ('products', NEW.id, 'name', NULL, NEW.name);
END//

--BEFORE UPDATE TRIGGER--
CREATE TRIGGER before_update
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END//

--AFTER UPDATE TRIGGER--
CREATE TRIGGER after_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    INSERT INTO log_table (table_name, row_id, column_name, old_value, new_value)
    VALUES ('products', OLD.id, 'name', OLD.name, NEW.name);
END//

--BEFORE DELETE TRIGGER--
CREATE TRIGGER before_delete
BEFORE DELETE ON products
FOR EACH ROW
BEGIN
    INSERT INTO log_table (table_name, row_id, column_name, old_value, new_value)
    VALUES ('products', OLD.id, 'name', OLD.name, NULL);
END//

--AFTER DELETE TRIGGER--
CREATE TRIGGER after_delete
AFTER DELETE ON products
FOR EACH ROW
BEGIN
    INSERT INTO log_table (table_name, row_id, column_name, old_value, new_value)
    VALUES ('products', OLD.id, 'name', OLD.name, NULL);
END//

--DATA VALIDATION--
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0)
);

--MAINTAINING REFERENTIAL INTEGRITY--
CREATE TABLE orders (
    id INT PRIMARY KEY,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES products (id)
);

--ENFORCING BUSINESS LOGIC--
CREATE TRIGGER enforce_business_logic
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.product_id NOT IN (SELECT id FROM products WHERE location = 'Mumbai') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Only Mumbai products are allowed';
    END IF;
END//

--SECURITY--
GRANT SELECT, INSERT, UPDATE, DELETE ON products TO 'user'@'%';
GRANT ALL PRIVILEGES ON products TO 'admin'@'%';

--PERFORMANCE IMPACT--
CREATE INDEX idx_product_name ON products (name);


--TRIGGER ORDER--
CREATE TRIGGER trigger1
BEFORE INSERT ON products
FOR EACH ROW
BEGIN
    SET NEW.created_at = NOW();
END//

CREATE TRIGGER trigger2
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    INSERT INTO log_table (table_name, row_id, column_name, old_value, new_value)
    VALUES ('products', NEW.id, 'name', NULL, NEW.name);
END//

--ADVANCED TRIGGER--
CREATE TRIGGER advanced_trigger
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN

