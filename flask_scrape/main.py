from flask import Flask, render_template, request, redirect, url_for, session
import requests
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route("/", methods=['POST', 'GET'])
@app.route('/index/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        session['url'] = request.form["url"]
        return redirect(url_for('upload'))
    return render_template('index.html')

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
    url = session.get('url', None)
    return render_template('result.html', url=url)
    
@app.route('/scrape/')
def scrape():
    url = session.get('url', None)
    response = requests.get(url)
    result = response.content
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO `scrape-sastodeal`(`URL`, `Scrape-content`) VALUES (%s, %s) ''', (url, result))
    mysql.connection.commit()
    cursor.close()
    return render_template('res.html')



app.run(debug=True)