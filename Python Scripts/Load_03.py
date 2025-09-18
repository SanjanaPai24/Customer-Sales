# Loading cleaned up data into SQL table
# Data is loaded to SQL server DB in the local machine

from sqlalchemy import create_engine
import pandas as pd

def load_to_db(cust_file, sales_file, db_url = "mssql+pyodbc://localhost\\SERVERNAME/DataBaseName?driver=ODBC+Driver+17+for+SQL+Server"):
    engine = create_engine(db_url)
    # Load customers and sales table
    df_cust = pd.read_csv(cust_file, parse_dates=["signup_date"])
    df_sales = pd.read_csv(sales_file, parse_dates=["transaction_date"])
    df_cust.to_sql("customers", engine, if_exists="replace", index=False)
    df_sales.to_sql("sales", engine, if_exists="replace", index=False)
    print("Loading to SQL tables completed!")

if __name__ == "__main__":
    load_to_db("customers_main.csv", "sales_main.csv")



#########################################    OPTIONAL    #####################################################################################

# To check if the connection can be established to SQL server DB

from sqlalchemy import create_engine

# # Replace with your actual database info (db_url = "mssql+pyodbc://sa:@localhost/MyDatabase?driver=ODBC+Driver+17+for+SQL+Server")
db_url = "mssql+pyodbc://localhost\\SERVERNAME/DataBaseName?driver=ODBC+Driver+17+for+SQL+Server"

# # Create engine
engine = create_engine(db_url)

# # Connect to the database
connection = engine.connect()
print("Connected to SQL Server.")

# # Close the connection
connection.close()
print("Connection closed.")
