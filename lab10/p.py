import psycopg2
import csv

# Подключение к БД
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345678"
)

# Создание таблицы phonebook
def create_phonebook_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
    """
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

# Чтение csv файла
def insert_from_csv(phonebook):
    command = "INSERT INTO phonebook(name, phone) VALUES (%s, %s)"
    with open(phonebook, "r") as csvfile:
        reader = csv.reader(csvfile)
        # next(reader) - если в файле бывают заголовки
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook")
            for row in reader:
                name = row[0]
                phone = row[1]
                cur.execute(command, (name, phone))
            conn.commit()


# Работа с консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with conn.cursor() as cur:
        cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()

# Обновление данных
def update_user(old_name, new_name=None, new_phone=None):
    with conn.cursor() as cur:
        if new_name:
            cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
        if new_phone:
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, old_name))
        conn.commit()

# Фильтр (поиск)
def search_users(filter_text):
    query = "SELECT * FROM phonebook WHERE name ILIKE %s OR phone LIKE %s"
    with conn.cursor() as cur:
        cur.execute(query, (f"%{filter_text}%", f"%{filter_text}%"))
        results = cur.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")

# Удаление
def delete_user(identifier):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (identifier, identifier))
        conn.commit()

# Меню
def main():
    create_phonebook_table()
    while True:
        print("\n PhoneBook Menu:")
        print("1. Upload from CSV")
        print("2. Insert from console")
        print("3. Update user")
        print("4. Search user")
        print("5. Delete user")
        print("6. Exit")
        choice = input("Select option: ")

        if choice == '1':
            insert_from_csv("phonebook.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            old_name = input("Old name: ")
            new_name = input("New name (or leave blank): ") or None
            new_phone = input("New phone (or leave blank): ") or None
            update_user(old_name, new_name, new_phone)
        elif choice == '4':
            search = input("Search: ")
            search_users(search)
        elif choice == '5':
            ident = input("Enter name or phone to delete: ")
            delete_user(ident)
        elif choice == '6':
            break
        else:
            print("Invalid option.")

    conn.close()

if __name__ == "__main__":
    main()
