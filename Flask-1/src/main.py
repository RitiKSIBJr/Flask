import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = 'C:\\Users\\lette\\OneDrive\\Desktop\\Flask'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File is uploaded'
    
    return 'File not up'




if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)