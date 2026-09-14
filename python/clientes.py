import os

import mariadb
from dotenv import load_dotenv

# Cargar las variables de configuración desde el archivo .env.
load_dotenv()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("MARIADB_DATABASE")
DB_USER = os.getenv("MARIADB_USER")
DB_PASSWORD = os.getenv("MARIADB_PASSWORD")


def conectar():
    """Establecer y devolver una conexión con la base de datos MariaDB."""
    
    
    return mariadb.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def crear_tabla(cursor):
    """Crear la tabla clientes si todavía no existe."""
    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL
        )
    """)


def insertar_clientes(cursor):
    """Insertar tres clientes de prueba mediante una consulta parametrizada."""
    
    
    clientes = [
        ("Juan",),
        ("María",),
        ("Pedro",)
    ]

    cursor.executemany(
        "INSERT INTO clientes (nombre) VALUES (?)",
        clientes
    )


def listar_clientes(cursor):
    """Obtener y mostrar todos los clientes ordenados por ID."""
    
    
    cursor.execute("SELECT id, nombre FROM clientes ORDER BY id")

    clientes = cursor.fetchall()

    print("\n LISTADO DE CLIENTES ")

    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nombre: {cliente[1]}")


def buscar_cliente(cursor, cliente_id):
    """Buscar y mostrar un cliente utilizando su ID."""
    
    
    cursor.execute(
        "SELECT id, nombre FROM clientes WHERE id = ?",
        (cliente_id,)
    )

    cliente = cursor.fetchone()

    print("\nBUSCAR CLIENTE")

    if cliente:
        print(f"ID: {cliente[0]}, Nombre: {cliente[1]}")
    else:
        print(f"No existe ningún cliente con ID {cliente_id}")


def modificar_cliente(cursor, cliente_id, nuevo_nombre):
    """Modificar el nombre de un cliente mediante su ID."""
    
    
    cursor.execute(
        "UPDATE clientes SET nombre = ? WHERE id = ?",
        (nuevo_nombre, cliente_id)
    )

    print("\n MODIFICAR CLIENTE ")

    if cursor.rowcount > 0:
        print(f"Cliente {cliente_id} modificado correctamente.")
    else:
        print(f"No existe ningún cliente con ID {cliente_id}")


def eliminar_cliente(cursor, cliente_id):
    """Eliminar un cliente utilizando su ID."""
    
    
    cursor.execute(
        "DELETE FROM clientes WHERE id = ?",
        (cliente_id,)
    )

    print("\n ELIMINAR CLIENTE ")

    if cursor.rowcount > 0:
        print(f"Cliente {cliente_id} eliminado correctamente.")
    else:
        print(f"No existe ningún cliente con ID {cliente_id}")


def main():
    """Funcion main"""
    
    
    connection = None
    cursor = None

    try:
        connection = conectar()
        cursor = connection.cursor()

        print("Conexión realizada correctamente.")

        crear_tabla(cursor)
        connection.commit()

        # Evitar insertar indefinidamente los datos de prueba.
        cursor.execute("SELECT COUNT(*) FROM clientes")
        cantidad = cursor.fetchone()[0]

        if cantidad == 0:
            insertar_clientes(cursor)
            connection.commit()
            print("\n INSERCIÓN ")
            print("Se han insertado 3 clientes.")
        else:
            print("\n INSERCIÓN ")
            print("Ya existen clientes. No se insertan datos de prueba.")

        listar_clientes(cursor)

        buscar_cliente(cursor, 1)

        modificar_cliente(cursor, 1, "Juan Modificado")
        connection.commit()

        listar_clientes(cursor)

        eliminar_cliente(cursor, 3)
        connection.commit()

        listar_clientes(cursor)

    except mariadb.Error as error:
        print(f"Error de MariaDB: {error}")

        if connection:
            connection.rollback()

    except ValueError as error:
        print(f"Error en la configuración: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()

        print("\nConexión cerrada.")


if __name__ == "__main__":
    main()