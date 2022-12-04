import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = 'C:\\Users\\lette\\OneDrive\\Desktop\\Flask'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/urluploader", methods=['GET', 'POST'])
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
        url = str(request.form.get("url"))
        if url:
            with open('urls.txt', 'a') as file:
                file.write(url + '\n')
            return url
        else:
            return 'URL is empty'
    




if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)