# import sqlite3

# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()

# username = input("Enter username: ")
# password = input("Enter password: ")

# # Vulnerable to SQL Injection
# query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
# cursor.execute(query)
# result = cursor.fetchone()

# if result:
#     print("Login successful!")
# else:
#     print("Invalid credentials!!!")


import sqlite3
import bcrypt

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Take input from the user
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# Basic input validation
if not username or not password:
    print("Username and password cannot be empty.")
    exit()

# Prepare and execute a safe SQL query
cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
record = cursor.fetchone()

if record:
    stored_hashed_password = record[0]
    # Check password against the hashed one
    if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
        print("Login successful!")
    else:
        print("Invalid password.")
else:
    print("Username not found.")

