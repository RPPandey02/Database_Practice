import sqlite3

# Connect to SQLite database (creates a new one if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table for employees
cursor.execute('''CREATE TABLE employees
                (id INTEGER PRIMARY KEY, name TEXT, department TEXT)''')

# Insert some data into the employees table
cursor.execute("INSERT INTO employees (name, department) VALUES ('John Doe', 'HR')")
cursor.execute("INSERT INTO employees (name, department) VALUES ('Jane Smith', 'Engineering')")
cursor.execute("INSERT INTO employees (name, department) VALUES ('Mark Johnson', 'Finance')")

# Create a table for tasks
cursor.execute('''CREATE TABLE tasks
                (id INTEGER PRIMARY KEY, task_name TEXT, employee_id INTEGER)''')

# Insert some data into the tasks table
cursor.execute("INSERT INTO tasks (task_name, employee_id) VALUES ('Hiring', 1)")
cursor.execute("INSERT INTO tasks (task_name, employee_id) VALUES ('Coding', 2)")
cursor.execute("INSERT INTO tasks (task_name, employee_id) VALUES ('Budgeting', 3)")

# Commit changes to the database
conn.commit()

# Perform a LEFT JOIN query
left_join_query = """
    SELECT employees.name, employees.department, tasks.task_name
    FROM employees
    LEFT JOIN tasks ON employees.id = tasks.employee_id
"""

print("Left Join Result:")
for row in cursor.execute(left_join_query):
    print(row)

# Perform a RIGHT JOIN query
right_join_query = """
    SELECT employees.name, employees.department, tasks.task_name
    FROM employees
    RIGHT JOIN tasks ON employees.id = tasks.employee_id
"""

print("\nRight Join Result:")
for row in cursor.execute(right_join_query):
    print(row)

# Close the connection
conn.close()
