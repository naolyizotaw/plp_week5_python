-- Question 1: Retrieve checkNumber, paymentDate, and amount from payments table
SELECT checkNumber, paymentDate, amount 
FROM payments;

-- Question 2: Retrieve orderDate, requiredDate, and status of orders with status 'In Process'
-- Sorted in descending order of orderDate
SELECT orderDate, requiredDate, status 
FROM orders 
WHERE status = 'In Process' 
ORDER BY orderDate DESC;

-- Question 3: Display firstName, lastName, and email of employees with job title 'Sales Rep'
-- Ordered in descending order of employeeNumber
SELECT firstName, lastName, email 
FROM employees 
WHERE jobTitle = 'Sales Rep' 
ORDER BY employeeNumber DESC;

-- Question 4: Retrieve all columns and records from the offices table
SELECT * 
FROM offices;

-- Question 5: Fetch productName and quantityInStock from products table
-- Sorted in ascending order of buyPrice and limited to 5 records
SELECT productName, quantityInStock 
FROM products 
ORDER BY buyPrice ASC 
LIMIT 5;