# using the DISTINCT keyword to handle duplicates in a table
# use temporary table to handle and clean dupicates and update the existing table. THIS IS FOR SQL

# create temp table to hold all unique records
CREATE TEMP TABLE temp_employee_table AS SELECT DISTINCT * FROM employees

# truncate original table to remove all duplicate records
TRUNCATE TABLE employees

# Insert the unique records back into the original table
INSERT INTO employees SELECT * FROM temp_employee_table

# drop the temp table
DROP TABLE temp_employee_table

# Verify the results
SELECT * FROM employees

############################
#Suppose we have a large table transactions with columns transaction_id, customer_id, product_id, quantity, price, and transaction_date.

# Find total sales per customer in the last year

SELECT customer_id, SUM(quantity * price) AS total_sales
FROM transactions
# WHERE transaction_date >= (year, -1, GETDATE()) # SQL
WHERE transaction_date >= (CURRENT_DATE - INTERVAL "1 year") #POStgresql
GROUP BY customer_id
ORDER BY total_sales DESC;

###############################