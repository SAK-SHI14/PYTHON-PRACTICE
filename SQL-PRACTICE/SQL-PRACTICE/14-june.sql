--GROUP BY :--
--WRITE A QUERY TO FIND THE TOTAL STOCK OF PRODUCTS FOR EACH LOCATION:--

SELECT location, SUM(stock) AS total_stock
FROM products
GROUP BY location;

----------------------------------------------------------------------------------------------------
--Write a query to find the number of products in each price range (e.g., 0-10000, 10000-200--

SELECT
    CASE
        WHEN price BETWEEN 0 AND 10000 THEN '0-10000'
        WHEN price BETWEEN 10001 AND 20000 THEN '10000-20000'
        WHEN price BETWEEN 20001 AND 50000 THEN '20000-50000'
        ELSE '50000+'
    END AS price_range,
    COUNT(*) AS num_products
FROM products
GROUP BY price_range;

--------------------------------------------------------------------------------------------------------
--Write a query to find the average age of customers grouped by their location (based on the address--

SELECT address, AVG(age) AS avg_age
FROM customers
GROUP BY address;

----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
--ORDER BY:--
--Write a query to retrieve all products ordered by their price in descending order--

SELECT *
FROM products
ORDER BY price DESC;

------------------------------------------------------------------------------------------------------
--Write a query to retrieve all customers ordered by their age in ascending order--

SELECT *
FROM customers
ORDER BY age ASC;
-----------------------------------------------------------------------------------------------------------------------------------------------
--Write a query to retrieve all orders ordered by the order amount in descending order and then by the customer name in ascending order--

SELECT *
FROM orders
ORDER BY order_amount DESC, customer_name ASC;
---------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------
--HAVING:--
--Write a query to find the locations where the total stock of products is greater than 20--

SELECT location, SUM(stock) AS total_stock
FROM products
GROUP BY location
HAVING SUM(stock) > 20;
----------------------------------------------------------------------------------------------------------------------
--Write a query to find the customers who have placed orders with a total amount greater than 10000--

SELECT customer_name
FROM orders
GROUP BY customer_name
HAVING SUM(order_amount) > 10000;
---------------------------------------------------------------------------------------------------------------------
--Write a query to find the products that have a stock level between 10 and 20 and are located in Mumbai--

SELECT *
FROM products
WHERE location = 'Mumbai'
  AND stock BETWEEN 10 AND 20;

---------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------
--Write a query to retrieve the distinct locations of products from the products table.--

SELECT DISTINCT location
FROM products;
----------------------------------------------------------------------------------------------------------------------------------------------
 --Write a query to retrieve the customer ID, customer name, and the length of their address--
   as address_length from the customer table.

SELECT customer_id, customer_name, LENGTH(address) AS address_length
FROM customer;
-----------------------------------------------------------------------------------------------------------------------------------------------
 --Write a query to retrieve the order ID, customer name, product name, and the concatenated--
 --  string 'Order for [product name] by [customer name]' as order_description from the orders, customer,--
 --  and products tables.--

SELECT o.order_id, c.customer_name, p.product_name, 
       CONCAT('Order for ', p.product_name, ' by ', c.customer_name) AS order_description
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;
-----------------------------------------------------------------------------------------------------------------------------------------------
-- Write a query to retrieve the product ID, product name, price, and a new column price_category that categorizes--
  -- the products based on their price range (e.g., 'Low' for prices less than 10000, 'Medium' for prices between 10000--
  -- and 50000, and 'High' for prices greater than 50000).--

SELECT product_id, product_name, price,
       CASE
           WHEN price < 10000 THEN 'Low'
           WHEN price BETWEEN 10000 AND 50000 THEN 'Medium'
           ELSE 'High'
       END AS price_category
FROM products;

----------------------------------------------------------------------------------------------------------------------------------------
-- Write a query to retrieve the customer ID, customer name, and the total order amount for each customer.--
 --  The total order amount should be retrieved from a subquery that calculates the sum of order amounts for each--
 --  customer.--

SELECT c.customer_id, c.customer_name, 
       (SELECT SUM(o.order_amount) FROM orders o WHERE o.customer_id = c.customer_id) AS total_order_amount
FROM customer c;