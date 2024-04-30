import datetime

# Assume the parsed entities
customer_table = "Customers"
order_table = "Orders"
date_column = "OrderDate"

# Assume the parsed date range (last month)
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=30)

# Construct the SQL query
sql_query = f"""
    SELECT *
    FROM {customer_table}
    WHERE CustomerID IN (
        SELECT CustomerID
        FROM {order_table}
        WHERE {date_column} >= '{start_date}' AND {date_column} <= '{end_date}'
    );
"""

print("Generated SQL Query:")
print(sql_query)
# Execute the query using your database connector
# ...
