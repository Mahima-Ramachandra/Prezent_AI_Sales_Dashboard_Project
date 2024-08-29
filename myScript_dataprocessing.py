import pandas as pd
import requests
import os
from datetime import datetime, timedelta
import numpy as np
import random

def generate_sample_data(output_dir):
    
    np.random.seed(42)

    # date range (last 3 years)
    end_date = datetime.today()
    start_date = end_date - timedelta(days=3*365)
    date_range = pd.date_range(start=start_date, end=end_date)

    # Create customer data
    num_customers = 100
    customer_ids = [f'CUST{str(i).zfill(4)}' for i in range(1, num_customers + 1)] #generates customer IDs like CUST0001, CUST0002, etc.)
    customer_names = [f'Customer_{i}' for i in range(1, num_customers + 1)]
    regions = ['North', 'South', 'East', 'West']
    customer_regions = [random.choice(regions) for _ in range(num_customers)]
    channels = ['Retail', 'Wholesale', 'Online']
    customer_channels = [random.choice(channels) for _ in range(num_customers)]

    customer_df = pd.DataFrame({
        'customer_id': customer_ids,
        'customer_name': customer_names,
        'region': customer_regions,
        'channel_category': customer_channels
    })

    # Create sales data
    num_sales = 10000
    sales_dates = np.random.choice(date_range, num_sales)#random dates for each sale
    product_ids = [f'PROD{str(i).zfill(3)}' for i in range(1, 21)]#creates 20 diff prod ids
    sales_values = np.round(np.random.uniform(10, 500, num_sales), 2)#rand sales val btwn 10 & 500
    quantities = np.random.randint(1, 10, num_sales)#rand quants btwn 1&9
    sales_customer_ids = np.random.choice(customer_ids, num_sales)#rand assigns cutomers to each sales
    currencies = ['USD', 'EUR', 'GBP', 'JPY']
    sales_currencies = np.random.choice(currencies, num_sales)#rand assigns currency to each sale

    # Add some randomness and anonymity
    for i in range(int(num_sales * 0.05)):
        sales_customer_ids[i] = np.nan

    # Add some anomalies
    sales_values[np.random.choice(range(num_sales), 20)] *= 10

    sales_df = pd.DataFrame({
        'sale_id': range(1, num_sales + 1),
        'sale_date': sales_dates,
        'customer_id': sales_customer_ids,
        'product_id': np.random.choice(product_ids, num_sales),
        'quantity': quantities,
        'sales_value': sales_values,
        'currency': sales_currencies,
        'sales_channel': np.random.choice(channels, num_sales)
    })

    # save dfs to CSV files
    customer_df.to_csv(os.path.join(output_dir, 'customer_data.csv'), index=False)
    sales_df.to_csv(os.path.join(output_dir, 'sales_data.csv'), index=False)

    print(f"CSV files 'customer_data.csv' and 'sales_data.csv' have been created in {output_dir}")

    return customer_df, sales_df

def get_exchange_rates():
    url = "https://v6.exchangerate-api.com/v6/c11a2331b51cc2e55732b236/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'conversion_rates' in data:
            return data['conversion_rates']
        else:
            print("Error: 'conversion_rates' not found in API response")
            print("API response:", data)
            raise KeyError("'conversion_rates' key not found in API response")
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        print("Response content:", response.text)
        raise Exception("Failed to fetch exchange rates")

def convert_to_usd(df, exchange_rates):
    def convert(row):
        if row['currency'] != 'USD':
            return row['sales_value'] / exchange_rates[row['currency']]
        return row['sales_value']
    
    df['sales_value_usd'] = df.apply(convert, axis=1)#apply function row by row for rows
    return df

def combine_data(sales_df, customer_df):
    return pd.merge(sales_df, customer_df, on='customer_id', how='left')

def main():
    # output directory
    output_dir = r"C:\Users\h547756\Downloads\My Assignment\OutputFiles"

   
    os.makedirs(output_dir, exist_ok=True)

    # sample data
    customer_df, sales_df = generate_sample_data(output_dir)
    
    # exchange rates
    try:
        exchange_rates = get_exchange_rates()
        print("Exchange rates successfully fetched.")
    except Exception as e:
        print(f"An error occurred while fetching exchange rates: {str(e)}")
        print("Cannot proceed without exchange rates. Exiting the program.")
        return  # Exit the main function

    # check if we have exchange rates else print a msg
    if exchange_rates:
        
        sales_df = convert_to_usd(sales_df, exchange_rates)
        
        
        final_df = combine_data(sales_df, customer_df)
        
        # save df as a Parquet file
        output_file = os.path.join(output_dir, 'final_output.parquet')
        final_df.to_csv(os.path.join(output_dir, 'final_data.csv'), index=False)#for my reference
        print(f"output file path",output_dir)
        final_df.to_parquet(output_file, index=False)
        
        print(f"Final output file has been created: {output_file}")
    else:
        print("No exchange rates available. Cannot create final output file.")

if __name__ == "__main__":
    main()