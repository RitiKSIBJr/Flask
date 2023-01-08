from flask import Flask, render_template, request, redirect, url_for, session
import requests
from bs4 import BeautifulSoup
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

# database
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
    productName, productPrice = product_and_price()
    print(productName, productPrice)
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO `sastodeal`(`URL`, `Product_Name`, `Product_Price`) VALUES (%s,%s,%s)''',(url, productName, productPrice))
    mysql.connection.commit()
    cursor.close()
    return render_template('res.html')


def product_and_price():
    url = session.get('url', None)
    if url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        product = soup.find("span", attrs={"class": "base"})
        price = soup.find("span", attrs={"class": "price"})
        return (product.text, price.text)


app.run(debug=True)
