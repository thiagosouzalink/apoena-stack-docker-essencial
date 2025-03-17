import sqlite3
import os


DATABASE = "/app/data/database.db"

def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    print("Database Inicializada")    
    
    
def data_entry(name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO entries (name) VALUES (?)
    """, (name,))
    conn.commit()
    cursor.close()
    print(f"O {name} foi inserido na Database Inicializada")
    
def get_entries():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    conn.close()
    
    print(entries)
    for entry in entries:
        print(entry)
        
        
def main():
    while True:
        print("Opções:")
        print()
        print("1. Iniciar DB")
        print("2. Inserir Nome")
        print("3. Listar Nomes")
        print("4. Exit")
        user_input = input("Insira uma opção: ")
        
        if user_input == "1":
            init_db()
        elif user_input == "2":
            name = input("Insira um nome para registrar: ")
            data_entry(name)
        elif user_input == "3":
            get_entries()
        elif user_input == "4":
            break
        else:
            print("Opção inválida, tente novamente\n")
    

if __name__ == "__main__":
    main()