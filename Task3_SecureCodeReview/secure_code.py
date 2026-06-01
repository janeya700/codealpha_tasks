import sqlite3
import hashlib

# Database connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# FIX 1 - SQL Injection Fixed
username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

# FIX 2 - Password Hashing
new_password = "admin123"
hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
cursor.execute("INSERT INTO users VALUES (?, ?)", ("admin", hashed_password))

# FIX 3 - Input Validation
age = input("Enter your age: ")
if age.isdigit() and 0 < int(age) < 150:
    cursor.execute("INSERT INTO profile VALUES (?)", (int(age),))
else:
    print("Invalid age!")

conn.commit()
conn.close()
