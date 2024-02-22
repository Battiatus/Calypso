from flask import Flask, request, send_from_directory, render_template, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
import os
from converter import evtx_to_json, evtx_to_csv, evtx_to_xml
import tempfile
import shutil

UPLOAD_FOLDER = tempfile.mkdtemp()
ALLOWED_EXTENSIONS = {'evtx'}

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Vérifie si le fichier fait partie de la requête
        if 'file' not in request.files:
            flash('Aucun fichier partie')
            return redirect(request.url)
        
        file = request.files['file']
        
        # Vérifie si l'utilisateur a bien sélectionné un fichier
        if file.filename == '':
            flash('Aucun fichier sélectionné')
            return redirect(request.url)
        
        # Vérifie si le fichier a la bonne extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            output_format = request.form.get('format')
            output_path = filepath.rsplit('.', 1)[0] + '.' + output_format
            
            # Ici, appel à la fonction de conversion appropriée
            if output_format == 'json':
                evtx_to_json(filepath, output_path)
            elif output_format == 'csv':
                evtx_to_csv(filepath, output_path)
            elif output_format == 'xml':
                evtx_to_xml(filepath, output_path)
            else:
                flash('Format de conversion non supporté')
                return redirect(request.url)
            
            return send_file(output_path, as_attachment=True)
        else:
            flash('Extension de fichier non autorisée')
            return redirect(request.url)
    return render_template('index.html')


@app.route('/cleanup', methods=['GET'])
def cleanup():
    shutil.rmtree(UPLOAD_FOLDER)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
