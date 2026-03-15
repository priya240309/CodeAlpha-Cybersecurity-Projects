

import sqlite3

print("=== Simple Login System ===")

# connecting to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# creating table
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")

username = input("Enter username: ")
password = input("Enter password: ")

# Vulnerable SQL query (SQL Injection risk)
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful!")
else:
    print("Invalid credentials")

conn.close()