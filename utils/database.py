import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", password="qwerty123", database="account_admin"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def create_connection(self):
        """Create a connection to the MySQL database."""
        if not self.connection or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        return self.connection

    def close_connection(self):
        """Close the MySQL database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        """Execute a query that modifies data (INSERT, UPDATE, DELETE)."""
        db = self.create_connection()
        cursor = db.cursor()
        try:
            cursor.execute(query, params)
            db.commit()
            print("Query executed successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            db.rollback()
        finally:
            cursor.close()
            self.close_connection()

    def fetch_data(self, query, params=None):
        """Fetch data from the database (SELECT)."""
        db = self.create_connection()
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            self.close_connection()

    # CRUD Operations

    # CREATE Operation
    def create(self, table, data):
        """Insert data into a specified table."""
        placeholders = ", ".join(["%s"] * len(data))
        columns = ", ".join(data.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(data.values()))

    # READ Operation
    def read(self, table, where_clause=None, params=None):
        """Read data from a specified table with an optional WHERE clause."""
        query = f"SELECT * FROM {table}"
        if where_clause:
            query += f" WHERE {where_clause}"
        return self.fetch_data(query, params)

    # UPDATE Operation
    def update(self, table, data, where_clause, params):
        """Update data in a specified table with a given WHERE clause."""
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.execute_query(query, tuple(data.values()) + tuple(params))

    # DELETE Operation
    def delete(self, table, where_clause, params):
        """Delete data from a specified table with a given WHERE clause."""
        query = f"DELETE FROM {table} WHERE {where_clause}"
        self.execute_query(query, params)

