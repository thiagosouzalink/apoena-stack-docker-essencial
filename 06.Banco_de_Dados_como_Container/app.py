from typing import Optional

from mysql.connector import connect, MySQLConnection, Error

import config as cfg


def create_connection(host: str, 
                      user: str, 
                      password: str, 
                      db: str,
                      port: str) -> Optional[MySQLConnection]:
    """
    Estabelece uma conexão com o banco de dados MySQL.

    Args:
        host (str): O endereço do servidor MySQL (ex: "localhost").
        user (str): O nome de usuário para acessar o banco de dados.
        password (str): A senha do usuário.
        db (str): O nome do banco de dados a ser acessado.

    Returns:
        Optional[mysql.connector.MySQLConnection]: A conexão com o 
        banco de dados MySQL, ou `None` em caso de erro na conexão.
    """
    try:
        connection = connect(
            host=host,
            user=user,
            password=password,
            database=db,
            port=port
        )
        
        print("Conexão Estabelecida")
        
        return connection
    except Error as e:
        print(f"Erro na conexão: {e}")
        return None


def execute_query(connection: MySQLConnection, 
                  query: str) -> None:
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    
    print("Query executada")
    
    
def main():
    connection = create_connection(
        host=cfg.db_host,
        user=cfg.db_user,
        password=cfg.db_password,
        db=cfg.db_name,
        port=cfg.db_port
    )
    
    create_table = """
    CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT,
        name TEXT NOT NULL,
        age INT,
        PRIMARY KEY(id)
    ) ENGINE = InnoDB;
    """
    
    execute_query(connection, create_table)
    
    insert_user = """
    INSERT INTO users (name, age)
    VALUES ('Jonh Doe', 28);
    """
    
    execute_query(connection, insert_user)
    
    select_users = "SELECT * FROM users;"
    
    cursor = connection.cursor()
    cursor.execute(select_users)
    users = cursor.fetchall()
    
    for user in users:
        print(user)
        
        
if __name__ == "__main__":
    main()