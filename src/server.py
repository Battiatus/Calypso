# src/server.py

from flask import Flask, request, send_from_directory, render_template, redirect, url_for
import os
from converter import evtx_to_json, evtx_to_csv, evtx_to_xml
import tempfile
import shutil

app = Flask(__name__, template_folder='../templates', static_folder='../static')
UPLOAD_FOLDER = tempfile.mkdtemp()
ALLOWED_EXTENSIONS = {'evtx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)
        output_format = request.form['format']
        temp_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(temp_path)
        output_path = os.path.splitext(temp_path)[0] + f'.{output_format}'
        if output_format == 'json':
            evtx_to_json(temp_path, output_path)
        elif output_format == 'csv':
            evtx_to_csv(temp_path, output_path)
        elif output_format == 'xml':
            evtx_to_xml(temp_path, output_path)
        return send_from_directory(directory=os.path.dirname(output_path), filename=os.path.basename(output_path), as_attachment=True)
    return render_template('index.html')

@app.route('/cleanup', methods=['GET'])
def cleanup():
    shutil.rmtree(UPLOAD_FOLDER)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
