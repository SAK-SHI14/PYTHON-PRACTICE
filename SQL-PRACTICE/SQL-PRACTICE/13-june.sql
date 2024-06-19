import mysql.connector

# Establish a connection
conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='database_name'
)

# Print the connection object
print(conn)

# Close the connection
conn.close()