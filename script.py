from flask import *
import joblib
import pandas as pd
import numpy as np
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

model1 = joblib.load('models/diabetes_model.pkl')   
model2 = joblib.load('models/heart_model.pkl')      
model3 = joblib.load('models/cancer_model.pkl')  

DATABASE = 'users.db'

def get_db():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    return con

@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home.html')
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        try:
            with get_db() as con:
                cursor = con.cursor()
                cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
                account = cursor.fetchone()
                if account:
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    msg = 'Logged in Successfully'
                    return render_template('home.html', msg=msg)
                else:
                    msg = 'Incorrect Username/Password'
        except Exception as e:
            msg = 'Error in Login'
            print(e)
    return render_template('login.html', msg=msg)

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        try:
            with get_db() as con:
                cursor = con.cursor()
                cursor.execute('SELECT * FROM users WHERE username=?', (username,))
                account = cursor.fetchone()
                if account:
                    msg = 'Account already exists'
                elif not re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', email):
                    msg = 'Invalid email address!'
                elif not re.match(r'^[A-Za-z0-9]+$', username):
                    msg = 'Username must contain only characters and numbers!'
                elif not username or not password or not email:
                    msg = 'Please fill out the form!'
                else:
                    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
                    con.commit()
                    msg = 'User successfully added!'
                    return redirect(url_for('login'))
        except Exception as e:
            msg = 'Error in registration'
            print(e)
    elif request.method == 'POST':
        msg = 'Please fill out the form'
    return render_template('registration.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    data = request.get_json()
    prediction = model1.predict([data['features']])  
    if prediction[0] == 0:
        result = "Negative"
    else:
        result = "Positive"
    return jsonify({'prediction': result})

@app.route('/predict_heart', methods=['POST'])
def predict_heart():
    data = request.get_json()
    prediction = model2.predict([data['features']])  
    if prediction[0] == 0:
        result = "Negative"
    else:
        result = "Positive"
    return jsonify({'prediction': result})

@app.route('/predict_cancer', methods=['POST'])
def predict_cancer():
    data = request.get_json()
    prediction = model3.predict([data['features']])  
    if prediction[0] == 0:
        result = "Negative"
    else:
        result = "Positive"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
