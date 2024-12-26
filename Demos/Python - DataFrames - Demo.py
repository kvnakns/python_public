import pandas as pd


# Loading Data:
# Load the CSV file into a DataFrame
df = pd.read_csv('/<My directory goes here>/FileDrop/Import/orders.csv')
print(df)



# Cleaning Data:
# Check for missing values
print(df.isnull().sum())

# Drop duplicates if any
df.drop_duplicates(inplace=True)



# Adding columns:
# Add a new column that calculates the total sales per order (quantity * price)
df['total_sales'] = df['quantity'] * df['price']
print(df)


# Filtering Data:
# Filter the DataFrame to find all orders with total sales greater than $40
high_value_orders = df[df['total_sales'] > 40]
print(high_value_orders)



# Aggregating Data:
# Group the data by customer_id to see the total sales per customer
sales_by_customer = df.groupby('customer_id')['total_sales'].sum().reset_index()
print(sales_by_customer)


# Group by customer_id and aggregate the total sales AND count of orders
sales_by_customer = df.groupby('customer_id').agg(
    total_sales=('total_sales', 'sum'),
    order_count=('order_id', 'count'),
    avg_sale=('total_sales', 'mean')
).reset_index()

# Print the resulting DataFrame
print(sales_by_customer)



# Options to use with agg() - min, max, std, var, median, first, last, nunique (number of unique)
#       quantile, mode, prod, sem, size, cumsum, cummax

# example that includes several of these aggregations:
sales_by_customer = df.groupby('customer_id').agg(
    total_sales=('total_sales', 'sum'),
    order_count=('order_id', 'count'),
    avg_sale=('total_sales', 'mean'),
    min_sale=('total_sales', 'min'),
    max_sale=('total_sales', 'max'),
    std_dev=('total_sales', 'std'),
    first_order=('order_date', 'first'),
    last_order=('order_date', 'last'),
    unique_products=('product_name', 'nunique')
).reset_index()

print(sales_by_customer)





# Exporting Data:
# Finally, you can export the cleaned and processed data back to a CSV file
sales_by_customer.to_csv('/<My directory goes here>/FileDrop/Output/output_orders.csv', index=False)
