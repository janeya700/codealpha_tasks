import sqlite3

# Database connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# VULNERABILITY 1 - SQL Injection
username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)

# VULNERABILITY 2 - Plain Text Password
new_password = "admin123"
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")

# VULNERABILITY 3 - No Input Validation
age = input("Enter your age: ")
print("Your age is: " + age)
cursor.execute("INSERT INTO profile VALUES (" + age + ")")

conn.commit()
conn.close()
