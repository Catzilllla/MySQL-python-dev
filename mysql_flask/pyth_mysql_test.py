from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector
from app_flask.app import site_m

SQL1 = "SHOW tables in mydata_base_command_pyth"
SQL2 = "CREATE TABLE categories (id INT PRIMARY KEY, id_category INT, name_category VARCHAR(100) NOT NULL);"

table = 'categories'
SQL2_1 = "DROP TABLE %()"

SQL3 = """
SELECT * FROM categories
"""

SQL3_1 = "UPDATE categories SET name_category = 'Forest Gump'"
SQL3_2 = "INSERT INTO categories (id, id_category, name_category) VALUES (id, 485948, 'ndfdsfkdsfds')"


SQL5 = """
CREATE TABLE author_2(
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE book (
    id INTEGER PRIMARY KEY, 
    title VARCHAR, 
    year INTEGER, 
    author_id INTEGER, 
    FOREIGN KEY(author_id) REFERENCES author(id)
); 
"""

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def create_server_connection(host_name, user_name, user_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
        print("\n\n===========SHOW DB's===========\n")
        show_db = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db)
            for db in cursor:
                print(db)
        print("===============================\n\n")
            
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection):
    cursor = connection.cursor()
    try:
        paramstyle = mysql.connector.paramstyle
        if paramstyle == 'qmark':
            ph = "?"
        elif paramstyle == 'pyformat':
            ph = "%s"
        else:
            raise Exception("Unexpected paramstyle: %s" % paramstyle)

        ph_ist = [('d11gh1g1'), ('ds22g2f2ds'), ('d3s3f3d3s3f')]

        sql_s = "INSERT INTO categories VALUES (%(ph)s, %(ph)s, %(ph)s)" % { "ph" : ph_ist }

        cursor.execute(SQL3)

        result = cursor.fetchall()
        for row in result:
            print(row)
        connection.commit()
        print("Query successful")

    except Error as err:
        print(f"Error: '{err}'")


if __name__ == "__main__":

    host_name = "localhost"
    user_name = "catzi"
    user_password = "483H36XQl!"
    db_name = "mydata_base_command_pyth"

    connection = create_server_connection(host_name, user_name, user_password, db_name)

    execute_query(connection)

    site_m()
