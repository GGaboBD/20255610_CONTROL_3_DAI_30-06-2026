from flask import Flask, jsonify, request
from database import obtener_conexion, convertir_fila_a_diccionario

app = Flask(__name__)

# Repositorio temporal de datos (Corregido sin espacios invisibles)
libros = {
    101: {"id": 101, "titulo": "Clean Code", "autor": "Robert C. Martin", "disponible": True},
    102: {"id": 102, "titulo": "Python Crash Course", "autor": "Eric Matthew", "disponible": True},
    103: {"id": 103, "titulo": "Architecture Patterns", "autor": "GoF", "disponible": False}
}

@app.get("/")  # 127.0.0.1:5000
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la app de biblioteca",
        "version": "2.0",
        "almacenamiento": "SQLite",
        "endpoints": [
            "GET /libros",        # Muestra toda la info
            "GET /libros/<id>",   # Info de un libro especifico
            "POST /libros",       # Crear un nuevo libro 
            "PUT /libros/<id>",   # Modificar la disponibilidad
            "DELETE /libros/<id>" # Borrar un libro
        ] 
    })

@app.get("/libros")
def mostrar_libros():

    conexion = obtener_conexion()

    libros = conexion.execute(
        "SELECT * FROM libros"
    ).fetchall()

    conexion.close()

    return jsonify([
        convertir_fila_a_diccionario(libro)
        for libro in libros
    ])

if __name__ == "__main__":
    app.run(debug=True)