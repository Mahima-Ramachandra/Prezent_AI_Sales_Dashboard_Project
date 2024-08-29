# %%
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Define the output directory
output_dir = r"C:\Users\h547756\Downloads\My Assignment\OutputFiles"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Set seed for reproducibility
np.random.seed(42)
# %%
# Define date range (last 3 years)
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)
date_range = pd.date_range(start=start_date, end=end_date)
# %%
# Create customer data
num_customers = 100  # Number of unique customers
customer_ids = [f'CUST{str(i).zfill(4)}' for i in range(1, num_customers + 1)]
customer_names = [f'Customer_{i}' for i in range(1, num_customers + 1)]
regions = ['North', 'South', 'East', 'West']
customer_regions = [random.choice(regions) for _ in range(num_customers)]
# %%
# Add customer channel category
channels = ['Retail', 'Wholesale', 'Online']
customer_channels = [random.choice(channels) for _ in range(num_customers)]
# %%
# Create customer DataFrame
customer_df = pd.DataFrame({
    'customer_id': customer_ids,
    'customer_name': customer_names,
    'region': customer_regions,
    'channel_category': customer_channels
})
# %%
# Create sales data
num_sales = 10000  # Number of sales records
sales_dates = np.random.choice(date_range, num_sales)
product_ids = [f'PROD{str(i).zfill(3)}' for i in range(1, 21)]  # 20 unique products
sales_values = np.round(np.random.uniform(10, 500, num_sales), 2)  # Sales amounts between 10 and 500
quantities = np.random.randint(1, 10, num_sales)  # Quantities between 1 and 10

# Randomly assign customers to sales
sales_customer_ids = np.random.choice(customer_ids, num_sales)

# Add currencies
currencies = ['USD', 'EUR', 'GBP', 'JPY']
sales_currencies = np.random.choice(currencies, num_sales)

# Add some randomness and anonymity
for i in range(int(num_sales * 0.05)):  # Anonymize 5% of the data
    sales_customer_ids[i] = np.nan

# Add some anomalies (e.g., very high sales value)
sales_values[np.random.choice(range(num_sales), 20)] *= 10

# Create sales DataFrame
sales_df = pd.DataFrame({
    'sale_id': range(1, num_sales + 1),
    'sale_date': sales_dates,
    'customer_id': sales_customer_ids,
    'product_id': np.random.choice(product_ids, num_sales),
    'quantity': quantities,
    'sales_value': sales_values,
    'currency': sales_currencies
})

# Create a second dimension at the sales level - Sales Channel
sales_df['sales_channel'] = np.random.choice(channels, num_sales)

# Write the DataFrames to CSV files
# Write the DataFrames to CSV files
customer_df.to_csv(os.path.join(output_dir, 'customer_data.csv'), index=False)
sales_df.to_csv(os.path.join(output_dir, 'sales_data.csv'), index=False)

print(f"CSV files 'customer_data.csv' and 'sales_data.csv' have been created in {output_dir}")
