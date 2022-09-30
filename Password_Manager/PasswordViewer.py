import psycopg2 #Simple program to allow the user to view the passwords saved in their table

host_name = "YOUR HOST NAME HERE"
database_name = input(f"What is the database name? ")
user_name = "YOUR USER NAME HERE"
password_name = input(f"Enter password for {database_name}. ")

conn = psycopg2.connect(
host=host_name,
database=database_name,
user=user_name,
password=password_name)

table_name = "YOUR TABLE NAME HERE"

cursor = conn.cursor()
command = f"""SELECT * FROM {table_name}; """
cursor.execute(command)
print(cursor.fetchall())