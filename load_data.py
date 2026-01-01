import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURATION ---
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "1234"  # <--- Make sure this is 1234 (or whatever you set)
DB_NAME = "hr_analytics"     # Double check this exists in Workbench
CSV_FILE = "WA_Fn-UseC_-HR-Employee-Attrition.csv"

try:
    print("1. Reading CSV file...")
    df = pd.read_csv(CSV_FILE)
    print(f"   - Found {len(df)} rows and {len(df.columns)} columns.")

    # 2. CLEANING
    df.columns = [c.replace(' ', '_').replace('-', '_') for c in df.columns]
    print("2. Column names cleaned.")

    print("3. Connecting to MySQL...")
    connection_str = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(connection_str)

    print("4. Uploading data...")
    df.to_sql(name='attrition_data', con=engine, if_exists='replace', index=False)

    print("-------------------------------------------------------")
    print("SUCCESS! Data uploaded to table 'attrition_data'.")
    print("-------------------------------------------------------")

except Exception as e:
    print("-------------------------------------------------------")
    print(f"FAILED: {e}")
    print("-------------------------------------------------------")
    print("Tip 1: Check if password is correct.")
    print("Tip 2: Did you run 'CREATE DATABASE hr_analytics;' in Workbench?")