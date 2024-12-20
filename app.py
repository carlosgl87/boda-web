from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Ruta principal para mostrar la galería
@app.route("/")
def gallery():
    image_folder = os.path.join(app.static_folder, "images")
    images = [f"images/{img}" for img in os.listdir(image_folder)]
    return render_template("index.html", images=images)

# Ruta para servir imágenes
@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(app.static_folder, 'images'), filename)

if __name__ == "__main__":
    app.run(debug=True)