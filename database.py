import sqlite3

# Constante con mi "base de datos"
DATABASE = "biblioteca.db" # nombre

def obtener_conexion():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory  = sqlite3.Row # Las lineas generadas de una consulta  en SQLserver se traten como objetos 'row' de Sqlite
    return conexion

def convertir_fila_a_diccionario(fila):
    return {
        "id": fila["id"],
        "titulo": fila["titulo"],
        "autor": fila["autor"],
        "disponible": bool(fila["disponible"])
    }
