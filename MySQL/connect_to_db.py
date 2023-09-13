import os
import bcrypt
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from .env file
load_dotenv()

# Get environment variables for DB connection and password hashing
db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")
pepper = os.environ.get("AUTH_PEPPER")


# Function to encrypt password
def hash_password(password):
    salted_password = password + pepper
    return bcrypt.hashpw(salted_password.encode("UTF-8"), bcrypt.gensalt())


# Function to validate password
def check_password(user_password, hashed_password):
    peppered_user_password = f"{user_password}{pepper}"
    return bcrypt.checkpw(peppered_user_password.encode("UTF-8"), hashed_password)


# Function to connect to MySQL DB
def connect_to_db():
    return mysql.connector.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )


# Main code
if __name__ == "__main__":
    # The code below is only run when run directly from this module

    # Connect to MySQL DB
    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    # Your SQL queries and other database operations go here

    # Don't forget to close the connection
    cursor.close()
    db_connection.close()

    # Password hashing and checking (for demonstration)
    my_password = "abc123"
    hashed_password = hash_password(my_password)

    user_password = input("Please input your password for testing: ")

    if check_password(user_password, hashed_password):
        print("Password successful. Access granted.")
    else:
        print("Incorrect password. Access denied.")
