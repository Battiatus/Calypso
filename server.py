from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Traiter les fichiers uploadés et les convertir
    return 'Fichiers reçus'

@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    # Envoyer le fichier converti au client
    return send_from_directory(directory='chemin_vers_les_fichiers_convertis', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
