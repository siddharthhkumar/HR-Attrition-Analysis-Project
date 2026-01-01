import mysql.connector

# CONFIGURATION
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",  # <--- Remember to put your password here
    "database": "FaceDataProject" 
}

try:
    # Attempt Connection
    conn = mysql.connector.connect(**db_config)
    
    if conn.is_connected():
        print("-------------------------------------------------")
        print("SUCCESS: Python is connected to MySQL!")
        print(f"Connected to Database: {db_config['database']}")
        print("-------------------------------------------------")
        
        # simple test query
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"Server responded: You are inside '{record[0]}'")

except mysql.connector.Error as err:
    print("-------------------------------------------------")
    print(f"FAILED: {err}")
    print("-------------------------------------------------")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()