import datetime
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
# get the current datetime and store it in a variable
currentDateTime = datetime.datetime.now()

connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS customers (fname TEXT, \
lname TEXT, email TEXT, password TEXT)')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO customers \
                           (fname, lname, email, password) VALUES (?,?,?,?)",
                           (fname,lname, email, password))
            users.commit()
        return render_template("option.html")
    else:
        return render_template('capture.html')



