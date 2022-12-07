import os
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import requests



UPLOAD_FOLDER = 'C:\\Users\\lette\\OneDrive\\Desktop\\Flask\\Flask-1\\src'
dir = 'C:\\Users\\lette\\OneDrive\\Desktop\\Flask\\Flask-1\\src'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def url_uploader():
    return render_template('url.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File is uploaded'
    
    return 'File not up'

@app.route('/urlinput', methods=['GET', 'POST'])
def get_url():
    if request.method == "POST":
        url = request.form.get("url")
        response = requests.get(url)  


        with open('src/static/fb.ico', 'wb+') as f:
            f.write(response.content)
           
        
        return send_from_directory(dir,path='static/img')

    else: 
        return 'Null'




if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)