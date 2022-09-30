import psycopg2 #Program used to insert randomly generated passwords into an SQL table
import string
import random

def password_generator(size, special):
    if(special == 'Y'):
        chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + '!' + '@' + '#' + '$' + '%' + '^' + '&' + '*'
        
        password = random.choice(string.punctuation)
        size -= 1
        for _ in range(size):
            password += (random.choice(chars))

        return password
    elif(special =='N'):
        chars=string.ascii_uppercase + string.digits + string.ascii_lowercase

        return ''.join(random.choice(chars) for _ in range(size))

number_of_characters = input("How long should the password be? ")

while(not number_of_characters.isnumeric()):
    number_of_characters = input("How long should the password be? ")

PW_length = int(number_of_characters)

SC_choice = input("Include Special Characters (Y/N)? ").capitalize()

while(SC_choice != 'Y' and SC_choice != 'N'):
    SC_choice = input("Include Special Characters (Y/N)? ").capitalize()

password = password_generator(PW_length,SC_choice)

print('\n',"Password Generated !",'\n')
confirm = 'N'

while(confirm != 'Y'):
    username = input("What is the username? ")
    confirm = input("Is %s correct (Y/N)? " %username ).capitalize()

    while(confirm != 'Y' and confirm != 'N'):
        confirm = input("Is %s correct (Y/N)? " %username).capitalize()

print('\n',"Username saved as %s !" %username,'\n')
confirm = 'N'

while(confirm != 'Y'):
    program = input("What is the program or website name? ")
    confirm = input("Is %s correct (Y/N)? " %program)

    while(confirm != 'Y' and confirm != 'N'):
        confirm = input("Is %s correct (Y/N)? "%program)

print('\n',"Program/Website name saved as %s"%program,'\n')

host_name = "YOUR HOST NAME HERE"
database_name = "YOUR DATABASE NAME HERE"
user_name = "YOUR USERNAME HERE"
password_name = "YOUR PASSWORD HERE"

conn = psycopg2.connect(
host=host_name,
database=database_name,
user=user_name,
password=password_name)

table_name = "YOUR TABLE NAME HERE"
column_for_websites = "YOUR COLUMN NAME HERE"
column_for_usernames = "YOUR COLUMN NAME HERE"
column_for_passwords = "YOUR COLUMN NAME HERE"

cursor = conn.cursor()
command = f"""INSERT INTO {table_name} ({column_for_websites}, {column_for_usernames}, {column_for_passwords})
VALUES ('{program}', '{username}', '{password}'); """
cursor.execute(command)
conn.commit()
cursor.close()
conn.close()

print("Inserted successfully to table, run PasswordViewer.py to see all passwords.")