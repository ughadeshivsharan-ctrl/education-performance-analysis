import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Connection
username = "root"
password = quote_plus("Shiva@3613")
database = "360_education_db"
port = 3306

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@localhost:{port}/{database}"
)

# Excel File
excel_file = r"C:\Users\LENOVO\Documents\python project\New folder\basic python.py\powerbi project\360_Education_Business_Analytics_Dataset.xlsx"

# Read all sheets
all_sheets = pd.read_excel(
        excel_file,
        sheet_name=None
)

# Insert into MySQL
for sheet_name, sheet_df in all_sheets.items():

    table_name = sheet_name.strip().lower()

    try:

        sheet_df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} inserted successfully.")

    except Exception as e:

        print(f"Error in {table_name}")
        print(e)


print("\nAll sheets have been processed.")