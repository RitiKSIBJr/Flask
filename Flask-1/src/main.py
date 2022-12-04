import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'C:/lette/OneDrive/Desktop/Flask'

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
        return flash('File Uploaded Successfully')
    
    return flash('File not up')




if __name__ == "__main__":
    app.run(debug=True)