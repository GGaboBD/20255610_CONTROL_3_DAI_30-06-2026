from database import obtener_conexion

def crear_base_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            disponible INTEGER NOT NULL
        )
                    """)
    
        # Arriba creamos la tabla sin datos
    
    cursor.execute("SELECT COUNT(*) FROM libros")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO libros(titulo, autor, disponible) VALUES(?, ?, ?)",
            [
                ("Clean Code", "Robert C. Martin", 1),
                ("Python Crash Course", "Erick Matthes", 1),
                ("Design Thinking", "GoF", 0)
            ]
        )
    
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_base_datos()