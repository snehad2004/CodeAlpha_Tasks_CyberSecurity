# import sqlite3

# # Create or connect to a database
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()

# # Create a table named 'users'
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     username TEXT,
#     password TEXT
# )
# ''')

# # Add one user
# cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")

# conn.commit()
# conn.close()
# print("✅ Database and sample user created.")




import sqlite3
import bcrypt

# Create or overwrite the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Drop existing users table if it exists
cursor.execute("DROP TABLE IF EXISTS users")

# Create the users table
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")

# Create bcrypt-hashed password
password = "admin123"
hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Insert the test user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", hashed_password.decode()))

conn.commit()
conn.close()

print("User 'admin' created with bcrypt password.")
