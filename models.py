import mysql.connector
from config import Config

class Database:
    def __init__(self):
        app_config = Config()
        self.db = mysql.connector.connect(
            host=app_config.DATABASE_HOST,
            user=app_config.DATABASE_USER,
            password=app_config.DATABASE_PASSWORD,
            database=app_config.DATABASE_NAME,
            port=app_config.DATABASE_PORT
        )

    # database operations

    def insert_data(self, table_name, **data):
        cursor = self.db.cursor()
        try:
            # Dynamically create the SQL query for insertion based on the table_name
            column_names = ', '.join(data.keys())
            value_placeholders = ', '.join(['%s'] * len(data))
            insert_query = f"INSERT INTO {table_name} ({column_names}) VALUES ({value_placeholders})"
            values = tuple(data.values())

            cursor.execute(insert_query, values)
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            self.db.rollback()
            raise Exception(f"Failed to insert data into {table_name}: {str(err)}")
        finally:
            cursor.close()

    # FETCH ALL DATA IN A TABLE
    def fetch_all_data(self, table_name):
        cursor = self.db.cursor(dictionary=True)
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()
            return data
        except mysql.connector.Error as err:
            error_message = f"Failed to fetch data from {table_name}: {str(err)}"
            return error_message  # Return the custom error message
        finally:
            cursor.close()

    # FETCH DATA IN A SPECIFIC COLUMNS (MULTIPLE COLUMNS)
    def fetch_columns_data(self, table_name, column_names):
        cursor = self.db.cursor(dictionary=True)
        try:
            columns = ', '.join(column_names)
            cursor.execute(f"SELECT {columns} FROM {table_name}")
            data = cursor.fetchall()
            return data
        except mysql.connector.Error as err:
            error_message = f"Failed to fetch data from {table_name}: {str(err)}"
            return error_message  # Return the custom error message
        finally:
            cursor.close()

    # FETCH ALL DATA WITH CONDITION OR NOT
    def select_all(self, table_name, condition_column=None, condition_value=None):
        cursor = self.db.cursor(dictionary=True)
        try:
            if condition_column and condition_value:
                # If a condition is provided, add it to the SQL query
                select_query = f"SELECT * FROM {table_name} WHERE {condition_column} = %s"
                cursor.execute(select_query, (condition_value,))
            else:
                # If no condition is provided, select all rows from the table
                cursor.execute(f"SELECT * FROM {table_name}")

            data = cursor.fetchall()
            return data
        except mysql.connector.Error as err:
            error_message = f"Failed to fetch data from {table_name}: {str(err)}"
            return error_message  # Return the custom error message
        finally:
            cursor.close()

    # UPDATE DATA IN A TABLE WITH CONDITION
    def update_data(self, table_name, where_column, where_value, **data):
        cursor = self.db.cursor(dictionary=True)  # Use a dictionary cursor for easier data retrieval
        try:
            set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
            update_query = f"UPDATE {table_name} SET {set_clause} WHERE {where_column} = %s"
            values = list(data.values()) + [where_value]

            cursor.execute(update_query, values)
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            self.db.rollback()
            error_message = f"Error updating data in {table_name}: {str(err)}"
            return error_message
        finally:
            cursor.close()

    # DELETE A DATA IN TABLE WITH CONDITION
    def delete_data(self, table_name, where_column, where_value):
        cursor = self.db.cursor()
        try:
            # Dynamically create the SQL query for delete based on the table_name
            delete_query = f"DELETE FROM {table_name} WHERE {where_column} = %s"
            cursor.execute(delete_query, (where_value,))
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            self.db.rollback()
            error_message = f"Error deleting data from {table_name}: {str(err)}"
            return error_message  # Return the custom error message
        finally:
            cursor.close()

    # JOIN MULTIPLE TABLE USING CONDITION (COLUMN)
    def join_multiple_tables(self, table_names, join_columns):
        cursor = self.db.cursor(dictionary=True)
        try:
            if len(table_names) < 2 or len(table_names) - 1 != len(join_columns):
                return "Invalid number of tables or join columns"

            join_query = f"SELECT * FROM {table_names[0]}"
            for i in range(1, len(table_names)):
                join_query += f" JOIN {table_names[i]} ON {table_names[i - 1]}.{join_columns[i - 1]} = {table_names[i]}.{join_columns[i - 1]}"

            cursor.execute(join_query)
            data = cursor.fetchall()
            return data
        except mysql.connector.Error as err:
            error_message = f"Failed to join tables: {str(err)}"
            return error_message  # Return the custom error message
        finally:
            cursor.close()

    def get_user_by_username(self, username):
        cursor = self.db.cursor(dictionary=True)
        try:
            query = "SELECT * FROM tbl_admin_users WHERE username = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            return user
        except mysql.connector.Error as err:
            error_message = f"Failed to fetch user by username: {str(err)}"
            return None
        finally:
            cursor.close()

    def get_seller_user_by_username(self, username):
        cursor = self.db.cursor(dictionary=True)
        try:
            query = "SELECT * FROM tbl_farmer_users WHERE username = %s"
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            return user
        except mysql.connector.Error as err:
            error_message = f"Failed to fetch user by username: {str(err)}"
            return None
        finally:
            cursor.close()