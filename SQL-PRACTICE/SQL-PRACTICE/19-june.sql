SELECT orders.*, products.* 
FROM orders
LEFT JOIN products ON orders.pid = products.pid
WHERE products.location = 'Mumbai';
SELECT orders.*, payment.*
FROM orders
RIGHT JOIN payment ON orders.oid = payment.oid
WHERE payment.mode = 'upi';
SELECT orders.oid, orders.amt, customer.cname, payment.mode
FROM orders
INNER JOIN customer ON orders.cid = customer.cid
INNER JOIN payment ON orders.oid = payment.oid
WHERE customer.age < 30;
SELECT orders.oid, orders.amt, customer.cname, payment.mode
FROM orders
INNER JOIN customer ON orders.cid = customer.cid
INNER JOIN payment ON orders.oid = payment.oid
WHERE customer.age < 30 AND payment.mode = 'credit';
SELECT orders.oid, orders.amt, customer.cname, products.pname, products.location
FROM orders
INNER JOIN customer ON orders.cid = customer.cid
INNER JOIN products ON orders.pid = products.pid
INNER JOIN payment ON orders.oid = payment.oid
WHERE payment.status IN ('in process', 'pending');
SELECT customer.cid, customer.cname, products.pname
FROM orders
INNER JOIN customer ON orders.cid = customer.cid
INNER JOIN products ON orders.pid = products.pid;
SELECT orders.oid, orders.amt, customer.cname, products.pname
FROM orders
RIGHT OUTER JOIN customer ON orders.cid = customer.cid
RIGHT OUTER JOIN products ON orders.pid = products.pid;
SELECT orders.oid, orders.amt, customer.cname, products.pname

FROM orders
FULL OUTER JOIN customer ON orders.cid = customer.cid
FULL OUTER JOIN products ON orders.pid = products.pid;
SELECT e1.ename AS Employee, e2.ename AS Manager
FROM employee e1
INNER JOIN employee e2 ON e1.manager_id = e2.eid;
SELECT orders.oid, orders.amt, customer.cname, products.pname
FROM orders
CROSS JOIN customer
CROSS JOIN products;
