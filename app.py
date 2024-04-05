from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/characters-json')
def characters_json():
    # Obtener los datos de los personajes directamente desde la caché
    # Realizar la solicitud a la API de Rick and Morty
    url = "https://rickandmortyapi.com/api/character"
    characters = requests.get(url, headers={'X-Cache': 'True'}).json()['results']
    return jsonify(characters)

if __name__ == '__main__':
    app.run(debug=True)