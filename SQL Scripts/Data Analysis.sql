--1. Total sales per customer
SELECT C.customer_id, C.first_name, C.last_name,
SUM(S.quantity * S.unit_price) AS Total_Sales
FROM customers AS C JOIN sales AS S
ON C.customer_id = S.customer_id
GROUP BY C.customer_id, C.first_name, C.last_name
ORDER BY Total_Sales DESC;

--another approach
SELECT C.customer_id, C.first_name, C.last_name,
SUM(S.total_sale) as total_sales
FROM customers AS C JOIN sales AS S
ON C.customer_id = S.customer_id
GROUP BY C.customer_id, C.first_name, C.last_name
ORDER BY total_Sales DESC;

--2. Monthly sales trends

SELECT FORMAT(transaction_date, 'yyyy-MM') AS Month,
--DATEPART(MONTH,transaction_date) AS Month,
SUM(quantity * unit_price) as Monthly_Sale
FROM sales 
GROUP BY FORMAT(transaction_date, 'yyyy-MM') 
ORDER BY Month DESC;

--3. Most popular product categories in terms of purchase

SELECT category, SUM(quantity) as Total_units_sold
FROM sales
GROUP BY category
ORDER BY Total_units_sold DESC;

--4. Most popular product categories in terms of revenue

SELECT category, SUM(quantity * unit_price) as Total_sales
FROM sales
GROUP BY category
ORDER BY Total_sales DESC;

--5. Average order value by payment method

SELECT payment_method,
AVG(quantity * unit_price) AS avg_order_value
FROM sales
GROUP BY payment_method;

--6. Customers who have purchased most units (TOP 3)

SELECT TOP 3 C.customer_id, CONCAT(C.first_name,' ', C.last_name) AS customer_name,
sum(S.quantity) as Total_units_purchased
FROM customers AS C
JOIN sales AS S
ON C.customer_id = S.customer_id
GROUP BY C.customer_id, CONCAT(C.first_name,' ', C.last_name)
ORDER BY Total_units_purchased DESC;

--7. Create a fact table having necessary details from customers and sales table

SELECT * INTO sales_fact
FROM 
(SELECT
  s.transaction_id,
  s.customer_id,
  c.first_name,
  c.last_name,
  s.product,
  s.category,
  s.quantity,
  s.unit_price,
  s.quantity * s.unit_price AS total_amount,
  s.transaction_date,
  s.payment_method
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id) AS t;
