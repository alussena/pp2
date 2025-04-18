import psycopg2
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

#inserting user info from csv 
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 2:
                continue
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )
    conn.commit()

#inserting user info from console
def insert_from_console():
    name = input("Enter user name: ")
    phone = input("Enter user phone: ")
    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()

#updating user info
def update_user():
    id = input("Enter user id: ")

    cur.execute("SELECT * FROM phonebook WHERE id = %s", (id,))
    if not cur.fetchone():
        print(f"No user found with id {id}.")
        return
    
    name = input("Enter new user name (or click 'Enter' to skip): ")
    phone = input("Enter new user phone (or click 'Enter' to skip): ")
    if name:
        cur.execute("UPDATE phonebook SET name = %s WHERE id = %s", (name, id))
        print(f"User with id {id} was updated.")
    if phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (phone, id))
        print(f"User with id {id} was updated.")
    conn.commit()

#searching user by filter
def search_user():
    print("Enter filter or click 'Enter' to skip")
    name_filter = input("Enter name or part: ").strip()
    phone_filter = input("Enter phone or part: ").strip()
    query = "SELECT * FROM phonebook WHERE TRUE"
    params = []

    if name_filter:
        query += " AND name ILIKE %s"
        params.append(f"%{name_filter}%")
    if phone_filter:
        query += " AND phone ILIKE %s"
        params.append(f"%{phone_filter}%")

    cur.execute(query, params)
    rows = cur.fetchall()

    if rows:
        print("\nResults:")
        for row in rows:
            print(f"id: {row[0]}, name: {row[1]}, phone: {row[2]}")
    else:
        print("Null")

#searching by pattern
def search_user_by_pattern():
    string = input("Enter patern to search: ")
    pattern = f"%{string}%"
    query = "SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s"
    cur.execute(query, (pattern, pattern))
    rows = cur.fetchall()
    if rows:
        print("\nResults:")
        for row in rows:
            print(f"id: {row[0]}, name: {row[1]}, phone: {row[2]}")
    else:
        print("Null")

#deleting users by filter
def delete_user():
    print("Delete user by: \n1. id \n2. name \n3. phone: ")
    choice = int(input())

    if choice==1:
        id = input("Enter id: ")
        cur.execute("SELECT * FROM phonebook WHERE id = %s", (id,))
        if cur.fetchone():
            cur.execute("DELETE FROM phonebook WHERE id = %s", (id,))
            conn.commit()
            print(f"User with id {id} was deleted.")
        else:
            print(f"No user found with id {id}.")

    elif choice==2:
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
        if cur.fetchone():
            cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
            conn.commit()
            print(f"User with name {name} was deleted.")
        else:
            print(f"No user found with name {name}.")

    elif choice==3:
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
        if cur.fetchone():
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
            conn.commit()
            print(f"User with phone {phone} was deleted.")
        else:
            print(f"No user found with phone {phone}.")
    else:
        print("Wrong choice. Please try again")

#searching by pattern procedure
# CREATE OR REPLACE FUNCTION search_users_by_pattern(p_pattern TEXT)
# RETURNS TABLE (
#     id INT,
#     name VARCHAR,
#     phone VARCHAR
# )
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     RETURN QUERY
#     SELECT *
#     FROM phonebook
#     WHERE name ILIKE '%' || p_pattern || '%'
#        OR phone ILIKE '%' || p_pattern || '%';
# END;
# $$;
def search_users_by_pattern_sql():
    pattern = input("Enter patern to search: ")
    cur.execute("SELECT * FROM search_users_by_pattern(%s);", (pattern,))
    results = cur.fetchall()

    if results:
        print("\nResults:")
        for row in results:
            print(row)
    else:
        print("Null")

#insert or update user procedure
# CREATE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
#         UPDATE phonebook SET phone = p_phone WHERE name = p_name;
#     ELSE
#         INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
#     END IF;
# END;
# $$;
def insert_or_update_user_procedure(name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()

#delete by name or phone procedure
# CREATE OR REPLACE PROCEDURE delete_user_by_name(p_name VARCHAR)
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     DELETE FROM phonebook WHERE name = p_name;
# END;
# $$;

# CREATE PROCEDURE delete_user_by_phone(p_phone VARCHAR(12))
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     DELETE FROM phonebook WHERE phone = p_phone;
# END;
# $$;
def delete_procedure():
    print("Delete user by: \n1. Name \n2. Phone")
    choice = int(input())
    if choice == 1:
        name = input("Enter user name: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
        if cur.fetchone():
            cur.execute("CALL delete_user_by_name(%s);", (name,))
        else:
            print("User does not exist")
    elif choice == 2:
        phone = input("Enter user phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
        if cur.fetchone():
            cur.execute("CALL delete_user_by_phone(%s);", (phone,))
        else:
            print("User does not exist")
    else:
        print("Wrong choice. Please, try again")


# insert_from_csv("contacts.csv")
# insert_from_console()
# update_user()
# search_user()
# delete_user()
insert_or_update_user_procedure("Alua", "87088481958")

cur.close()
conn.close()
