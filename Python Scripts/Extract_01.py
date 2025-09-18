# Extracting csv tables

import pandas as pd

def extract_customers (filepath="customers.csv"):
    return pd.read_csv(filepath, parse_dates=["signup_date"])

def extract_sales(filepath="sales.csv"):
    return pd.read_csv(filepath, parse_dates=["transaction_date"])

if __name__ == "__main__":
    df_cust = extract_customers()
    print(df_cust)
    df_sales = extract_sales()
    print(df_sales)

    # Save to staging files
    df_cust.to_csv("customers_stg.csv", index=False)
    df_sales.to_csv("sales_stg.csv", index=False)
    print("Extraction Completed!")
