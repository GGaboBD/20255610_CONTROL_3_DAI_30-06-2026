from flask import Flask, jsonify, request

app = Flask(__name__)

# Repositorio temporal de datos (Corregido sin espacios invisibles)
libros = {
    101: {"id": 101, "titulo": "Clean Code", "autor": "Robert C. Martin", "Disponible": True},
    102: {"id": 102, "titulo": "Python Crash Course", "autor": "Eric Matthew", "Disponible": True},
    103: {"id": 103, "titulo": "Architecture Patterns", "autor": "GoF", "Disponible": False}
}

@app.get("/")  # 127.0.0.1:5000
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la app de biblioteca",
        "version": "1.0",
        "endpoints": [
            "GET /libros",        # Muestra toda la info
            "GET /libros/<id>",   # Info de un libro especifico
            "POST /libros",       # Crear un nuevo libro 
            "PUT /libros/<id>",   # Modificar la disponibilidad
            "DELETE /libros/<id>" # Borrar un libro
        ] 
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)