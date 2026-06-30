from flask import Flask, jsonify, request

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
        "version": "1.0",
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
    return jsonify(list(libros.values()))

@app.get("/libros/<int:id>")
def obtener_libro(id):
    libro = libros.get(id)

    if libro:
        return jsonify(libro)
    return jsonify({"error": "libro no encontrado"}),404

@app.post("/libros")
def agregar_libro():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion"})
    if "titulo" not in datos or "autor" not in datos or "disponible" not in datos:
        return jsonify({"error": "Los campos son requeridos"}), 400
    
    nuevo_id = max(libros.keys())+1

    libros[nuevo_id] = {
        "id": nuevo_id,
        "titulo": datos["titulo"],
        "autor": datos["autor"],
        "disponible": datos["disponible"]
    }

    return jsonify(libros[nuevo_id]),201

if __name__ == "__main__":
    app.run(debug=True, port=5001)