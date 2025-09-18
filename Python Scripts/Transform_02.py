# Transforming data in staging tables

import pandas as pd

def transform_customers(df):
    # Turn the string into title case and remove leading/trailing spaces
    df["first_name"] = df["first_name"].str.title().str.strip()
    df["last_name"] = df["last_name"].str.title().str.strip()
    # replace missing emails, signup_date with placeholder
    df["email"] = df["email"].fillna("unknown@email.com")
    df['signup_date'] = df['signup_date'].fillna(pd.Timestamp("9999-01-01"))
    return df

def transform_sales(df):
    # Drop row if quantity<=0 (means invalid transaction)
    df = df[df["quantity"]>0]
    # replace missing transaction_date with placeholder
    df["transaction_date"] = df["transaction_date"].fillna(pd.Timestamp("9999-01-01"))
    # Add a column for total_sale
    df["total_sale"] = df["quantity"] * df["unit_price"]
    return df

if __name__ == "__main__":
    df_cust = pd.read_csv("customers_stg.csv", parse_dates=["signup_date"])
    df_sales = pd.read_csv("sales_stg.csv", parse_dates=["transaction_date"])
    df_cust_transformed = transform_customers(df_cust)
    df_sales_transformed = transform_sales(df_sales)
    df_cust_transformed.to_csv("customers_main.csv", index=False)
    df_sales_transformed.to_csv("sales_main.csv", index=False)
    print("Transformation Completed!")
