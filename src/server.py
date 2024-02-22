from flask import Flask, request, render_template, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
from converter import evtx_to_json, evtx_to_csv, evtx_to_xml  # Assurez-vous que les chemins d'importation sont corrects

app = Flask(__name__, template_folder='../templates', static_folder='../static')
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'evtx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier part.'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné.'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Ici, choisissez le format de conversion en fonction de votre logique
        output_format = request.form.get('format', 'json')  # Exemple : obtenir le format depuis le formulaire
        if output_format == 'json':
            output_filepath = filepath + '.json'
            evtx_to_json(filepath, output_filepath)
        elif output_format == 'csv':
            output_filepath = filepath + '.csv'
            evtx_to_csv(filepath, output_filepath)
        elif output_format == 'xml':
            output_filepath = filepath + '.xml'
            evtx_to_xml(filepath, output_filepath)
        else:
            return jsonify({'error': 'Format de conversion non supporté.'}), 400
        return send_from_directory(directory=os.path.dirname(output_filepath), filename=os.path.basename(output_filepath), as_attachment=True)
    return jsonify({'error': 'Extension de fichier non autorisée.'}), 400

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
