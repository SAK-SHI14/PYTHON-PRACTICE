--CHAR_LENGTH() function--
SELECT CHAR_LENGTH('Hello World');  -- outputs 11

--ASCII() function--
SELECT ASCII('A');  -- outputs 65

 --CONCAT() function--
 SELECT CONCAT 'Hello', ', 'World');  -- outputs "Hello World"
 
 --INSTR() function--
 SELECT INSTR('Hello World', 'o');  -- outputs 5
 
--LCASE() and LOWER() functions--
SELECT LCASE('HELLO WORLD');  -- outputs "hello world"
SELECT LOWER('HELLO WORLD');  -- outputs "hello world"

-- UCASE() and UPPER() functions--
SELECT UCASE('hello world');  -- outputs "HELLO WORLD"
SELECT UPPER('hello world');  -- outputs "HELLO WORLD"

--SUBSTR() function--
SELECT SUBSTR('Hello World', 1, 5);  -- outputs "Hello"

 --LPAD() function--
 SELECT LPAD('Hello', 10, '*');  -- outputs "*****Hello"
 
 --RPAD() function--
 SELECT RPAD('Hello', 10, '*');  -- outputs "Hello*****"
 
 --TRIM() function--
 SELECT TRIM('   Hello World   ');  -- outputs "Hello World"
 
 DATE AND TIME FUNCTIONS:
 current date():
 SELECT CURRENT_DATE AS current_date;
 
 DATEDIFF:
 SELECT DATEDIFF('2023-07-20', '2023-06-15') AS days_between;
 
 DATE (expression):
 SELECT DATE('2023-06-15 12:34:56') AS date_only;
 
 CURRENT_TIME:
 SELECT CURRENT_TIME AS current_time;
 
 LAST_DAY:
 SELECT LAST_DAY('2023-05-01') AS last_day_of_month;
 
 SYSDATE:
 SELECT SYSDATE AS current_datetime;
 
 ADDDATE:
 SELECT ADDDATE(CURRENT_DATE, INTERVAL 3 MONTH) AS date_plus_three_months;
 
 NUMERIC FUNCTIONS:
 
  CEIL(number)
  SELECT CEIL(3.2) AS result; -- Output: 4
SELECT CEIL(-3.2) AS result; -- Output: -3

 TRUNC(number, [decimals])
 SELECT TRUNC(3.1416, 2) AS result; -- Output: 3.14
SELECT TRUNC(3.1416) AS result; -- Output: 3

SIGN(number)
SELECT SIGN(5) AS result; -- Output: 1
SELECT SIGN(-5) AS result; -- Output: -1
SELECT SIGN(0) AS result; -- Output: 0

ABS(number)
SELECT ABS(5) AS result; -- Output: 5
SELECT ABS(-5) AS result; -- Output: 5

MOD(dividend, divisor)
SELECT MOD(17, 5) AS result; -- Output: 2
SELECT MOD(-17, 5) AS result; -- Output: -2

RAND()
SELECT RAND() AS result;

DEGREES(angle)
SELECT DEGREES(PI()/2) AS result; -- Output: 90

RADIANS(angle)
SELECT RADIANS(90) AS result; -- Output: 1.5708
 