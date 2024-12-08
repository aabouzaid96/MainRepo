from db_connection import get_connection



def fetch_data():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM accounts_user;")  # Replace 'your_table' with an actual table name
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    fetch_data()